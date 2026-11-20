"""Verificación estructural de la plataforma de estanques — versión actualizada.

Basada en el cálculo original del autor (02_material_bruto/calculos_originales/2026_yo_diseno-estructura-colab.py),
con las DIMENSIONES FINALES de las láminas 3.1–3.2, las EETT y el itemizado Rev. 1, y con las
verificaciones LRFD de AISC 360-16 (perfiles tubulares, capítulos E, F, G y H) aplicadas de forma
consistente.

Diferencias con el cálculo original (ver 04_analisis/README.md):
- Geometría: plataforma 5,00 × 2,00 m (no 5,50 × 3,00), vanos de 2,28 m (no 2,75), vigas
  secundarias de 1,70 m de luz (no 3,00) y estanques de 1000 L (no 785 L).
- Perfiles finales: pilares y vigas principales 150×150×6; vigas secundarias 150×100×3.
- Cada viga principal recibe la mitad de la carga de los estanques (el original cargaba una sola viga con el total).
- El pilar se verifica con LRFD (E3 + H1-1); el original mezclaba tensiones admisibles con cargas mayoradas.
- La combinación sísmica usa 1,2D + 1,0L + 1,4E (tabla 2.2 de la tesis); la zona sísmica queda como parámetro.

Todo dato marcado "SUPUESTO" debe confirmarse antes de llevar los resultados a la versión final.
Ejecutar desde la raíz del repo:  python 04_analisis/scripts/10_estructura.py
"""
import csv
import math
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
RES = RAIZ / "04_analisis/resultados"
TABLA = RAIZ / "tesis/tablas/verificacion_estructural.tex"

# =============================================================================
# 1. PARÁMETROS (fuente entre corchetes)
# =============================================================================
g = 9.81
P = dict(
    largo=5.00, ancho=2.00,            # m   [lámina 3.2]
    vano_long=2.28,                    # m   [lámina 3.1: pilares a 2,28 m, 3 por lado]
    luz_sec=1.70,                      # m   [lámina 3.1: separación transversal de pilares]
    sep_sec=0.40,                      # m   [lámina 3.2: vigas secundarias cada 0,40 m]
    H_pilar=2.25,                      # m   [lámina 3.1]
    n_pilares=6,                       # [lámina 3.2]
    V_estanque=1.000,                  # m3  [EETT / itemizado: 3 estanques de 1000 L]
    n_estanques=3,
    D_estanque=1.00,                   # m   [lámina 3.2]
    m_estanque_vacio=40.0,             # kg  [SUPUESTO del cálculo original]
    q_tablero=0.50,                    # kN/m2 D [SUPUESTO del cálculo original: tablero + fijaciones]
    t_tablero=0.015,                   # m   [EETT: tablero fenólico 15 mm]
    E_madera=11.0e6,                   # kN/m2 [SUPUESTO del cálculo original, pino radiata]
    K_def_madera=2.0,                  # [SUPUESTO del cálculo original, fluencia lenta]
    E=2.1e8, Fy=250e3,                 # kN/m2 [cálculo original; A270ES — verificar Fy en NCh203]
    gamma_acero=77.0,                  # kN/m3
    K_pilar=2.1,                       # [cálculo original: pilar en voladizo, sin arriostrar]
    A0_zona={2: 0.30},                 # g   [NCh2369:2025, Tabla 2: Linares en zona 2]
    R1=3.0,                            # [SUPUESTO del cálculo original]
    n_pilares_sismo=2,                 # [SUPUESTO conservador del cálculo original: un marco toma el corte]
    zapata=(1.00, 1.00, 0.50),         # m   [lámina 3.2 / EETT]
    gamma_hormigon=24.0,               # kN/m3
    q_adm=150.0,                       # kPa [SUPUESTO del cálculo original — sin estudio de suelos]
    placa=(0.300, 0.016), dist_pernos=0.22, A_perno=285e-6, Fu_perno=550e3,  # [EETT / cálculo original]
    fc=25e3,                           # kN/m2 [cálculo original G25; EETT dice G30 — por unificar]
)


def tubo(B, H, t):
    """Propiedades de un perfil cajón B (ancho) × H (alto) × t (m), eje fuerte."""
    bi, hi = B - 2 * t, H - 2 * t
    A = B * H - bi * hi
    Ix = (B * H**3 - bi * hi**3) / 12
    Zx = (B * H**2 - bi * hi**2) / 4
    return dict(B=B, H=H, t=t, A=A, Ix=Ix, Sx=2 * Ix / H, Zx=Zx, r=math.sqrt(Ix / A))


