"""Exporta la tesis LaTeX a Word (.docx) para que el profesor guía pueda editarla y comentarla.

El profesor guía pidió (correo del 16-11-2026) recibir las versiones en Word. El "master" sigue siendo
el LaTeX de tesis/; este script genera una COPIA editable en salida/tesis.docx. Los cambios que el
profesor haga en Word se traspasan a mano al LaTeX (receta herramientas/recetas/, comparar con `make diff`).

Qué hace (pandoc no entiende varias cosas del LaTeX de la tesis, así que se preprocesa):
- Números de figuras, tablas, ecuaciones, secciones y anexos: se leen de los .aux de la última
  compilación (por eso exige `make pdf` antes) y se escriben en \\cref, títulos y ecuaciones.
- siunitx (\\qty, \\unit, \\num, \\qtyrange, \\qtyproduct, \\ang) → texto con coma decimal.
- Figuras TikZ → PNG (compiladas aparte); figuras PDF → PNG.
- Citas → pandoc --citeproc con estilo APA 7 (herramientas/estilos/apa.csl) e idioma es-CL.
- \\pendiente{...} y \\revisar{...} → texto en cursiva azul / verde en el Word.
- Formato base: carta, Times New Roman 12, interlineado 1,5, márgenes 2,5/3 cm (REGLAS_FORMATO).

Uso (desde la raíz):  make word      (o: python3 herramientas/latex_a_word.py)
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
TESIS = RAIZ / "tesis"
BUILD = RAIZ / "salida/build"
TMP = RAIZ / "salida/word"
SALIDA = RAIZ / "salida/tesis.docx"
CSL = RAIZ / "herramientas/estilos/apa.csl"

PARTES = ["preliminares/resumen", "capitulos/01_introduccion", "capitulos/02_marco_teorico",
          "capitulos/03_metodologia", "capitulos/04_resultados", "capitulos/05_discusion",
          "capitulos/06_conclusiones"]

# ---------------------------------------------------------------- etiquetas (.aux)
ETIQ = {}
for aux in BUILD.rglob("*.aux"):
    for m in re.finditer(r"\\newlabel\{([^}@]+)\}\{\{([^}]*)\}", aux.read_text(errors="ignore")):
        ETIQ[m.group(1)] = m.group(2)
if not ETIQ:
    sys.exit("No hay etiquetas: ejecuta primero `make pdf`.")

NOMBRE = {"fig": ("figura", "figuras"), "tab": ("tabla", "tablas"), "ec": ("ecuación", "ecuaciones"),
          "sec": ("sección", "secciones"), "cap": ("capítulo", "capítulos"), "anx": ("anexo", "anexos"),
          "pag": ("página", "páginas")}


def num(clave):
    return ETIQ.get(clave, "??")


def cref(m):
    mayus = m.group(1) == "C"
    claves = [c.strip() for c in m.group(2).split(",")]
    pref = claves[0].split(":")[0]
    sing, plur = NOMBRE.get(pref, ("", ""))
    nums = [f"({num(c)})" if pref == "ec" else num(c) for c in claves]
    lista = nums[0] if len(nums) == 1 else ", ".join(nums[:-1]) + " y " + nums[-1]
    nombre = sing if len(nums) == 1 else plur
    if mayus:
        nombre = nombre.capitalize()
    return f"{nombre} {lista}".strip()


# ---------------------------------------------------------------- siunitx
UNIDADES = {"meter": "m", "metre": "m", "gram": "g", "liter": "L", "litre": "L", "day": "d", "hour": "h",
            "minute": "min", "second": "s", "pascal": "Pa", "newton": "N", "volt": "V", "siemens": "S",
            "percent": "\\%", "degree": "°", "kilogram": "kg", "tonne": "t", "celsius": "°C", "degreeCelsius": "°C"}
PREFIJOS = {"kilo": "k", "milli": "m", "centi": "c", "micro": "µ", "mega": "M", "giga": "G"}
POTENCIA = {"square": "²", "cubic": "³"}


def unidad(texto):
    tokens = re.findall(r"\\([A-Za-z]+)|([^\\\s]+)", texto)
    partes, actual, pre, pot, per = [], "", "", "", False
    for macro, lit in tokens:
        if lit:
            partes.append(("/" if per else "", lit)); per = False; continue
        if macro == "per":
            per = True
        elif macro in POTENCIA:
            pot = POTENCIA[macro]
        elif macro in PREFIJOS:
            pre = PREFIJOS[macro]
        elif macro in UNIDADES:
            partes.append(("/" if per else "", pre + UNIDADES[macro] + pot)); pre = pot = ""; per = False
    s = ""
    for sep, u in partes:
        s += (sep if sep else ("·" if s else "")) + u
    return s


def numero(t):
    t = t.strip().replace(" ", "")
    m = re.fullmatch(r"([-+]?)(\d+)(?:\.(\d+))?(?:e([-+]?\d+))?", t)
    if not m:
        return t.replace(".", ",")
    signo, ent, dec, exp = m.groups()
    if len(ent) >= 4:
        ent = f"{int(ent):,}".replace(",", ".")
    s = signo.replace("-", "−") + ent + ("," + dec if dec else "")
    if exp:
        s += f" × 10^{exp}^"
    return s


def qty(n, u):
    u = unidad(u)
    return f"{numero(n)}{'' if u in (r'\%', '°') else ' '}{u}"


B = r"\{((?:[^{}]|\{[^{}]*\})*)\}"  # argumento con un nivel de llaves anidadas


def siunitx(s):
    s = re.sub(r"\\qtyproduct" + B + B, lambda m: " × ".join(numero(x) for x in m.group(1).split("x")) + " " + unidad(m.group(2)), s)
    s = re.sub(r"\\qtyrange" + B + B + B, lambda m: f"{numero(m.group(1))} a {qty(m.group(2), m.group(3))}", s)
    s = re.sub(r"\\numrange" + B + B, lambda m: f"{numero(m.group(1))} a {numero(m.group(2))}", s)
    s = re.sub(r"\\qty" + B + B, lambda m: qty(m.group(1), m.group(2)), s)
    s = re.sub(r"\\unit" + B, lambda m: unidad(m.group(1)), s)
    s = re.sub(r"\\num" + B, lambda m: numero(m.group(1)), s)
    s = re.sub(r"\\ang" + B, lambda m: numero(m.group(1)) + "°", s)
    return s


# ---------------------------------------------------------------- figuras
def png_de_pdf(pdf: Path) -> str:
    destino = TMP / "fig" / (pdf.stem + ".png")
    destino.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["pdftoppm", "-r", "200", "-png", "-singlefile", str(pdf), str(destino.with_suffix(""))], check=True)
    return str(destino)


N_TIKZ = [0]


def tikz_a_png(codigo: str) -> str:
    N_TIKZ[0] += 1
    d = TMP / "tikz"; d.mkdir(parents=True, exist_ok=True)
    tex = d / f"tikz{N_TIKZ[0]}.tex"
    tex.write_text("\\documentclass[border=4pt]{standalone}\n\\usepackage[T1]{fontenc}\\usepackage[utf8]{inputenc}"
                   "\\usepackage{newtxtext,newtxmath}\\usepackage{tikz}\\usetikzlibrary{arrows.meta,calc,positioning,patterns}"
                   "\\usepackage{siunitx}\n\\begin{document}\n" + codigo + "\n\\end{document}\n")
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", tex.name], cwd=d, capture_output=True)
    if r.returncode != 0:
        print(f"  ! TikZ {tex.name} no compiló; se omite la figura"); return ""
    return png_de_pdf(tex.with_suffix(".pdf"))


def grafico(m):
    nombre = m.group(2)
    for cand in [TESIS / "figuras" / nombre, *(TESIS / "figuras").glob(nombre + ".*"), TESIS / nombre]:
        if cand.is_file():
            ruta = png_de_pdf(cand) if cand.suffix == ".pdf" else str(cand)
            return f"\\includegraphics[width=0.8\\textwidth]{{{ruta}}}"
    return f"[FIGURA NO ENCONTRADA: {nombre}]"


# ---------------------------------------------------------------- numerar títulos y ecuaciones
def numerar_entornos(s):
    def entorno(m):
        cuerpo, tipo = m.group(0), m.group(1)
        etiqs = re.findall(r"\\label\{((?:fig|tab):[^}]+)\}", cuerpo)
        rot = "Figura" if tipo.startswith("figure") else "Tabla"
        # subfiguras: numerar solo el título principal (el último \caption)
        if etiqs:
            pos = cuerpo.rfind("\\caption{")
            if pos >= 0:
                cuerpo = cuerpo[:pos] + f"\\caption{{\\textbf{{{rot} {num(etiqs[-1])}:}} " + cuerpo[pos + 9:]
        return cuerpo
    s = re.sub(r"\\begin\{(figure\*?|table\*?)\}.*?\\end\{\1\}", entorno, s, flags=re.S)
    s = re.sub(r"\\label\{(ec:[^}]+)\}", lambda m: f"\\tag{{{num(m.group(1))}}}", s)
    return s


def numerar_titulos(s):
    """Numera capítulos, secciones y subsecciones (capítulo y sección desde el .aux; subsección por conteo)."""
    cnt = {"cap": "", "sec": "", "sub": 0}

    def titulo(m):
        nivel, texto, etiqueta = m.group(1), m.group(2), m.group(3)
        n = num(etiqueta) if etiqueta else ""
        if nivel == "chapter":
            cnt["cap"] = n if n != "??" else ""
        elif nivel == "section":
            cnt["sub"] = 0
            if not n or n == "??":
                n = ""
            cnt["sec"] = n
        elif nivel == "subsection" and cnt["sec"]:
            cnt["sub"] += 1
            n = f"{cnt['sec']}.{cnt['sub']}"
        n = "" if n == "??" else n
        return f"\\{nivel}{{{n + '. ' if n else ''}{texto}}}"
    return re.sub(r"\\(chapter|section|subsection)\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}\s*(?:\\label\{([^}]+)\})?", titulo, s)


# ---------------------------------------------------------------- macros propias
MACROS = r"""
\newcommand{\pendiente}[1]{⟦P Por hacer: #1⟧}
\newcommand{\revisar}[1]{⟦R Nota: #1⟧}
\newcommand{\enquote}[1]{“#1”}
\newcommand{\NoCaseChange}[1]{#1}
\newcommand{\iniciaranexos}{}
"""


def preprocesar(s):
    s = re.sub(r"(?<!\\)%.*", "", s)                                    # comentarios
    s = s.replace("\\pendiente{}", "⟦P Por hacer⟧")
    s = re.sub(r"\\(chapter|section)\*", r"\\\1", s)
    s = re.sub(r"\\addcontentsline\{[^}]*\}\{[^}]*\}\{[^}]*\}", "", s)
    s = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}",
               lambda m: f"\\includegraphics[width=0.85\\textwidth]{{{tikz_a_png(m.group(0))}}}", s, flags=re.S)
    s = re.sub(r"\\includegraphics(\[[^\]]*\])?\{([^}]+)\}",
               lambda m: m.group(0) if m.group(2).startswith(str(TMP)) else grafico(m), s)
    s = re.sub(r"\\input\{(tablas/[^}]+)\}", lambda m: (TESIS / (m.group(1) + ("" if m.group(1).endswith(".tex") else ".tex"))).read_text(), s)
    s = numerar_entornos(s)
    s = numerar_titulos(s)
    s = re.sub(r"\\(c|C)ref\{([^}]+)\}", cref, s)
    s = re.sub(r"\\(?:ref|pageref)\{([^}]+)\}", lambda m: num(m.group(1)), s)
    s = re.sub(r"\\label\{[^}]+\}", "", s)
    s = siunitx(s)
    s = s.replace("\\,", " ").replace("~", " ")
    return s


# ---------------------------------------------------------------- documento de referencia (estilos Word)
def documento_referencia() -> Path:
    from docx import Document
    from docx.enum.text import WD_LINE_SPACING
    from docx.shared import Cm, Pt, RGBColor
    ref = TMP / "referencia.docx"
    with open(ref, "wb") as f:
        f.write(subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"],
                               capture_output=True, check=True).stdout)
    doc = Document(ref)
    for sec in doc.sections:
        sec.page_width, sec.page_height = Cm(21.59), Cm(27.94)
        sec.top_margin = sec.bottom_margin = Cm(2.5)
        sec.left_margin = sec.right_margin = Cm(3)
    for st in doc.styles:
        if st.type != 1:
            continue
        try:
            st.font.name = "Times New Roman"
            st.font.color.rgb = RGBColor(0, 0, 0)
            if st.element.rPr is not None and st.element.rPr.rFonts is not None:
                for a in ("w:eastAsia", "w:cs"):
                    st.element.rPr.rFonts.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}" + a.split(":")[1], "Times New Roman")
        except Exception:
            pass
    for nombre, tam in [("Normal", 12), ("Body Text", 12), ("First Paragraph", 12), ("Compact", 11),
                        ("Image Caption", 11), ("Table Caption", 11), ("Heading 1", 14), ("Heading 2", 12),
                        ("Heading 3", 12), ("Title", 16), ("Bibliography", 12)]:
        try:
            st = doc.styles[nombre]
        except KeyError:
            continue
        st.font.size = Pt(tam)
        st.font.name = "Times New Roman"
        st.font.color.rgb = RGBColor(0, 0, 0)
        if nombre.startswith("Heading") or nombre == "Title":
            st.font.bold = True
            st.font.italic = False
        pf = st.paragraph_format
        if nombre in ("Normal", "Body Text", "First Paragraph", "Bibliography"):
            pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
            pf.space_after = Pt(6)
    doc.save(ref)
    return ref


# ---------------------------------------------------------------- posproceso: resaltar marcas
def resaltar(docx: Path):
    from docx import Document
    from docx.shared import RGBColor
    doc = Document(docx)
    parrafos = list(doc.paragraphs)
    for t in doc.tables:
        for fila in t.rows:
            for celda in fila.cells:
                parrafos.extend(celda.paragraphs)
    for p in parrafos:
        color = None
        for run in p.runs:
            txt = run.text
            ini = None
            if "⟦P " in txt:
                color, ini = RGBColor(0x1F, 0x3A, 0x7A), txt.index("⟦P ")
            elif "⟦R " in txt:
                color, ini = RGBColor(0x1B, 0x6B, 0x5E), txt.index("⟦R ")
            if color is not None:
                run.font.color.rgb = color
                run.font.italic = True
            if "⟧" in txt:
                color = None
            if any(c in txt for c in ("⟦", "⟧")):   # no tocar runs con imágenes (run.text las borraría)
                run.text = txt.replace("⟦P ", "[").replace("⟦R ", "[").replace("⟦P", "[").replace("⟧", "]")
    doc.save(docx)


def main():
    if TMP.exists():
        shutil.rmtree(TMP)
    TMP.mkdir(parents=True)
    if not CSL.exists():
        sys.exit(f"Falta {CSL} (estilo APA 7 de citation-style-language).")
    cuerpo = []
    for parte in PARTES:
        texto = (TESIS / (parte + ".tex")).read_text()
        cuerpo.append(preprocesar(texto))
    comandos = (TESIS / "config/comandos.tex").read_text()
    titulo = re.search(r"\\newcommand\{\\tesisTitulo\}\{(.*)\}\s*$", comandos, re.M).group(1).replace("\\NoCaseChange{SpA}", "SpA")
    autor = re.search(r"\\newcommand\{\\tesisAutor\}\{(.*)\}", comandos)
    fuente = TMP / "tesis_para_word.tex"
    fuente.write_text("\\documentclass{report}\n" + MACROS + "\\begin{document}\n" + "\n\n".join(cuerpo) +
                      "\n\n\\chapter{Referencias}\n\\printbibliography\n\\end{document}\n")
    ref = documento_referencia()
    cmd = ["pandoc", str(fuente), "-f", "latex", "-o", str(SALIDA), "--citeproc",
           "--bibliography", str(TESIS / "bib/referencias.bib"), "--csl", str(CSL),
           "-M", "lang=es-CL", "-M", f"title={titulo}", "--reference-doc", str(ref),
           "--resource-path", f"{TESIS}:{TESIS / 'figuras'}"]
    if autor:
        cmd += ["-M", f"author={autor.group(1)}"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    for linea in r.stderr.splitlines():
        if "WARNING" in linea and "Could not convert TeX math" not in linea:
            print("  pandoc:", linea)
    if r.returncode != 0:
        sys.exit(r.stderr)
    resaltar(SALIDA)
    print(f"==> {SALIDA.relative_to(RAIZ)}  (notas en cursiva: azul = por hacer, verde = nota)")


if __name__ == "__main__":
    main()
