# Revisión del profesor guía sobre la v3.0 (correo del 16-11-2026)

> Fuente: `02_material_bruto/revisiones_profesor/2026-11-16_profesor_revision-v3.0-comentada.pdf`
> (47 anotaciones de "leovera", extraídas con pymupdf) y correo `01_normativa/proyecto/texto/2026-11-16_profesor_correo-solicita-cambios.md`.
> Páginas = páginas del PDF comentado. **Estas instrucciones mandan** sobre cualquier sugerencia de IA.
> Estado: ✅ aplicado en `tesis/` · 🟧 en curso / parcial · ⬜ pendiente.

## 0. Instrucciones generales (correo)

| # | Instrucción | Estado |
|---|---|---|
| G1 | Enviar **el viernes por la mañana** (20-11-2026) una versión actualizada con **marco teórico** y **materiales y métodos** | ⬜ |
| G2 | **Incluir los objetivos aprobados por la Escuela** (inscripción VF-V2, inicios de octubre) y trabajar sobre ellos | ✅ objetivos y título actualizados |
| G3 | Enviar **en Word** para que pueda editar | ✅ `make word` genera `salida/tesis.docx` |
| G4 | Todas las **tablas** y **figuras** se mencionan primero en el texto; tablas **solo con líneas horizontales** (aplica a todo el documento) | 🟧 tablas ya en `booktabs`; revisar menciones |

## 1. Preliminares

| # | Pág. | Comentario (textual o resumido) | Dónde | Estado |
|---|---|---|---|---|
| R1 | 3 | **Resumen: cambiar casi en su totalidad.** Cuatro párrafos: (1) introductorio, (2) objetivo general y algo de metodología, (3) resultados, (4) síntesis de conclusiones | `tesis/preliminares/resumen.tex` | 🟧 párrafos 1–2 redactados; 3–4 como `\pendiente` |
| R2 | 3 | "Antes de decir esto, debes partir por el objetivo de la investigación" (antes de LRFD/balance de masa) | resumen | ⬜ (incluido en R1) |
| R3 | 3 | Tachado "Frutícola SABA SpA" → "**la Región del Maule**" (en "reúso en el riego de frutales en …") | resumen | ⬜ (incluido en R1) |
| R4 | 4 | Abstract: "Corregir cuando se tenga la versión en español" | `abstract.tex` | ⬜ después de R1 |
| R5 | 6, 9, 10 | "**Pág.**": agregar el rótulo "Pág." sobre la columna de números en el índice general, de figuras y de tablas | `tesis/config/formato.tex` | ✅ |

## 2. Capítulo 1 — Introducción

| # | Pág. | Comentario | Estado |
|---|---|---|---|
| I1 | 13 | Tachar "mediante" → "**como por ejemplo avanzar en la..**" (reúso de aguas residuales) | ✅ |
| I2 | 13 | "habitualmente inviable" → "**complejo**" (sistemas convencionales en zonas rurales) | ✅ |
| I3 | 13 | Reemplazar "El desafío de ingeniería radica en adaptar los modelos … Frutícola SABA SpA." por: "**Por tanto, y para poder avanzar en la implementación de este tipo de alternativas, existe el desafío de realizar diseños de ingeniería que garanticen calidad del agua apta para riego.**" | ✅ |
| I4 | 14 | Justificación: completar "La necesidad de este desarrollo de ingeniería …" con "**de una estación experimental de humedales construidos que sea capaz de tratar diferentes aguas residuales y generar efluentes aptos para riego.**" | ✅ |
| I5 | 15 | "Estos objetivos específicos **no son los finales aprobados por la escuela** a inicios de octubre. Actualizar" | ✅ |

## 3. Capítulo 2 — Marco teórico

