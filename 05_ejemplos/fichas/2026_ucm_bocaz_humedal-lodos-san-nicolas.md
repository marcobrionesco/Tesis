# Ejemplo: Bocaz (2026) — Humedal construido para lodos de la PTAS de Villa Esperanza (San Nicolás) — UCM

- **Archivos:** `05_ejemplos/tesis/2026_ucm_bocaz_humedal-lodos-san-nicolas_cuerpo.pdf` (portada → bibliografía, 99 págs.) y `…_anexos.pdf` (pp. 85–147); texto en `.md` al lado.
- **Tipo:** Proyecto de Título, Ingeniería Civil **UCM**, versión final (portada octubre 2026; hoja de firmas agosto 2026).
- **Autor / guía / comisión:** Pedro I. Bocaz Pavez / **Dr. Ismael Vera Puerto** (mismo guía) / comisión Vera, **Carlos Arias**, Guillermo Barrientos.
- **Tema:** humedal de flujo vertical para deshidratar y estabilizar lodos primarios y secundarios de una PTAS RTB30 (25 viviendas,
  125 hab.); 2,05 t ST/año, 30 kg ST/m²·año → 70 m²; diseño hidráulico, operación, verificaciones y evaluación económica. Hecha en LaTeX.
- **Relación con mi tesis:** **ALTA como modelo de forma** — tesis de diseño, del mismo guía, aprobada en 2026 y con la misma normativa.
- **¿Es fuente citable?** Tesis de pregrado: citar las fuentes originales que usa (Uggetti, 2012; Andreoli et al., 2007; Von Sperling, 2007…), no la tesis.

## Estructura (cuerpo)

- Preliminares: **Resumen → Abstract → Agradecimientos** → índices (con rótulo "Pág.").
- Cap. 1 Introducción: planteamiento del problema, antecedentes del proyecto (ubicación, loteo, tabla de datos generales), justificación, objetivos, **alcances y limitaciones**.
- Cap. 2 Marco teórico: el residuo (generación y características, tabla de características típicas) → tecnologías → humedales (funcionamiento, procesos, componentes, carga/reposo).
- Cap. 3 Metodología: antecedentes; **"Criterios, supuestos y parámetros de diseño"** (como no hay datos medidos, adopta valores de literatura y elige los conservadores); **diagrama de flujo del procedimiento de diseño** (fig. 3.3); un apartado por paso de cálculo, cada uno con una tabla "Parámetro | Símbolo | Unidad | Valor"; verificaciones; evaluación económica.
- Cap. 4 **Análisis y Resultados** (mismo orden que la metodología; incluye pérdidas de carga y selección de bomba con tablas de cálculo, planta, cortes, verificaciones). **No tiene capítulo de Discusión aparte.**
- Cap. 5 Conclusiones (abre con el cumplimiento del objetivo general y da cifras) + **Recomendaciones y líneas de investigación futura** (lista numerada).
- Resumen en **4 párrafos** (contexto → objetivo y método → resultados con cifras → conclusión y limitación), justo lo que pidió el profesor (R1).

## Contenido de los anexos (archivo `_anexos`)

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
| Resumen de 4 párrafos con cifras | pp. I–II | Plantilla para terminar R1 (párrafos 3–4) cuando estén los resultados | `preliminares/resumen.tex` |
| Sección "Criterios, supuestos y parámetros de diseño" | cap. 3.1.2 | Reunir en un solo lugar nuestros supuestos (q_adm 150 kPa, φ′, factores de restitución 0,85/0,9, Hazen-Williams C, n.º de pulsos…) | `capitulos/03_metodologia.tex` |
| Diagrama de flujo del procedimiento de diseño | fig. 3.3 | Diagrama OE1 → OE2 → OE3 (caracterización → dimensionamiento → hidráulica → estructura → planos) en TikZ | `capitulos/03_metodologia.tex` |
| Tablas "Parámetro / Símbolo / Unidad / Valor" por cálculo | tablas 3.2–4.5 | Usarlas en dimensionamiento, ADT de bombas y verificación de zapatas | `capitulos/03–04` |
| Conclusiones que abren con el objetivo general cumplido + recomendaciones numeradas | cap. 5 | Reescritura del cap. 6 | `capitulos/06_conclusiones.tex` |
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

- Agradecimientos **después** del Abstract (como el template, no como los Lineamientos) → evidencia para la pregunta 16.
- Sin capítulo de Discusión: la UCM y este guía aceptan "Análisis y Resultados" + Conclusiones. Nuestra tesis mantiene Discusión (DECISIONES); consultar si se fusiona.
- Anexos numerados ".1, .2…" (error de la plantilla LaTeX), no romanos.
