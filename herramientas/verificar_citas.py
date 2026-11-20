"""Verifica que toda cita en la tesis exista en referencias.bib, y lista las
entradas del .bib que no se citan. Uso: python3 herramientas/verificar_citas.py
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
TESIS = RAIZ / "tesis"
BIB = TESIS / "bib" / "referencias.bib"

patron_cita = re.compile(r"\\(?:[a-zA-Z]*cite[a-zA-Z]*|cite)\*?(?:\[[^\]]*\]){0,2}\{([^}]*)\}")
claves_bib = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", BIB.read_text(encoding="utf-8")))

citadas: dict[str, list[str]] = {}
for tex in sorted(TESIS.rglob("*.tex")):
    for n, linea in enumerate(tex.read_text(encoding="utf-8").splitlines(), 1):
        if linea.lstrip().startswith("%"):
            continue
        for grupo in patron_cita.findall(linea):
            for clave in (c.strip() for c in grupo.split(",")):
                if clave:
                    citadas.setdefault(clave, []).append(f"{tex.relative_to(RAIZ)}:{n}")

faltan = {c: l for c, l in citadas.items() if c not in claves_bib}
sin_usar = sorted(claves_bib - citadas.keys())

if faltan:
    print("❌ Citas SIN entrada en referencias.bib (¿inventadas o sin agregar?):")
    for c, lugares in faltan.items():
        print(f"   {c}  ->  {', '.join(lugares)}")
else:
    print(f"✅ Las {len(citadas)} claves citadas existen en referencias.bib.")
if sin_usar:
    print("ℹ️  Entradas del .bib que no se citan:", ", ".join(sin_usar))
sys.exit(1 if faltan else 0)
