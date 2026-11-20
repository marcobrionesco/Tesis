# Receta 10 — Autoevaluación con la rúbrica oficial

**Entrada:** la tesis completa (o el capítulo indicado) + `01_normativa/RUBRICA.md`.
**Salida:** `03_seleccion/notas/autoevaluacion_AAAA-MM-DD.md`.

Evalúa el informe **como lo haría la comisión** con la rúbrica ICV-611.

## Pasos

1. Ejecutar `make pdf` y `make revisar`; anotar faltas de formato y de extensión.
2. Para cada uno de los 10 criterios de `RUBRICA.md`, en orden de peso
   (Metodología 20 % → Marco teórico, Resultados, Discusión 15 % → Introducción 10 % → resto 5 %):
   - Recorrer la lista de control del nivel "Sobresaliente".
   - Asignar un puntaje (0–4) **citando evidencia concreta** (sección, página, línea).
   - Si no llega a 4, indicar **exactamente qué falta** para subir un nivel.
3. Calcular la nota ponderada estimada: Σ(puntaje/4 × peso), en escala 1–7 si el usuario lo pide.
4. Estimar el veredicto probable (Aprobado / Obs. menores / Revisiones mayores / Reprobado).
5. Listar las **5 mejoras de mayor impacto** (peso del criterio × distancia al 4).

## Formato del informe

| Criterio | Peso | Puntaje estimado | Evidencia | Qué falta para subir |
|---|---|---|---|---|

Sé exigente: es mejor que la comisión encuentre menos de lo que encontró esta revisión.
