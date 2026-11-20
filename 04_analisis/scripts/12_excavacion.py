"""Perfiles de zanjas sanitarias: cotas de fondo, profundidad de excavación, tapada y volumen.

Basada en 02_material_bruto/calculos_originales/2026_yo_calculo-excavacion-colab.py (pendiente 2 %).
Cambios:
- Un solo cálculo para las tres zanjas, sin repetir código, con salida en CSV y figura.
- Se calcula con el diámetro del original (52 mm) y con el de las EETT (PVC sanitario 110 mm).
- Se agrega el volumen de excavación (regla del trapecio) con un ancho de zanja SUPUESTO por confirmar.
Ejecutar desde la raíz del repo:  python 04_analisis/scripts/12_excavacion.py
"""
import csv
from pathlib import Path

import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parents[2]
RES = RAIZ / "04_analisis/resultados"
plt.style.use(Path(__file__).with_name("estilo_tesis.mplstyle"))

PENDIENTE = 0.02            # [autor; EETT: 1–3 %]
ANCHO_ZANJA = 0.40          # m  SUPUESTO — confirmar con EETT/CO
CAMA_ARENA = 0.10           # m  [EETT: cama de arena de 10 cm bajo el tubo]
DIAMETROS = {"original 52 mm": 0.052, "EETT PVC 110 mm": 0.110}

# (nombre, distancias m, cotas de terreno m, cota de fondo inicial m, tapada mínima m) — datos del autor.
# Cota de fondo inicial: la de las corridas guardadas en el documento de resultados (zanjas 1 y 2);
# el script original tenía otros valores (117,5 y 118,5). Zanja 3: sin corrida guardada (SUPUESTO = script).
ZANJAS = [
    ("Zanja 1: cámara química galpón – cámara nueva", [0, 31, 85, 107], [118.5, 117.5, 116.5, 117.5], 116.80, 0.50),
    ("Zanja 2: cámara oficina – cámara nueva", [0, 2, 14, 21], [119.5, 119.5, 118.5, 117.5], 116.50, 0.30),
    ("Zanja 3: cámara casa – cámara nueva", [0, 20, 36, 49], [119.44, 118.5, 117.5, 117.5], 118.0, 0.50),
]

filas, resumen = [], []
fig, axs = plt.subplots(len(ZANJAS), 1, figsize=(6.0, 7.5))
for ax, (nombre, x, zt, z0, tap_min) in zip(axs, ZANJAS):
    fondo = [z0 - PENDIENTE * xi for xi in x]
    for etq, D in DIAMETROS.items():
        prof = [t - f + CAMA_ARENA for t, f in zip(zt, fondo)]          # excavación desde terreno a sello (con cama)
        tapada = [t - (f + D) for t, f in zip(zt, fondo)]
        vol = sum((prof[i] + prof[i + 1]) / 2 * (x[i + 1] - x[i]) * ANCHO_ZANJA for i in range(len(x) - 1))
        for xi, t, f, p, tp in zip(x, zt, fondo, prof, tapada):
            filas.append([nombre, etq, xi, t, round(f, 3), round(p, 3), round(tp, 3), "OK" if tp >= tap_min else "TAPADA INSUFICIENTE"])
        resumen.append([nombre, etq, x[-1], round(min(tapada), 2), tap_min, round(max(prof), 2), round(vol, 1)])
    ax.plot(x, zt, "o-", color="saddlebrown", label="Terreno")
    ax.plot(x, fondo, "b-", label="Fondo del tubo")
    ax.plot(x, [f + DIAMETROS["EETT PVC 110 mm"] for f in fondo], "b--", lw=0.8, label="Clave (Ø 110 mm)")
    ax.set_title(nombre, fontsize=8); ax.set_ylabel("Cota [m]")
axs[-1].set_xlabel("Distancia [m]"); axs[0].legend(fontsize=6)
RES.mkdir(parents=True, exist_ok=True)
fig.savefig(RES / "excavacion_perfiles.pdf")
with open(RES / "excavacion_perfiles.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["zanja", "diametro", "dist_m", "cota_terreno", "cota_fondo", "excavacion_m", "tapada_m", "estado"]); w.writerows(filas)
with open(RES / "excavacion_resumen.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["zanja", "diametro", "largo_m", "tapada_min_m", "tapada_exigida_m", "excavacion_max_m", "volumen_m3"]); w.writerows(resumen)
for r in resumen:
    print(f"{r[0]:<48} {r[1]:<16} L={r[2]:>4} m  tapada mín={r[3]:.2f} (exig. {r[4]:.2f})  exc. máx={r[5]:.2f} m  V={r[6]:.1f} m3")
print("Excavaciones > 1,5 m requieren entibación/talud según NCh349 (ver EETT).")
print(f"Volumen total (Ø 110 mm, ancho {ANCHO_ZANJA} m SUPUESTO): {sum(r[6] for r in resumen if '110' in r[1]):.1f} m3")
