"""Cálculo de impulsiones (ADT) y verificación contra catálogos — versión actualizada.

Basada en 02_material_bruto/calculos_originales/2026_yo_calculo-bombas-colab.py (Hazen-Williams, C = 140),
que pedía los datos por teclado; los datos que el autor ingresó están registrados en
02_material_bruto/calculos_originales/2026_yo_calculo-partidas-resultados.md.

Cambios:
- Datos fijos y trazables (sin input()); se calcula el caso ORIGINAL y el caso con TUBERÍAS FINALES
  (diámetros y longitudes del itemizado Rev. 1 y de las EETT).
- Se agregan pérdidas singulares (K de la tabla 2.1 de la tesis) — cantidades de piezas por confirmar.
- Se compara el requerimiento (Q, ADT) con las curvas de catálogo que el autor adjuntó.

"SUPUESTO" = dato por confirmar antes de llevarlo a la versión final.
Ejecutar desde la raíz del repo:  python 04_analisis/scripts/11_bombas.py
"""
import csv
from pathlib import Path

import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parents[2]
RES = RAIZ / "04_analisis/resultados"
TABLA = RAIZ / "tesis/tablas/bombas_adt.tex"
plt.style.use(Path(__file__).with_name("estilo_tesis.mplstyle"))

C_HW = 140                       # PVC [tabla 2.1 de la tesis]
K = {"codo90": 0.6, "retencion": 2.5, "tee": 0.6}   # [tabla 2.1 de la tesis]
g = 9.81


def hf_hw(Q, D, L, C=C_HW):
    """Pérdida por fricción Hazen-Williams (SI): Q m3/s, D m, L m -> m."""
    return 10.67 * L * (Q / C) ** 1.852 / D ** 4.87


# Curvas de catálogo (Q en L/min, H en m) — transcritas de las imágenes del documento de partidas
CATALOGO = {
    "Tecson AHS-05 (sum.)": [(20, 11), (80, 9.5), (120, 7), (170, 4), (220, 1)],
    "Tecson AHS-10 (sum.)": [(20, 17), (80, 15), (120, 13), (170, 11), (220, 9), (280, 8.5), (330, 4), (360, 1)],
    "Ebara DW 75M (sum.)": [(100, 8), (200, 6.3), (300, 4.8), (400, 3.4), (500, 2.2)],
    "Ebara DW 100M (sum.)": [(100, 10.6), (200, 8.7), (300, 7.1), (400, 5.5), (500, 4), (600, 2.6)],
    "Ebara DWO 150M (sup.)": [(100, 9.5), (200, 8.9), (300, 7.9), (400, 6.9), (550, 5.1)],
    "Ebara DWO 200M (sup.)": [(100, 12.7), (200, 12.3), (300, 11.5), (400, 10.5), (550, 8.6), (750, 5.8)],
}
# Bomba periférica supuesta por el autor (pregunta 4, 20-11-2026): Pedrollo JSWm 1A, 0,55 kW (0,75 HP), la misma en las
# tres líneas. Curva del catálogo Pedrollo JSW1-JSW2 50 Hz (aspiración 0 m), Q en L/min -> H en m.
PEDROLLO_1A = [(0, 48), (5, 43), (10, 39), (20, 31.5), (25, 28.5), (30, 26), (40, 22), (45, 20.5), (50, 19), (60, 17)]


def H_catalogo(modelo, q_lmin):
    pts = CATALOGO[modelo]
    if q_lmin < pts[0][0]:
        return None  # fuera de la curva publicada (caudal menor al mínimo del catálogo)
    for (q1, h1), (q2, h2) in zip(pts, pts[1:]):
        if q1 <= q_lmin <= q2:
            return h1 + (h2 - h1) * (q_lmin - q1) / (q2 - q1)
    return None