def flexion(s):
    """phi*Mn de un perfil cajón (AISC F7), con control de esbeltez del ala."""
    E, Fy = P["E"], P["Fy"]
    lam = (s["B"] - 3 * s["t"]) / s["t"]
    lp, lr = 1.12 * math.sqrt(E / Fy), 1.40 * math.sqrt(E / Fy)
    Mp = Fy * s["Zx"]
    Mn = Mp if lam <= lp else Mp - (Mp - Fy * s["Sx"]) * (3.57 * lam * math.sqrt(Fy / E) - 4.0)
    return 0.9 * min(Mn, Mp), ("compacta" if lam <= lp else "no compacta" if lam <= lr else "esbelta"), lam


def corte(s):
    """phi*Vn de un perfil cajón (AISC G4, kv = 5)."""
    h = s["H"] - 3 * s["t"]
    E, Fy = P["E"], P["Fy"]
    Cv2 = 1.0 if h / s["t"] <= 1.10 * math.sqrt(5 * E / Fy) else 1.10 * math.sqrt(5 * E / Fy) / (h / s["t"])
    return 0.9 * 0.6 * Fy * (2 * h * s["t"]) * Cv2


def compresion(s, KL):
    """phi*Pn (AISC E3)."""
    E, Fy = P["E"], P["Fy"]
    esb = KL / s["r"]
    Fe = math.pi**2 * E / esb**2
    Fcr = (0.658 ** (Fy / Fe)) * Fy if esb <= 4.71 * math.sqrt(E / Fy) else 0.877 * Fe
    return 0.9 * Fcr * s["A"], esb


filas = []  # (elemento, perfil, verificación, demanda, capacidad, unidad, razón)


def registrar(elem, perfil, verif, dem, cap, unid):
    filas.append((elem, perfil, verif, dem, cap, unid, dem / cap))


# =============================================================================
# 2. CARGAS
# =============================================================================
m_agua = P["V_estanque"] * 1000
P_est = (m_agua + P["m_estanque_vacio"]) * g / 1000                        # kN por estanque
A_apoyo = math.pi * P["D_estanque"] ** 2 / 4                               # m2 (base circular)
viga_p, viga_s = tubo(0.150, 0.150, 0.006), tubo(0.100, 0.150, 0.003)

# =============================================================================
# 3. TABLERO DE MADERA: lámina continua sobre las vigas secundarias (pregunta 2, decisión del autor 20-11-2026)
#    Franja de 1 m; carga = presión bajo la base del estanque lleno + tablero. Viga continua de Euler-Bernoulli
#    por elementos finitos (20 elementos por vano). Diseño: 3 apoyos (2 vanos cargados, el caso más desfavorable).
#    k_def = 2,0: clase de servicio 3 (intemperie), EN 1995-1-1 para madera aserrada [fuente por citar].
# =============================================================================
w_tab = P_est / A_apoyo + P["q_tablero"]                                   # kN/m2
I_tab = 1.0 * P["t_tablero"] ** 3 / 12


def flecha_continua(n_vanos, L, w, EI, x_carga=None, ne=20):
    """Deflexión máxima (m) de una viga continua de n_vanos iguales; carga w en [x0, x1] (todo si None)."""
    import numpy as np
    n = n_vanos * ne
    le = L / ne
    K = np.zeros((2 * n + 2, 2 * n + 2)); F = np.zeros(2 * n + 2)
    k = EI / le**3 * np.array([[12, 6*le, -12, 6*le], [6*le, 4*le**2, -6*le, 2*le**2],
                               [-12, -6*le, 12, -6*le], [6*le, 2*le**2, -6*le, 4*le**2]])
    x0, x1 = x_carga if x_carga else (0.0, n_vanos * L)
    for e in range(n):
        idx = [2*e, 2*e+1, 2*e+2, 2*e+3]
        K[np.ix_(idx, idx)] += k
        xc = (e + 0.5) * le
        if x0 <= xc <= x1:
            F[idx] += w * np.array([le/2, le**2/12, le/2, -le**2/12])
    fijos = [2 * (i * ne) for i in range(n_vanos + 1)]
    libres = [i for i in range(2 * n + 2) if i not in fijos]
    u = np.zeros(2 * n + 2)
    u[libres] = np.linalg.solve(K[np.ix_(libres, libres)], F[libres])
    return max(abs(u[0::2]))