| # | Pág. | Comentario | Estado |
|---|---|---|---|
| M1 | 16 | El marco teórico debe **empezar con la definición de agua residual y sus características**, "ojalá una **tabla** que resuma aguas similares a las de los tres tipos" (doméstica, lavado de agroquímicos, estero) | 🟧 sección creada; columna de aguas servidas con datos de Dotro et al. (2021); faltan agroquímicos y estero |
| M2 | 16 | "Esto es incorrecto. **La NCh1333 no habla de sólidos ni de materia orgánica**" → eliminar la frase sobre SST/DBO₅/coliformes | ✅ |
| M3 | 16 | Sección SbN: "Aquí **solo se debe hablar de las SbN**, nada de los efluentes" (título sin "y calidad de efluentes") | ✅ |
| M4 | 16 | Eliminar el párrafo del DS 90; "La parte final debe decir que **hay un tipo de SbN que son los humedales construidos**" | ✅ |
| M5 | 16 | "Hablar primero de manera **sucinta de los HC en general y decir los tipos**. Luego resaltar **por qué se selecciona el HC vertical**: básicamente porque **al nitrificar genera nitrato**, que es la forma de nitrógeno que más usan las plantas" | ✅ tipos y por qué vertical con Dotro et al. (2021); queda `\pendiente` solo la fuente agronómica del nitrato |
| M6 | 16 | "**Primero se define**, luego cómo se **diseñan** y luego cómo se **operan**. Sigue esa lógica" | ✅ definición → tipos → diseño (reglas generales, tabla 2.2, balance de O₂) → operación y mantención, todo con Dotro et al. (2021) |
| M7 | 17 | Figura del HCFV: "¿Lo hiciste tú? Debes decir de dónde sale. Si es tuyo, decir **elaboración propia**" | ✅ (la figura actual es TikZ propia: "Fuente: elaboración propia") |
| M8 | 17 | Ec. del balance de oxígeno (OD): "**explicar cada uno de los términos** de la ecuación" | ✅ todos los términos explicados, con Dotro et al. (2021) y Platzer (1999) |
| M9 | 17 | Ec. de aporte de oxígeno (OI): ídem; "fíjate cómo está en el **libro de Dotro que tradujimos con Carlos**" | ✅ contrastado con la traducción (Dotro et al., 2021, ec. 4.1–4.8): coincide |
| M10 | 17 | "Deutsche Vereinigung für Wasserwirtschaft…" → **usar solo la sigla** (DWA) | ✅ |
| M11 | 18 | Junto a la explicación de Hazen-Williams ("Donde J es …"): "**Esto es lo que te falta arriba**" = así deben explicarse los términos de las ecuaciones anteriores | 🟧 (ver M8–M9) |
| M12 | 18 | Tablas: mencionarlas primero en el texto; **solo líneas horizontales** (todas) | 🟧 |
| M13 | 19 | Quitar "(Objetivo Específico 2)" de los títulos: "lo de ligar el texto con los objetivos **se hace en la metodología**, no en el marco teórico" | ✅ |

## 4. Capítulo 3 — Metodología ("Materiales y métodos" en el correo)

| # | Pág. | Comentario | Estado |
|---|---|---|---|
| T1 | 21 | Al empezar el OE1, **primero localizar dónde se va a realizar el proyecto** | 🟧 sección "Área de estudio" al inicio |
| T2 | 26 | El plano de emplazamiento general (fig. 3.4), "**sin aún indicar los elementos**, va al inicio del capítulo" | 🟧 movido a "Área de estudio" |
| T3 | 21 | "Aquí también debes poner **lo que hicimos de las caracterizaciones de calidad**. Porque sin las caracterizaciones no llegas a los valores de carga" | 🟧 (campañas, puntos, parámetros ya descritos; ampliar: muestreo, laboratorio, métodos → pregunta al profesor) |
| T4 | 21 | "Está más o menos. Debe **ligarse con anexos donde se muestren las fichas** que se utilizaron. Te voy a compartir el **trabajo de Diego** de donde nos basamos para generar las fichas. Fíjate cómo está ahí redactado" | ✅ recibido (05_ejemplos/…yevenes…); metodología reescrita a su modo y **Anexo I** con las fichas y el registro de usos |
| T5 | 21 | Título "Procedimiento de Dimensionamiento de Humedales Construidos (HCFV)" → "**Dimensionamiento de HC-FV**" | ✅ |
| T6 | 22 | "Como unidad base se seleccionaron contenedores IBC de 1 m³…": "**Esto es resultado.** Aquí solo se explica cómo se calcula o se diseña" | 🟧 movido a resultados |
| T7 | 22 | (otro párrafo) "Esto es resultados, aquí es metodología" | 🟧 |
| T8 | 23 | Figuras: mencionarlas primero en el texto | 🟧 |
| T9 | 23 | Líneas a presión: "Ojo, aquí hablar de manera **genérica**, no especificar elementos aún" | 🟧 |

## 5. Consecuencias de los nuevos objetivos (VF-V2)

- **OE1 nuevo** = determinar características fisicoquímicas y de producción de las 3 fuentes → la **caracterización pasa a ser parte del alcance** (antes era insumo).
- **OE2 nuevo** = "diseño depurativo" + cálculo hidráulico → el **dimensionamiento del humedal (balance de oxígeno, 6 m²)** pasa a ser parte del alcance (se cierra la duda de cómo presentarlo; igual corresponde citar el diseño del proyecto ANID como base).
- **OE3 nuevo** = diseño y cálculo estructural de "los diferentes elementos" (no solo la plataforma) → incluye zapatas, placa base y estructura auxiliar de dosificadores.
- **Título**: agrega ", Región del Maule".
