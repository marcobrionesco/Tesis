"""Ordena la curva de nivel (puntos topográficos) y genera un mapa de apoyo.

Entrada : 02_material_bruto/datos_crudos/2026-11-19_yo_curva-nivel.xlsx (id, norte, este, cota, descripción)
Salidas : 04_analisis/datos/curva_nivel.csv
          04_analisis/resultados/topografia_puntos.png  (para identificar qué punto es cada obra)
Coordenadas UTM (m). Ejecutar desde la raíz del repo: python 04_analisis/scripts/05_topografia.py
"""
import csv
from pathlib import Path

import matplotlib.pyplot as plt
import openpyxl

RAIZ = Path(__file__).resolve().parents[2]
XLSX = RAIZ / "02_material_bruto/datos_crudos/2026-11-19_yo_curva-nivel.xlsx"
CSV = RAIZ / "04_analisis/datos/curva_nivel.csv"
PNG = RAIZ / "04_analisis/resultados/topografia_puntos.png"
plt.style.use(Path(__file__).with_name("estilo_tesis.mplstyle"))

puntos = []
for (celda,) in openpyxl.load_workbook(XLSX, data_only=True).active.iter_rows(values_only=True, max_col=1):
    if celda:
        i, n, e, z, desc = celda.split(",")
        puntos.append(dict(id=int(i), norte=float(n), este=float(e), cota=float(z),
                           descripcion=desc.replace("Point_generic", "").strip("_") or ""))
CSV.parent.mkdir(parents=True, exist_ok=True)
with open(CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(puntos[0])); w.writeheader(); w.writerows(puntos)

fig, ax = plt.subplots(figsize=(6, 6))
sc = ax.scatter([p["este"] for p in puntos], [p["norte"] for p in puntos], c=[p["cota"] for p in puntos], cmap="viridis", s=25)
for p in puntos:
    ax.annotate(f"{p['id']}" + (f" {p['descripcion']}" if p["descripcion"] else ""), (p["este"], p["norte"]), fontsize=6,
                xytext=(2, 2), textcoords="offset points")
fig.colorbar(sc, label="Cota [m]")
ax.set_xlabel("Este [m]"); ax.set_ylabel("Norte [m]"); ax.set_aspect("equal")
PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(PNG, format="png", dpi=150)
cotas = [p["cota"] for p in puntos]
print(f"{len(puntos)} puntos; cota {min(cotas):.2f}–{max(cotas):.2f} m; con nombre: "
      + ", ".join(f"{p['id']} ({p['descripcion']}, {p['cota']} m)" for p in puntos if p["descripcion"]))