EI_tab = P["E_madera"] * I_tab
sep_tab = P["sep_sec"]
d_tab_1v = 5 * w_tab * sep_tab**4 / (384 * EI_tab) * P["K_def_madera"]           # modelo original (un vano)
d_tab = flecha_continua(2, sep_tab, w_tab, EI_tab) * P["K_def_madera"]            # diseño: 3 apoyos
sens_tablero = {f"{nv} vanos": flecha_continua(nv, sep_tab, w_tab, EI_tab,
                (nv * sep_tab / 2 - 0.5, nv * sep_tab / 2 + 0.5)) * P["K_def_madera"] for nv in (3, 5, 8)}
registrar("Tablero", "15 mm", "Deflexión largo plazo (continuo, $L/300$)", d_tab * 1000, sep_tab / 300 * 1000, "mm")

# =============================================================================
# 4. VIGA SECUNDARIA 150×100×3 (luz 1,70 m, carga puntual = 50 % de un estanque)
# =============================================================================
L = P["luz_sec"]
wD = P["q_tablero"] * P["sep_sec"] + P["gamma_acero"] * viga_s["A"]
PL = 0.5 * P_est
Mu = 1.2 * wD * L**2 / 8 + 1.6 * PL * L / 4
Vu = 1.2 * wD * L / 2 + 1.6 * PL / 2
fMn, clase_s, _ = flexion(viga_s)
registrar("Viga secundaria", "150×100×3", "Flexión", Mu, fMn, "kN·m")
registrar("Viga secundaria", "150×100×3", "Corte", Vu, corte(viga_s), "kN")
d_s = 5 * wD * L**4 / (384 * P["E"] * viga_s["Ix"]) + PL * L**3 / (48 * P["E"] * viga_s["Ix"])
registrar("Viga secundaria", "150×100×3", "Deflexión (L/300)", d_s * 1000, L / 300 * 1000, "mm")

# =============================================================================
# 5. VIGA PRINCIPAL 150×150×6 (continua de 2 vanos de 2,28 m; cada viga toma la mitad)
# =============================================================================
Lv = P["vano_long"]
n_sec = round(P["largo"] / P["sep_sec"]) + 1
peso_sec_total = n_sec * P["luz_sec"] * P["gamma_acero"] * viga_s["A"]
wD_p = (P["q_tablero"] * P["ancho"] * P["largo"] + peso_sec_total) / (2 * P["largo"]) + P["gamma_acero"] * viga_p["A"]
wL_p = P["n_estanques"] * P_est / (2 * P["largo"])
wu = 1.2 * wD_p + 1.6 * wL_p
Mu_p = wu * Lv**2 / 8                       # momento negativo sobre el pilar central (gobierna)
Vu_p = 5 * wu * Lv / 8
fMn_p, clase_p, lam_p = flexion(viga_p)
registrar("Viga principal", "150×150×6", "Flexión", Mu_p, fMn_p, "kN·m")
registrar("Viga principal", "150×150×6", "Corte", Vu_p, corte(viga_p), "kN")
d_p = (wD_p + wL_p) * Lv**4 / (185 * P["E"] * viga_p["Ix"])               # flecha máx. de viga de 2 vanos
registrar("Viga principal", "150×150×6", "Deflexión (L/300)", d_p * 1000, Lv / 300 * 1000, "mm")

# =============================================================================
# 6. PILAR CENTRAL 150×150×6 (voladizo, K = 2,1) — gravitacional y sísmico
# =============================================================================
RD = 1.25 * wD_p * Lv                       # reacción central (10/8·w·L) por carga muerta
RL = 1.25 * wL_p * Lv
peso_pilares = P["n_pilares"] * P["H_pilar"] * P["gamma_acero"] * viga_p["A"]
W_sismico = (P["n_estanques"] * P_est + 2 * wD_p * P["largo"] + peso_pilares / 2)   # masa en la cubierta
fPn, esb = compresion(viga_p, P["K_pilar"] * P["H_pilar"])
fMn_c = flexion(viga_p)[0]
Pu_grav = 1.2 * RD + 1.6 * RL
registrar("Pilar central", "150×150×6", "Compresión (1,2D+1,6L)", Pu_grav, fPn, "kN")
sismo = {}
# NCh2369:2025 (pregunta 1, decisión del autor): categoría I (I = 0,8), suelo C supuesto, R = 3, xi = 0,02 (soldado);
# período con pilares en voladizo y tablero como diafragma rígido (verificado abajo) -> 6 pilares comparten el corte.
SUELO_C = (1.05, 4.5, 0.40, 1.50, 3.0, 0.35)        # S, r, T0, p, q, T1 (Tabla 6)


