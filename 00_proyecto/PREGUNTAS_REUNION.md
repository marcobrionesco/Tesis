---
title: "Preguntas para la reunión con el profesor guía"
subtitle: "Proyecto de Título — Estación experimental de humedales construidos (ANID/Anillos/ATE250033)"
author: "Marco Briones Escobar"
date: "Noviembre 2026"
---

**Contexto.** Se revisó la versión 3.0 del informe y se cruzó con la inscripción, la propuesta ANID,
los datos de caracterización, los planos, las EETT, el itemizado y los cálculos. Estas son las decisiones
que necesito confirmar para cerrar el informe. Están ordenadas por prioridad.

# A. Prioridad alta (cambian resultados del informe)

**1. Estructura: sismo y zapatas (NCh2369).** Linares está en **zona 2** (NCh2369:2025, Tabla 2; A~0~ = 0,30 g),
y la norma exige que al menos el 80 % del área de cada zapata quede apoyada (combinaciones ASD). Con el diseño final
(5,00 × 2,00 m, pilares 150×150×6, zapatas 1,0 × 1,0 × 0,5 m), si el sismo lo reparten los 6 pilares el cálculo previo
daba 85 % (cumple); con 2 pilares en voladizo, la zapata vuelca. Para rehacerlo necesito definir:
(a) ¿NCh2369:2003 o 2025 (oficializada el 9-03-2026, con transición)? (b) ¿Categoría de ocupación I (I = 0,8) o II
(I = 1,0)? (c) ¿Sistema resistente: marco a momento sin anclajes dúctiles (R = 3) u otro? (d) ¿Tipo de suelo (no hay
mecánica de suelos)? Con Terzaghi (Das, 2015), los 150 kPa admisibles supuestos equivalen a una arena con φ′ ≈ 32°; ¿se acepta ese supuesto o se pide un ensayo? (e) ¿El tablero y las vigas trabajan como diafragma que reparte el sismo entre los 6 pilares?

Respuesta (propuesta del autor, 20-11, a confirmar en la reunión): (a) NCh2369:2025 (la 2003 da el mismo veredicto); (b) categoría I; (c) marco a momento soldado, R = 3, ξ = 0,02; (d) suelo C supuesto y q_adm = 150 kPa (φ′ ≈ 32°), recomendar mecánica de suelos; (e) sí, diafragma con 6 pilares → 91 % de área apoyada. Con categoría II y suelo C bajaría a 76 % (habría que agrandar la zapata).

**2. Tablero y límite de deformación.** El tablero de 15 mm no cumple la deflexión L/300 con el método usado
(2,9 mm frente a 1,33 mm). Cumple con 21 mm o con vigas secundarias cada 0,30 m. ¿Se cambia? Además, la NCh427/1 no fija
L/300: sugiere L/500 a L/1000 para vigas que soportan equipos. ¿Qué límite usar, considerando la horizontalidad que
necesitan los sifones?

Respuesta (propuesta del autor, 20-11, a confirmar en la reunión): tablero continuo sobre 3 apoyos: 1,21 mm < 1,33 mm (L/300); L/500 solo referencia; vigas cada 0,40 m y tablero de 15 mm se mantienen.

**3. Línea de impulsión del estero.** Con PVC de 25 mm en 140 m y un caudal de llenado de
1000 L en 30 min, la altura dinámica requerida es de unos 31 m (ninguna bomba de los catálogos llega).
¿Se aumenta el diámetro (con 40 mm bajaría a unos 14 m), se llena más lento o se cambia el trazado?

Respuesta (propuesta del autor, 20-11, a confirmar en la reunión): se mantiene PVC 25; llenado ≤ 60 min (30 deseable); con la bomba supuesta el estero llena en ≈ 36 min.

**4. Selección de bombas.** Las bombas no están en el itemizado (las provee el equipo del proyecto).
¿Ya se compraron o definieron modelos? Si no, ¿propongo yo la selección en la tesis a partir del cálculo?

