"""Ejemplo del patrón de trabajo de 04_analisis.

1. Define (o lee) datos.
2. Calcula.
3. Guarda la figura en tesis/figuras/ (PDF vectorial) con el estilo de la tesis.
4. Exporta una tabla LaTeX en tesis/tablas/.
5. Usa SymPy para obtener la ecuación en LaTeX sin transcribirla a mano.

Ejecutar desde la raíz del repo:  python 04_analisis/scripts/ejemplo_figura.py
(o `make figuras`)
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import sympy as sp

RAIZ = Path(__file__).resolve().parents[2]
FIGURAS = RAIZ / "tesis" / "figuras"
TABLAS = RAIZ / "tesis" / "tablas"
plt.style.use(Path(__file__).with_name("estilo_tesis.mplstyle"))


def coma(x: float, dec: int = 2) -> str:
    """Formatea un número con coma decimal (estilo español)."""
    return f"{x:.{dec}f}".replace(".", ",")


# --- 1. Datos: oscilador de 1 GDL en vibración libre amortiguada ---
periodo = 0.5          # s
xi = 0.05              # razón de amortiguamiento
u0 = 1.0               # cm, desplazamiento inicial

# --- 2. Cálculo simbólico con SymPy (la ecuación queda lista para LaTeX) ---
t, wn, z, U0 = sp.symbols("t omega_n xi u_0", positive=True)
wd = wn * sp.sqrt(1 - z**2)
u_sym = U0 * sp.exp(-z * wn * t) * (sp.cos(wd * t) + z / sp.sqrt(1 - z**2) * sp.sin(wd * t))
print("Ecuación en LaTeX:\n  u(t) =", sp.latex(u_sym))

u_num = sp.lambdify(t, u_sym.subs({wn: 2 * np.pi / periodo, z: xi, U0: u0}), "numpy")
tt = np.linspace(0, 3, 600)
uu = u_num(tt)

# --- 3. Figura ---
fig, ax = plt.subplots()
ax.plot(tt, uu, label=rf"$\xi = {coma(xi)}$")
ax.plot(tt, u0 * np.exp(-xi * 2 * np.pi / periodo * tt), "k--", lw=0.8, label="Envolvente")
ax.set_xlabel("Tiempo $t$ [s]")
ax.set_ylabel("Desplazamiento $u$ [cm]")
ax.legend()
# Coma decimal en los ejes (estilo español)
for eje in (ax.xaxis, ax.yaxis):
    eje.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}".replace(".", ",")))
FIGURAS.mkdir(parents=True, exist_ok=True)
fig.savefig(FIGURAS / "ejemplo_vibracion.pdf")

# --- 4. Tabla LaTeX (booktabs + siunitx) ---
filas = []
for xi_i in (0.02, 0.05, 0.10):
    reduccion = 1 - np.exp(-2 * np.pi * xi_i / np.sqrt(1 - xi_i**2))
    filas.append(rf"  \num{{{xi_i}}} & \num{{{reduccion * 100:.1f}}} \\")
tabla = "\n".join([
    r"% Archivo GENERADO por 04_analisis/scripts/ejemplo_figura.py — no editar a mano",
    r"\begin{tabular}{cc}",
    r"  \toprule",
    r"  Amortiguamiento $\xi$ & Reducción de amplitud por ciclo [\%] \\",
    r"  \midrule",
    *filas,
    r"  \bottomrule",
    r"\end{tabular}",
    "",
])
TABLAS.mkdir(parents=True, exist_ok=True)
(TABLAS / "ejemplo_tabla.tex").write_text(tabla, encoding="utf-8")
print("Listo: figura y tabla generadas.")
