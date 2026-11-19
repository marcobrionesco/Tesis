#!/usr/bin/env bash
# Genera un PDF con los cambios marcados (rojo = borrado, azul = agregado)
# entre una versión anterior (etiqueta/commit de git) y la actual.
# Útil para mostrar al profesor guía qué cambió desde la última entrega.
# Uso: bash herramientas/diff_versiones.sh v0.1-entrega-guia
set -euo pipefail
desde="$1"
command -v latexdiff-vc >/dev/null || { echo "Falta latexdiff (sudo apt install latexdiff)"; exit 1; }
cd tesis
latexdiff-vc --git --flatten -r "$desde" main.tex
mkdir -p ../salida/diff
latexmk -r latexmkrc -pdf -outdir=../salida/diff "main-diff${desde}.tex"
cp "../salida/diff/main-diff${desde}.pdf" "../salida/cambios_desde_${desde}.pdf"
rm -f "main-diff${desde}.tex"
echo "==> salida/cambios_desde_${desde}.pdf"
