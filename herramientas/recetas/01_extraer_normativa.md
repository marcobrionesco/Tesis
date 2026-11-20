# Receta 01 — Extraer la normativa de formato

> ✅ Ya aplicada el 2026-11-19 con la normativa ICV-611 (UCM). Repetir solo si la universidad entrega documentos nuevos.

**Entrada:** documentos en `01_normativa/originales/`.
**Salida:** `01_normativa/REGLAS_FORMATO.md` completo + plantilla LaTeX ajustada.

## Pasos

1. Leer **todos** los documentos de `01_normativa/originales/`.
2. Llenar cada fila de `REGLAS_FORMATO.md` con el valor exigido y la **fuente exacta** (documento y página).
   - Si un dato no aparece en la normativa, escribir `NO ESPECIFICADO` (no suponer).
   - Si dos documentos se contradicen, anotar ambos y agregarlo a "Bloqueos" en `00_proyecto/ESTADO.md`.
3. Aplicar cada regla en la plantilla:
   - Papel, tamaño de letra, una/doble cara → `tesis/main.tex` (`\documentclass`).
   - Márgenes, interlineado, títulos, numeración → `tesis/config/formato.tex`.
   - Fuente → `tesis/config/paquetes.tex`.
   - Norma de citas → opción `style=` de `biblatex` en `paquetes.tex` (APA: `apa`; IEEE: `ieee`; ISO 690: `iso`; numérica: `numeric-comp`).
   - Portada → `tesis/portada/portada.tex` y datos en `tesis/config/comandos.tex`.
   - Orden de secciones preliminares → `tesis/main.tex`.
4. Marcar ✅ en la columna "¿Aplicada?" de cada regla aplicada.
5. Compilar con `make pdf` y verificar visualmente portada, índice y un capítulo.
6. Registrar en `00_proyecto/DECISIONES.md` cualquier interpretación de una regla ambigua.
