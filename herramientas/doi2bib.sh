#!/usr/bin/env bash
# Obtiene la entrada BibTeX REAL de un DOI desde doi.org (Crossref/DataCite).
# Uso: bash herramientas/doi2bib.sh 10.xxxx/yyyy [>> tesis/bib/referencias.bib]
# Después, revisar la clave y ajustarla al formato apellidoAAAApalabra.
set -euo pipefail
doi="${1#https://doi.org/}"
curl -sSLf -H "Accept: application/x-bibtex; charset=utf-8" "https://doi.org/${doi}" \
  || { echo "No se encontró el DOI: $doi" >&2; exit 1; }
echo
