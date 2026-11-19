# 05_ejemplos — Referencias de otros trabajos ("moodboard")

En edición de video, la carpeta de **referencias** guarda trabajos ajenos que sirven
de modelo: cómo se ve un buen corte, una buena gráfica, un buen ritmo. No se editan
ni se copian; se **estudian**. Aquí va lo mismo para la tesis.

| Subcarpeta | Qué va |
|---|---|
| `tesis/` | Tesis o memorias de título de otros (UCM u otras universidades) |
| `memorias_calculo/` | Memorias de cálculo profesionales o académicas (hidráulica, estructuras, fundaciones...) |
| `fichas/` | Una ficha por ejemplo: qué aprender de él y qué NO copiar (plantilla `_PLANTILLA_ficha_ejemplo.md`) |

## Diferencia con otras carpetas

| Carpeta | Qué es | ¿Se cita en la tesis? |
|---|---|---|
| `02_material_bruto/` | Material **propio** (borradores, datos, planos) | No (se reescribe) |
| `02_material_bruto/papers/` | Fuentes bibliográficas (artículos, libros, normas) | **Sí**, en `referencias.bib` |
| `05_ejemplos/` | Trabajos **ajenos** usados como modelo de forma y método | Solo si se usa un dato o método de ellos (y debe ser fuente válida según la normativa) |

## Reglas

1. **No se modifican** los archivos originales.
2. **No se copia texto** de los ejemplos a la tesis (sería plagio). Se toma la *estructura*, el *orden* o el *tipo de tabla/figura*.
3. Si un ejemplo aporta un dato, ecuación o criterio que se usará, se cita su **fuente original** (la norma o el libro que el ejemplo cita), no el ejemplo.
4. Nombre: `AAAA_autor-o-institucion_tema.ext` — ej.: `2022_ucm_humedales-riego.pdf`, `2024_empresa-x_memoria-plataforma-acero.pdf`.
5. Cada ejemplo lleva su ficha en `fichas/` (receta `herramientas/recetas/11_analizar_ejemplo.md`).

## Inventario

| Archivo | Tipo | Relación | Ficha |
|---|---|---|---|
| `tesis/2024_ucm_guerrero_humedales-vs-convencional-nirivilo` | Tesis UCM 2024 (guía: Dr. Vera Puerto) | **Alta**: humedal vertical, balance de O₂, bombas | `fichas/2024_ucm_guerrero_…md` |
| `memorias_calculo/2026_peritaje-estructural-cerchas-templo-esperanza-plan` | Memoria de cálculo / peritaje 2026 | **Alta para OE2** (presentación del cálculo estructural) | `fichas/2026_peritaje-…md` |
| `tesis/2026_ucm_jove_fluctuaciones-presion-cfd` | Tesis UCM 2026 (guía: M. Quiroz) | Media: modelo de problema/brecha, conclusiones | `fichas/2026_ucm_jove_…md` |
| `tesis/2026_ucm_arancibia_escorrentia-cuencas-mediterraneas` | Tesis UCM 2026 (guía: Dr. Barrientos) | Baja: modelo de "área de estudio" y "datos" | `fichas/2026_ucm_arancibia_…md` |

Cada PDF tiene al lado un `.md` con el texto extraído (para que cualquier IA lo lea).