def c_2025(A0, I=0.8, R=3.0, xi=0.02, T=0.21, suelo=SUELO_C):
    S, r, T0, p, q, T1 = suelo
    Ar = 1.4 * A0
    SaH = Ar * S * (1 + r * (T / T0) ** p) / (1 + (T / T0) ** q)
    Cr = 0.16 * R
    Rs = R if T >= Cr * T1 else 1.5 + (R - 1.5) * T / (Cr * T1)
    C = I * SaH / Rs * (0.05 / xi) ** 0.4
    return min(max(C, 0.25 * I * Ar * S), 2.75 * I * Ar * S / (R + 1) * (0.05 / xi) ** 0.4)


for zona, A0 in P["A0_zona"].items():
    C = c_2025(A0)
    V = C * W_sismico
    F_col = V / P["n_pilares"]                       # 6 pilares con diafragma
    M_E = F_col * P["H_pilar"]
    casos = []
    for Pu in (1.2 * RD + 1.0 * RL, 0.9 * RD + 1.0 * RL):   # 1,2D + SO + E y 0,9D + SO + E (E sin mayorar, NCh2369:2025)
        Mu_c = 1.0 * M_E
        r = Pu / fPn + (8 / 9) * Mu_c / fMn_c if Pu / fPn >= 0.2 else Pu / (2 * fPn) + Mu_c / fMn_c
        casos.append((r, Pu, Mu_c))
    r, Pu, Mu_c = max(casos)
    sismo[zona] = dict(C=C, V=V, M_E=M_E, Pu=Pu, Mu=Mu_c, interaccion=r)
    filas.append(("Pilar central", "150×150×6", f"Flexocompresión sísmica (NCh2369:2025)", r, 1.0, "—", r))

# Diafragma (NCh2369:2025, 5.3.3): flexible si su deformación en el plano > 2 × desplazamiento medio de los pilares.
# Tablero de 15 mm como viga de gran altura (2,0 m) entre líneas de pilares (2,28 m), deformación por corte;
# G del tablero SUPUESTO (0,5 GPa; se prueba también 0,05 GPa).
s0 = sismo[min(sismo)]
w_diaf = s0["V"] / P["largo"]                                   # kN/m
d_pilar = (s0["V"] / P["n_pilares"]) * P["H_pilar"] ** 3 / (3 * P["E"] * viga_p["Ix"])
diafragma = {}
for G_tab in (0.5e6, 0.05e6):                                   # kN/m2
    d_diaf = w_diaf * P["vano_long"] ** 2 / (8 * G_tab * P["t_tablero"] * P["ancho"])
    diafragma[G_tab] = d_diaf
# =============================================================================
# 7. ZAPATA 1,00 × 1,00 × 0,50 m (presión de contacto en servicio, sismo sin mayorar)
# =============================================================================
Bz, Lz, hz = P["zapata"]
peso_zap = Bz * Lz * hz * P["gamma_hormigon"]
P_serv = RD + RL + peso_zap + P["H_pilar"] * P["gamma_acero"] * viga_p["A"]
q_est = P_serv / (Bz * Lz)
registrar("Zapata", "1,0×1,0×0,5 m", "Presión estática", q_est, P["q_adm"], "kPa")
for zona, s in sismo.items():
    M_serv = s["M_E"] * (P["H_pilar"] + hz) / P["H_pilar"]                 # momento llevado al sello
    e = M_serv / P_serv
    s.update(e=e)
    # La estabilidad sísmica de la zapata se verifica con la NCh2369:2025 en 14_sismo_2003_vs_2025.py
    # (pregunta 1: 6 pilares con diafragma, categoría I, suelo C -> 91 % de área apoyada).

# =============================================================================
# 8. PLACA BASE Y PERNOS (método del autor, sismo de la zona más exigente)
# =============================================================================
s3 = sismo[max(sismo)]
lp, tp = P["placa"]
fp = s3["Pu"] / lp**2 + s3["Mu"] / (lp**3 / 6)
m = (lp - 0.150) / 2
t_req = math.sqrt(4 * fp * m**2 / 2 / (0.9 * P["Fy"]))
registrar("Placa base", "300×300×16 mm", "Espesor requerido", t_req * 1000, tp * 1000, "mm")
T_perno = max(0.0, (s3["Mu"] / P["dist_pernos"] - s3["Pu"] / 2) / 2)
phiTn = 0.75 * 0.75 * P["Fu_perno"] * P["A_perno"]
registrar("Pernos de anclaje", "4 × Ø 3/4\"", "Tracción por perno", T_perno, phiTn, "kN")