Respuesta (propuesta del autor, 20-11, a confirmar en la reunión): bomba periférica supuesta Pedrollo JSWm 1A (0,75 HP, la que se compró), la misma en las tres líneas.

**5. Caudal del estero y de agroquímicos.** La propuesta indica operar estas líneas "con las mismas
características de carga" que la doméstica (30 g DQO/m²·d). Con la DQO medida, eso exigiría unos
28 400 L/d en el estero (inviable), 2 400 L/d en AGR2 y 460 L/d en AGR1. ¿Qué criterio de caudal uso
(por ejemplo, igual carga hidráulica que la línea doméstica)? Además, según Agriculture and Agri-Food Canada (2018), un predio típico genera solo 5000–7000 L/año de agua de lavado de equipos (unos 50–70 L/d en temporada): ¿cuánta produce el predio y alcanza para la línea de agroquímicos?

Respuesta (propuesta del autor, 20-11, a confirmar en la reunión): 750 L/d por línea (igual carga hidráulica); déficit completado con agua del estero; DQO de la mezcla ≤ 240 mg/L.

# B. Prioridad media (coherencia del informe)

**6. Fichas y aforos de oficinas.** Ya tengo el trabajo de Diego y las fichas (gracias). Falta: ¿cómo se hizo el
**aforo** de los artefactos (instrumento, repeticiones)? ¿Hubo más fichas después del 1 de febrero (el registro llega a
la 3.ª semana de febrero)? ¿La columna repetida "02S1" es la 2.ª semana de febrero? ¿El factor de restitución de la casa
es 0,85 (documento de cálculo) y no 0,8 (v3.0)? ¿Los **tiempos de retención** comprometidos en la inscripción son los del
lecho (referencial en un humedal vertical, según Dotro et al.) o los de los estanques de acumulación y dosificadores?

Respuesta (propuesta del autor, 20-11, a confirmar en la reunión): aforo volumétrico (0,92 L, 3 aperturas); WC 9,1 L del fabricante; semanas 01S4 y 02S1–02S4; TRH por unidad de la cadena (pulsos de 125 L y porosidad: supuestos a confirmar).

**7. Datos de caracterización.** La base de datos difiere en 10 celdas del resumen; por ejemplo,
la DQO total de AS1 en la semana 1 (2478 mg/L) se excluyó del resumen (con ella, la media subiría de 411 a
757 mg/L). ¿Qué fuente manda y con qué criterio se excluyó ese valor? ¿Tipo de muestra, laboratorio y
métodos analíticos?

Respuesta (propuesta del autor, 20-11, a confirmar en la reunión): mandan los informes del laboratorio; muestras puntuales; semana 1 de AS1/AS2 atípica (excluida de las medias); coliformes totales; métodos no informados (pedir al laboratorio).

**8. Nitrógeno bajo.** En las aguas servidas el nitrógeno total es de 2,0–2,7 mg/L y el amonio de 1,3–2,0 mg/L
(la literatura chilena reporta 20–120 mg/L de nitrógeno total). ¿Hay una causa conocida (punto de muestreo, dilución)? Además, el nitrato medido (9,3 y 5,9 mg/L) supera al nitrógeno total: ¿se informó como NO~3~^-^ o como N-NO~3~^-^?
¿Se mantiene la meta de aprox. 3 g NH~4~^+^/m²·d de la Fase 1? ¿Uso los valores de diseño (DQO 300/400; NH~4~^+^ 1,5/1,0)
o las medias medidas (338/411; 1,98/1,28)?

Respuesta (propuesta del autor, 20-11, a confirmar en la reunión): se sigue el cálculo del profesor (300/400; NTK 1,5/1,0; fosa 25 %); las medias medidas validan (17–33 g DQO/m²·d); nitrógeno bajo por dilución en oficinas; meta de 3 g NH₄⁺/m²·d como referencia (dosificar amonio: trabajo futuro).

