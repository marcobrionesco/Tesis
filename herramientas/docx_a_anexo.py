"""Convierte un documento Word de especificaciones técnicas (EETT) en un anexo LaTeX.

Uso: python3 herramientas/docx_a_anexo.py ENTRADA.docx SALIDA.tex
Genera solo el CUERPO (sin \\chapter): el capítulo y las notas van en un archivo envoltorio
que hace \\input del cuerpo (ej. tesis/anexos/anexo_eett.tex).
- Descarta todo lo anterior al primer título que empiece con "SECTOR" (portada e índice).
- Normaliza títulos: "SECTOR N: ..." -> \\section; grupos en MAYÚSCULAS -> \\subsection;
  partidas -> \\subsubsection* (sin número).
- Convierte los títulos en mayúsculas a tipo oración y quita numeraciones manuales ("2.1.").
Requiere pandoc.
"""
import re
import subprocess
import sys
from pathlib import Path

entrada, salida = sys.argv[1:3]
md = subprocess.run(["pandoc", entrada, "-t", "gfm", "--wrap=none"], capture_output=True, text=True, check=True).stdout
lineas = md.splitlines()
inicio = next(i for i, l in enumerate(lineas) if re.match(r"^#+\s*SECTOR\b", l))
cuerpo = lineas[inicio:]


def oracion(t):
    t = re.sub(r"^\d+(\.\d+)*\.?\s*", "", t.strip().strip("*").strip())
    if t.isupper() or sum(c.isupper() for c in t) > 0.6 * sum(c.isalpha() for c in t):
        t = t.lower()
        t = t[0].upper() + t[1:]
        t = re.sub(r"\b(ibc|pvc|pead)\b", lambda m: m.group(1).upper(), t)
    return t


nuevo = []
for l in cuerpo:
    m = re.match(r"^(#+)\s*(.*)$", l)
    negrita_sola = re.fullmatch(r"\*\*([^*]+)\*\*", l.strip())
    if m or negrita_sola:
        texto = (m.group(2) if m else negrita_sola.group(1)).strip()
        if not texto.strip("* "):
            continue
        if re.match(r"(?i)^sector\s+\d", texto):
            nuevo.append("# " + oracion(texto))
        elif texto.strip("*").isupper() or re.match(r"^\d+\.\d+\.\s", texto):
            nuevo.append("## " + oracion(texto))
        else:
            nuevo.append("### " + oracion(texto))
    else:
        nuevo.append(l)
tex = subprocess.run(["pandoc", "-f", "gfm", "-t", "latex", "--wrap=none"], input="\n".join(nuevo),
                     capture_output=True, text=True, check=True).stdout
tex = re.sub(r"\\hypertarget\{[^}]*\}\{%\n", "", tex)
tex = re.sub(r"\\label\{[^}]*\}\}", "", tex)
tex = re.sub(r"\\subsubsection\{", r"\\subsubsection*{", tex)
tex = tex.replace(r"\tightlist", "")
cabecera = (f"% Anexo GENERADO por herramientas/docx_a_anexo.py desde {Path(entrada).name}\n"
            f"% Para corregir el contenido, editar el Word original y volver a generar.\n\n")
Path(salida).write_text(cabecera + tex, encoding="utf-8")
print("->", salida)
