"""Procesa la caracterización de afluentes (fase previa del proyecto ANID ATE250033).

Entrada : 04_analisis/datos/caracterizacion_afluentes.csv  (de 01_extraer_caracterizacion.py)
Salidas : tesis/tablas/caracterizacion_afluentes.tex   (tabla de medias por punto)
          tesis/figuras/caracterizacion_afluentes.pdf  (DQO, DBO5, SST y NH4+ por punto)
          04_analisis/resultados/caracterizacion_resumen.csv (n, media, mín., máx.)
          04_analisis/resultados/caudal_equivalente_carga.csv (apoyo a la distribución de caudales)

Criterios:
- Media aritmética para parámetros fisicoquímicos; media GEOMÉTRICA para coliformes
  (práctica habitual en microbiología). Valores censurados (<, >) se usan con su límite.
- n = número de campañas con dato (las celdas vacías o "-" no se cuentan).

Ejecutar desde la raíz del repo:  python 04_analisis/scripts/02_caracterizacion.py
"""
import csv
import math
import statistics
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parents[2]
DATOS = RAIZ / "04_analisis/datos/caracterizacion_afluentes.csv"
RES = RAIZ / "04_analisis/resultados"
TABLA = RAIZ / "tesis/tablas/caracterizacion_afluentes.tex"
FIG = RAIZ / "tesis/figuras/caracterizacion_afluentes.pdf"
plt.style.use(Path(__file__).with_name("estilo_tesis.mplstyle"))

PUNTOS = ["EST", "AS1", "AS2", "AGR1", "AGR2"]
N_TIPICO = {"EST": 6, "AS1": 6, "AS2": 2, "AGR1": 6, "AGR2": 6}
UNIDAD_TEX = {
    "-": "", "°C": r"(\unit{\degreeCelsius})", "µS/cm": r"(\unit{\micro\siemens\per\centi\meter})",
    "mV": r"(\unit{\milli\volt})", "mg/L": r"(\unit{\milli\gram\per\liter})", "NTU": "(NTU)",
    "NMP/100 mL": r"(NMP/\qty{100}{\milli\liter})",
}
NOMBRE_TEX = {"DBO5": r"DBO$_5$", "Amonio": r"Amonio (NH$_4^+$)", "Nitrato": r"Nitrato (NO$_3^-$)",
              "Fosfato": r"Fosfato (PO$_4^{3-}$)", "E. coli": r"\textit{E.~coli}"}
MICRO = ("Coliformes fecales", "E. coli")

# --- Lectura ---
datos = defaultdict(list)       # (parámetro, punto) -> valores
orden, unidades = [], {}
with open(DATOS, encoding="utf-8") as f:
    for r in csv.DictReader(f):
        if r["parametro"] not in unidades:
            orden.append(r["parametro"]); unidades[r["parametro"]] = r["unidad"]
        if r["valor"] != "":
            datos[(r["parametro"], r["punto"])].append(float(r["valor"]))


def resumen(par, pto):
    v = datos.get((par, pto), [])
    if not v:
        return None
    media = math.exp(statistics.mean(math.log(x) for x in v)) if par in MICRO else statistics.mean(v)
    return dict(n=len(v), media=media, min=min(v), max=max(v))


def fmt(x, par):
    if par in MICRO:
        e = math.floor(math.log10(x)); m = x / 10**e
        return rf"\num{{{m:.1f}e{e}}}"
    dec = 0 if abs(x) >= 100 else 1 if abs(x) >= 10 else 2
    return rf"\num{{{x:.{dec}f}}}"


