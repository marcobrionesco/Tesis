"""Verifica las reglas de extensión de la normativa ICV-611 sobre el PDF compilado.
(01_normativa/REGLAS_FORMATO.md y RUBRICA.md). Requiere haber corrido `make pdf`.

- Cuerpo principal (Introducción → Bibliografía): máx. 80 páginas.
- Resumen y Agradecimientos: máx. 1 página cada uno.
- Palabras clave: entre 3 y 5.
- Bibliografía: >= 15 referencias, >= 10 de los últimos 10 años (meta de la rúbrica).
"""
import re
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
AUX = RAIZ / "salida" / "build" / "main.aux"
MAX_CUERPO = 80

if not AUX.exists():
    print("⚠️  No hay compilación previa: ejecuta `make pdf` primero.")
    sys.exit(0)

aux = AUX.read_text(encoding="utf-8", errors="replace")
paginas = dict(re.findall(r"\\newlabel\{(pag:[^}]+)\}\{\{[^}]*\}\{([^}]*)\}", aux))


def romano(s: str) -> int:
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
    s = s.upper()
    total = 0
    for i, c in enumerate(s):
        v = vals[c]
        total += -v if i + 1 < len(s) and vals[s[i + 1]] > v else v
    return total


def num(p: str) -> int:
    return int(p) if p.isdigit() else romano(p)


errores = 0


def informar(ok: bool, texto: str) -> None:
    global errores
    print(("✅ " if ok else "❌ ") + texto)
    errores += 0 if ok else 1


if "pag:fin-cuerpo" in paginas:
    n = num(paginas["pag:fin-cuerpo"])
    informar(n <= MAX_CUERPO, f"Cuerpo principal: {n} de máx. {MAX_CUERPO} páginas")
for seccion in ("resumen", "agradecimientos"):
    ini, fin = paginas.get(f"pag:{seccion}-ini"), paginas.get(f"pag:{seccion}-fin")
    if ini and fin:
        n = num(fin) - num(ini) + 1
        informar(n <= 1, f"{seccion.capitalize()}: {n} página(s) (máx. 1)")

resumen = (RAIZ / "tesis/preliminares/resumen.tex").read_text(encoding="utf-8")
m = re.search(r"Palabras clave:\}\s*(.+)", resumen)
if m and "pendiente" not in m.group(1):
    claves = [c for c in re.split(r"[,;]", m.group(1).strip().rstrip(".")) if c.strip()]
    informar(3 <= len(claves) <= 5, f"Palabras clave: {len(claves)} (entre 3 y 5)")
else:
    print("ℹ️  Palabras clave aún pendientes.")

bib = (RAIZ / "tesis/bib/referencias.bib").read_text(encoding="utf-8")
anios = [int(a) for a in re.findall(r"^\s*(?:year|date)\s*=\s*\{(\d{4})", bib, re.M)]
total = len(re.findall(r"^@\w+\s*\{", bib, re.M))
recientes = sum(a >= date.today().year - 10 for a in anios)
print(("✅ " if total >= 15 and recientes >= 10 else "ℹ️  ")
      + f"Referencias: {total} (meta ≥ 15), de los últimos 10 años: {recientes} (meta ≥ 10)")

sys.exit(1 if errores else 0)
