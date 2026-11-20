"""Extrae la base de datos de macroparámetros del proyecto (PDF) y la compara con la
tabla resumen de caracterización (fuente usada en la tesis).

Entradas : 02_material_bruto/datos_crudos/2026-11-19_proyecto_bd-macroparametros-nbs-waterry.pdf
           04_analisis/datos/caracterizacion_afluentes.csv  (de 01_extraer_caracterizacion.py)
Salidas  : 04_analisis/datos/bd_macroparametros.csv        (formato largo con fechas)
           04_analisis/resultados/qa_bd_vs_resumen.csv     (celdas que no coinciden)
Ejecutar desde la raíz del repo:  python 04_analisis/scripts/04_validar_bd.py
"""
import csv
from pathlib import Path

import pymupdf

RAIZ = Path(__file__).resolve().parents[2]
PDF = RAIZ / "02_material_bruto/datos_crudos/2026-11-19_proyecto_bd-macroparametros-nbs-waterry.pdf"
RESUMEN = RAIZ / "04_analisis/datos/caracterizacion_afluentes.csv"
SALIDA = RAIZ / "04_analisis/datos/bd_macroparametros.csv"
QA = RAIZ / "04_analisis/resultados/qa_bd_vs_resumen.csv"

CAMPOS = ["punto", "fase", "fecha", "semana", "pH", "T", "EC", "ORP", "TDS", "DO", "BOD5", "COD_total",
          "COD_disuelta", "TSS", "NH4", "NO3", "TN", "PO4", "TP", "E_coli", "Coliformes", "Turbiedad"]
MAPA = {"pH": "pH", "T": "Temperatura", "EC": "Conductividad eléctrica", "ORP": "Potencial de óxido-reducción",
        "TDS": "Sólidos disueltos totales", "DO": "Oxígeno disuelto", "BOD5": "DBO5", "COD_total": "DQO total",
        "COD_disuelta": "DQO disuelta", "TSS": "SST", "NH4": "Amonio", "NO3": "Nitrato", "TN": "Nitrógeno total",
        "PO4": "Fosfato", "TP": "Fósforo total", "E_coli": "E. coli", "Coliformes": "Coliformes fecales",
        "Turbiedad": "Turbiedad"}

# --- Extracción por posición de columnas ---
palabras = pymupdf.open(PDF)[0].get_text("words")
inicios = sorted((w for w in palabras if w[4] in ("AS1", "AS2", "AGR1", "AGR2", "EST") and w[0] < 60), key=lambda w: w[1])
datos = [w for w in palabras if w[1] >= inicios[0][1] - 3]
filas = []
for w in sorted(datos, key=lambda w: (w[1] + w[3]) / 2):
    yc = (w[1] + w[3]) / 2
    if filas and abs(yc - filas[-1][0]) < 3:
        filas[-1][1].append(w)
    else:
        filas.append([yc, [w]])
xs = sorted((w[0] + w[2]) / 2 for _, ws in filas for w in ws)
grupos = [[xs[0]]]
for x in xs[1:]:
    (grupos.append([x]) if x - grupos[-1][-1] > 9 else grupos[-1].append(x))
centros = [sum(g) / len(g) for g in grupos]
registros = []
for _, ws in filas:
    celdas = {}
    for w in sorted(ws, key=lambda w: w[0]):
        k = min(range(len(centros)), key=lambda i: abs(centros[i] - (w[0] + w[2]) / 2))
        celdas.setdefault(k, []).append(w[4])
    vals = [" ".join(celdas.get(i, [])) for i in range(len(centros))]
    semana, ph = vals[3].split(" ", 1)  # semana y pH quedan en la misma columna
    registros.append(dict(zip(CAMPOS, vals[:3] + [semana, ph] + vals[4:])))
assert len(registros) == 30, len(registros)
SALIDA.parent.mkdir(parents=True, exist_ok=True)
with open(SALIDA, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=CAMPOS); w.writeheader(); w.writerows(registros)


# --- Comparación con la tabla resumen ---
def norm(t):
    t = t.replace(" ", "").replace(",", ".").replace("x10e", "x10")
    try:
        return float(t)
    except ValueError:
        return t


resumen = {(r["punto"], r["parametro"], int(r["semana"])): r["texto_original"]
           for r in csv.DictReader(open(RESUMEN, encoding="utf-8"))}
diferencias = []
for r in registros:
    for campo, par in MAPA.items():
        a, b = r[campo], resumen.get((r["punto"], par, int(r["semana"])), "")
        if a in ("", "-") and b in ("", "-"):
            continue
        if norm(a) != norm(b):
            diferencias.append([r["punto"], r["semana"], r["fecha"], par, a, b])
QA.parent.mkdir(parents=True, exist_ok=True)
with open(QA, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows([["punto", "semana", "fecha", "parametro", "valor_bd", "valor_resumen"], *diferencias])
fechas = sorted({(int(r["semana"]), r["fecha"]) for r in registros})
print("Campañas:", ", ".join(f"S{s} {fch}" for s, fch in fechas))
print(f"{len(diferencias)} diferencias BD vs. resumen -> {QA.relative_to(RAIZ)}")
for d in diferencias:
    print("  ", d)
