# Receta 03 — Ficha de lectura de una fuente

**Entrada:** un PDF en `02_material_bruto/papers/` (o DOI).
**Salida:** `03_seleccion/fichas_lectura/apellido-año-palabra.md` + entrada en `tesis/bib/referencias.bib`.

## Pasos

1. Leer el documento (al menos resumen, introducción, metodología, conclusiones y las secciones relevantes).
2. Llenar `_PLANTILLA_ficha.md`. Todo dato o cita textual **con número de página**.
3. Obtener la referencia real: `bash herramientas/doi2bib.sh <DOI>` o exportar desde Zotero.
   Ajustar la clave a `apellidoAAAApalabra` y agregarla a `referencias.bib`.
4. Indicar en qué capítulos se usará y con qué otras fichas coincide o choca.
5. No extrapolar: la ficha dice lo que la fuente dice, no lo que nos gustaría que dijera.