# =============================================================================
# 8b. ESTRUCTURA AUXILIAR DE LOS DOSIFICADORES (pregunta 12, decisión del autor 20-11-2026)
#     Tres marcos independientes (uno por dosificador): 0,75 × 0,95 m en planta, 1,50 m de alto, 4 columnas y 4 barras
#     superiores de perfil 15 × 15 × 6 mm (pared gruesa: casi macizo). Carga de OPERACIÓN: volumen de un pulso
#     (120 kg de agua, dato del autor) + 15 kg de tanque y sifón (SUPUESTO). ASD, Fy = 250 MPa (SUPUESTO).
# =============================================================================
b_aux, t_aux, L_col = 0.015, 0.006, 1.50
I_aux = (b_aux**4 - (b_aux - 2 * t_aux) ** 4) / 12
A_aux = b_aux**2 - (b_aux - 2 * t_aux) ** 2
S_aux = I_aux / (b_aux / 2)
r_aux = math.sqrt(I_aux / A_aux)
W_aux = (120 + 15) * g / 1000                       # kN por marco
P_barra = W_aux / 4                                 # kN por barra (4 barras)
sig_adm = 0.6 * P["Fy"]                             # kN/m2 (ASD)
aux = {}
for L_b in (0.75, 0.95):
    M_dist, M_punt = P_barra * L_b / 8, P_barra * L_b / 4
    aux[L_b] = dict(r_dist=M_dist / S_aux / sig_adm, r_punt=M_punt / S_aux / sig_adm,
                    f_dist=5 * P_barra * L_b**3 / (384 * P["E"] * I_aux), f_punt=P_barra * L_b**3 / (48 * P["E"] * I_aux))
registrar("Estructura auxiliar", "15×15×6", "Barra superior, carga distribuida (luz 0,95 m)",
          P_barra * 0.95 / 8 / S_aux / 1000, sig_adm / 1000, "MPa")
registrar("Estructura auxiliar", "15×15×6", "Barra superior, carga puntual (luz 0,95 m)",
          P_barra * 0.95 / 4 / S_aux / 1000, sig_adm / 1000, "MPa")
esb_aux = L_col / r_aux
Fe_aux = math.pi**2 * P["E"] / esb_aux**2
Pa_col = 0.877 * Fe_aux * A_aux / 1.67               # kN (AISC E3, pandeo elástico; ASD)
registrar("Estructura auxiliar", "15×15×6", "Columna, compresión (pandeo)", W_aux / 4, Pa_col, "kN")
# Estimación sísmica preliminar con el coeficiente de la torre (pregunta 1): C = 0,35; centro de gravedad a 1,9 m
W_sis_aux = W_aux + 0.25
F_aux = 0.35 * W_sis_aux
M_volc_aux, M_est_aux = F_aux * 1.9, W_sis_aux * 0.75 / 2

# Cargas por pilar para la verificación sísmica de zapatas (14_sismo_2003_vs_2025.py)
import json
RES.mkdir(parents=True, exist_ok=True)
(RES / "estructura_cargas.json").write_text(json.dumps(dict(
    wD_p=wD_p, wL_p=wL_p, Lv=Lv, peso_zap=peso_zap, peso_pilar=P["H_pilar"] * P["gamma_acero"] * viga_p["A"],
    W_sismico=W_sismico, P_est=P_est, m_vacio_kN=P["m_estanque_vacio"] * g / 1000, n_estanques=P["n_estanques"],
    H=P["H_pilar"], hz=hz, B=Bz), indent=1), encoding="utf-8")