# --- Resumen CSV ---
RES.mkdir(parents=True, exist_ok=True)
with open(RES / "caracterizacion_resumen.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["parametro", "unidad", "punto", "n", "media", "min", "max", "tipo_media"])
    for par in orden:
        for pto in PUNTOS:
            s = resumen(par, pto)
            if s:
                w.writerow([par, unidades[par], pto, s["n"], round(s["media"], 4), s["min"], s["max"],
                            "geométrica" if par in MICRO else "aritmética"])

# --- Tabla LaTeX ---
filas = []
for par in orden:
    celdas = []
    for pto in PUNTOS:
        s = resumen(par, pto)
        if not s:
            celdas.append("---"); continue
        txt = fmt(s["media"], par)
        if s["n"] != N_TIPICO[pto]:
            txt += rf"\textsuperscript{{({s['n']})}}"
        celdas.append(txt)
    nombre = NOMBRE_TEX.get(par, par) + (" " + UNIDAD_TEX[unidades[par]] if UNIDAD_TEX[unidades[par]] else "")
    filas.append(f"  {nombre} & " + " & ".join(celdas) + r" \\")
tabla = "\n".join([
    "% Archivo GENERADO por 04_analisis/scripts/02_caracterizacion.py — no editar a mano",
    r"\begin{tabular}{@{}>{\raggedright\arraybackslash}p{5.2cm}ccccc@{}}",
    r"  \toprule",
    r"  Parámetro & EST & AS1 & AS2 & AGR1 & AGR2 \\",
    r"  \midrule",
    *filas,
    r"  \bottomrule",
    r"  \multicolumn{6}{@{}p{0.97\textwidth}@{}}{\footnotesize Media aritmética de las campañas; coliformes: media geométrica. "
    r"$n = 6$ campañas por punto, salvo AS2 ($n = 2$); entre paréntesis, el $n$ cuando difiere. "
    r"EST: estero Batuco; AS1: oficinas; AS2: casa; AGR1: bodega de agroquímicos; AGR2: sala de bombas.}",
    r"\end{tabular}",
    "",
])
TABLA.parent.mkdir(parents=True, exist_ok=True)
TABLA.write_text(tabla, encoding="utf-8")

# --- Figura: parámetros de carga por punto (escala log, barras = rango) ---
pars = [("DQO total", "DQO"), ("DBO5", "DBO$_5$"), ("SST", "SST"), ("Amonio", "NH$_4^+$")]
fig, ax = plt.subplots(figsize=(6.0, 3.4))
ancho = 0.18
for i, (par, etq) in enumerate(pars):
    xs, ys, err = [], [], [[], []]
    for j, pto in enumerate(PUNTOS):
        s = resumen(par, pto)
        if s:
            xs.append(j + (i - 1.5) * ancho); ys.append(s["media"])
            err[0].append(s["media"] - s["min"]); err[1].append(s["max"] - s["media"])
    ax.bar(xs, ys, width=ancho, label=etq, yerr=err, capsize=2, error_kw=dict(lw=0.6))
ax.set_yscale("log")
ax.set_xticks(range(len(PUNTOS)), PUNTOS)
ax.set_ylabel("Concentración [mg/L]")
ax.set_xlabel("Punto de muestreo")
ax.legend(ncol=4, loc="upper center", bbox_to_anchor=(0.5, 1.15), frameon=False)
FIG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(FIG)

# --- Apoyo a la distribución de caudales (OE1) ---
# Caudal que daría la MISMA carga orgánica de la Fase 1 (30 g DQO/m2·d en 6 m2 = 180 g DQO/d)
CARGA_DQO = 30 * 6  # g/d — dato del proyecto ANID (01_normativa/proyecto/ALCANCE.md)
with open(RES / "caudal_equivalente_carga.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["punto", "DQO_media_mg_L", "caudal_equivalente_L_d", "carga_hidraulica_mm_d"])
    print("Caudal para 180 g DQO/d (Fase 1):")
    for pto in PUNTOS:
        s = resumen("DQO total", pto)
        q = CARGA_DQO / s["media"] * 1000  # L/d  (g/d ÷ mg/L = m3/d)
        w.writerow([pto, round(s["media"], 2), round(q), round(q / 6)])
        print(f"  {pto}: DQO {s['media']:.1f} mg/L -> {q:,.0f} L/d ({q/6:,.0f} mm/d en 6 m2)")
print("Listo: tabla, figura y resúmenes generados.")
