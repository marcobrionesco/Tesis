"""Comparación del coeficiente sísmico y de la estabilidad de las zapatas: NCh2369:2003 (fórmula simplificada del
cálculo original, C = 2,7·A0/R) frente a NCh2369:2025 (espectro de diseño, 5.4; corte mínimo 5.12 y máximo 5.13).

Criterio de zapatas (NCh2369:2025, 10.1): con combinaciones ASD (0,70·E), al menos 80 % del área apoyada.
Longitud apoyada con e > B/6: 3(B/2 − e) (Das, 2015, 16.7) ⇒ 80 % ⇔ e ≤ 0,233·B.

SUPUESTOS (declarados en la tesis): zona 2 (A0 = 0,30 g, Ar = 1,4·A0); R = 3, ξ = 0,02 (marco a momento soldado
sin anclajes dúctiles); período de pilares en voladizo T ≈ 0,21 s (6 pilares) y 0,36 s (2 pilares); peso sísmico y
carga del pilar central de 10_estructura.py (W = 42,6 kN; N = D + 0,75 SO = 22,0 kN); H = 2,25 m; zapata 1,0 × 1,0 × 0,5 m.
"""
import csv
from pathlib import Path

RES = Path(__file__).resolve().parents[1] / "resultados"
SUELOS = {"B": (1.00, 4.5, 0.30, 1.60, 3.0, 0.27), "C": (1.05, 4.5, 0.40, 1.50, 3.0, 0.35),
          "D": (1.00, 3.5, 0.60, 1.00, 2.5, 0.41)}       # S, r, T0, p, q, T1 (Tabla 6)
A0, R, XI = 0.30, 3.0, 0.02
AR = 1.4 * A0
import json as _json
_cg = _json.loads((Path(__file__).resolve().parents[1] / "resultados" / "estructura_cargas.json").read_text(encoding="utf-8"))
# Pilar central, combinación ASD D + 0,75 SO + 0,70 E (NCh2369:2025, 4.5.1)
P_SERV = 10 / 8 * _cg["wD_p"] * _cg["Lv"] + _cg["peso_zap"] + _cg["peso_pilar"] + 0.75 * 10 / 8 * _cg["wL_p"] * _cg["Lv"]
W, H, HZ, B = _cg["W_sismico"], 2.25, 0.50, 1.00
T_PILARES = {6: 0.21, 2: 0.36}


def c_2025(I, suelo, T):
    S, r, T0, p, q, T1 = SUELOS[suelo]
    SaH = AR * S * (1 + r * (T / T0) ** p) / (1 + (T / T0) ** q)
    Cr = 0.16 * R
    Rs = R if T >= Cr * T1 else 1.5 + (R - 1.5) * T / (Cr * T1)
    C = I * SaH / Rs * (0.05 / XI) ** 0.4
    Cmin = 0.25 * I * AR * S
    Cmax = 2.75 * I * AR * S / (R + 1) * (0.05 / XI) ** 0.4
    return min(max(C, Cmin), Cmax)


def zapata(C, n, factor_E):
    V = C * W
    M = factor_E * V * H / n * (H + HZ) / H          # momento por pilar llevado al sello
    e = M / P_SERV
    if e >= B / 2:
        return V, e, None
    apoyo = 1.0 if e <= B / 6 else 3 * (B / 2 - e) / B
    return V, e, apoyo


filas = []
for n in (2, 6):
    filas.append(("2003", "—", "—", n, 2.7 * A0 / R, 1.0))
for I in (0.8, 1.0):
    for suelo in SUELOS:
        for n in (2, 6):
            filas.append(("2025", I, suelo, n, c_2025(I, suelo, T_PILARES[n]), 0.70))

RES.mkdir(parents=True, exist_ok=True)
with open(RES / "sismo_2003_vs_2025.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["norma", "I", "suelo", "pilares", "C", "V_kN", "e_m", "area_apoyada", "cumple_80"])
    for norma, I, suelo, n, C, fE in filas:
        V, e, ap = zapata(C, n, fE)
        w.writerow([norma, I, suelo, n, round(C, 3), round(V, 1), round(e, 3),
                    "vuelca" if ap is None else round(ap, 2), ap is not None and ap >= 0.80])
        print(f"{norma} I={I} suelo={suelo} {n} pilares: C={C:.3f} V={V:.1f} kN e={e:.2f} m "
              f"apoyo={'vuelca' if ap is None else f'{ap:.0%}'}")


# =============================================================================
# CASO ADOPTADO, POR POSICIÓN DEL PILAR (central / esquina) Y MODELO DEL PILAR
# Combinaciones ASD de la NCh2369:2025 (4.5.1) para fundaciones (10.1):
#   (1) D + 0,75 SO + 0,70 E   (estanques llenos; SO = contenido de los estanques)
#   (2) D + 0,70 E             (estanques vacíos; masa sísmica sin agua)
# Modelos del pilar: voladizo empotrado (momento en la base = F·H, conservador) y marco a momento soldado
# (R = 3, sistema adoptado): punto de inflexión a media altura (método del portal) -> momento en la base = F·H/2.
# Reacciones de la viga principal continua de 2 vanos: central 10/8·w·L; esquina 3/8·w·L.
# =============================================================================
import json
cg = json.loads((RES / "estructura_cargas.json").read_text(encoding="utf-8"))
C_ad = c_2025(0.8, "C", T_PILARES[6])
W_lleno = cg["W_sismico"]
W_vacio = cg["W_sismico"] - cg["n_estanques"] * (cg["P_est"] - cg["m_vacio_kN"])
filas_ad = []
for pos, k in (("central", 10 / 8), ("esquina", 3 / 8)):
    D = k * cg["wD_p"] * cg["Lv"] + cg["peso_zap"] + cg["peso_pilar"]
    SO = k * (cg["wL_p"] * cg["Lv"])
    SO_vacio = k * cg["n_estanques"] * cg["m_vacio_kN"] / (2 * 5.0) * cg["Lv"]
    for modelo, brazo in (("voladizo", cg["H"]), ("marco", cg["H"] / 2)):
        for comb, N, Wsis in (("D+0,75SO+0,70E", D + 0.75 * SO, W_lleno), ("D+0,70E (vacíos)", D + SO_vacio, W_vacio)):
            F = C_ad * Wsis / 6
            M = 0.70 * F * (brazo + cg["hz"])
            e = M / N
            ap = 1.0 if e <= cg["B"] / 6 else (3 * (cg["B"] / 2 - e) / cg["B"] if e < cg["B"] / 2 else 0.0)
            filas_ad.append((pos, modelo, comb, round(N, 1), round(e, 3), round(ap, 2)))
with open(RES / "zapatas_por_pilar.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["pilar", "modelo", "combinacion", "N_kN", "e_m", "area_apoyada"]); w.writerows(filas_ad)
print("\nCaso adoptado por pilar (C = %.3f):" % C_ad)
for r in filas_ad:
    print("  %-8s %-9s %-18s N = %5.1f kN  e = %.3f m  apoyo = %3.0f %%" % (r[0], r[1], r[2], r[3], r[4], r[5] * 100))