# Líneas: (nombre, tipo, Q L/s, z_succion m, z_impulsion m, L m, Di m, presión final m, piezas, fuente)
Q_LLENADO = 1000 / (30 * 60)     # L/s: 1000 L en 30 min [criterio del autor]
LINEAS = [
    # --- caso ORIGINAL (datos ingresados por el autor) ---
    ("Superficie (original)", "orig", Q_LLENADO, 6.0, 5.0, 100.0, 0.030, 0.0, {}, "autor"),
    ("Sumergible (original)", "orig", Q_LLENADO, 0.0, 5.0, 100.0, 0.030, 0.0, {}, "autor"),
    ("Riego (original)", "orig", 160 / 3600, 0.0, 0.5, 65.0, 0.030, 10.197, {}, "autor"),
    # --- caso con TUBERÍAS FINALES (itemizado Rev. 1 / EETT); Di y piezas: SUPUESTO ---
    ("Aguas servidas (PVC 50)", "final", Q_LLENADO, 0.0, 5.0, 95.0, 0.0452, 0.0, {"codo90": 6, "retencion": 1, "tee": 2}, "itemizado 1.1.5"),
    ("Estero (PVC 25)", "final", Q_LLENADO, 6.0, 5.0, 140.0, 0.0220, 0.0, {"codo90": 6, "retencion": 1, "tee": 2}, "itemizado 1.2.5"),
    ("Agroquímicos (PVC 25)", "final", Q_LLENADO, 0.0, 5.0, 80.0, 0.0220, 0.0, {"codo90": 6, "retencion": 1, "tee": 2}, "itemizado 1.3.1"),
    ("Riego (PVC 25)", "final", 160 / 3600, 0.0, 0.5, 65.0, 0.0220, 10.197, {"codo90": 4, "tee": 3}, "EETT sector 3"),
]

resultados = []
for nombre, caso, q_ls, zs, zi, L, D, hp, piezas, fuente in LINEAS:
    Q = q_ls / 1000
    V = Q / (3.1416 * D**2 / 4)
    L_total = zs + zi + L  # criterio del autor: suma la succión y la impulsión vertical a la longitud
    hf = hf_hw(Q, D, L_total)
    hs = sum(K[p] * n for p, n in piezas.items()) * V**2 / (2 * g)
    adt = zs + zi + hf + hs + hp
    resultados.append(dict(linea=nombre, caso=caso, Q_ls=q_ls, Q_lmin=q_ls * 60, D_mm=D * 1000, L_m=L, V_ms=V,
                           hf_m=hf, hs_m=hs, z_m=zs + zi, presion_m=hp, ADT_m=adt, fuente=fuente))

# Verificación contra catálogos
for r in resultados:
    ok = []
    for modelo in CATALOGO:
        h = H_catalogo(modelo, r["Q_lmin"])
        if h is not None and h >= r["ADT_m"]:
            ok.append(f"{modelo} ({h:.1f} m)")
    r["bombas_que_cumplen"] = "; ".join(ok) if ok else "ninguna dentro de su curva publicada"

