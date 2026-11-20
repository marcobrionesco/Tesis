"""Construye la base de caracterización DIRECTAMENTE desde los seis informes del Laboratorio del Agua (FCI, UCM).

Fuente primaria (decisión del autor, pregunta 7, 20-11-2026): 02_material_bruto/laboratorio/2026_lab-ucm_informe-*.md
(convertidos con pandoc desde los .docx originales). La base anterior y el resumen del proyecto tenían errores.
Salida: 04_analisis/datos/caracterizacion_afluentes.csv (mismo formato + columna 'atipica').

Criterio de la semana 1 (dato del autor): muestras mal tomadas en AS1 y AS2 (SST, turbiedad y DQO muy superiores al
resto). Se conservan como valores medidos, marcados atipica = 1, y se excluyen de las medias de diseño.
Los coliformes del laboratorio son TOTALES (no fecales).
Ejecutar desde la raíz del repo:  python 04_analisis/scripts/00_laboratorio_a_csv.py
"""
import csv
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
LAB = sorted((RAIZ / "02_material_bruto/laboratorio").glob("2026_lab-ucm_informe-*.md"))
SALIDA = RAIZ / "04_analisis/datos/caracterizacion_afluentes.csv"
COLS = {"Estero": "EST", "AS 1": "AS1", "AS 2": "AS2", "AGR 1": "AGR1", "AGR 2": "AGR2"}
FILAS = [  # (patrón del rótulo del laboratorio, parámetro, unidad)
    (r"^pH", "pH", "-"), (r"^Temperatura", "Temperatura", "°C"), (r"^CE", "Conductividad eléctrica", "µS/cm"),
    (r"^ORP", "Potencial de óxido-reducción", "mV"), (r"^OD", "Oxígeno disuelto", "mg/L"),
    (r"^TDS", "Sólidos disueltos totales", "mg/L"), (r"^Turbiedad", "Turbiedad", "NTU"),
    (r"^DQO.*\(1\)", "DQO total", "mg/L"), (r"^DQO.*\(2\)", "DQO disuelta", "mg/L"), (r"^DBO", "DBO5", "mg/L"),
    (r"^SST", "SST", "mg/L"), (r"^NH", "Amonio", "mg/L"), (r"^NO", "Nitrato", "mg/L"), (r"^NT", "Nitrógeno total", "mg/L"),
    (r"^PT", "Fósforo total", "mg/L"), (r"^PO", "Fosfato", "mg/L"),
    (r"^Coliformes", "Coliformes totales", "NMP/100 mL"), (r"^E\.? ?coli", "E. coli", "NMP/100 mL"),
]


def limpiar(s):
    s = re.sub(r"</?sup>|</?sub>|<span[^>]*>|</span>|\*", "", s)
    return s.replace("\\", "").strip()


def valor(txt):
    t = limpiar(txt).replace(" ", "")
    if t in ("", "-", "—"):
        return "", ""
    cens = ""
    if t[0] in "<>":
        cens, t = t[0], t[1:]
    m = re.match(r"^([\d,\.]+)x10(\d+)$", t)
    if m:
        return float(m.group(1).replace(",", ".")) * 10 ** int(m.group(2)), cens
    return float(t.replace(",", ".")), cens


filas = []
for semana, archivo in enumerate(LAB, start=1):
    lineas = [l for l in archivo.read_text(encoding="utf-8").splitlines() if l.startswith("|")]
    cab = [limpiar(c) for c in lineas[0].strip("|").split("|")]
    idx = {COLS[c]: i for i, c in enumerate(cab) if c in COLS}
    for l in lineas[2:]:
        celdas = l.strip("|").split("|")
        rot = limpiar(celdas[0])
        for patron, par, uni in FILAS:
            if re.search(patron, rot):
                break
        else:
            continue
        for pto in ["EST", "AS1", "AS2", "AGR1", "AGR2"]:
            if pto not in idx:
                continue
            v, cens = valor(celdas[idx[pto]])
            atip = 1 if (semana == 1 and pto in ("AS1", "AS2")) else 0
            filas.append([pto, par, uni, semana, v, cens, limpiar(celdas[idx[pto]]), atip])

ORDEN_P = [p for _, p, _ in FILAS]
ORDEN_PT = ["EST", "AS1", "AS2", "AGR1", "AGR2"]
filas.sort(key=lambda r: (ORDEN_P.index(r[1]), ORDEN_PT.index(r[0]), r[3]))
with open(SALIDA, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["punto", "parametro", "unidad", "semana", "valor", "censura", "texto_original", "atipica"])
    w.writerows(filas)
print(f"{len(filas)} valores desde {len(LAB)} informes -> {SALIDA.relative_to(RAIZ)}")
