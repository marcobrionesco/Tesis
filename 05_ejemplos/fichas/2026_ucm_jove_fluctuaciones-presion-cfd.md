# Ejemplo: Jove (2026) — Fluctuaciones de presión en modelo físico asistido por CFD

- **Archivo:** `05_ejemplos/tesis/2026_ucm_jove_fluctuaciones-presion-cfd.pdf` (105 págs.; texto en `.md` al lado)
- **Tipo:** Proyecto de Título, Ingeniería Civil UCM, junio 2026
- **Autor / guía:** Diego J. Jove Bascuñán / Marco Quiroz Valeria (integró la comisión de Guerrero, 2024; ayudó con su formato LaTeX)
- **Tema:** metodología para caracterizar fluctuaciones de presión en el modelo físico del Embalse Ancoa, comparando un sistema de adquisición de arquitectura abierta con uno comercial, apoyado en CFD (OpenFOAM, LES).
- **Relación con mi tesis:** **MEDIA** — tema distinto (hidráulica experimental y CFD), pero es un **modelo reciente de la misma Escuela** en estructura, redacción y uso de literatura.
- **¿Es fuente citable?** No para mi tema; sirve como modelo de forma.

## Qué hace bien (imitar la forma, no el texto)

| Aspecto | Dónde (pág. PDF) | Cómo aplicarlo en mi tesis | Archivo destino |
|---|---|---|---|
| **Planteamiento del problema con brecha explícita**: contexto → por qué importa → qué existe (con citas 2018–2024) → qué falta ("brecha económica y operativa") → propuesta | §1.1–1.2 (p. 13–15) | Reescribir §1.1 siguiendo esa secuencia: déficit hídrico del Maule → reúso < 1 % en Chile (Vera-Puerto et al., 2022) → tratamiento rural insuficiente (Vera et al., 2016) → falta de estaciones experimentales multifuente → este proyecto | `01_introduccion.tex` |
| Sección **"Alcances y estructura de la tesis"** | §1.4 (p. 16) | Completar mi §1.6 (alcances) y agregar un párrafo de estructura | `01_introduccion.tex` |
| Objetivos con sigla **OE1, OE2, OE3** y resultados titulados por objetivo | §1.3, cap. 6 | Ya lo hago ("objetivo específico 1"); usar la misma etiqueta en Resultados, Discusión y Conclusiones | todos |
| **Marco teórico enfocado**: solo la teoría que después se usa (cada ecuación reaparece en la metodología) | cap. 2 | Revisar que cada concepto de mi cap. 2 se use después; agregar la tabla de criterios de diseño de HCFV | `02_marco_teorico.tex` |
| **Protocolos de metodología** detallados y reproducibles (pasos, criterios de aceptación, verificación) | cap. 4–5 | Para mi metodología (20 %): explicitar criterios de aceptación de cada cálculo (OI > OD, carga ≤ máx., ratio LRFD ≤ 1, deflexión ≤ L/300, q_act ≤ q_adm) | `03_metodologia.tex` |
| **Conclusiones con "límites de aplicabilidad"** y una **matriz de decisión** de síntesis | §7.1, Tabla 7.1 (p. 95–98) | Mis secciones pendientes de limitaciones y trabajo futuro; una tabla final de síntesis "objetivo → resultado → cumple/no cumple" | `06_conclusiones.tex` |
| **Bibliografía reciente**: aprox. la mitad de las referencias son de 2016 o posteriores | Bibliografía | Meta para mi marco teórico | `referencias.bib` |

## Qué NO imitar

- Une "Resultados y Discusión" en un capítulo: los lineamientos ICV-611 piden capítulos separados.
- Muy extenso en teoría general (turbulencia, espectros) para un proyecto de 80 páginas: en mi caso el marco teórico debe ser enfocado y crítico, no un manual.

## Diferencias de formato con la normativa UCM actual

- Revisar al compararlo: su encabezado de capítulo usa "Capítulo N" en línea aparte; el template UCM usa "N. Título". Mi plantilla sigue el template oficial.