**9. Hormigón de zapatas.** G30 (EETT, itemizado) o G25 (lámina 3.2 y cálculo).

Respuesta (propuesta del autor, 20-11, a confirmar en la reunión): G25 (lámina 3.2); se corrigen EETT e itemizado.

**10. Capas filtrantes.** La lámina 2.2 indica grava 0,15 – arena 0,60 – grava 0,15 m; las EETT invierten
los tamaños de grava y llaman "de filtración" a la gravilla superior; el itemizado pide 3 m³ de arena y
18 m³ de gravilla (con 18 IBC serían unos 10,8 m³ de arena y 2,7 m³ de cada grava). ¿Cuál es la correcta?

Respuesta (propuesta del autor, 20-11, a confirmar en la reunión): capas de la lámina 2.2; EETT e itemizado corregidos.

**11. Zanja de la casa.** Con las cotas del cálculo, la tapada mínima es de 0,11 m (exigida 0,50 m),
y el cálculo usa un tubo de 52 mm mientras las EETT indican PVC sanitario de 110 mm. ¿Cotas y diámetro correctos?

Respuesta (propuesta del autor, 20-11, a confirmar en la reunión): trayectos modificados en terreno; sin resultados de excavación, solo criterios.

**12. Estructura auxiliar de los dosificadores.** No tiene cálculo, y el perfil indicado
("15×15×6 mm") no es físicamente posible. ¿Qué perfil se usa? ¿La incluyo en el cálculo?

Respuesta (propuesta del autor, 20-11, a confirmar en la reunión): marco auxiliar de perfil 15 × 15 × 6 mm (casi macizo), verificado para el pulso (1,32 kN): barras 0,37–0,93; columnas esbeltas (KL/r = 340), estabilidad por arriostramiento y anclaje.

# C. Prioridad baja (formato y referencias)

**13.** Norma de reúso: según Vera-Puerto et al. (2022), la NCh3456 (partes 1–4, versiones comité) se aprobó en mayo de 2021, y su parte 2 tiene cuatro categorías (I a IV; la IV con DBO~5~ 35 y SST 80 mg/L, la "Categoría D" de las memorias CEAZA). ¿Me puede facilitar el texto para citarla directamente? *(Tarea interna del autor: se gestiona al enviar la versión 4.)*

**14.** ¿Me puede facilitar el anexo "Bibliographic-references-2025" de la propuesta *(Tarea interna del autor: se gestiona al enviar la versión 4.)*
(referencias completas de Vera-Puerto et al. 2021a, 2021b, 2023 y 2024)?

**15.** ¿Las redes deben dimensionarse también para la Fase 2 (60 g DQO/m²·d)?

Respuesta (propuesta del autor, 20-11): se dimensiona para la Fase 1; Fase 2 con 3 IBC por línea (o 1500 L/d, menos recomendable).

**16.** Orden de las páginas preliminares: los Lineamientos ponen Agradecimientos antes del Resumen;
el template, después del Abstract (así lo hizo Bocaz, 2026, tesis aprobada que usted guió). ¿Cuál prefiere? ¿Mantengo un capítulo de Discusión aparte o lo integro en "Análisis y Resultados" como en esa tesis?

Respuesta (propuesta del autor, 20-11): se mantiene el orden de los Lineamientos y la Discusión aparte; confirmar.

**17.** ¿Tiene observaciones escritas sobre la versión 3.0 que le envié? *(Tarea interna del autor: se gestiona al enviar la versión 4.)*

**18. Nitrato y plantas del humedal.** Redacté la selección del humedal vertical según su indicación: al nitrificar genera nitrato, que asimilan las plantas del propio humedal (Dotro et al., 2021: 0,2–0,8 g N/m²·d). ¿Tiene una fuente que respalde que el nitrato es la forma de nitrógeno que más usan esas plantas?


Respuesta (propuesta del autor, 20-11): se suavizó la redacción: solo asimilación de 0,2–0,8 g N/m²·d (Dotro et al., 2021).