# =============================================================================
# 9. SALIDAS
# =============================================================================
RES.mkdir(parents=True, exist_ok=True)
with open(RES / "estructura_verificacion.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["elemento", "perfil", "verificacion", "demanda", "capacidad", "unidad", "razon"])
    w.writerows([[a, b, c, round(d, 3), round(e, 3), u, round(r, 3)] for a, b, c, d, e, u, r in filas])

def num(x):
    return rf"\num{{{x:.2f}}}" if abs(x) < 100 else rf"\num{{{x:.0f}}}"

lineas = []
for elem, perfil, verif, dem, cap, unid, r in filas:
    u = "" if unid == "—" else f" {unid}"
    razon = rf"\num{{{r:.2f}}}" if r <= 1.0 else r"\textbf{" + f"{r:.2f}".replace(".", ",") + "}"
    lineas.append(f"  {elem} & {perfil} & {verif} & {num(dem)}{u} & {num(cap)}{u} & {razon} \\\\")
TABLA.parent.mkdir(parents=True, exist_ok=True)
TABLA.write_text("\n".join([
    "% Archivo GENERADO por 04_analisis/scripts/10_estructura.py — no editar a mano",
    r"\begin{tabular}{@{}>{\raggedright\arraybackslash}p{2.2cm}>{\raggedright\arraybackslash}p{2.3cm}>{\raggedright\arraybackslash}p{3.6cm}rrc@{}}",
    r"  \toprule",
    r"  Elemento & Perfil & Verificación & Demanda & Capacidad & Razón \\",
    r"  \midrule", *lineas, r"  \bottomrule",
    r"  \multicolumn{6}{@{}p{0.97\textwidth}@{}}{\footnotesize Razón = demanda/capacidad; en negrita, las que superan 1 (no cumple). Zona sísmica~2 (NCh2369:2025). Estructura auxiliar verificada con ASD.}",
    r"\end{tabular}", ""]), encoding="utf-8")

print(f"Diafragma: desplazamiento del pilar = {d_pilar*1000:.2f} mm; deformación del tablero = "
      + ", ".join(f"{d*1000:.2f} mm (G = {G/1e6:.2f} GPa)" for G, d in diafragma.items()) + f"; flexible si > {2*d_pilar*1000:.2f} mm")
print(f"Auxiliar: I = {I_aux*1e12:.0f} mm4, A = {A_aux*1e6:.0f} mm2, r = {r_aux*1000:.2f} mm, W = {W_aux:.2f} kN, KL/r = {esb_aux:.0f}, Pa = {Pa_col:.2f} kN")
for L_b, v in aux.items():
    print(f"  barra {L_b} m: razón distribuida {v['r_dist']:.2f} (flecha {v['f_dist']*1000:.1f} mm), puntual {v['r_punt']:.2f} (flecha {v['f_punt']*1000:.1f} mm)")
print(f"  sismo: F = {F_aux:.2f} kN, M vuelco = {M_volc_aux:.2f} kN·m, M estabilizante = {M_est_aux:.2f} kN·m")
print(f"Estanque lleno: {P_est:.2f} kN | carga sísmica W = {W_sismico:.1f} kN | KL/r pilar = {esb:.1f}")
print(f"Viga principal: ala {clase_p} (b/t = {lam_p:.1f}); viga secundaria: {clase_s}")
for z, s in sismo.items():
    print(f"Zona {z}: C = {s['C']:.3f}, V = {s['V']:.1f} kN, M_E pilar = {s['M_E']:.2f} kN·m (6 pilares; zapata en 14_sismo)")
for zona, s_ in []:
    M6 = s_["M_E"] * P["n_pilares_sismo"] / P["n_pilares"]
    e6 = M6 * (P["H_pilar"] + hz) / P["H_pilar"] / P_serv
    r6 = s_["Pu"] / fPn / 2 + 1.4 * M6 / fMn_c
    print(f"  zona {zona}: M_E = {M6:.2f} kN·m, interacción = {r6:.2f}, e zapata = {e6:.3f} m (B/6 = {Lz/6:.3f}, B/2 = {Lz/2:.2f})")
print(f"Tablero: un vano (original) = {d_tab_1v*1000:.2f} mm; continuo 3 apoyos = {d_tab*1000:.2f} mm; "
      + "; ".join(f"{k} = {v*1000:.2f} mm" for k, v in sens_tablero.items()) + f" (L/300 = {sep_tab/300*1000:.2f}; L/500 = {sep_tab/500*1000:.2f})")
print(f"{'Elemento':<18}{'Verificación':<36}{'Demanda':>10}{'Capacidad':>11}{'Razón':>8}")
for elem, perfil, verif, dem, cap, unid, r in filas:
    print(f"{elem:<18}{verif:<36}{dem:>10.2f}{cap:>11.2f}{r:>8.2f}  {'OK' if r <= 1 else 'NO CUMPLE'}")
