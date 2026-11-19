# REGLAS DE FORMATO — Resumen operativo de la normativa universitaria

> Los documentos originales van en `01_normativa/originales/` (PDF, Word, etc.)
> y **no se modifican**. Este archivo es la versión "ejecutable": cada regla
> en una línea, con la página del original de donde sale y dónde se aplica
> en la plantilla LaTeX.
> Se llena con la receta `herramientas/recetas/01_extraer_normativa.md`.
>
> Estado: ⚠️ **SIN COMPLETAR** — los valores actuales de la plantilla son provisorios.

## Página y tipografía

| Regla | Valor exigido | Fuente (doc, pág.) | Dónde se aplica | ¿Aplicada? |
|---|---|---|---|---|
| Tamaño de papel | [Carta / A4] | | `tesis/config/formato.tex` (geometry) | ⬜ |
| Margen izquierdo | [ej. 4 cm] | | `formato.tex` | ⬜ |
| Margen derecho | [ej. 2,5 cm] | | `formato.tex` | ⬜ |
| Margen superior | [ej. 2,5 cm] | | `formato.tex` | ⬜ |
| Margen inferior | [ej. 2,5 cm] | | `formato.tex` | ⬜ |
| Fuente | [ej. Times New Roman / Arial] | | `formato.tex` | ⬜ |
| Tamaño de fuente | [ej. 12 pt] | | `main.tex` (opción de clase) | ⬜ |
| Interlineado | [ej. 1,5] | | `formato.tex` (setspace) | ⬜ |
| Impresión | [una cara / doble cara] | | `main.tex` | ⬜ |
| Numeración de páginas | [romana en preliminares, arábiga desde cap. 1; posición] | | `formato.tex` (fancyhdr) | ⬜ |

## Estructura obligatoria (orden)

| # | Sección | ¿Obligatoria? | Fuente | Archivo |
|---|---|---|---|---|
| 1 | Portada | | | `tesis/portada/portada.tex` |
| 2 | [Hoja de calificación / dedicatoria / agradecimientos ...] | | | |
| 3 | Resumen (máx. [N] palabras) | | | `tesis/preliminares/resumen.tex` |
| 4 | Abstract | | | `tesis/preliminares/abstract.tex` |
| 5 | Índice general / figuras / tablas | | | `main.tex` |
| ... | | | | |

## Portada

- Logo: [sí/no, posición, tamaño]
- Textos exactos y orden: [universidad, facultad, departamento, título, "Memoria para optar al título de...", autor, profesor guía, comisión, ciudad, año]

## Títulos y numeración

- Capítulos: [formato, mayúsculas, numeración]
- Secciones: [hasta qué nivel se numera]
- Figuras y tablas: [numeración por capítulo "Figura 2.3" o corrida; título arriba/abajo; fuente bajo la figura]
- Ecuaciones: [numeración por capítulo (2.1), alineación]

## Citas y bibliografía

- Norma de citación: [APA 7 / IEEE / ISO 690 / Vancouver]
- Título de la sección: [Bibliografía / Referencias]

## Otros

- Extensión mínima/máxima: [...]
- Idioma: [...]
- Formato de entrega: [PDF/A, impreso, empastado...]
