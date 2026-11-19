# Receta 11 — Analizar un ejemplo (tesis o memoria de cálculo ajena)

**Entrada:** un archivo en `05_ejemplos/tesis/` o `05_ejemplos/memorias_calculo/`.
**Salida:** ficha en `05_ejemplos/fichas/<mismo-nombre>.md` (plantilla `_PLANTILLA_ficha_ejemplo.md`)
y, si el usuario lo aprueba, una lista de mejoras concretas para `tesis/`.

## Pasos

1. Leer el ejemplo completo (si es PDF, convertirlo: `make convertir ARCHIVO=...`).
2. Leer `00_proyecto/ESTADO.md` y el triaje vigente para saber **qué le falta a mi tesis**.
3. Llenar la ficha enfocándose en lo que resuelve esas carencias. Por ejemplo:
   - Cómo presenta los **resultados** de cálculo (tablas de verificación, ADT, curvas de bombas).
   - Cómo estructura la **memoria de cálculo** (datos → hipótesis → fórmulas → resultados → verificación).
   - Cómo hace el **estado del arte** (tablas comparativas de autores, análisis crítico).
   - Qué **normas y criterios** usa (anotar la fuente original, no el ejemplo).
4. Señalar diferencias de formato con `01_normativa/REGLAS_FORMATO.md`: **la normativa UCM manda**.
5. Proponer mejoras como tabla `aspecto | ejemplo (pág.) | cambio propuesto | archivo destino`.
   **No copiar texto**: reescribir con las palabras y los datos propios.
6. Si se adopta un dato o criterio, buscar y citar su **fuente original** en `referencias.bib`.
7. Registrar en `00_proyecto/BITACORA.md` qué ejemplos se analizaron.
