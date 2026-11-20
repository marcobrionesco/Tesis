"""Sensibilidad de la capacidad de soporte de la zapata a φ' (sin estudio de mecánica de suelos).

Terzaghi, zapata cuadrada: q_u = 1,3 c' N_c + q N_q + 0,4 γ B N_γ (Das, 2015, ec. 16.4, p. 482);
q_adm = q_u / FS, FS = 3 (Das, 2015, ec. 16.14 y ej. 16.1, p. 487–488).
Factores N de la Tabla 16.1 (Das, 2015, p. 483). Compacidad según Tabla 10.1 (p. 230).
SUPUESTOS (marcados en la tesis): suelo granular c' = 0, γ = 18 kN/m³, D_f = 0,50 m (altura de la zapata), sin napa.
"""
import csv
from pathlib import Path

RES = Path(__file__).resolve().parents[1] / "resultados"
# φ' : (N_c, N_q, N_γ) — Das (2015), Tabla 16.1
N = {28: (31.61, 17.81, 13.70), 29: (34.24, 19.98, 16.18), 30: (37.16, 22.46, 19.13),
     31: (40.41, 25.28, 22.65), 32: (44.04, 28.52, 26.87), 33: (48.09, 32.23, 31.94),
     34: (52.64, 36.50, 38.04), 35: (57.75, 41.44, 45.41), 36: (63.53, 47.16, 54.36)}
B, Df, gamma, c, FS = 1.00, 0.50, 18.0, 0.0, 3.0
q = gamma * Df


def compacidad(phi):
    return "suelto" if phi < 35 else "compacto"   # Tabla 10.1: suelto 30–35°, compacto 35–40°


filas = []
for phi, (Nc, Nq, Ng) in N.items():
    qu = 1.3 * c * Nc + q * Nq + 0.4 * gamma * B * Ng
    filas.append((phi, round(qu, 1), round(qu / FS, 1), compacidad(phi) if phi >= 30 else "muy suelto"))

RES.mkdir(parents=True, exist_ok=True)
with open(RES / "capacidad_soporte_sensibilidad.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["phi_grados", "q_u_kPa", "q_adm_kPa", "compacidad_tabla_10_1"]); w.writerows(filas)
for r in filas:
    print(f"φ' = {r[0]}°: q_u = {r[1]:6.1f} kPa, q_adm = {r[2]:6.1f} kPa ({r[3]})")