RES.mkdir(parents=True, exist_ok=True)
with open(RES / "bombas_adt.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(resultados[0])); w.writeheader()
    w.writerows({k: (round(v, 3) if isinstance(v, float) else v) for k, v in r.items()} for r in resultados)

# =============================================================================
# CASO ADOPTADO (preguntas 3 y 4, decisión del autor 20-11-2026)
# Llenado de 1000 L en <= 60 min (30 min deseable). Cota de llegada 125,27 m s.n.m. en las tres líneas.
# Desniveles: estero 111,45 -> 125,27 (13,82 m, plano 2.1); agroquímicos y aguas servidas con nivel del agua
# SUPUESTO 2 m bajo la tapa de la fosa (120,85 y 118,7 m) -> 6,4 y 8,6 m. Punto de operación con la JSWm 1A.
# =============================================================================
PIEZAS = {"codo90": 6, "retencion": 1, "tee": 2}
ADOPTADO = [("Estero", "PVC 25", 140.0, 0.0220, 13.82), ("Agroquímicos", "PVC 25", 80.0, 0.0220, 6.4),
            ("Aguas servidas", "PVC 50", 95.0, 0.0452, 8.6)]


def H_bomba(q):
    for (q1, h1), (q2, h2) in zip(PEDROLLO_1A, PEDROLLO_1A[1:]):
        if q1 <= q <= q2:
            return h1 + (h2 - h1) * (q - q1) / (q2 - q1)
    return None


def H_sistema(q, L, D, dz):
    Q = q / 60000
    V = Q / (3.1416 * D**2 / 4)
    return dz + hf_hw(Q, D, L) + sum(K[p] * n for p, n in PIEZAS.items()) * V**2 / (2 * g)


adoptado = []
for nombre, tubo, L, D, dz in ADOPTADO:
    q = 0.1
    while q < PEDROLLO_1A[-1][0] and H_bomba(q) > H_sistema(q, L, D, dz):
        q += 0.01
    borde = q >= PEDROLLO_1A[-1][0] - 0.01
    adoptado.append(dict(linea=nombre, tubo=tubo, L_m=L, Di_mm=D * 1000, dz_m=dz,
                         ADT_33_m=H_sistema(1000 / 30, L, D, dz), Q_op_lmin=q, H_op_m=H_bomba(q),
                         t_llenado_min=1000 / q, borde_curva=borde))
with open(RES / "bombas_punto_operacion.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(adoptado[0])); w.writeheader()
    w.writerows({k: (round(v, 2) if isinstance(v, float) else v) for k, v in r.items()} for r in adoptado)

filas = []
for r in adoptado:
    pre = r"$\geq$\," if r["borde_curva"] else ""
    pre_t = r"$\leq$\," if r["borde_curva"] else ""
    filas.append(rf"  {r['linea']} & {r['tubo']} ({r['Di_mm']:.1f}) & \num{{{r['L_m']:.0f}}} & \num{{{r['dz_m']:.2f}}} & "
                 rf"\num{{{r['ADT_33_m']:.1f}}} & {pre}\num{{{r['Q_op_lmin']:.0f}}} & {pre_t}\num{{{r['t_llenado_min']:.0f}}} \\")
TABLA.parent.mkdir(parents=True, exist_ok=True)
TABLA.write_text("\n".join([
    "% Archivo GENERADO por 04_analisis/scripts/11_bombas.py — no editar a mano",
    r"\begin{tabular}{@{}lcccccc@{}}",
    r"  \toprule",
    r"  Línea & Tubería ($D_i$, \unit{\milli\meter}) & $L$ (\unit{\meter}) & $\Delta z$ (\unit{\meter}) & ADT a \qty{33.3}{\liter\per\minute} (\unit{\meter}) & $Q$ de operación (\unit{\liter\per\minute}) & Llenado de \qty{1000}{\liter} (\unit{\minute}) \\",
    r"  \midrule", *filas, r"  \bottomrule",
    r"  \multicolumn{7}{@{}p{0.97\textwidth}@{}}{\footnotesize Hazen-Williams con $C_{HW} = 140$ y pérdidas singulares de 6 codos, 1 válvula de retención y 2 tees. Punto de operación con la bomba periférica Pedrollo JSWm~1A (\qty{0.55}{\kilo\watt}). En aguas servidas el punto queda en el borde de la curva publicada (\qty{60}{\liter\per\minute}).}",
    r"\end{tabular}", ""]), encoding="utf-8")

# Figura de apoyo: curvas de catálogo y puntos requeridos
fig, ax = plt.subplots(figsize=(6.0, 3.6))
for modelo, pts in CATALOGO.items():
    ax.plot([p[0] for p in pts], [p[1] for p in pts], marker=".", lw=1, label=modelo)
for r in resultados:
    if r["caso"] == "final":
        ax.plot(r["Q_lmin"], r["ADT_m"], "k^", ms=6)
        ax.annotate(r["linea"].split(" (")[0], (r["Q_lmin"], r["ADT_m"]), fontsize=7, xytext=(4, 3), textcoords="offset points")
ax.set_xlabel("Caudal [L/min]"); ax.set_ylabel("Altura [m]"); ax.set_xlim(0, 600); ax.set_ylim(0, 30)
ax.legend(fontsize=6, ncol=2)
fig.savefig(RES / "bombas_catalogo_vs_requerido.pdf")

for r in adoptado:
    print(f"ADOPTADO {r['linea']:<15} ADT(33,3)={r['ADT_33_m']:.1f} m  Q_op={r['Q_op_lmin']:.1f} L/min  llenado={r['t_llenado_min']:.0f} min")
for r in resultados:
    print(f"{r['linea']:<26} Q={r['Q_lmin']:6.1f} L/min D={r['D_mm']:5.1f} mm V={r['V_ms']:4.2f} m/s "
          f"hf={r['hf_m']:6.2f} hs={r['hs_m']:5.2f} ADT={r['ADT_m']:6.2f} m -> {r['bombas_que_cumplen']}")
