"""Junta el contexto de la tesis en UN archivo Markdown para subirlo a otra IA
(ChatGPT, Gemini, NotebookLM...) cuando esa IA no puede leer el repositorio.

Uso:  python3 herramientas/empaquetar_contexto.py [--sin-tesis] [--con-bruto]
Salida: salida/contexto_completo.md
"""
import argparse
import subprocess
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SALIDA = RAIZ / "salida" / "contexto_completo.md"

p = argparse.ArgumentParser()
p.add_argument("--sin-tesis", action="store_true", help="no incluir los .tex de la tesis")
p.add_argument("--con-bruto", action="store_true", help="incluir textos (.md/.txt/.tex) de 02_material_bruto")
args = p.parse_args()

secciones = [
    ("Instrucciones para la IA", ["AGENTS.md"]),
    ("Proyecto", ["00_proyecto/CONTEXTO.md", "00_proyecto/ESTADO.md", "00_proyecto/DECISIONES.md",
                  "00_proyecto/PLAN.md", "00_proyecto/GLOSARIO.md", "00_proyecto/BITACORA.md"]),
    ("Normativa", ["01_normativa/REGLAS_FORMATO.md", "01_normativa/RUBRICA.md", "01_normativa/PROCESO_TITULACION.md"]),
    ("Selección: triaje", sorted(str(f.relative_to(RAIZ)) for f in (RAIZ / "03_seleccion/triaje").glob("*.md") if not f.name.startswith("_"))),
    ("Selección: fichas de lectura", sorted(str(f.relative_to(RAIZ)) for f in (RAIZ / "03_seleccion/fichas_lectura").glob("*.md") if not f.name.startswith("_"))),
    ("Selección: notas", sorted(str(f.relative_to(RAIZ)) for f in (RAIZ / "03_seleccion/notas").glob("*.md"))),
]
if not args.sin_tesis:
    tex = ["tesis/main.tex", "tesis/config/comandos.tex"]
    tex += sorted(str(f.relative_to(RAIZ)) for d in ("preliminares", "capitulos", "anexos")
                  for f in (RAIZ / "tesis" / d).glob("*.tex") if "guia_plantilla" not in f.name)
    secciones.append(("Tesis (LaTeX)", tex + ["tesis/bib/referencias.bib"]))
if args.con_bruto:
    secciones.append(("Material bruto (sin triaje: puede contener errores)",
                      sorted(str(f.relative_to(RAIZ)) for f in (RAIZ / "02_material_bruto").rglob("*")
                             if f.suffix in {".md", ".txt", ".tex"} and f.name != "README.md")))

try:
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=RAIZ, capture_output=True, text=True).stdout.strip()
except OSError:
    commit = "?"

partes = [f"# Contexto completo de la tesis\n\nGenerado el {date.today()} desde el commit `{commit}`.\n"
          "Lee primero la sección 'Instrucciones para la IA'.\n"]
for titulo, archivos in secciones:
    if not archivos:
        continue
    partes.append(f"\n\n# ===== {titulo} =====\n")
    for a in archivos:
        ruta = RAIZ / a
        if ruta.is_file():
            lang = {".tex": "latex", ".bib": "bibtex"}.get(ruta.suffix, "")
            contenido = ruta.read_text(encoding="utf-8", errors="replace")
            cuerpo = f"```{lang}\n{contenido}\n```" if lang else contenido
            partes.append(f"\n\n## Archivo: `{a}`\n\n{cuerpo}\n")

SALIDA.parent.mkdir(parents=True, exist_ok=True)
SALIDA.write_text("".join(partes), encoding="utf-8")
print(f"==> {SALIDA.relative_to(RAIZ)} ({SALIDA.stat().st_size // 1024} KB). Súbelo a la IA o a NotebookLM.")
