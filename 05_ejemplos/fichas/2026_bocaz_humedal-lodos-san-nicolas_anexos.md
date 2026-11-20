# Ejemplo: Bocaz (2026) — Humedal de tratamiento de lodos, Villa Esperanza (San Nicolás) — solo anexos

- **Archivo:** `05_ejemplos/tesis/2026_bocaz_humedal-lodos-san-nicolas_anexos.pdf` (63 págs.; texto en `.md` al lado)
- **Tipo:** Proyecto de Título (versión final), Pedro Bocaz, 2026. **El archivo contiene solo los anexos** (pp. 85–147 impresas):
  no trae portada, cuerpo de la tesis, institución ni profesor guía.
- **Tema:** humedal construido para deshidratar y estabilizar los lodos de una PTAS de lodos activados (RTB30) de un
  conjunto de 25 viviendas, sector El Manzano, comuna de San Nicolás (agosto 2026).
- **Relación con mi tesis:** **media** — es un humedal de **lodos** (no de agua residual), pero sus anexos son un buen modelo de
  **cómo presentar el diseño de un humedal pequeño**: planos, cuadro de parámetros, itemizado por partida.
- **¿Es fuente citable?** No (tesis de pregrado, y sin el cuerpo no se ven sus fuentes). Solo modelo de forma.

## Contenido de los anexos

| Anexo | Contenido | Pág. impresa |
|---|---|---|
| 1 | 2 planos (lámina "1 de 2" y "2 de 2"): emplazamiento sobre imagen satelital, planta, cortes A-A y B-B, **vista de capas del medio granular**, detalle de distribución de vegetación, **simbología**, vista 3D de tuberías, detalles de cruces de tuberías y berma, **cuadro resumen de cantidades** | 87–88 |
| 2 | Manual de operación y mantención del humedal (puesta en marcha, operación, reinicio, monitoreo, contingencias, registro) | 90–116 |
| 3 | Ficha técnica de la PTAS RTB30 (proveedor) | 118–123 |
| 4 | Presupuesto general y análisis de precios unitarios por partida | 125–145 |
| 5 | Horas de operador y costos anuales de operación | 147 |

## Qué hace bien (para imitar la forma, no el texto)

| Aspecto | Dónde (pág.) | Cómo aplicarlo en mi tesis | Archivo destino |
|---|---|---|---|
| **Cuadro de "parámetros de diseño y operación"** en una sola tabla (vida útil, superficie, cargas, frecuencias, volúmenes, caudal de bomba, velocidad de descarga) | p. 96 | Tabla resumen por línea (doméstica, agroquímicos, estero): área, carga orgánica e hidráulica, n.º de pulsos, volumen por dosis, TRH, caudal y ADT de bomba. Cierra el OE2 de un vistazo | `capitulos/04_resultados.tex` |
| **Cuadro resumen de cantidades dentro del plano** (excavación, geomembrana, tuberías, medios granulares, plantas) | p. 88 | Proponer al profesor agregarlo a las láminas (cruza con el itemizado y la pregunta 10 de capas) | planos (pregunta) |
| **Vista de capas del medio granular** con espesor y granulometría de cada capa | p. 87 | Nuestra figura TikZ del HCFV ya lo hace; cuidar que coincida con la lámina 2.2 (pregunta 10) | `capitulos/02_marco_teorico.tex` |
| Simbología completa y escalas en cada vista; plano numerado "1 de 2" | p. 87–88 | Revisar que las láminas del anexo tengan simbología y escalas | anexos de planimetría |
| Itemizado agrupado en obras previas / obra gruesa / instalaciones / otros, con unidad y cantidad | p. 125 | Comparar con el orden de nuestro itemizado (anexo III) | `anexos/anexo_itemizado.tex` |

## Métodos, criterios o valores útiles

| Elemento | Pág. | Fuente original que cita el ejemplo | ¿Verificado? |
|---|---|---|---|
| Capas (lodos): arena gruesa 0,5–1 mm (0,25 m), grava 8–10 mm (0,20 m), bolones 50 mm (0,30 m); geomembrana HDPE 1,5 mm; drenaje PVC 110 mm perforado, i = 1 % | 87–88 | No visible (sin cuerpo de la tesis) | No — es para lodos, **no comparable** con un HCFV de agua residual |
| Totora (*Schoenoplectus californicus*): 280 plantas en 70 m² (4 plantas/m²) | 88, 125 | No visible | No |
| Humedal de lodos: 30 kg ST/m²·año; reposo 60 d; vida útil 30 años en 3 ciclos de 10 | 96 | No visible | No (fuera de nuestro tema) |

## Qué NO imitar

- **Anexos numerados con números arábigos** ("Anexo 1"): la normativa UCM exige **números romanos** (ya implementado en `tesis/`).
- **Manual de operación y mantención**, **presupuesto con APU** y **costos de operación**: no están en el alcance inscrito
  (`01_normativa/proyecto/ALCANCE.md`: la operación es del proyecto ANID; la tesis entrega memoria, planos, EETT e itemizado). No agregarlos.
- Cuadros de plano con campos vacíos de formulario (propietario, autorizaciones ESSBIO): no aplican a una estación experimental.

## Diferencias de formato con la normativa UCM

- Sin el cuerpo de la tesis no se puede comparar el resto (márgenes, títulos, citas).
