#!/usr/bin/env bash
# Convierte un documento (Word, ODT, HTML, LaTeX...) a Markdown con Pandoc,
# dejando la copia AL LADO del original (que no se modifica).
# Para PDF usa pdftotext (paquete poppler-utils).
# Uso: bash herramientas/convertir.sh ruta/archivo.docx
set -euo pipefail
entrada="$1"
salida="${entrada%.*}.md"
case "${entrada,,}" in
  *.pdf)
    command -v pdftotext >/dev/null || { echo "Instala poppler-utils (pdftotext)"; exit 1; }
    pdftotext -layout "$entrada" "${entrada%.*}.txt"
    salida="${entrada%.*}.txt" ;;
  *)
    command -v pandoc >/dev/null || { echo "Instala pandoc: https://pandoc.org/installing.html"; exit 1; }
    # Extrae imágenes a una carpeta al lado y conserva ecuaciones como LaTeX
    pandoc "$entrada" -t gfm+tex_math_dollars --wrap=none \
      --extract-media="$(dirname "$entrada")/media_$(basename "${entrada%.*}")" -o "$salida" ;;
esac
echo "==> Copia en texto: $salida"
echo "    (Para pasar a LaTeX directo: pandoc \"$entrada\" -t latex -o archivo.tex)"
