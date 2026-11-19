"""Convierte el itemizado del proyecto (PDF) en tabla LaTeX para el anexo.

Entrada : 02_material_bruto/otros/EE-ATE250033_itemizado-rev1.pdf
Salidas : 04_analisis/datos/itemizado_rev1.csv  (extracción fiel: ítem, descripción, unidad, cantidad)
          tesis/tablas/itemizado.tex             (longtable; ortografía corregida en las descripciones)

Las cantidades y unidades NO se modifican. Solo se corrigen errores de tipeo en el
texto y se completan dos descripciones cortadas en el PDF original.
Ejecutar desde la raíz del repo:  python 04_analisis/scripts/03_itemizado.py
"""
import csv
import re
from pathlib import Path

import pymupdf

RAIZ = Path(__file__).resolve().parents[2]
PDF = RAIZ / "02_material_bruto/otros/EE-ATE250033_itemizado-rev1.pdf"
CSV = RAIZ / "04_analisis/datos/itemizado_rev1.csv"
TEX = RAIZ / "tesis/tablas/itemizado.tex"

# Límites de columnas (pt) medidos en el PDF original
COLS = {"item": (0, 100), "desc": (100, 370), "unidad": (370, 420), "cantidad": (420, 452)}

filas = []
for pagina in pymupdf.open(PDF):
    lineas = {}
    for w in pagina.get_text("words"):
        clave = next((k for k in lineas if abs(k - w[3]) <= 2), round(w[3]))
        lineas.setdefault(clave, []).append(w)
    for k in sorted(lineas):
        palabras = sorted(lineas[k], key=lambda w: w[0])
        celda = {c: " ".join(w[4] for w in palabras if a <= w[0] < b) for c, (a, b) in COLS.items()}
        if re.fullmatch(r"\d+(\.\d+)*", celda["item"]):
            filas.append([celda["item"], celda["desc"], celda["unidad"], celda["cantidad"]])

CSV.parent.mkdir(parents=True, exist_ok=True)
with open(CSV, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows([["item", "descripcion", "unidad", "cantidad"], *filas])

CORRECCIONES = {  # primero las descripciones cortadas, luego la ortografía
    "(llegadas a tanque aguas serv": "(llegada a tanque de aguas servidas)",
    "Fosa septica de acum": "fosa séptica de acumulación)",
    "Suminisitro": "Suministro", "Suiministro": "Suministro", "Sumnistro": "Suministro",
    "instalción": "instalación", "Instalación": "instalación", "septica": "séptica",
    "Camaras": "Cámaras", "Hidraulico": "Hidráulico", "hidraulico": "hidráulico", "Hidraulica": "Hidráulica",
    "hidraulicas": "hidráulicas", "Tuberias": "Tuberías", "Valvulas": "Válvulas", "Electrico": "Eléctrico",
    "estereo": "estero", "Segundaria": "secundaria", "Riego(Sector": "Riego (Sector",
    "( Contempla": "(contempla", "25mm": "25 mm", "64mm": "64 mm", "16mm": "16 mm",
}
UNIDADES = {"un": "un", "ml": "m", "m3": r"\unit{\cubic\meter}", "M3": r"\unit{\cubic\meter}",
            "m2": r"\unit{\square\meter}", "gl": "gl", "": ""}


def limpiar(texto):
    for a, b in CORRECCIONES.items():
        texto = texto.replace(a, b)
    texto = texto[0].upper() + texto[1:] if texto else texto
    return texto.replace("&", r"\&").replace("%", r"\%")


cuerpo = []
for item, desc, uni, cant in filas:
    nivel = item.count(".")
    d = limpiar(desc)
    if nivel == 0:
        cuerpo.append(rf"  \midrule" + "\n" + rf"  \textbf{{{item}}} & \multicolumn{{3}}{{l}}{{\textbf{{{d}}}}} \\")
    elif nivel == 1:
        cuerpo.append(rf"  \textbf{{{item}}} & \multicolumn{{3}}{{l}}{{\textit{{{d}}}}} \\")
    else:
        cuerpo.append(rf"  {item} & {d} & {UNIDADES.get(uni, uni)} & {cant} \\")

tabla = "\n".join([
    "% Archivo GENERADO por 04_analisis/scripts/03_itemizado.py — no editar a mano",
    r"\begin{longtable}{@{}l>{\raggedright\arraybackslash}p{10.2cm}cr@{}}",
    r"  \caption{Itemizado de partidas de la estación experimental (revisión 1).}\label{tab:itemizado} \\",
    r"  \toprule",
    r"  Ítem & Descripción & Unidad & Cantidad \\",
    r"  \midrule",
    r"  \endfirsthead",
    r"  \toprule",
    r"  Ítem & Descripción & Unidad & Cantidad \\",
    r"  \midrule",
    r"  \endhead",
    r"  \bottomrule",
    r"  \endfoot",
    *cuerpo,
    r"\end{longtable}",
    "",
])
TEX.parent.mkdir(parents=True, exist_ok=True)
TEX.write_text(tabla, encoding="utf-8")
print(f"{len(filas)} ítems -> {TEX.relative_to(RAIZ)}")
