<!-- Texto extraído automáticamente de 2026_ucm_jove_fluctuaciones-presion-cfd.pdf (originales: Ejemplo_tesis_1_compressed-1.pdf + Ejemplo_tesis_1_compressed-2.pdf). Solo para lectura por IA; puede tener errores de extracción. NO copiar texto a la tesis. -->

=== PÁG 1 del PDF ===
UNIVERSIDAD CATÓLICA DEL MAULE
FACULTAD DE CIENCIAS DE LA INGENIERÍA
ESCUELA DE INGENIERÍA CIVIL
METODOLOGÍA PARA LA CARACTERIZACIÓN DE FLUCTUACIONES DE
PRESIÓN EN MODELOS FÍSICOS HIDRÁULICOS ASISTIDA POR CFD:
EVALUACIÓN DE UN SISTEMA DE ARQUITECTURA ABIERTA (SAA) Y UN
SISTEMA COMERCIAL DE REFERENCIA (SCR).
DIEGO JAVIER JOVE BASCUÑÁN
PROFESOR GUÍA: MARCO QUIROZ VALERIA
TALCA, JUNIO 2026


=== PÁG 2 del PDF ===
UNIVERSIDAD CATÓLICA DEL MAULE
FACULTAD DE CIENCIAS DE LA INGENIERÍA
ESCUELA DE INGENIERÍA CIVIL
Proyecto de Título presentado en conformidad a los requisitos para obtener el título de
Ingeniero Civil
METODOLOGÍA PARA LA CARACTERIZACIÓN DE FLUCTUACIONES DE
PRESIÓN EN MODELOS FÍSICOS HIDRÁULICOS ASISTIDA POR CFD:
EVALUACIÓN DE UN SISTEMA DE ARQUITECTURA ABIERTA (SAA) Y UN
SISTEMA COMERCIAL DE REFERENCIA (SCR).
DIEGO JAVIER JOVE BASCUÑÁN
PROFESOR GUÍA: MARCO QUIROZ VALERIA
COMISIÓN EXAMINADORA
Dr. NATALIA BUSTAMANTE PENAGOS
Ing. RODRIGO HERRERA HERNÁNDEZ
Dr. MARCO QUIROZ VALERIA
NOTA FINAL EXAMEN DE TÍTULO
FIRMA
PROFESOR DE COMISIÓN EXTERNA
PROFESOR DE COMISIÓN EXTERNA
PROFESOR DE COMISIÓN INTERNA
TALCA, JUNIO 2026


=== PÁG 3 del PDF ===
I
Resumen
La evaluación de presiones hidrodinámicas fluctuantes en estructuras de alta energía es crí-
tica para la seguridad estructural (Fiorotto and Rinaldo, 1992). Ante los altos costos de la instru-
mentación industrial, que restringen la densidad espacial de medición, esta tesis desarrolla una
metodología híbrida asistida por simulación numérica (CFD). Se evalúan los límites metrológi-
cos de un Sistema de Arquitectura Abierta (SAA) mediante su validación independiente frente a
un Sistema Comercial de Referencia (SCR).
El SAA (microcontroladores y transductores capacitivos con DSP interno (Stanghellini et al.,
2020)) se integra con una prospección topológica CFD (WMLES-VOF) (Bayon et al., 2016).
La metodología se implementó en el modelo físico del Embalse Ancoa (escala 1:40), aislando
variables hidráulicas mediante medición simultánea.
Los resultados revelan una dualidad metrológica. El SAA actúa como filtro paso-bajo natural;
la impedancia elasto-hidráulica y latencia del DSP subestiman la energía fluctuante (RMS) hasta
un ≈50 % (H. Tijdeman, 1965; Jentzsch et al., 2024). Simultáneamente, el ruido de cuantización
(ADC de 10 bits) induce una desviación leptocúrtica en las cargas. No obstante, la Densidad Es-
pectral de Potencia (PSD) confirmó la congruencia con la cascada de Kolmogorov (f −5/3) (Kol-
mogorov, 1991a) para la macroturbulencia dominante (f ≤20 Hz) hasta el límite del subrango
inercial (≈100 Hz). Pese a atenuar amplitud y alterar curtosis, el SAA preserva la topología
estocástica del flujo.
Se concluye que este marco es metrológicamente válido para el diseño de estabilidad global y
el mapeo de cargas medias y macroturbulentas. Establecidas sus fronteras operativas, el protocolo
reserva imperativamente evaluar la microturbulencia disipativa y cavitación incipiente al SCR
(Fattor et al., 2003).
Palabras clave: CFD, Modelo Físico, Fluctuación de Presión.


=== PÁG 4 del PDF ===
II
Abstract
The evaluation of fluctuating hydrodynamic pressures in high-energy structures is critical for
structural safety (Fiorotto and Rinaldo, 1992). Given the high costs of industrial instrumentation,
which restrict spatial measurement density, this thesis develops a hybrid methodology assisted
by numerical simulation (CFD). The metrological limits of an Open Architecture System (OAS)
are evaluated through independent validation against a Commercial Reference System (CRS).
The OAS (microcontrollers and capacitive transducers with internal DSP (Stanghellini et al.,
2020)) is integrated with a CFD topological prospection (WMLES-VOF) (Bayon et al., 2016).
The methodology was deployed in the Ancoa Dam physical model (1:40 scale), isolating hydrau-
lic variables through simultaneous measurement.
Results reveal a metrological duality. The OAS acts as a natural low-pass filter; elasto-
hydraulic impedance and DSP latency underestimate the fluctuating energy (RMS) by up to
≈50 % (H. Tijdeman, 1965; Jentzsch et al., 2024). Simultaneously, quantization noise (10-bit
ADC) induces a leptokurtic deviation in the loads. Nevertheless, Power Spectral Density (PSD)
confirmed congruence with the Kolmogorov cascade (f −5/3) (Kolmogorov, 1991a) for the do-
minant macroturbulence (f ≤20 Hz) up to the inertial subrange limit (≈100 Hz). Despite atte-
nuating amplitude and altering kurtosis, the OAS preserves the stochastic topology of the flow.
It is concluded that this framework is metrologically valid for global stability design and the
mapping of mean and macroturbulent loads. Having established its operational boundaries, the
protocol imperatively reserves evaluating dissipative microturbulence and incipient cavitation to
the CRS (Fattor et al., 2003).
Keywords: CFD, Physical Model, Pressure Fluctuation.


=== PÁG 5 del PDF ===
III
Agradecimientos
“Sus vidas son una carta escrita en nuestro corazón…” decía el apóstol Pablo. Yo mismo soy una carta, espe-
rando el compartir de quien(es) me escribe(n). Así he sido escrito: al compartir, conversar, hablar, reír y/o llorar con
ustedes, queridos lectores.
Este documento ha sido redactado con la ayuda de muchos, pero sería vano si esto no estuviera escrito en
mi vida. Si mi vida no muestra el agradecimiento que merecen cada uno de los que me ayudaron en este camino,
entonces esta tesis no debe ser tomada en cuenta.
Agradezco, entonces, no por haber consolidado este documento (que es un gran paso para mi vida profesional),
sino por el camino en conjunto. ¿Qué habría sido de esta tesis si mi querido amigo Darwin Vega Vidal no me
hubiese acogido en mi débil enseñanza media y no me hubiese mostrado la mayor humildad e inteligencia que he
conocido nunca? ¿O qué habría sido de mí si Cecilia Bascuñán, Javiera Jove, Katherine Jove y Mario Silva (mi
familia) no me hubiesen contenido en mis difíciles momentos donde no tenía fuerzas? ¿A qué mundo pertenecería
esta tesis sin la valiosísima amistad de Pedro Bocaz Pavéz? Pregunto entonces: ¿de quién es este mérito? ¿Mío?
Es de todos quienes me han acompañado y han valorado mi persona.
Por supuesto que necesitaría más páginas para agradecer que para el contenido mismo de esta tesis. Pero no
puedo dejar de agradecer al profesor Marco Quiroz Valeria, que pacientemente me acompañó en todo este tiempo;
a Rodrigo Herrera Hernández, quien no escatimó el tiempo invertido en esta tesis y, por supuesto, al INH, que
confió en mí tanto en la práctica como en la tesis y puso a disposición recursos, experiencia e instalaciones para
el desarrollo íntegro de este proyecto de título. A Natalia Bustamante Penagos, quien amablemente quiso formar
parte de esta comisión y, aún más, formó la base de todo este documento en mí.
Y, por supuesto, al hermoso grupo vida de San Fernando, que domingo a domingo aguantó mi cansancio,
oró por mí, y se dejó humildemente ser liderado por este servidor en aprendizaje (si alguna vez dejaré de ser un
aprendiz).
A Dios, de quien todo lo anterior provino y quien bendijo mi vida. Único digno de honra. Todo lo bueno viene
de Dios.
Y dijo Dios a la humanidad:
«Servir fielmente al Señor: eso es sabiduría;
apartarse del mal: eso es inteligencia.»
Job 28:28 (DHH)


=== PÁG 6 del PDF ===
IV
Índice general
Resumen
I
Abstract
II
Agradecimientos
IV
Índice de figuras
IX
Índice de tablas
X
1. Introducción
1
1.1. Contexto General: Verificación de Obras Hidráulicas . . . . . . . . . . . . . .
1
1.2. Planteamiento del Problema y propuesta de estudio . . . . . . . . . . . . . . .
2
1.3. Objetivos
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
1.3.1.
Objetivo General . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
1.3.2.
Objetivos Específicos . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
1.4. Alcances y Estructura de la Tesis . . . . . . . . . . . . . . . . . . . . . . . . .
4
2. Marco Teórico
6
2.1. Hidrodinámica del Flujo en SECDES
. . . . . . . . . . . . . . . . . . . . . .
6
2.1.1.
Componentes de la Presión en Flujos de Alta Velocidad
. . . . . . . .
6
2.2. Similitud de Froude y Escalas de Transferencia . . . . . . . . . . . . . . . . .
7
2.3. Fundamentos de Metrología y Procesamiento de Señales . . . . . . . . . . . .
8
2.3.1.
Validación de Linealidad (Regresión por Mínimos Cuadrados) . . . . .
8
2.3.2.
Análisis Estadístico de las Fluctuaciones de Presión . . . . . . . . . . .
9


=== PÁG 7 del PDF ===
2.3.2.1.
Valor Cuadrático Medio (RMS) . . . . . . . . . . . . . . . .
9
2.3.2.2.
Asimetría (Skewness) . . . . . . . . . . . . . . . . . . . . .
10
2.3.2.3.
Curtosis (Kurtosis) . . . . . . . . . . . . . . . . . . . . . . .
10
2.3.3.
Análisis Espectral: Método de Welch
. . . . . . . . . . . . . . . . . .
11
2.3.3.1.
Resolución en Frecuencia del Espectro (PSD) y Ventana Tem-
poral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
2.3.3.2.
Criterio de Nyquist y Aliasing Espectral
. . . . . . . . . . .
12
2.4. Física de la Turbulencia . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
2.4.1.
Cascada de Energía de Kolmogorov . . . . . . . . . . . . . . . . . . .
13
2.4.2.
Caracterización Espectral de la Macroturbulencia y Riesgos Estructurales 14
2.4.2.1.
Estimación de la Frecuencia Dominante (Número de Strouhal)
14
2.4.2.2.
Zonificación Espectral y Riesgos Estructurales . . . . . . . .
14
2.5. Fundamentos de la Dinámica de Fluidos Computacional (CFD) . . . . . . . . .
15
2.5.1.
Ecuaciones de Gobierno para una Simulación a Grandes Escalas . . . .
15
2.5.1.1.
Definición del Filtro Espacial (∆) . . . . . . . . . . . . . . .
16
2.5.2.
Modelo de Subgrilla de una Ecuación (kEqn) . . . . . . . . . . . . . .
16
2.5.3.
Física de la Capa Límite y Modelación de Pared
. . . . . . . . . . . .
18
3. Equipamiento y Facilidades Experimentales
20
3.1. El Modelo Físico del Embalse Ancoa
. . . . . . . . . . . . . . . . . . . . . .
20
3.2. Sistema de Alimentación Hidráulica . . . . . . . . . . . . . . . . . . . . . . .
24
3.3. Sistema Comercial de Referencia (SCR) . . . . . . . . . . . . . . . . . . . . .
24
3.3.1.
Adquisidor de Datos (DAQ) . . . . . . . . . . . . . . . . . . . . . . .
25
3.3.2.
Transductores Keller Serie 25Y
. . . . . . . . . . . . . . . . . . . . .
25
3.4. Sistema de Arquitectura Abierta (SAA)
. . . . . . . . . . . . . . . . . . . . .
26
3.4.1.
Adquisidor de Datos (DAQ) y Flexibilidad Topológica . . . . . . . . .
26
3.4.2.
Transductores Keller Serie 41X
. . . . . . . . . . . . . . . . . . . . .
27
4. Metodología de la implementación del Modelo Numérico (CFD)
30
4.1. Selección del Solver y Esquemas Numéricos . . . . . . . . . . . . . . . . . . .
30
4.1.1.
Configuración de Esquemas de Discretización . . . . . . . . . . . . . .
31


=== PÁG 8 del PDF ===
4.2. Pre-procesamiento de la Geometría y Dominio Computacional . . . . . . . . .
33
4.2.1.
Procedimiento de Reparación Topológica . . . . . . . . . . . . . . . .
33
4.2.2.
Definición de Fronteras (Patches) . . . . . . . . . . . . . . . . . . . .
34
4.3. Estrategia de Discretización Espacial (Malla)
. . . . . . . . . . . . . . . . . .
36
4.4. Modelación de la Turbulencia y Condiciones de Borde
. . . . . . . . . . . . .
39
4.4.1.
Modelo de Turbulencia y Tratamiento de Pared . . . . . . . . . . . . .
39
4.4.1.1.
Definición y Suavizado del Filtro Espacial (∆) . . . . . . . .
39
4.4.1.2.
Tratamiento de Pared WMLES y Verificación del y+ . . . . .
39
4.4.2.
Definición de Campos y Fronteras . . . . . . . . . . . . . . . . . . . .
40
4.5. Control de la Simulación y Post-proceso . . . . . . . . . . . . . . . . . . . . .
42
4.5.1.
Control de Extracción de Datos y Funciones de Monitoreo . . . . . . .
42
4.5.2.
Criterio de Convergencia y Estado Estacionario . . . . . . . . . . . . .
43
5. Metodología Experimental
44
5.1. Configuración de la Interfaz Mecánica de Medición . . . . . . . . . . . . . . .
44
5.1.1.
Optimización de la Fijación y Estanqueidad . . . . . . . . . . . . . . .
44
5.1.2.
Diseño de Acoples y Conexión a Mangueras
. . . . . . . . . . . . . .
45
5.2. Metodología de Caracterización Metrológica Estática . . . . . . . . . . . . . .
46
5.2.1.
Diseño del Banco de Calibración (Principio de Sifón) . . . . . . . . . .
46
5.2.2.
Protocolo de Carga Escalonada
. . . . . . . . . . . . . . . . . . . . .
47
5.3. Resultados de Calibración y Selección de Instrumentación
. . . . . . . . . . .
49
5.3.1.
Análisis del Sistema de Arquitectura Abierta (SAA)
. . . . . . . . . .
49
5.3.2.
Análisis del Sistema Comercial de Referencia (SCR) . . . . . . . . . .
51
5.4. Protocolo de Instalación In-Situ y Caracterización Dinámica . . . . . . . . . .
53
5.4.1.
Compensación Topográfica y Procedimiento de Tara Hidráulica . . . .
53
5.4.2.
Caracterización del Rendimiento de Adquisición (SAA)
. . . . . . . .
54
5.5. Verificación de Condiciones de Contorno Geométricas
. . . . . . . . . . . . .
56
5.6. Estimación Teórica del Espectro de Energía . . . . . . . . . . . . . . . . . . .
58
6. Resultados y Discusión
62
6.1. Caracterización Numérica del Flujo (OE 1)
. . . . . . . . . . . . . . . . . . .
63


=== PÁG 9 del PDF ===
6.2. Validación Experimental y Discusión del Desfase Espacial . . . . . . . . . . .
67
6.2.1.
Configuración Física y Cinemática del Flujo
. . . . . . . . . . . . . .
67
6.2.2.
Registro de Fluctuaciones de Presión y Desfase Espacial . . . . . . . .
70
6.3. Caracterización Comparativa del Desempeño Instrumental (OE 2) . . . . . . .
73
6.3.1.
Sincronía Temporal y Respuesta Transitoria . . . . . . . . . . . . . . .
73
6.3.1.1.
Análisis Espectral Comparativo y Cascada de Kolmogorov
.
74
6.4. Evaluación Estadística y Determinación de Límites del SAA . . . . . . . . . .
77
6.4.1.
Comportamiento Metrológico en Puntos Adyacentes . . . . . . . . . .
78
6.4.2.
Limitaciones en el Punto de Máxima Fluctuación de Presión . . . . . .
78
6.4.3.
Evaluación de la Asimetría y Curtosis . . . . . . . . . . . . . . . . . .
79
7. Conclusiones y Recomendaciones
81
7.1. Conclusiones y Límites de Aplicabilidad . . . . . . . . . . . . . . . . . . . . .
81
7.1.1.
Matriz de Decisión Metrológica (Síntesis OE 3) . . . . . . . . . . . . .
83
7.2. Recomendaciones y Trabajo Futuro
. . . . . . . . . . . . . . . . . . . . . . .
85
7.3. Síntesis Global
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
86
Bibliografía
87


=== PÁG 10 del PDF ===
VIII
Índice de figuras
3.1. Vista general del modelo físico del Embalse Ancoa . . . . . . . . . . . . . . .
21
3.2. Componentes del modelo físico del Embalse Ancoa . . . . . . . . . . . . . . .
22
3.3. Imagen de los Dientes de disipación del Modelo físico
. . . . . . . . . . . . .
23
3.4. Imagen del Vertedero del Modelo físico . . . . . . . . . . . . . . . . . . . . .
23
3.5. Render del Salto de Esquí . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
3.6. Componentes del sistema de alimentación hidráulica
. . . . . . . . . . . . . .
24
3.7. Diagrama eléctrónico del DAQ del SAA . . . . . . . . . . . . . . . . . . . . .
26
3.8. Transductor de presión capacitivo Keller Serie 41X . . . . . . . . . . . . . . .
28
3.9. Montaje experimental de los sistemas de adquisición
. . . . . . . . . . . . . .
29
4.1. Definición de las fronteras (patches) en el dominio computacional utilizando
Blender . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
4.2. Malla generada por snappyHexMesh . . . . . . . . . . . . . . . . . . . . . . .
38
5.1. Detalle de la instalación de tomas de presión . . . . . . . . . . . . . . . . . . .
46
5.2. Montaje experimental para la calibración estática . . . . . . . . . . . . . . . .
48
5.3. Serie de tiempo en el banco de calibración estático
. . . . . . . . . . . . . . .
50
5.4. Curvas de Calibración Sensores Capacitivos . . . . . . . . . . . . . . . . . . .
50
5.5. Serie de tiempo en el banco de calibración estático
. . . . . . . . . . . . . . .
52
5.6. Curvas de Calibración sistema comercial . . . . . . . . . . . . . . . . . . . . .
52
5.7. Curva de caracterización del rendimiento (fs vs Baudios) del SAA . . . . . . .
55
5.8. Validación Topográfica In-Situ . . . . . . . . . . . . . . . . . . . . . . . . . .
57
5.9. Evidencia del levantamiento topográfico . . . . . . . . . . . . . . . . . . . . .
58
5.10. Espectro Teórico de Densidad de Potencia y Bandas de Turbulencia
. . . . . .
61


=== PÁG 11 del PDF ===
6.1. Comparación visual del modelo matemático y físico . . . . . . . . . . . . . . .
64
6.2. Comparación de fluctuaciones RMS: CFD vs Teoría . . . . . . . . . . . . . . .
65
6.3. Plano transversal de control en el modelo numérico . . . . . . . . . . . . . . .
66
6.4. Caracterización cinemática numérica integrada
. . . . . . . . . . . . . . . . .
67
6.5. Ubicación de sensores en el modelo físico . . . . . . . . . . . . . . . . . . . .
68
6.6. Medición de tirante con sensor ultrasónico . . . . . . . . . . . . . . . . . . . .
69
6.7. Distribución de presión: Numérico vs Físico . . . . . . . . . . . . . . . . . . .
72
6.8. Sincronización y respuesta transitoria en series temporales
. . . . . . . . . . .
73
6.9. Validación espectral comparativa: SAA vs SCR . . . . . . . . . . . . . . . . .
76


=== PÁG 12 del PDF ===
X
Índice de tablas
2.1. Relaciones de Escala para el Modelo Ancoa . . . . . . . . . . . . . . . . . . .
8
2.2. Relación entre dominios espectrales de presión, solicitaciones estructurales y via-
bilidad instrumental. Adaptado de Lopardo (2018); Pope (2000). . . . . . . . .
15
4.1. Resumen de las condiciones de borde aplicadas en OpenFOAM
. . . . . . . .
40
5.1. Parámetros de calibración SAA . . . . . . . . . . . . . . . . . . . . . . . . . .
51
5.2. Parámetros de calibración SCR . . . . . . . . . . . . . . . . . . . . . . . . . .
53
6.1. Resumen de Ensayos en Modelo Físico Embalse Ancoa . . . . . . . . . . . . .
63
6.2. Contraste estadístico y sensibilidad frecuencial SAA vs SCR . . . . . . . . . .
77
7.1. Matriz de Decisión Metrológica para Diseño Hidráulico . . . . . . . . . . . . .
84


=== PÁG 13 del PDF ===
1
Capítulo 1
Introducción
1.1.
Contexto General: Verificación de Obras Hidráulicas
El diseño de los Sistemas de Evacuación de Crecidas y Disipación de Energía (SECDE)
es un desafío crítico en la ingeniería de presas. Estas estructuras deben disipar enormes canti-
dades de energía cinética para proteger la integridad de la obra y el entorno (Chanson, 2004).
Históricamente, la modelación física a escala reducida ha sido el método más confiable para
verificar estos diseños, permitiendo observar fenómenos complejos como la aireación y la macro-
turbulencia en condiciones controladas que las formulaciones analíticas no alcanzan a cubrir con
precisión (Novak et al., 2007). Para obras hidráulicas que concentran una gran carga de energía
potencial, como el Embalse Ancoa, una solución consiste en transformar dicha carga y disipar la
resultante energía cinética extrema mediante un SECDE (INH, 2015b). En este caso de estudio,
dicho sistema está compuesto secuencialmente por un vertedero lateral, un canal colector, un
rápido de descarga conformado por dos tramos de distinta pendiente, y una estructura terminal
tipo salto de esquí. Es en este salto de esquí donde se produce la disipación final de energía,
lograda mediante la proyección atmosférica, paulatina aireación e impacto hidrodinámico del
chorro supercrítico (Heller et al., 2005).
En el salto de esquí, la variable determinante para el diseño estructural no es la presión estáti-
ca media, sino las fluctuaciones de presión (Rafael Santiago Seoane and Raúl Antonio Lopardo,
2006). La turbulencia del chorro y su impacto en el radier generan solicitaciones transitorias que
pueden inducir fatiga mecánica, vibraciones estructurales y fuerzas de levantamiento (uplift) en


=== PÁG 14 del PDF ===
2
las losas de hormigón. Para capturar estos fenómenos, es imperativo contar con instrumentación
de alta resolución temporal capaz de registrar eventos extremos de corta duración. Sin datos
experimentales, el sobredimensionamiento o la falla imprevista se convierten en riesgos latentes
para la infraestructura (Chanson, 2004).
1.2.
Planteamiento del Problema y propuesta de estudio
A pesar de su importancia, la captura de las fluctuaciones de presión en obras de SECDE
enfrenta una brecha económica y operativa significativa. Los equipos de adquisición de datos
(DAQ) utilizados en los Sistemas Comerciales de Referencia (SCR) ofrecen precisión metro-
lógica (HR Wallingford, 2024), pero son costosos y operan como arquitecturas cerradas (“cajas
negras”). Esta rigidez comercial imposibilita la modificación del hardware o software según las
necesidades experimentales del investigador y limita la cantidad de sensores que pueden imple-
mentarse simultáneamente en modelos complejos debido a los altos costos asociados (Galli et al.,
2024).
En respuesta a esto, los sistemas de arquitectura abierta (SAA) basados en microcontrola-
dores han emergido como una alternativa económica para la instrumentación en fluidos (Stanghe-
llini et al., 2020; Rodríguez-Juárez et al., 2018). Sin embargo, su adopción está restringida por la
ausencia de protocolos de validación metrológica (Jentzsch et al., 2024; Figliola and Beasley,
2019). A diferencia de los SCR, que operan como sistemas propietarios con respuesta dinámi-
ca certificada de fábrica para capturar el espectro turbulento (HR Wallingford, 2024), los SAA
integran componentes electrónicos genéricos. Por consiguiente, la precisión de su respuesta diná-
mica operando en conjunto es desconocida. Específicamente, se desconoce cómo la integración
de un transductor comercial con un DAQ de bajo costo degrada la señal dadas las posibles limita-
ciones de latencia y sincronización del microcontrolador. Por tanto, resulta imperativo establecer
si un SAA puede constituir una alternativa ingenieril válida frente a los estándares comerciales
bajo condiciones de flujo real.
Este estudio aborda la problemática descrita mediante la modelación física, asistida por la
modelación numérica. Durante la modelación física, se implementa un Sistema de Arquitectura
Abierta (SAA) basado en los principios de código abierto propuestos por el proyecto OpenS-


=== PÁG 15 del PDF ===
3
WAP (Stanghellini et al., 2020). Este SAA se estructura a partir de un DAQ basado en un mi-
crocontrolador Arduino Mega 2560, acoplado a transductores capacitivos de la serie Keller 41X
(KELLER Druckmesstechnik AG, 2023). Para validar esta instrumentación, se desarrolla un es-
tudio de benchmarking tecnológico que contrasta el desempeño del SAA frente al SCR, este
último compuesto por el DAQ HR-Wallingford TOPS (HR Wallingford, 2024) y sensores de
tecnología piezorresistiva de diafragma enrasado (KELLER AG für Druckmesstechnik, 2024).
La evaluación metrológica se ejecutó bajo condiciones de operación simultánea, capturando las
fluctuaciones de presión de manera paralela e independiente a través de los mismos puntos hi-
dráulicos en el escenario de estudio.
Como escenario de estudio, se utiliza el modelo físico a escala 1:40 del evacuador de crecidas
del Embalse Ancoa, diseñado, construido y operado por el Instituto Nacional de Hidráulica
(INH) (INH, 2015b). En este contexto, la modelación numérica (CFD mediante OpenFOAM)
se emplea como una herramienta de asistencia metodológica para caracterizar el campo de flujo
general, predecir los rangos de presión y delimitar espacialmente las zonas de máxima fluctua-
ción, permitiendo definir los puntos de interés para la instrumentación.
1.3.
Objetivos
1.3.1.
Objetivo General
Desarrollar una metodología técnico-experimental para la caracterización de fluctuaciones
de presión en modelos físicos hidráulicos, asistida por simulación numérica (CFD) para definir
los rangos de presión y fluctuaciones en la zona de estudio, evaluando el desempeño de un Siste-
ma de Arquitectura Abierta (SAA) mediante su comparación independiente frente a un Sistema
Comercial de Referencia (SCR) en el modelo físico del Embalse Ancoa (INH).
1.3.2.
Objetivos Específicos
OE 1: Implementar una simulación numérica tridimensional mediante la estrategia WM-
LES y el solver interFoam en OpenFOAM del modelo físico del Embalse Ancoa, con
el fin de caracterizar el campo de presiones, velocidades y superficie libre (por medio del


=== PÁG 16 del PDF ===
4
campo αwater) en el salto de esquí, definiendo los rangos de presión esperados y determi-
nando la distribución espacial de los sensores a partir de la zona de máxima fluctuación
turbulenta.
OE 2: Evaluar el desempeño de un Sistema de Arquitectura Abierta (SAA) frente a un
Sistema Comercial de Referencia (SCR) en el vertedero tipo salto de esquí del Embalse
Ancoa, mediante la comparación independiente de presiones en puntos hidráulicos com-
partidos bajo diferentes regímenes de caudal, analizando series temporales, estadísticos
de presión y la Densidad Espectral de Potencia (PSD) para cuantificar el impacto de la
variación de la tasa de muestreo en la resolución del espectro de energía turbulenta.
OE 3: Desarrollar protocolos técnicos para resolver los desafíos constructivos asociados
al SAA, contrastando su respuesta frente al SCR para caracterizar la funcionalidad y sus
límites operativos.
1.4.
Alcances y Estructura de la Tesis
El documento se estructura en siete capítulos que describen el flujo metodológico de la in-
vestigación. El Capítulo 2 expone el marco teórico, definiendo las ecuaciones gobernantes de la
hidrodinámica, las leyes de similitud de Froude, los modelos de subgrilla para CFD (WMLES) y
los fundamentos metrológicos para el análisis de señales. El Capítulo 3 describe el modelo físico
y sus componentes hidráulicos, como bombas y caudalímetros; asimismo, presenta los sistemas
de adquisición de datos SCR y SAA, especificando la arquitectura del DAQ y los sensores que
integran cada uno.
El Capítulo 4 describe la configuración del modelo numérico en OpenFOAM, el cual asiste
al diseño experimental al predecir los rangos de presión y definir los puntos de interés a medir en
los ensayos del modelo físico. El Capítulo 5 establece el diseño experimental previo necesario
para los ensayos, abarcando el montaje de las líneas de transmisión (mangueras), la calibración
estática del SAA y SCR, la comprobación de parámetros geométricos del modelo físico y la
estimación del espectro esperado de los ensayos. El Capítulo 6 expone los resultados del modelo
numérico y del modelo físico, contrastando los datos obtenidos con modelos teóricos. Asimismo,


=== PÁG 17 del PDF ===
5
valida la señal adquirida por ambos sistemas a través de un análisis espectral y establece sus
límites operativos por medio de estadísticos. Finalmente, el Capítulo 7 presenta las conclusiones
del estudio, determinando los límites operativos comprobados del SAA y SCR y estableciendo
sus restricciones técnicas para el diagnóstico de fenómenos de alta frecuencia.


=== PÁG 18 del PDF ===
6
Capítulo 2
Marco Teórico
Este capítulo establece los fundamentos teóricos para la comprensión de la hidrodinámica
en los SECDES, las leyes de similitud física, los principios metrológicos del procesamiento
de señales y la modelación numérica mediante Simulación a Grandes Escalas (LES). La base
conceptual integra la literatura clásica de la hidráulica con criterios de instrumentación dinámica.
2.1.
Hidrodinámica del Flujo en SECDES
Los SECDES son estructuras diseñadas para operar en regímenes de flujo supercrítico, donde
la macroturbulencia y los fenómenos de aireación actúan como los principales mecanismos de
disipación de energía (Novak et al., 2007; Heller et al., 2005; Lopardo, 2018).
2.1.1.
Componentes de la Presión en Flujos de Alta Velocidad
La presión total instantánea P(t) en un punto sobre el SECDE puede descomponerse, según
la descomposición de Reynolds, en una componente media temporal y una componente fluctuan-
te turbulenta (Chanson, 2004; Pope, 2000):
P(t) = P + P ′(t)
(2.1)
Donde P es la presión media (suma de las componentes hidrostática y centrífuga) y P ′(t)
representa la fluctuación instantánea originada por la naturaleza turbulenta del flujo. En el diseño


=== PÁG 19 del PDF ===
7
de SECDES, esta última es la responsable de las solicitaciones dinámicas que pueden compro-
meter la integridad estructural (Fiorotto and Rinaldo, 1992; Fattor et al., 2003).
2.2.
Similitud de Froude y Escalas de Transferencia
La modelación física se fundamenta teóricamente en el cumplimiento de las similitudes geo-
métrica, cinemática y dinámica (Chanson, 2004; Novak et al., 2007). No obstante, alcanzar una
similitud dinámica absoluta es inviable al utilizar el mismo fluido en modelo y prototipo, debido
a la imposibilidad de satisfacer simultáneamente las escalas de fuerzas gravitacionales (Froude),
viscosas (Reynolds) y de tensión superficial (Weber) (Novak et al., 2007). Dado que en flujos a
superficie libre la inercia es contrarrestada predominantemente por la aceleración de gravedad,
se adopta el Número de Froude (Fr) como parámetro gobernante (Ettema, 2000).
Esta decisión metodológica impone la igualdad del parámetro adimensional entre el modelo
(m) y el prototipo (p), de modo que Frm = Frp. El cumplimiento de esta ley dinámica arrastra
intrínsecamente la similitud cinemática, definiendo las relaciones de transferencia para veloci-
dades y tiempos (Ettema, 2000; Chanson, 2004). El Número de Froude se define explícitamente
como la relación entre las fuerzas inerciales y gravitacionales, o equivalentemente, como el co-
ciente entre la velocidad del flujo y la celeridad de propagación de las ondas de gravedad de
pequeña amplitud (Ettema, 2000):
Fr =
V
√gL
(2.2)
Donde:
V : Velocidad característica del flujo, definida como la velocidad media en la sección de
control.
g: Aceleración de gravedad.
L: Longitud característica del escurrimiento.
En el análisis de saltos de esquí, la elección de L responde al fenómeno de propagación
de ondas de gravedad (Ettema, 2000; Chanson, 2004). Esta investigación adopta el tirante de


=== PÁG 20 del PDF ===
8
escurrimiento de aproximación (h0) como longitud característica en lugar del radio hidráulico.
Esta elección se fundamenta en que, en canales anchos y rápidas de descarga, la profundidad
hidráulica es matemáticamente equivalente al tirante (Chanson, 2004). Según Heller et al. (2005),
el flujo de aproximación queda descrito por el Número de Froude incidente (F = V /√gh0) y la
curvatura relativa (h0/R), proporcionando una base metrológica estable para la caracterización
de presiones.
Para el presente estudio, se adopta la escala geométrica del modelo físico original del Embal-
se Ancoa, establecida en λL = 40 para minimizar los efectos de escala viscosos (INH, 2015b).
Las relaciones de transferencia se presentan en la Tabla 2.1.
Tabla 2.1: Relaciones de Escala (Criterio de Froude, λL = 40). Fuente: Adaptado de INH (2015b)
Magnitud
Similitud
Relación
Factor de Escala
Longitud (L)
Geométrica
λL
40
Velocidad (V )
Cinemática
λV = λ1/2
L
6.32
Tiempo (T)
Cinemática
λT = λ1/2
L
6.32
Caudal (Q)
Dinámica
λQ = λ5/2
L
10,119.29
Presión (P)
Dinámica
λP = λL
40
Frecuencia (f)
Cinemática
λf = λ−1/2
L
0.158
Es crucial notar que la escala de presión es lineal (λP = 40). Por tanto, una lectura de 1 cm
en el modelo equivale a 40 cm en el prototipo.
2.3.
Fundamentos de Metrología y Procesamiento de Señales
Para validar la instrumentación y analizar la turbulencia, se utilizan métodos estadísticos y
espectrales.
2.3.1.
Validación de Linealidad (Regresión por Mínimos Cuadrados)
La calibración estática de sensores busca establecer una función de transferencia lineal entre
la señal eléctrica (xi) y la variable física (yi). El método de Mínimos Cuadrados Ordinarios


=== PÁG 21 del PDF ===
9
(OLS) estima la pendiente (m) y el intercepto (b) minimizando la suma de los errores cuadráticos
(Figliola and Beasley, 2019):
yi = m · xi + b + ϵi
(2.3)
Llevándolo a una función lineal:
ˆyi = ˆm · xi + ˆb
(2.4)
La calidad del ajuste se evalúa mediante el Coeficiente de Determinación (R2), donde un
valor R2 ≈1 indica una respuesta perfectamente lineal del sensor.
El OLS determina los siguientes valores para los coeficientes:
ˆm = xiyi −¯xi ¯yi
x2
i −xi2
(2.5)
ˆb = ¯y −ˆm · ¯x
(2.6)
siendo el operador promedio de una sucesión ai definido como ¯a =
Pn
i=1 ai
n
.
Además el coeficiente de determinación R2 se define como:
R2 = 1 −
Pn
i=1 (yi −ˆyi)2
Pn
i=1 (yi −¯y)2
(2.7)
2.3.2.
Análisis Estadístico de las Fluctuaciones de Presión
Para caracterizar la naturaleza estocástica de las fluctuaciones de presión P ′(t), se utilizan
momentos estadísticos de orden superior. Estos parámetros son fundamentales para evaluar la
intensidad de la turbulencia y la distribución probabilística de las cargas dinámicas sobre el fondo
de la estructura (Figliola and Beasley, 2019).
2.3.2.1.
Valor Cuadrático Medio (RMS)
La raíz cuadrática media (Root Mean Square, RMS) de la señal fluctuante P ′(t) representa
la desviación estándar de la presión, y es una medida directa de la intensidad de la turbulencia
o la energía asociada a las fluctuaciones. Para una señal discreta de N puntos, se calcula como
(Figliola and Beasley, 2019):


=== PÁG 22 del PDF ===
10
P ′
rms =
v
u
u
t 1
N
N
X
i=1
(P ′
i)2 =
v
u
u
t 1
N
N
X
i=1
(Pi −P)2
(2.8)
Donde Pi es el valor instantáneo de presión en el tiempo ti y P es la presión media temporal.
Un valor alto de P ′
rms indica fluctuaciones de presión de gran amplitud.
2.3.2.2.
Asimetría (Skewness)
El coeficiente de asimetría (Skewness, S) es el tercer momento central normalizado de la
distribución de probabilidad. Mide el grado de asimetría de la distribución de las fluctuaciones
respecto a su valor medio (Figliola and Beasley, 2019). Se calcula como:
S =
1
N(P ′
rms)3
N
X
i=1
(Pi −P)3
(2.9)
Si S ≈0, la distribución tiende a la simetría respecto al tercer momento (como una dis-
tribución Normal), condición que caracteriza al movimiento turbulento de canal ordinario
sin separación de flujo (Fattor et al., 2003).
Si S > 0, la distribución presenta una cola elongada hacia la derecha, indicando la ocu-
rrencia de peaks de presión positiva cuyas amplitudes extremas superan en magnitud a
las fluctuaciones negativas, fenómeno típicamente asociado a zonas de estancamiento o
impacto directo del flujo (Fattor et al., 2003).
Si S < 0, la distribución exhibe una cola extendida hacia la izquierda, denotando peaks de
presión negativa (subpresiones) de magnitud crítica respecto al valor medio. Físicamente,
esta condición localiza zonas de separación de la capa límite, revelando una predominancia
de fuerzas de succión críticas para el riesgo de cavitación y el levantamiento de losas
(Fattor et al., 2003).
2.3.2.3.
Curtosis (Kurtosis)
El coeficiente de curtosis (Kurtosis, K) es el cuarto momento central normalizado. Mide el
“apuntamiento” o la pesadez de las colas de la distribución de probabilidad en comparación con
una distribución Normal. Se define como (Figliola and Beasley, 2019):


=== PÁG 23 del PDF ===
11
K =
1
N(P ′
rms)4
N
X
i=1
(Pi −P)4
(2.10)
Una distribución Normal perfecta tiene una curtosis de K = 3.
Si K > 3 (distribución leptocúrtica): Indica una mayor probabilidad de eventos extre-
mos (peaks de presión muy alejados de la media) en comparación con una distribución
Normal.
Si K < 3 (distribución platicúrtica): Indica una distribución más plana, donde las fluc-
tuaciones se mantienen dentro de un rango más acotado y predecible.
2.3.3.
Análisis Espectral: Método de Welch
Para caracterizar el contenido energético de la turbulencia, se utiliza la Densidad Espectral
de Potencia (PSD). Bajo condiciones de régimen permanente (donde la señal de presión se asu-
me estadísticamente estacionaria), el cálculo directo de la Fast-Fourier Transform (FFT) sobre
toda la serie temporal resulta en un estimador inconsistente debido a la naturaleza estocástica del
flujo turbulento: la varianza del espectro no disminuye aunque aumente la duración del registro,
generando gráficas con excesivo ruido que dificultan la identificación de frecuencias dominantes
(BENDAT and PIERSOL, 2010).
Para solucionar esto, se implementa el Método de Welch (Welch, 1967). Este algoritmo di-
vide la señal temporal en segmentos superpuestos y promedia sus periodogramas modificados.
Como concluyen Proakis and Manolakis (2007), este procedimiento establece un compromi-
so fundamental (trade-off) entre resolución y estabilidad: la división en segmentos reduce la
varianza del estimador espectral (suavizando el ruido), pero lo hace a expensas de reducir la
resolución en frecuencia, ensanchando los lóbulos principales del espectro.
2.3.3.1.
Resolución en Frecuencia del Espectro (PSD) y Ventana Temporal
Dado este compromiso, la elección de la ventana temporal es crítica. La resolución en fre-
cuencia (∆f) del estimador espectral es inversamente proporcional a la duración de cada seg-
mento (Tw):


=== PÁG 24 del PDF ===
12
∆f = 1
Tw
=
fs
nperseg
(2.11)
Siendo fs la frecuencia de muestreo y nperseg el número de puntos por segmento. En este
contexto, ∆f representa la resolución en frecuencia de la Transformada Discreta y del estimador
PSD (la separación entre los intervalos de frecuencia calculados), no una frecuencia física adicio-
nal del flujo. Específicamente para el análisis de la macroturbulencia en disipadores de energía,
investigaciones empíricas han demostrado que una resolución espectral en torno a ∆f ≈0, 2 Hz
resulta óptima para aislar claramente las frecuencias bajas dominantes (Lopardo and Romagnoli,
2008). Satisfacer esta selectividad frecuencial requiere matemáticamente el uso de ventanas de
integración (Tw = 1/∆f) de aproximadamente 5 segundos. Al aplicar el Método de Welch sobre
registros de longitud adecuada, esta partición de la serie temporal garantiza suficientes promedios
para mantener el error estándar de la estimación espectral en márgenes controlados, alcanzando
típicamente valores cercanos al 17 % en estricto cumplimiento con la teoría de señales aleatorias
(BENDAT and PIERSOL, 2010).
2.3.3.2.
Criterio de Nyquist y Aliasing Espectral
Para digitalizar las fluctuaciones de presión, compuestas físicamente por una superposición
de estructuras vorticiales de múltiples tamaños y frecuencias, el sistema de adquisición de datos
debe cumplir el Criterio de Nyquist-Shannon (Figliola and Beasley, 2019). En el contexto de
la hidrodinámica experimental, este criterio establece que, para estimar el espectro turbulento y
evitar la contaminación de la señal por el solapamiento de componentes no resueltas (fenómeno
de aliasing), la frecuencia de muestreo (fs) debe ser superior al doble de la frecuencia máxima
de interés energético presente en el flujo (fmax) (Figliola and Beasley, 2019):
fs > 2 · fmax
(2.12)
Donde fN = fs/2 define el límite de Nyquist o frecuencia de plegamiento. De esta manera,
para la caracterización de la macroturbulencia en modelos físicos, resulta imperativo operar en
un régimen de sobremuestreo (fs ≫fd). Esta condición metrológica garantiza la identificación
precisa de la frecuencia dominante (fd) y el cálculo consistente del PSD (BENDAT and PIER-
SOL, 2010), asegurando la estimación de la transferencia de energía en el subrango inercial para


=== PÁG 25 del PDF ===
13
verificar la convergencia hacia la pendiente teórica de −5/3 de la cascada de Kolmogorov (Pope,
2000).
Desde una perspectiva metrológica, el incumplimiento de este criterio induce el fenómeno
de aliasing. Físicamente, la energía contenida en las componentes de alta frecuencia, asociadas a
las escalas disipativas de la turbulencia (Pope, 2000), que exceden el límite de fN se redistribuye
o “pliega” erróneamente hacia las bandas de baja frecuencia del espectro digitalizado (Figliola
and Beasley, 2019; Proakis and Manolakis, 2007). Este artefacto de digitalización altera la com-
posición de los momentos centrales de la señal: induce un sesgo sistemático que sobreestima la
desviación estándar (RMS) y distorsiona la curtosis. En consecuencia, la ausencia de un sobre-
muestreo corrompe la integridad de las señales adquiridas, invalidando la caracterización de la
turbulencia por parte del sistema de adquisición (BENDAT and PIERSOL, 2010; Figliola and
Beasley, 2019).
2.4.
Física de la Turbulencia
2.4.1.
Cascada de Energía de Kolmogorov
La teoría de la turbulencia isótropa de Kolmogorov (1991a) describe cómo la energía cinética
se transfiere desde los grandes vórtices hacia las escalas microscópicas disipativas. En el dominio
espacial, el espectro de energía E(κ) (donde κ representa el número de onda direccional) decae a
través del subrango inercial siguiendo una ley de potencia universal proporcional a κ−5/3 (Pope,
2000). Al registrar fluctuaciones de presión con transductores fijos, la Hipótesis de Turbulencia
Congelada de Taylor permite trasladar esta distribución espacial al dominio de la frecuencia (f),
estableciendo que el PSD de la señal temporal obedece la relación (Pope, 2000):
Sxx(f) ∝f −5/3
(2.13)
Esta pendiente de −5/3 en un espectro Log-Log es la firma de un flujo turbulento desarro-
llado. Metrológicamente, el sistema de adquisición debe estimar esta pendiente (BENDAT and
PIERSOL, 2010), preservando la energía de la señal hasta que sea atenuada por la frecuencia
de corte de la línea de transmisión (mangueras) o el piso de ruido del transductor (Figliola and


=== PÁG 26 del PDF ===
14
Beasley, 2019; Jentzsch et al., 2024).
2.4.2.
Caracterización Espectral de la Macroturbulencia y Riesgos Estruc-
turales
Para evaluar la representatividad de las mediciones dinámicas capturadas por el SAA y el
SCR, se requiere definir métricas que vinculen la cinemática del flujo con la respuesta en fre-
cuencia esperada en el PSD. Esta estimación analítica permite validar si los peaks energéticos
registrados tienen un origen hidrodinámico (Lopardo and Romagnoli, 2008; Fattor et al., 2003).
2.4.2.1.
Estimación de la Frecuencia Dominante (Número de Strouhal)
En los SECDE, la mayor parte del contenido energético de las fluctuaciones de presión se
concentra en las bajas frecuencias, asociadas a vórtices de mayor escala (Toso and Bowers, 1988;
Bollaert and Schleiss, 2003; Fattor et al., 2003). La frecuencia asociada a la máxima energía (fd)
se estima mediante el Número de Strouhal (Sd) (Lopardo, 2018) definido como:
Sd = fd · ho
Uo
(2.14)
Donde Uo y ho son la velocidad media y el tirante de escurrimiento incidentes en la sección
de control. Basado en mediciones experimentales de presión sobre la base de resaltos hidráulicos
libres, Lopardo (2018) determinaron que el número de Strouhal asociado a este peak de inyección
de energía macroturbulenta se enmarca estrictamente en el rango de 0,01 a 0,08.
2.4.2.2.
Zonificación Espectral y Riesgos Estructurales
El análisis del PSD permite diferenciar tres dominios hidrodinámicos, los cuales se vincu-
lan directamente con los mecanismos de falla de la estructura (Fattor et al., 2003; Fiorotto and
Rinaldo, 1992). La caracterización de cada dominio advierte sobre distintas solicitaciones estruc-
turales y define la viabilidad metrológica y los límites operativos de los sistemas (Tabla 2.2).


=== PÁG 27 del PDF ===
15
Tabla 2.2: Relación entre dominios espectrales de presión, solicitaciones estructurales y viabili-
dad instrumental. Adaptado de Lopardo (2018); Pope (2000).
Zona Espectral
Métrica / Fenomenología
Riesgo Estructural
Macroturbulencia
(Inyección de Ener-
gía)
Peak energético (fd) predi-
cho por Sd ∈[0,01, 0,08].
Riesgo: Levantamiento de losas
(slab uplift) y resonancia hidroelás-
tica.
Sub-rango Inercial
Decaimiento universal
según Ley de Kolmogorov
(−5/3)
Fidelidad Instrumental: Referen-
cia universal para validar que los
transductores capturan la física real
del flujo turbulento y no ruido eléc-
trico espurio.
Escalas Disipativas
(Alta Frecuencia)
Fluctuaciones extremas
instantáneas (f > 150 Hz
en modelo).
Riesgo: Cavitación incipiente y
fatiga de alto ciclo.
2.5.
Fundamentos de la Dinámica de Fluidos Computacional
(CFD)
2.5.1.
Ecuaciones de Gobierno para una Simulación a Grandes Escalas
Las Simulaciones a Grandes Escalas (Large Eddy Simulation, LES) resuelve directamente
los grandes vórtices de la turbulencia y modela los más pequeños. Esto se logra aplicando un
filtro espacial G a las ecuaciones de Navier-Stokes (Pope, 2000).
El campo de velocidad se descompone en una parte resuelta (⟨Uj⟩, no debe ser confundida
con la velocidad media) y una parte sub-malla (u′):
∂⟨Uj⟩
∂t
+ ∂⟨Ui⟩⟨Uj⟩
∂xi
= −∂⟨p⟩
∂xj
+ ν ∂2 ⟨Uj⟩
∂xi∂xi
−∂τ sgs
ij
∂xi
(2.15)


=== PÁG 28 del PDF ===
16
Siendo τ sgs
ij
el tensor de esfuerzos de subgrilla (anisotrópico) que debe ser modelado, ⟨p⟩es
la presión filtrada modificada. Estas son las definiciones fundamentales en términos cinemáticos
(estándar de OpenFOAM):
τ R
ij = ⟨UiUj⟩−⟨Ui⟩⟨Uj⟩
(2.16)
kr = 1
2τ R
ii
(2.17)
τ sgs
ij
= τ R
ij −2
3krδij
(2.18)
⟨p⟩= ⟨p⟩+ 2
3kr
(2.19)
Así, τ R
ij es el tensor de esfuerzos residuales exacto, kr es la energía cinética residual (escala de
subgrilla), δij es la delta de Kronecker y ⟨p⟩es la presión estática cinemática filtrada por G.
La presión filtrada modificada ⟨p⟩(la cual absorbe la parte isotrópica del tensor residual)
puede ser despejada al aplicar el operador divergencia a las ecuaciones de Navier-Stokes filtradas.
Debido a la condición de incompresibilidad (∇· ⟨U⟩= 0), esto conduce a la siguiente ecuación
de Poisson para el campo de presiones (Pope, 2000):
∇2 ⟨p⟩= −∂2(⟨Ui⟩⟨Uj⟩)
∂xi∂xj
−∂2τ sgs
ij
∂xi∂xj
(2.20)
2.5.1.1.
Definición del Filtro Espacial (∆)
El ancho del filtro ∆determina el tamaño a partir del cual se modela la turbulencia. En
volúmenes finitos, la definición base es la raíz cúbica del volumen de la celda (OpenCFD Ltd,
2023; Breuer et al., 2003):
∆= (Vcelda)1/3
(2.21)
En mallas con transiciones abruptas, se utilizan filtros suavizados (smooth delta) para evitar
inestabilidades numéricas.
2.5.2.
Modelo de Subgrilla de una Ecuación (kEqn)
Para el cierre de las ecuaciones de Navier-Stokes filtradas, es necesario modelar el tensor de
esfuerzos anisotrópico (τ sgs
ij ). En esta investigación se utilizó el modelo de viscosidad de remo-


=== PÁG 29 del PDF ===
17
lino de una ecuación (One Equation Eddy Viscosity Model), fundamentado en la teoría estadística
de Yoshizawa (1986).
A diferencia de los modelos algebraicos simples (como Smagorinsky), que asumen un equi-
librio local instantáneo entre la producción y disipación de turbulencia (Pk ≈ϵ) (Smagorinsky,
1963), este modelo resuelve una ecuación de transporte diferencial para la energía cinética tur-
bulenta residual (kr), definida previamente.
La inclusión de esta ecuación de transporte permite modelar la historia de la energía turbu-
lenta, capturando los efectos de transporte convectivo y difusión de la turbulencia aguas abajo
(Pope, 2000). Esto resulta crítico para flujos de no-equilibrio con fuerte separación, como el
despegue del chorro en el salto de esquí (Ferziger et al., 2019). La ecuación gobernante es:
∂kr
∂t + ∇· (⟨U⟩kr) −∇· [(ν + νsgs)∇kr] = Pk −ϵ
(2.22)
El lado izquierdo representa la tasa de cambio temporal y el transporte advectivo por el flujo
medio. En el lado derecho, los términos fuente se definen como:
Producción (Pk): Generación de energía turbulenta debido a la cizalladura del flujo re-
suelto. Se modela como Pk = 2νsgs| ⟨S⟩|2, donde | ⟨S⟩| es la magnitud del tensor de tasa
de deformación.
Disipación (ϵ): Tasa de destrucción de la energía turbulenta por viscosidad molecular,
modelada como:
ϵ = Cϵk3/2
r
∆
(2.23)
Finalmente, la viscosidad de subgrilla (νsgs) ya no se obtiene solo del gradiente de velocidad
local, sino que depende directamente de la energía cinética transportada (kr) y la escala del filtro
(∆), según la relación dimensional de Yoshizawa (1986):
νsgs = Ck∆
p
kr
(2.24)
Donde las constantes del modelo calibradas para flujo incompresible son típicamente Ck =
0,094 y Cϵ = 1,048.


=== PÁG 30 del PDF ===
18
2.5.3.
Física de la Capa Límite y Modelación de Pared
El escurrimiento sobre las fronteras sólidas de los SECDE desarrolla una capa límite turbu-
lenta donde los efectos de la viscosidad molecular y de la inercia varían en función de la distancia
normal a la pared (y) (Pope, 2000). Para universalizar el análisis del perfil de velocidades y los
esfuerzos de corte en esta región, se utiliza la distancia adimensional de pared (y+), definida
según la expresión:
y+ = uτy
ν
=
q
τw
ρ y
ν
(2.25)
Donde uτ representa la velocidad de fricción (o velocidad de corte), τw es el esfuerzo de
corte en la pared, ρ la densidad del fluido, y es la distancia normal a la superficie sólida y ν es
la viscosidad cinemática del fluido (Pope, 2000; Ferziger et al., 2019). De acuerdo con la teoría
clásica de la turbulencia (Pope, 2000), la estructura interna de la capa límite se subdivide en tres
regiones fundamentales con comportamientos mecánicos diferenciados:
1. Subcapa viscosa (y+ < 5): Región adyacente a la pared dominada por la viscosidad mo-
lecular, donde el perfil de velocidades adimensionales (u+) presenta un comportamiento
lineal (u+ = y+). La resolución directa de esta capa en modelos numéricos de alta energía
exige un refinamiento de malla extremo, denominado Wall-Resolved LES (WRLES).
2. Capa de transición o buffer layer (5 < y+ < 30): Zona de transición compleja donde
los esfuerzos viscosos y los esfuerzos de Reynolds son de magnitudes comparables. Al no
existir una ley analítica simple que describa esta región, su modelación introduce incer-
tidumbres numéricas significativas si el primer nodo de cálculo se sitúa dentro de estos
límites.
3. Región logarítmica (y+ > 30): Zona donde la inercia turbulenta es la fuerza dominante
y el perfil de velocidades sigue la Ley de la Pared:
u+ = 1
κ ln(y+) + B
(2.26)
Donde κ es la constante de von Kármán (≈0, 41) y B es una constante de integración
asociada a la rugosidad de la superficie (≈5, 2 para paredes lisas).


=== PÁG 31 del PDF ===
19
En la modelación numérica de flujos con altos números de Reynolds, la estrategia WMLES
(Wall-Modeled LES) emplea Funciones de Pared (Wall Functions) para obviar la resolución
de la subcapa viscosa. Estas formulaciones imponen analíticamente las condiciones de borde
en el primer nodo de la malla basándose en la Ley de la Pared, asumiendo que dicho nodo se
encuentra dentro de la región logarítmica (y+ > 30). Este enfoque permite capturar la física de
la macroturbulencia y las fluctuaciones de presión en el radier con una eficiencia computacional
compatible con las dimensiones de las estructuras de ingeniería hidráulica (Ferziger et al., 2019).


=== PÁG 32 del PDF ===
20
Capítulo 3
Equipamiento y Facilidades
Experimentales
En la ingeniería hidráulica experimental, la precisión de los resultados depende críticamente
de la integridad de la infraestructura de soporte y la precisión de la instrumentación (Ettema,
2000; Heller et al., 2005). Este capítulo describe el montaje físico del modelo del Embalse An-
coa, los sistemas de alimentación, la arquitectura del Sistema Comercial de Referencia (SCR) y
del Sistema de Arquitectura Abierta (SAA), junto con los protocolos lógicos para la captura y
procesamiento de datos.
3.1.
El Modelo Físico del Embalse Ancoa
La experimentación se realiza en las instalaciones del Instituto Nacional de Hidráulica (INH).
El modelo físico representa el evacuador de crecidas del Embalse Ancoa, construido a una escala
geométrica de λL = 40 (INH, 2015b). El diseño hidrodinámico se rige por la ley de similitud de
Froude, garantizando la representatividad proporcional de las fuerzas inerciales y gravitatorias
que dominan los flujos con superficie libre (Ettema, 2000). Esta escala fue seleccionada analítica-
mente para asegurar un Número de Reynolds suficientemente alto en el modelo, lo cual mantiene
un régimen plenamente turbulento y minimiza los efectos de escala viscosos y de tensión super-
ficial que podrían alterar la cinemática del flujo (INH, 2015b; Ettema, 2000).


=== PÁG 33 del PDF ===
21
Figura 3.1: Vista general del modelo físico del Embalse Ancoa (Escala 1:40) en las instalaciones
del INH. Render (arriba) y foto tomada durante un ensayo (abajo). Fuente: INH (2016b).
Materialidad: La estructura fue fabricada en acrílico transparente, permitiendo la observa-
ción directa de fenómenos como la aireación y la separación de la capa límite. Para cumplir
con la rugosidad de Manning del prototipo en el modelo físico, la relación teórica de Man-
ning impone un factor de escala nr = λ1/6
L
≈1, 85. Al emplear acrílico (nm ≈0, 009) para
representar el revestimiento de hormigón del prototipo (np ≈0, 018), el modelo alcanza
una relación efectiva de 2, 0. Esta desviación marginal respecto al escalamiento teórico
resulta metrológicamente aceptable, ya que en el régimen supercrítico de la estructura la


=== PÁG 34 del PDF ===
22
hidrodinámica está gobernada de forma predominante por las fuerzas inerciales y las pér-
didas singulares, relegando la fricción de pared a un plano secundario (INH, 2015b).
Geometría y Componentes del Sistema: El modelo físico reproduce la configuración
geométrica del evacuador de crecidas del Embalse Ancoa (INH, 2015a):
• Vertedero Lateral y Canal Colector: Perfil tipo Ogee de 1,13 m que descarga hacia
un canal colector de sección variable.
• Rápido de Descarga: Canal en régimen supercrítico con pendientes del 5,6 % y
25 %, unidas por una transición convexa.
• Salto de Esquí: Deflector curvo con un radio R = 42,5 cm en el modelo físico
(equivalente a 17 m en escala real o prototipo) y un ángulo de lanzamiento final de
5◦(INH, 2015a, 2024).
Figura 3.2: Componentes del modelo físico del Embalse Ancoa. Se observan los distintos tramos
con sus respectivos nombres. El Vertedero y los Dientes de Disipación indican donde físicamente
se encuentran, sin embargo no son visibles en la imagen. Fuente: Modificado de INH (2016b)


=== PÁG 35 del PDF ===
23
Figura 3.3: Imagen de los Dientes de Disipa-
ción. Fuente: Elaboración Propia
Figura 3.4: Imagen del Vertedero. Fuente: Ela-
boración Propia
Figura 3.5: Render del Salto de Esquí. Fuente: Modificado
de INH (2016b)


=== PÁG 36 del PDF ===
24
3.2.
Sistema de Alimentación Hidráulica
Se utilizó el circuito cerrado del laboratorio para garantizar condiciones de borde estables:
1. Impulsión: Sistema de bombeo controlado por válvula de regulación para la generación
de regímenes permanentes.
2. Estanque de aquietamiento: Estanque de aquietamiento con disipadores de energía in-
terno actuando como reservorio previo al modelo físico.
3. Control de Caudal: Medición mediante flujómetros electromagnéticos, asegurando que
las condiciones de borde de la simulación CFD sean replicables.
Figura 3.6: Componentes de alimentación: flujómetro (izq.) y estanque de aquietamiento con
limnímetro integrado (der.). Fuente: Elaboración propia.
3.3.
Sistema Comercial de Referencia (SCR)
Como sistema comercial de referencia se utiliza el ecosistema de instrumentación de HR
Wallingford, diseñado específicamente para la medición de presión en modelos hidráulicos. El
sistema se compone de una matriz de transductores piezorresistivos Keller Serie 25Y (KELLER
AG für Druckmesstechnik, 2024) y una unidad central de procesamiento TOPS (HR Wallingford,
2024).


=== PÁG 37 del PDF ===
25
3.3.1.
Adquisidor de Datos (DAQ)
El SCR utiliza una unidad Transducer Output and Power Supply (TOPS) con capacidad
para 8 canales independientes. Cada canal suministra una alimentación regulada de 24 V DC al
transductor y recibe una señal analógica de salida en el rango de 0 V a 10 V (HR Wallingford,
2024).
La digitalización y transmisión de datos se realiza vía USB 2.0 hacia la estación de trabajo.
El procesamiento se ejecuta mediante TracerDaq Pro, configurado en esta investigación con
una tasa de adquisición variable que alcanza un máximo de 3333 Hz. Este nivel de sobremues-
treo asegura el cumplimiento del criterio de Nyquist incluso para la microturbulencia (escalas
disipativas), erradicando el riesgo de aliasing en la banda de alta frecuencia.
3.3.2.
Transductores Keller Serie 25Y
La captura de presión en el SCR se ejecuta con transductores piezorresistivos Keller Serie
25Y (KELLER AG für Druckmesstechnik, 2024). Sus características reportadas son:
Precisión y Linealidad: Error combinado de linealidad e histéresis inferior al ±0,25 %
del fondo de escala (FS).
Geometría de Medición: Configuración de diafragma enrasado (flush face) de 17 mm de
diámetro, garantizando medición puntual de presión sin distorsiones por cavidades o aire
atrapado.
Respuesta Dinámica: Frecuencia de resonancia natural en aire de 2 kHz, con respuesta
plana en el rango de frecuencias de la macroturbulencia hidráulica.
Referencia de Presión: Tipo Vented Gauge (PR), compensado automáticamente a presión
atmosférica mediante tubo capilar interno en el cable.
Rango Térmico: Compensación activa de temperatura con error de banda de ±0,5 % FS
entre 0 y 50 ◦C.


=== PÁG 38 del PDF ===
26
3.4.
Sistema de Arquitectura Abierta (SAA)
El SAA es una arquitectura híbrida que integra hardware open-source para el DAQ, y sen-
sores comerciales de referencia para la captura de las fluctuaciones de presión.
3.4.1.
Adquisidor de Datos (DAQ) y Flexibilidad Topológica
El núcleo del DAQ del SAA es un microcontrolador Arduino Mega 2560 (INH, 2020). La
placa de expansión (Shield) realiza el acondicionamiento de la señal mediante una etapa de con-
versión corriente-voltaje, mapeando el rango industrial estándar de 4 mA a 20 mA a la ventana
de cuantización del ADC de 10 bits. Su esquema eléctrico y topología de expansión fueron di-
señados por la unidad de ingeniería del Instituto Nacional de Hidráulica (INH), permitiendo la
lectura simultánea e independiente de hasta 12 canales de instrumentación (INH, 2020; INH and
Peña, 2020).
FILE NAME:
BY:
DATE:
PAGE:
DAQ_presion_arduino.pdsprj
2/4/2020
Carolina Peña Bozo
A
B
C
D
E
F
G
H
J
K
A
B
C
D
E
F
G
H
J
K
0
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6
7
8
9
PATH:
1
of
1
REV:
TIME:
DESIGN TITLE:
Plano eléctrico DAQ-PRESIÓN
PG5/OC0B
1
PE0/RXD0/PCINT8/PDI
2
PE1/TXD0/PDO
3
PE2/XCK0/AIN0
4
PE3/OC3A/AIN1
5
PE4/OC3B/INT4
6
PE5/OC3C/INT5
7
PE6/T3/INT6
8
PE7/ICP3/CLKO/INT7
9
PH0/RXD2
12
PH1/TXD2
13
PH2/XCK2
14
PH3/OC4A
15
PH4/OC4B
16
PH5/OC4C
17
PH6/OC2B
18
PB0/SS/PCINT0
19
PB1/SCK/PCINT1
20
PB2/MOSI/PCINT2
21
PB3/MISO/PCINT3
22
PB4/OC2A/PCINT4
23
PB5/OC1A/PCINT5
24
PB6/OC1B/PCINT6
25
PB7/OC0A/OC1C/PCINT7
26
PH7/T4
27
PG3/TOSC2
28
PG4/TOSC1
29
RESET
30
XTAL2
33
XTAL1
34
PL0/ICP4
35
PL1/ICP5
36
PL2/T5
37
PL3/OC5A
38
PL4/OC5B
39
PL5/OC5C
40
PL6
41
PL7
42
PD0/SCL/INT0
43
PD1/SDA/INT1
44
PD2/RXD1/INT2
45
PD3/TXD1/INT3
46
PD4/ICP1
47
PD5/XCK1
48
PD6/T1
49
PD7/T0
50
PG0/WR
51
PG1/RD
52
PC0/A8
53
PC1/A9
54
PC2/A10
55
PC3/A11
56
PC4/A12
57
PC5/A13
58
PC6/A14
59
PC7/A15
60
PJ0/RXD3/PCINT9
63
PJ1/TXD3/PCINT10
64
PJ2/XCK3/PCINT11
65
PJ3/PCINT12
66
PJ4/PCINT13
67
PJ5/PCINT14
68
PJ6/PCINT15
69
PG2/ALE
70
PA7/AD7
71
PA6/AD6
72
PA5/AD5
73
PA4/AD4
74
PA3/AD3
75
PA2/AD2
76
PA1/AD1
77
PA0/AD0
78
PJ7
79
PK7/ADC15/PCINT23
82
PK6/ADC14/PCINT22
83
PK5/ADC13/PCINT21
84
PK4/ADC12/PCINT20
85
PK3/ADC11/PCINT19
86
PK2/ADC10/PCINT18
87
PK1/ADC9/PCINT17
88
PK0/ADC8/PCINT16
89
PF7/ADC7/TDI
90
PF6/ADC6/TDO
91
PF5/ADC5/TMS
92
PF4/ADC4/TCK
93
PF3/ADC3
94
PF2/ADC2
95
PF1/ADC1
96
PF0/ADC0
97
AREF
98
AVCC
100
ARDUINO-MEGA
ATMEGA2560
10.0
VO
1
VCC
3
GND
2
SENSOR 2
GP2D12
12v
S1
S2
S3
S4
S5
S6
S7
S8
S9
S10
S11
S12
ANALOG IN
VOUT
MCI Olimex
+ CH0
-  CH0
+ CH1
-  CH1
+ CH2
-  CH2
+ CH3
-  CH2
0
1
2
3
+
-
S1
SHIELD-ARDUINO
ANALOG IN
VOUT
MCI Olimex
+ CH0
-  CH0
+ CH1
-  CH1
+ CH2
-  CH2
+ CH3
-  CH2
0
1
2
3
+
-
S3
SHIELD-ARDUINO
ANALOG IN
VOUT
MCI Olimex
+ CH0
-  CH0
+ CH1
-  CH1
+ CH2
-  CH2
+ CH3
-  CH2
0
1
2
3
+
-
S2
SHIELD-ARDUINO
S1
S5
10.0
VO
1
VCC
3
GND
2
SENSOR 5
GP2D12
S9
10.0
VO
1
VCC
3
GND
2
SENSOR 9
GP2D12
S10
10.0
VO
1
VCC
3
GND
2
SENSOR 10
GP2D12
S6
10.0
VO
1
VCC
3
GND
2
SENSOR 6
GP2D12
S2
S3
10.0
VO
1
VCC
3
GND
2
SENSOR 3
GP2D12
S7
10.0
VO
1
VCC
3
GND
2
SENSOR 7
GP2D12
S8
10.0
VO
1
VCC
3
GND
2
SENSOR 8
GP2D12
S4
10.0
VO
1
VCC
3
GND
2
SENSOR 4
GP2D12
10.0
VO
1
VCC
3
GND
2
SENSOR 1
GP2D12
D1
LED-GREEN
GABINETE ELECTRÓNICO
Figura 3.7: Diagrama electrónico del DAQ del SAA. La arquitectura permite la gestión centrali-
zada de hasta 12 canales de instrumentación. Fuente: INH (2020)


=== PÁG 39 del PDF ===
27
La estandarización de las entradas mediante lazos de corriente de 4 mA a 20 mA permite
al SAA integrar simultáneamente transductores de presión y sensores ultrasónicos de nivel
(Microsonic ZWS-15/CI/QS) (INH and Peña Bozo, 2024). Esta configuración posibilitó la me-
dición empírica del tirante de la lámina de agua, parámetro cinemático indispensable para el
cálculo del Número de Froude incidente.
Para la alimentación eléctrica del SAA, se utiliza un banco de baterías externas de 12 V DC
(INH and Peña, 2020; INH and Peña Bozo, 2024). Esta configuración aísla el sistema de la red
eléctrica del laboratorio, previniendo la inducción de ruido electromagnético en la digitalización
de la señal.
La transferencia de datos al ordenador se realiza mediante comunicación serial. Para ello,
se utiliza un script programado en Python (librería pyserial) que lee el puerto y almacena las
series temporales directamente en archivos de texto (.txt) (INH and Peña, 2020). Asimismo, la
frecuencia de muestreo efectiva (fs) del equipo se controla ajustando la velocidad de transmisión
(tasa de baudios) en el código principal (INH and Peña, 2020).
3.4.2.
Transductores Keller Serie 41X
La medición se realizó con sensores capacitivos equipados con Procesamiento Digital Inte-
grado (DSP) para su compensación térmica y linealización (KELLER Druckmesstechnik AG,
2023). La transmisión de los datos opera mediante un lazo de corriente de 4-20 mA, un estándar
industrial que asegura una alta inmunidad frente al ruido electromagnético del entorno experi-
mental (Figliola and Beasley, 2019; KELLER Druckmesstechnik AG, 2023).
Tecnología de Medición: La captura de las presiones fluctuantes se ejecuta mediante trans-
ductores de tecnología capacitiva (KELLER Druckmesstechnik AG, 2023). Poseen un ran-
go nominal de 0,1 bar (100 mbar ≈101,97 cm c a) y un error máximo de ±0,2 % full-scale.
Procesamiento Digital Integrado (DSP): A diferencia de los sensores analógicos de ins-
trumentación clásica, esta serie procesa la señal mediante un microprocesador interno. Este
componente aplica algoritmos de compensación matemática polinomial (P(S, T)) para co-
rregir desviaciones de linealidad y mitigar la deriva térmica antes de emitir la lectura de
salida al lazo de corriente (KELLER Druckmesstechnik AG, 2023).


=== PÁG 40 del PDF ===
28
Transmisión por Lazo de Corriente: El equipo está configurado con una salida analógica
de 2 hilos (4 mA a 20 mA). Para posibilitar su digitalización unificada, la placa Shield del
DAQ del SAA ejecuta la conversión de esta señal de corriente a voltaje de manera previa
a su ingreso a los pines analógicos del microcontrolador (INH, 2020).
Figura 3.8: Transductor capacitivo Keller Serie 41X. Se aprecian en su etiqueta las especifica-
ciones de rango dinámico (0,1 bar) y la designación de pines para la salida analógica (4 mA a
20 mA) y digital (RS485). Fuente: Elaboración propia.


=== PÁG 41 del PDF ===
29
Figura 3.9: Montaje experimental paralelo. Arriba: Unidad TOPS del Sistema Comercial de Refe-
rencia (SCR). Abajo: Sistema de Arquitectura Abierta (SAA) conformado por el Arduino Mega
y la placa de expansión de canales analógicos. Fuente: Elaboración propia.


=== PÁG 42 del PDF ===
30
Capítulo 4
Metodología de la implementación del
Modelo Numérico (CFD)
En este capítulo se detalla la implementación del modelo numérico utilizado para simular el
flujo en el modelo físico del Embalse Ancoa. A diferencia de la exposición teórica del Capítulo 2,
esta sección se centra en las estrategias y definición de parámetros de discretización, configura-
ción del solver y los criterios de estabilidad adoptados para asegurar la convergencia del modelo
WMLES.
La metodología se estructura en un flujo de trabajo secuencial que abarca desde la definición
del dominio computacional hasta el post-procesamiento de los campos obtenidos.
4.1.
Selección del Solver y Esquemas Numéricos
Para la resolución del flujo bifásico (agua-aire) con superficie libre, se seleccionó el solver
interFoam de la suite de OpenFOAM. La idoneidad de este solver ha sido ratificada mediante
evaluaciones exhaustivas de su desempeño numérico. Deshpande et al. (2012) validaron la im-
plementación del método de Volumen de Fluido (VOF) y la técnica de compresión de interfaz
(MULES), demostrando su capacidad para conservar la masa y mantener interfaces nítidas en
flujos dominados por la tensión superficial y la gravedad.
En el contexto de la ingeniería hidráulica computacional, Bayon et al. (2016) compararon sis-
temáticamente el desempeño del solver interFoam (OpenFOAM) frente al software comercial


=== PÁG 43 del PDF ===
31
FLOW-3D en la modelación de un resalto hidráulico estacionario, empleando en ambas plata-
formas el enfoque de las ecuaciones de Navier Stokes Promediadas por Reynolds (Reynolds-
Averaged Navier-Stokes, RANS) con el modelo de turbulencia k −ϵ y el método de seguimiento
de interfaz VOF. Sus resultados confirmaron, mediante métricas de error, que la herramienta de
código abierto no solo alcanza resultados equivalentes al software licenciado comercialmente,
sino que presenta superioridad predictiva en variables cinemáticas clave. Específicamente, Open-
FOAM demostró una mayor precisión en la reconstrucción de los perfiles de velocidad vertical
(97, 6 % frente al 90, 3 % de FLOW-3D) y un mejor ajuste en la posición de la superficie libre al
ser contrastada con datos experimentales (R2 = 0, 982 para OpenFOAM frente a R2 = 0, 966 pa-
ra FLOW-3D). Estos antecedentes metrológicos justifican con robustez estadística la viabilidad
técnica de utilizar el software open-source para la caracterización hidrodinámica.
4.1.1.
Configuración de Esquemas de Discretización
Los esquemas numéricos del modelo se definen en el diccionario fvSchemes de OpenFOAM.
Su parametrización prescinde de un análisis de sensibilidad numérico paramétrico; en su lugar,
se adopta la matriz de discretización estructurada por el INH para su modelo LES del prototipo
del Embalse Ancoa (INH, 2016a; Negrete et al., 2016).
Dado que los esquemas de discretización son operadores matemáticos que actúan de manera
adimensional sobre las ecuaciones de gobierno, su implementación en el dominio computacio-
nal a escala 1:40 conserva su viabilidad analítica. La estabilidad de esta matriz está regida por
parámetros locales (Ferziger et al., 2019). Al adaptar la malla al dominio reducido, la solidez
algorítmica se preserva mediante el cumplimiento del Número de Courant (Co < 1) para la in-
tegración temporal (Ferziger et al., 2019). Esto garantiza la convergencia del solver interFoam
y la preservación nítida de la interfaz mediante el método VOF (Deshpande et al., 2012). Simul-
táneamente, la formulación del filtro espacial LES se autoajusta de forma intrínseca a la escala
geométrica reducida, dado que su longitud (∆) depende de la raíz cúbica del volumen local de
cada celda computacional (Breuer et al., 2003).
Los esquemas utilizados se describen a continuación:
Términos Temporales (∂/∂t): Se aplica el esquema CrankNicolson 0.7. En la arquitec-


=== PÁG 44 del PDF ===
32
tura de OpenFOAM, el coeficiente de 0,7 actúa como un factor que introduce una fracción
de integración implícita (Euler) al esquema de segundo orden puro (Ferziger et al., 2019).
Esta parametrización estabiliza el algoritmo VOF ante la severa deformación de la interfaz
en el salto de esquí (Deshpande et al., 2012), conservando simultáneamente la energía de
la macroturbulencia resuelta sin una atenuación excesiva.
Gradientes (∇): Se emplea el esquema cellLimited Gauss linear 1 para las varia-
bles de flujo (U, p, k, ω). El limitador de celda preserva la precisión de segundo orden
en el cálculo espacial, previniendo la generación de sobreimpulsos numéricos o valores
escalares no físicos en las zonas de gradiente pronunciado.
Términos Convectivos (∇· (ϕU)):
• Momento Lineal (∇· (ρUU)): Para el término advectivo div(rhoPhi,U), se im-
plementa el esquema LUST (Linear Upwind Stabilized Transport) (OpenCFD Ltd,
2023). Esta formulación híbrida pondera un 75 % de diferencias centrales (linear)
para minimizar la disipación numérica inducida por el error de truncamiento y con-
servar la energía cinética de la macroturbulencia resuelta (Breuer et al., 2003), junto
a un 25 % de esquema descentrado aguas arriba (linearUpwind) para suprimir osci-
laciones espurias locales y garantizar la estabilidad algorítmica de la matriz (Ferziger
et al., 2019).
• Fracción de Fase (α): Se utiliza Gauss vanLeer. Su propiedad TVD (Total Varia-
tion Diminishing) resulta matemáticamente imperativa para mantener el acotamiento
de la variable escalar entre 0 y 1 (Deshpande et al., 2012).
• Compresión de Interfaz: El esquema interfaceCompression activa el término
de velocidad de compresión artificial convectiva ∇· (ucα[1 −α]) característico del
algoritmo MULES. La inclusión de este término resulta matemáticamente imperativa
para contrarrestar la difusión numérica intrínseca del método VOF, manteniendo así
la nitidez de la superficie libre (Rusche, 2002; Deshpande et al., 2012).
Términos Laplacianos y Derivadas Normales: Se configura el esquema Gauss linear
limited 0.333. En regiones de alta curvatura geométrica, la adaptación de la malla indu-


=== PÁG 45 del PDF ===
33
ce una desviación no ortogonal en las celdas hexaédricas. Para abordar esta deformación,
la contribución ortogonal del gradiente se evalúa implícitamente, mientras que el compo-
nente no ortogonal se incorpora como una corrección diferida explícita (Ferziger et al.,
2019). La aplicación del factor limitador (0,333) restringe la magnitud máxima de esta
corrección, lo cual resulta fundamental para preservar la dominancia diagonal de la matriz
y garantizar la estabilidad del sistema (Rusche, 2002; Ferziger et al., 2019).
4.2.
Pre-procesamiento de la Geometría y Dominio Compu-
tacional
La geometría base del modelo físico del Embalse Ancoa (escala 1 : 40) se obtuvo a partir de
un levantamiento digital en formato STL (Stereolithography). Sin embargo, la geometría original
presentaba características constructivas del modelo físico (como el espesor de las paredes de
acrílico) inadecuadas para la definición del volumen de control fluido.
Fue necesario implementar un proceso de limpieza y reparación topológica utilizando el
software de código abierto Blender.
4.2.1.
Procedimiento de Reparación Topológica
El archivo STL fue sometido a las siguientes operaciones topológicas para garantizar su
compatibilidad con los algoritmos de mallado de OpenFOAM:
1. Extracción del Volumen Fluido: Se eliminaron las caras correspondientes al espesor
estructural del material sólido, definiendo y aislando únicamente las superficies ”moja-
das”que interactúan físicamente con el fluido (o el aire) del modelo.
2. Corrección de Normales: Se reorientaron los vectores normales de todas las caras super-
ficiales para asegurar que apunten consistentemente hacia el interior del dominio compu-
tacional.
3. Eliminación de Defectos (3D Print Toolbox): Se empleó el complemento 3D Print
Toolbox, herramienta de diagnóstico de Blender, el cual provee parámetros topológicos


=== PÁG 46 del PDF ===
34
críticos para evaluar la viabilidad del dominio computacional. Específicamente, se inter-
vinieron las siguientes anomalías:
Zero Faces: Detección y eliminación de caras degeneradas o con área nula que co-
rrompen el cálculo de flujos en las fronteras.
Zero Edges: Identificación de aristas de longitud cero, subsanadas mediante la fusión
de vértices duplicados o coincidentes.
Non-Manifold Geometry: Corrección de inconsistencias topológicas, tales como aris-
tas compartidas por más de dos caras o volúmenes unidos por un único vértice. Este
paso es crítico para asegurar un dominio volumétrico estanco y hermético, condición
indispensable para que el mallador identifique unívocamente las regiones interior y
exterior.
4. Discrepancia Geométrica en el Límite de Salida: El dominio computacional modelado
incluyó una sección plana de 21 cm inmediatamente aguas abajo del labio del salto de es-
quí, la cual representa una discrepancia geométrica respecto al modelo físico construido
en acrílico. No obstante, desde la perspectiva de la mecánica de fluidos, esta diferencia
estructural carece de impacto sobre la zona de estudio. Dado que el escurrimiento sobre el
deflector opera en un régimen supercrítico (Fr ≫1), la velocidad del flujo es superior a
la celeridad de la onda, lo que impide físicamente que cualquier perturbación geométrica o
hidráulica se propague hacia aguas arriba (Novak et al., 2007; Chanson, 2004). En conse-
cuencia, esta extensión no altera en absoluto el campo de presiones ni la cinemática sobre
la curvatura del salto de esquí, manteniendo intacta la validez de los resultados extraídos
en los puntos de interés.
Este proceso, aunque laborioso, resultó indispensable para evitar la divergencia del algoritmo
durante la generación de la malla base para la simulación.
4.2.2.
Definición de Fronteras (Patches)
En el entorno de Blender, se definieron cinco regiones de frontera (patches) para la asigna-
ción de condiciones de borde, ilustradas en la Figura 4.1:


=== PÁG 47 del PDF ===
35
Inlet: Sección aguas arriba para el ingreso del flujo.
Outlet: Sección de descarga libre aguas abajo. Se sitúa al final de la extensión longitudinal
de 21 cm.
Atmosfera: Frontera superior abierta a la atmósfera, permitiendo la entrada y salida de
aire.
Aliviadero: Superficies sólidas que representan la estructura (vertedero, rápido y salto de
esquí), configuradas con condición de no deslizamiento.
Dientes: Aunque tiene todos los atributos de Aliviadero, se define aparte para tener un
mejor mallado en esta zona que contiene distinciones geométricas.
Figura 4.1: Definición de las fronteras (patches) en el dominio computacional utilizando Blender.
(A) vista en perspectiva superior. (B) vista inferior. Fuente: Elaboración propia.


=== PÁG 48 del PDF ===
36
4.3.
Estrategia de Discretización Espacial (Malla)
El procedimiento de generación de malla se estructuró a partir de un dominio base de discreti-
zación hexaédrica (blockMesh), sobre el cual el algoritmo snappyHexMesh esculpió la compleja
topología del modelo físico como modelo computacional. La configuración final estabilizada del
diccionario snappyHexMeshDict se fundamentó en los siguientes criterios físicos y topológicos:
Refinamiento Espacial y Capa Límite: Para capturar los gradientes convectivos de la
macroturbulencia, el subdiccionario refinementRegions impuso un refinamiento volu-
métrico (nivel 4) en las zonas críticas (Vertedero, Dientes y Aireador, las cuales pre-
sentan discontinuidades geométricas). Simultáneamente, para capturar la cizalladura nor-
mal a la pared, el bloque addLayersControls forzó la extrusión de 5 capas prismáticas
(nSurfaceLayers 5) con un ratio de expansión de 1,3 sobre la superficie del aliviadero.
Esta arquitectura de malla es una exigencia inherente de la modelación LES para resolver
adecuadamente las estructuras cercanas a la pared interactuando con las Wall Functions
(Breuer et al., 2003).
Adaptación y Relajación Iterativa (Calidad de Malla): La adaptación forzada de celdas
hexaédricas a la curvatura del vertedero Ogee representó el mayor desafío topológico. Para
lograr que la malla se ciñera a la geometría, se debió incrementar el esfuerzo algorítmico
en el subdiccionario snapControls (nSolveIter 250 y tolerance 2.0).
Gestión de la Deformación (Skewness): Para evitar el colapso del solver por celdas co-
rruptas durante el snapping, fue imperativo relajar iterativamente los umbrales en mesh-
QualityControls. Se admitió una no-ortogonalidad máxima (maxNonOrtho) de 65◦y
una deformación interna acotada (maxInternal Skewness). Desde la perspectiva numé-
rica, esta relajación geométrica es una concesión obligada en mallas no estructuradas com-
plejas, asumiendo que los errores de truncamiento derivados serán controlados por los
esquemas limitadores configurados en fvSchemes (Ferziger et al., 2019).
El proceso de convergencia topológica bajo estos parámetros resultó en una malla no estruc-
turada (discretización espacial de conectividad irregular adaptada a geometrías complejas) de
aproximadamente 5.2 millones de celdas. Operando bajo la restricción del criterio de Courant


=== PÁG 49 del PDF ===
37
(Co < 1), esta arquitectura permitió una tasa de cálculo de ≈10 s de tiempo simulado por cada
24 horas de ejecución, paralelizando el esfuerzo en 120 núcleos de procesamiento.


=== PÁG 50 del PDF ===
38
Figura 4.2: Cortes transversales y detalles de la malla no estructurada generada mediante
snappyHexMesh con una resolución de 5.2 millones de celdas.


=== PÁG 51 del PDF ===
39
4.4.
Modelación de la Turbulencia y Condiciones de Borde
4.4.1.
Modelo de Turbulencia y Tratamiento de Pared
Se activó el modelo de turbulencia de subgrilla de una ecuación (kEqn), descrito teóricamen-
te en el Capítulo 2. Este modelo resuelve el transporte de la energía cinética turbulenta (ksgs), lo
cual es crítico para capturar la advección de turbulencia desde el rápido hacia el salto de esquí
(Yoshizawa, 1986).
4.4.1.1.
Definición y Suavizado del Filtro Espacial (∆)
La escala de longitud del filtro (∆) determina el límite entre los remolinos resueltos y los
modelados. Si bien la definición base adoptada corresponde a la raíz cúbica del volumen de la
celda (∆0 =
3√Vcelda) (Breuer et al., 2003), su implementación directa genera inestabilidades
numéricas en mallas no estructuradas con transiciones de refinamiento abruptas (Pope, 2000;
Ferziger et al., 2019).
Para mitigar este efecto, se configuró el esquema delta smooth en el diccionario turbu-
lenceProperties (que define la estrategia de turbulencia a utilizar). Este método aplica un
algoritmo de suavizado espacial al campo ∆, regido por el coeficiente maxDeltaRatio configu-
rado en 1.1.
∆eff = f(∆0, ∆vecinos)
s.t.
∆i
∆j
≤1,1
(4.1)
Esta configuración restringe la variación del ancho del filtro entre celdas adyacentes a un
máximo del 10 %, amortiguando los saltos artificiales en la viscosidad de subgrilla (νsgs) en las
interfaces de refinamiento de la malla, lo cual resulta crítico para mantener la estabilidad del
solver interFoam en la zona de la superficie libre.
4.4.1.2.
Tratamiento de Pared WMLES y Verificación del y+
Para el tratamiento de pared, dada la estrategia WMLES (Wall-Modeled LES), se aplica-
ron funciones de pared (nutkWallFunction) en las fronteras sólidas. Esto permite modelar la


=== PÁG 52 del PDF ===
40
subcapa viscosa basándose en la ley logarítmica, evitando el costo computacional de resolverla
explícitamente (Pope, 2000; Ferziger et al., 2019).
La validez de esta estrategia se verificó a posteriori mediante el análisis del parámetro adi-
mensional y+. Para la malla implementada de 5.2M celdas, los valores promedio se mantuvieron
mayoritariamente en el entorno de la región logarítmica (y+ ≈30). Este resultado confirma la
pertinencia de utilizar nutkWallFunction, garantizando que el cálculo de los gradientes de ve-
locidad y esfuerzos de corte en la pared sea físicamente coherente con las asunciones teóricas de
la ley de pared estándar (Sección 2.5.3).
4.4.2.
Definición de Campos y Fronteras
Las condiciones de borde para las variables hidrodinámicas (U, p_rgh, α) y turbulentas (k, νt,
νsgs) se resumen en la Tabla 4.1. Se inició la simulación con el caudal más bajo (≈14,82 lt/s)
para asegurar la estabilidad inicial del campo de velocidades.
Tabla 4.1: Resumen de las condiciones de borde aplicadas en OpenFOAM. Fuente: Elaboración
propia.
Variable
Inlet
Outlet
Atmosfera
Dientes
Aliviadero (Wall)
U
flowRateInletVelocity
inletOutlet
pressureInletOutletVelocity
noSlip
noSlip
p_rgh
fixedFluxPressure
zeroGradient
TotalPressure
fixedFluxPressure
fixedFluxPressure
αwater
fixedValue
zeroGradient
inletOutlet
zeroGradient
zeroGradient
k
fixedValue
inletOutlet
inletOutlet
kqRWallFunction
kqRWallFunction
νt
calculated
calculated
calculated
nutURoughWallFunction
nutURoughWallFunction
νsgs
zeroGradient
zeroGradient
zeroGradient
nutkWallFunction
nutkWallFunction
Cada condición de borde se define de la siguiente manera:
flowRateInletVelocity: Condición de borde que prescribe un perfil de velocidad en la
entrada basándose en un caudal volumétrico escalar (Q) definido por el usuario, ajustando
la velocidad normal a la superficie para cumplir con la continuidad.
inletOutlet: Condición de borde híbrida que previene inestabilidades numéricas en fron-
teras abiertas. Funciona como zeroGradient (flujo libre) cuando el fluido sale del domi-
nio, y cambia a fixedValue (generalmente cero o un valor de referencia) si se detecta
flujo reverso (entrada de fluido) para evitar la entrada de perturbaciones no físicas.


=== PÁG 53 del PDF ===
41
pressureInletOutletVelocity: Condición utilizada comúnmente en parches atmosfé-
ricos (“Opening”). Calcula la velocidad basándose en el gradiente de presión local; si hay
flujo saliente, aplica gradiente cero, y si hay flujo entrante, calcula la velocidad normal a
partir de la presión interna.
noSlip: Condición de adherencia física (“no deslizamiento”). Fija la velocidad del fluido
en la pared a cero (U = 0), representando la fricción viscosa real en superficies sólidas
(dientes y aliviadero).
fixedFluxPressure: Condición esencial para la presión piezométrica (prgh = p −ρgz)
en simulaciones con gravedad (como interFoam). Ajusta el gradiente de presión en la
pared para asegurar que el flujo másico sea consistente con la condición de velocidad,
considerando explícitamente los efectos de la gravedad (fuerzas de cuerpo) para evitar
velocidades parásitas en las paredes.
ZeroGradient: Condición de tipo Neumann que establece que la derivada normal de la
variable en la frontera es cero ( ∂ϕ
∂n = 0). Indica que el valor de la variable se extrapola
desde el interior del dominio y no varía perpendicularmente al parche.
TotalPressure: Fija la presión total (p0 = p + 0,5ρ|U|2) en la frontera. Cuando la ve-
locidad cambia, la presión estática (p) se ajusta dinámicamente. Es ideal para fronteras
atmosféricas donde se busca simular una condición de “atmósfera en reposo” o presión
ambiente constante.
FixedValue: Condición de tipo Dirichlet que impone un valor constante y fijo en la fron-
tera (ej. valor de αwater = 1 en la entrada para indicar que entra solo agua).
kqRWallFunction: Función de pared para la energía cinética turbulenta (k). Proporciona
una condición de borde para k en paredes rugosas o lisas, asumiendo un equilibrio entre
la producción y la disipación turbulenta en la capa logarítmica.
nutURoughWallFunction: Función de pared para la viscosidad turbulenta (νt) que incor-
pora el efecto de la rugosidad superficial. Calcula νt basándose en la velocidad, la distancia


=== PÁG 54 del PDF ===
42
a la pared y la altura de rugosidad equivalente (ks o Cs), fundamental para simular estruc-
turas de hormigón.
nutkWallFunction: Función de pared cinemática estándar que asume que el primer nodo
computacional se encuentra en la región logarítmica (y+ > 30). Utilizada aquí para el
cálculo de la viscosidad turbulenta y de sub-malla en las superficies sólidas del modelo.
Calculated: Indica que la variable en la frontera no se fija directamente, sino que se
deriva o calcula a partir de otros campos o variables internas en cada paso de tiempo
(común para νt y νsgs que dependen de k y U).
4.5.
Control de la Simulación y Post-proceso
Debido al gran volumen de datos generado por una simulación LES, fue inviable almacenar
todos los pasos de tiempo. Se implementó una estrategia de post-procesamiento en tiempo de
ejecución (Run-time Post-processing).
4.5.1.
Control de Extracción de Datos y Funciones de Monitoreo
La gestión de los datos resultantes de la simulación se configuró a través del diccionario
controlDict, implementando una estrategia de extracción dividida en dos niveles:
1. Muestreo Espaciotemporal de Campos Completos (writeInterval): Para el análi-
sis hidrodinámico global y la prospección topológica, se configuró la escritura de los campos
tridimensionales completos (presión, velocidad y fracción de volumen) a intervalos de 0,1 s de
tiempo simulado. A partir de estos estados guardados, se extrajeron las series temporales en los
nodos coincidentes con la ubicación exacta de los sensores en el modelo físico. Esta resolución
temporal de muestreo (10 Hz) resulta óptima y suficiente para mapear la envolvente de presio-
nes medias y localizar el punto de máximo impacto (Xpm), evitando la saturación extrema del
almacenamiento que implicaría guardar el volumen 3D a alta frecuencia.
2. Funciones de Monitoreo (functionObjects): Para extraer información escalar crítica
y de validación de forma continua durante la ejecución del solver, sin necesidad de guardar el
volumen de celdas completo en cada paso de tiempo, se implementaron las siguientes rutinas:


=== PÁG 55 del PDF ===
43
Muestreo de la Subcapa (yPlus): Monitoreo continuo de los valores de y+ en las fron-
teras sólidas para validar empíricamente la viabilidad de la estrategia WMLES a lo largo
de todo el dominio temporal.
Balance de Masa (surfaceFieldValue): Integración matemática de los flujos másicos
en los parches de entrada (Inlet) y salida (Outlet) para verificar la conservación estricta de
la masa y la convergencia global de la simulación.
4.5.2.
Criterio de Convergencia y Estado Estacionario
La simulación se inicializó con un bloque de agua pre-cargado en el estanque para acelerar el
proceso. Se ejecutó el modelo transitorio durante 30 s de tiempo físico hasta alcanzar el equilibrio
dinámico, momento en el cual el caudal de salida se igualó de forma sostenida al de entrada.
Una vez alcanzado el régimen cuasi-estacionario, se extendió la simulación por 10 segundos
adicionales exclusivamente para la recolección de estadísticas de turbulencia. Durante esta ven-
tana temporal, el muestreo de alta frecuencia permitió consolidar los valores medios (RMS) y la
distribución del campo de presiones (p_rgh) para su posterior análisis topológico y comparación
con la literatura y la instrumentación experimental.

=== PÁG 56 del PDF ===
44
Capítulo 5
Metodología Experimental
La ejecución de los ensayos en el modelo físico requiere protocolos rigurosos para garantizar
la repetibilidad de los resultados. Este capítulo detalla el diseño experimental, los procedimientos
de caracterización metrológica, la optimización del sistema de adquisición y la verificación de
las condiciones de contorno hidráulicas.
5.1.
Configuración de la Interfaz Mecánica de Medición
Para la adquisición de datos de presión en el fondo del salto de esquí del modelo físico (Em-
balse Ancoa), se ejecutaron perforaciones perpendiculares al escurrimiento. Estas conformaron
una alineación longitudinal equiespaciada, cuya ubicación espacial fue determinada por el punto
de máxima fluctuación de presión determinada por el modelo matemático (ver Capítulo 6), con-
figurando tomas de presión estática directamente sobre el fondo de acrílico (Figliola and Beas-
ley, 2019). Estas tomas se conectaron a mangueras de silicona de grado médico (ϕext = 5 mm,
ϕint = 3 mm) para trasladar la señal hasta el diafragma de los sensores.
5.1.1.
Optimización de la Fijación y Estanqueidad
Para asegurar la fijación y estanqueidad de las tomas de presión, se probaron distintos espe-
sores de acrílico (4 mm y 8 mm) y diámetros de perforación (4 mm, 5 mm y 6 mm), utilizando
adhesivo de poliuretano (SikaFlex 11FC) como sellante. Los resultados determinaron que la con-


=== PÁG 57 del PDF ===
45
figuración óptima consiste en:
1. Espesor del acrílico: Las placas de 8 mm entregan mayor superficie de contacto, mejo-
rando la estabilidad de la manguera ante la manipulación.
2. Diámetro de perforación: Orificios de 4 mm para generar un ajuste por interferencia con
la manguera de 5 mm.
3. Mecanismo de sellado: Uso de SikaFlex para asegurar la fijación ante vibraciones y evitar
la intrusión de aire, requisito crítico para no alterar la compresibilidad de la columna de
agua (H. Tijdeman, 1965).
5.1.2.
Diseño de Acoples y Conexión a Mangueras
La conexión de los sensores a las mangueras de silicona requirió el uso de adaptadores para
unificar los distintos tipos de roscas y asegurar la estanqueidad del sistema. Para resolver esto,
se combinó impresión 3D con componentes metálicos comerciales:
Conexión del SAA (Sensores Capacitivos): Se utilizaron acoples fabricados íntegramen-
te en impresión 3D (PLA). La pieza cuenta con una rosca hembra G1/4" que se ajusta
directo al sensor, y en el otro extremo tiene un conector tipo espiga para insertar la man-
guera de silicona. Para sellar los poros del plástico impreso y evitar fugas, los acoples se
recubrieron con resina química.
Conexión del SCR (Sensores Piezorresistivos): Dado su formato industrial, se utilizó
una conexión en dos etapas. Primero, se conectó al sensor un acople reductor de acero
(de G1/2" hembra a G1/4" macho) para dar un soporte mecánico firme. Sobre esta pieza
de acero, se enroscó un adaptador impreso en 3D (de G1/4" hembra a espiga). De este
modo, ambos tipos de sensores terminaron con el mismo conector de espiga para acoplar
las mangueras de silicona.
Además, para asegurar la estanqueidad, se utilizó sellos tipo bonded entre el sensor y el
acople.


=== PÁG 58 del PDF ===
46
Figura 5.1: Detalle de la instalación de tomas de presión. Izquierda: ubicación en el modelo
físico. Derecha: Vista inferior del salto de esquí con las mangueras de silicona conectadas. Fuente:
Elaboración propia.
5.2.
Metodología de Caracterización Metrológica Estática
Una vez establecida la conexión física, se determinó la curva de calibración de cada trans-
ductor para traducir su respuesta eléctrica a unidades de presión (Figliola and Beasley, 2019).
Independientemente de si la señal se registra en bytes (SAA) o en Voltios (SCR), la calibración
estática permite obtener la regresión lineal que define la sensibilidad estática y la desviación
del cero para cada cadena de medición (Deutscher Kalibrierdienst and Physikalisch-Technische
Bundesanstalt, 2014).
5.2.1.
Diseño del Banco de Calibración (Principio de Sifón)
Ante la falta de un patrón certificado que cumpliera con la resolución requerida en el rango
operativos de los sensores (SAA y SCR), se optó por utilizar la carga hidrostática directa (P =
ρg∆h) como instrumento de referencia de presión (Figliola and Beasley, 2019). En metrología,
los manómetros de nivel líquido son reconocidos explícitamente como patrones de referencia,
ya que derivan la magnitud de la presión a partir de dimensiones físicas fundamentales: longitud
y densidad (Deutscher Kalibrierdienst and Physikalisch-Technische Bundesanstalt, 2014).


=== PÁG 59 del PDF ===
47
Para materializar este principio, se diseñó un montaje basado en vasos comunicantes (sifón)
que consta de:
1. Columna Variable: Recipiente cilíndrico que actúa como reservorio móvil de nivel varia-
ble.
2. Línea de Sifón: Transmisión de la presión por gravedad hacia los sensores ubicados en
una cota inferior fija.
3. Sistema de Distribución: Integración de válvulas de tres vías de grado médico para la
calibración simultánea isobárica de múltiples sensores y la purga selectiva de aire.
La medición de la columna de agua se realizó mediante un limnímetro con una precisión de
±0,1 mm.
5.2.2.
Protocolo de Carga Escalonada
Bajo esta configuración física, se implementó una adaptación unidireccional del protocolo de
carga escalonada establecido en la directriz alemana DKD-R 6-1 (Deutscher Kalibrierdienst and
Physikalisch-Technische Bundesanstalt, 2014). Debido a las restricciones operativas del banco
de vasos comunicantes, que dificultaban extraer el fluido de forma sistemática y controlada en
comparación con la facilidad de la fase de llenado, el ensayo se limitó a secuencias de carga
estrictamente ascendentes.
De la normativa europea se adoptó el siguiente criterio de escalonamiento:
1. Definición de Escalones: 10 niveles de carga hidráulica discreta. El ensayo inició a partir
de una carga hidrostática mínima, estrictamente necesaria para garantizar el cebado por
gravedad de la manguera y habilitar el principio de vasos comunicantes previniendo la
intrusión de aire. Esto permitió cubrir un rango de calibración efectivo de 25 cm c a entre
la cota mínima y la máxima.
2. Ventana de Estabilización: Cada carga se mantuvo constante durante un tiempo de reposo
de 60 s para asegurar el equilibrio inercial del sistema.


=== PÁG 60 del PDF ===
48
Figura 5.2: Banco de calibración mediante vasos comunicantes y válvulas de tres vías. Fuente:
Elaboración propia.
3. Transición: Se asignó un intervalo de 5 s para el incremento del nivel y la estabilización
del fluido en el siguiente escalón.
En consecuencia, la ejecución completa de la curva de calibración requirió un tiempo efecti-
vo de aproximadamente 15 minutos, contemplando un minuto de estabilización en la cota base,
dos minutos de espera en la carga máxima y el registro de la descarga final. Esto asegura la
estabilización mecánica del sensor antes de concluir el ensayo (Deutscher Kalibrierdienst and
Physikalisch-Technische Bundesanstalt, 2014). Esta adaptación metodológica permitió determi-
nar la sensibilidad estática y la linealidad de ambas cadenas de medición (SAA y SCR). La
evaluación de la histéresis se omitió del protocolo debido a la inviabilidad operativa de ejecu-


=== PÁG 61 del PDF ===
49
tar descargas de fluido controladas en el banco. No obstante, esta restricción carece de impacto
metrológico para el fenómeno en estudio: el flujo en el salto de esquí es supercrítico y plena-
mente turbulento (INH, 2016a). Al estar gobernado por fluctuaciones macroturbulentas (P ′) de
gran amplitud y baja frecuencia, la membrana del sensor no experimenta ciclos cuasi-estáticos,
haciendo que el error de histéresis resulte físicamente irrelevante (Chanson, 2004; Figliola and
Beasley, 2019). Por consiguiente, la conversión de la señal depende exclusivamente de la sensi-
bilidad estática obtenida durante la carga ascendente. En este régimen dinámico, la pérdida de
precisión no proviene de desviaciones estáticas del diafragma, sino de la atenuación inducida
por la inercia de la línea de transmisión y el filtrado electrónico (DSP) intrínseco del sensor (H.
Tijdeman, 1965; Jentzsch et al., 2024).
5.3.
Resultados de Calibración y Selección de Instrumenta-
ción
5.3.1.
Análisis del Sistema de Arquitectura Abierta (SAA)
La ejecución del protocolo de carga escalonada permitió registrar la respuesta temporal de los
transductores capacitivos frente a incrementos discretos de presión hidrostática (Figura 5.3). La
estabilización horizontal observada en cada escalón evidencia el equilibrio inercial del sistema
de vasos comunicantes, validando la correcta adopción de los tiempos de espera exigidos por la
norma (Deutscher Kalibrierdienst and Physikalisch-Technische Bundesanstalt, 2014). A partir
de estas series temporales estabilizadas, se extrajeron los promedios de cada carga para construir
las curvas de calibración individuales (Figura 5.4) y determinar la sensibilidad estática de la
cadena de medición mediante una regresión por Mínimos Cuadrados Ordinarios (OLS) (Figliola
and Beasley, 2019).
A partir de los datos obtenidos, se seleccionaron los sensores más aptos para el SAA (ver
Tabla 5.1). La tabla actúa como la herramienta de decisión fundamental del estudio, reportando
la linealidad (R2), la sensibilidad (pendiente), la dispersión de la señal (rango intercuartílico) y
el error máximo absoluto.


=== PÁG 62 del PDF ===
50
Figura 5.3: Serie de tiempo obtenida en la calibración de los 8 sensores capacitivos Keller. Fuente:
Elaboración propia.
Figura 5.4: Curvas de calibración obtenidas para el SAA. Las barras de error ilustran la desvia-
ción respecto al promedio en cada carga. Fuente: Elaboración propia.


=== PÁG 63 del PDF ===
51
Tabla 5.1: Parámetros de calibración y error máximo estimado para los sensores capacitivos
Keller (SAA). Sensores descartados marcados con (*). Fuente: Elaboración propia.
Indice
Sensor
Pendiente (bits/cm.c.a.)
Intercepto (bits)
R2
Rango IQ
Error máx (cm.c.a.)
0
Keller S1
24.82
130.91
0.9961
1.60
0.06
1
Keller S2
24.13
181.09
0.9857
1.40
0.06
2
Keller S3
23.76
163.49
0.9969
1.90
0.08
3
Keller S4 (*)
23.80
169.70
0.9940
2.40
0.10
5
Keller S6 (*)
26.39
50.99
0.9993
5.00
0.19
6
Keller S7
24.02
154.77
0.9975
1.70
0.07
7
Keller S8
24.82
153.00
0.9898
0.90
0.04
8
Keller S9
25.25
118.76
0.9965
1.00
0.04
Criterios de Selección y Descarte Operativo:
Sensores S4 y S6 (Descartados): Excluidos del arreglo final de forma preventiva por
registrar un ruido de señal superior al umbral aceptable (Rango Intercuartílico elevado,
particularmente S6 con IQ = 5,00 bytes) y errores máximos absolutos cercanos al límite
de tolerancia.
Sensores Seleccionados: El ensayo validó el uso de los sensores S1, S2, S3, S7, S8 y
S9, los cuales demostraron una alta linealidad (R2 > 0,985) y un error máximo acotado
(≤0,08 cm.c.a.).
5.3.2.
Análisis del Sistema Comercial de Referencia (SCR)
Los sensores piezorresistivos del sistema de referencia (HR Wallingford) mostraron un alto
coeficiente de determinación (R2 > 0,999) (ver 5.2). Los diagramas de caja (boxplots) sobre
cada punto experimental evidencian una dispersión de señal prácticamente nula (Figura 5.6).


=== PÁG 64 del PDF ===
52
Figura 5.5: Serie de tiempo obtenida en la calibración de los 6 sensores piezorresistivos Keller
del SCR. Fuente: Elaboración propia.
Figura 5.6: Curvas de Calibración obtenidas para los sensores piezorresistivos del SCR. Las
barras de error ilustran la desviación respecto al promedio en cada carga. Fuente: Elaboración
propia.


=== PÁG 65 del PDF ===
53
Tabla 5.2: Parámetros de calibración y error máximo estimado para los sensores del SCR. Fuente:
Elaboración propia.
Indice
Sensor
Pendiente (V/cm.c.a.)
Intercepto (V)
R2
Rango IQ
Error máx (cm.c.a.)
0
HR1
0.0516
0.5734
0.9992
0.0096
0.19
1
HR2
0.0490
0.9108
1.0000
0.0087
0.18
2
HR3
0.0495
1.0402
0.9999
0.0084
0.17
3
HR4
0.0489
1.5922
1.0000
0.0087
0.18
4
HR5
0.0490
1.3138
1.0000
0.0084
0.17
5
HR6
0.0492
1.4460
0.9999
0.0101
0.20
Consistencia y Análisis Comparativo: Al contrastar ambas tecnologías, se evidencia que el
SCR posee una linealidad superior (R2 > 0,999) al SAA (R2 > 0,985). No obstante, los sensores
escogidos del SAA tienen asociado un error máximo < 0,1 cm.c.a. que resultan competitivas
frente a los errores máximos del SCR (< 0,2 cm.c.a.).
5.4.
Protocolo de Instalación In-Situ y Caracterización Diná-
mica
5.4.1.
Compensación Topográfica y Procedimiento de Tara Hidráulica
La configuración geométrica del montaje en el modelo físico introduce una diferencia de
cota ineludible entre el diafragma del sensor y la toma de presión mecanizada en el salto de
esquí. Esto genera una componente de presión hidrostática constante (offset) que desplaza verti-
calmente la curva de calibración obtenida en el laboratorio. Para demostrar que la sensibilidad
estática del sensor (la pendiente de calibración m) permanece invariante ante este desfase, se
define una traslación lineal x′ = x + c, donde x representa la variable independiente (presión
patrón impuesta durante la calibración) y c es la constante de traslación equivalente a la carga
hidrostática por diferencia de cota. Al evaluar el estimador de la pendiente mediante Mínimos
Cuadrados Ordinarios (OLS), se comprueba matemáticamente su invariabilidad:
m′ = Cov(x + c, y)
Var(x + c)
= (x + c)y −(¯x + c)¯y
(x + c)2 −(¯x + c)2 = xy −¯x¯y
x2 −¯x2 = m
(5.1)


=== PÁG 66 del PDF ===
54
Validada matemáticamente la invariabilidad de la pendiente (m′ = m), la determinación del
nuevo intercepto operativo (bsitio) se ejecutó de forma sistemática para todos y cada uno de los
ensayos. Asumiendo el purgado y la saturación total de las mangueras de silicona como una con-
dición previa ya establecida en el montaje, se aplicó el siguiente protocolo de Tara Hidráulica:
1. Extinción del Flujo: Tras la detención del sistema de bombeo, se dispuso de un tiempo
de espera hasta asegurar la disipación total del escurrimiento, garantizando que el fluido
en la toma quedara estrictamente enrasado a la cota del salto de esquí (condición de carga
dinámica nula).
2. Registro Estacionario: Al inicio y/o al término de cada corrida experimental, se procedió
a la adquisición ininterrumpida de la señal base de los sensores durante un período de 5 min
bajo esta condición estática. Esta estrategia operativa permitía optimizar la toma de datos
encadenando ensayos consecutivos, utilizando un único período de reposo como lectura
final del primer evento y lectura inicial del subsiguiente, minimizando así los ciclos de
arranque y detención de las bombas de impulsión.
3. Aislamiento del Cero Hidráulico: Se definió el intercepto local (bsitio) de cada prueba
como la media aritmética de los datos capturados en dicha serie temporal estática. La sus-
tracción de este valor a las mediciones brutas permitió no solo anular el offset topográfico
de la columna, sino también neutralizar la deriva temporal del cero (zero drift) induci-
da por la electrónica entre ensayos, en estricto cumplimiento con la directriz DKD-R 6-1
(Deutscher Kalibrierdienst and Physikalisch-Technische Bundesanstalt, 2014; Figliola and
Beasley, 2019).
5.4.2.
Caracterización del Rendimiento de Adquisición (SAA)
A diferencia del SCR, cuya unidad de interfaz (TOPS) y entorno propietario garantizan una
frecuencia de muestreo fija e ininterrumpida para la alta dinámica (alcanzando tasas de 3,3 kHz),
la frecuencia de adquisición (fs) en el SAA carece de un reloj de hardware dedicado de forma
exclusiva a la temporización discreta de la señal. En consecuencia, el desempeño dinámico del
SAA está estrictamente gobernado por el cuello de botella que impone la velocidad de transmi-
sión del protocolo serial RS485 inherente a su instrumentación (KELLER Druckmesstechnik


=== PÁG 67 del PDF ===
55
AG, 2023). Para determinar los límites operativos y la capacidad de respuesta, se evaluó em-
píricamente esta dependencia, modelando el comportamiento del SAA mediante una regresión
lineal (R2 ≈0,99):
Figura 5.7: Caracterización del rendimiento del SAA. Regresión lineal entre la velocidad de
transmisión (Baudios) y la tasa de muestreo efectiva (fs). El sistema demuestra capacidad para
operar en un rango amplio, alcanzando hasta ≈300 Hz a 115 200 baudios. Fuente Elaboración
propia.
fs ≈A · Baudios + B
(5.2)
La configuración del puerto serial a 115 200 bps permitió estabilizar una tasa de muestreo
efectiva de fs ≈300 Hz (Figura 5.7). De acuerdo con el teorema de muestreo de Nyquist-
Shannon, esta tasa define una frecuencia de corte de 150 Hz. Considerando que la literatura es-
tablece que la energía dominante de la macroturbulencia en SECDE se concentra en frecuencias
inferiores a los 25 Hz, la tasa de 300 Hz garantiza un sobremuestreo robusto (Toso and Bowers,
1988; Fiorotto and Rinaldo, 1992). Este margen de seguridad previene el solapamiento espectral
(aliasing) y asegura una densidad de datos óptima para la posterior estimación de la Densidad
Espectral de Potencia (PSD) mediante el método de Welch.


=== PÁG 68 del PDF ===
56
5.5.
Verificación de Condiciones de Contorno Geométricas
La geometría del salto de esquí (curvatura y ángulo de despegue) define directamente la
magnitud y distribución de las fluctuaciones de presión. Para validar los registros experimentales
frente a las formulaciones empíricas de (Heller et al., 2005; Nazari et al., 2015), es indispensa-
ble asegurar las magnitudes físicas efectivas del modelo. Por ello, se realizó un levantamiento
topográfico sobre la superficie del salto de esquí de acrílico.
La medición consistió en una matriz de 25 puntos coordenados (5 × 5) capturados con es-
tación total y prisma georreferenciado, abarcando desde el labio de despegue hacia el segundo
tramo del rápido de descarga (cubriendo el eje central, los cuartos y los bordes laterales). Para de-
terminar los parámetros topológicos as-built, la nube de puntos se ajustó mediante una regresión
no lineal por mínimos cuadrados a un modelo geométrico a tramos. Esta función rige el acople
espacial entre el perfil rectilíneo del rápido y el arco circular del salto de esquí. A través de la
regresión, se obtienen todos los parámetros necesarios que definen la geometría de la estructu-
ra: las coordenadas del centro de la circunferencia (xc, yc), el radio de curvatura (R), el ángulo
de inclinación longitudinal del rápido (α) y el ángulo de despegue del salto de esquí (alpha),
asegurando la continuidad cinemática en el punto de transición (xt, yt):
y(x) =





yt + tan(α)(x −xt)
si x < xt
(Rápido de descarga)
yc −
q
R2 −(x −xc)2
si x ≥xt
(Salto de esquí)
(5.3)
La convergencia de esta optimización matemática sobre los datos empíricos arrojó una geo-
metría efectiva caracterizada por un radio R = 44,9 cm (equivalente a 17,96 m en el prototipo),
una pendiente de empalme en el rápido de α ≈45,3◦y un ángulo de despegue de θ ≈4,12◦.
Para validar el modelo de regresión, los parámetros angulares se corroboraron in-situ me-
diante dos niveles electrónicos de precisión independientes. Las lecturas instrumentales arroja-
ron valores de 45,5◦y 45,4◦para el rápido (α) y exactamente 4◦en el labio de salida (θ). La
desviación máxima de ≈0,2◦entre la matriz topográfica y la medición topográfica confirma la
convergencia del ajuste y rinde cuenta de las tolerancias constructivas milimétricas del acrílico
termomoldeado.
Para evidenciar esta congruencia espacial, la Figura 5.8 presenta la superficie paramétrica


=== PÁG 69 del PDF ===
57
optimizada superpuesta a la nube de puntos medidos en el laboratorio. Finalmente, la integración
de estas dimensiones empíricas en la topología del archivo STL utilizado como dominio compu-
tacional garantiza que tanto el modelo CFD como la instalación física operan bajo condiciones
de contorno cinemáticas idénticas, aislando el análisis de las fluctuaciones de presión de posibles
sesgos por deformación constructiva.
Figura 5.8: Levantamiento topográfico del modelo físico. Fuente: Elaboración propia.


=== PÁG 70 del PDF ===
58
a) Estación Total
b) Medición con Prisma
Figura 5.9: Evidencia del levantamiento topográfico en el salto de esquí del modelo físico modelo
físico. Fuente: Elaboración propia.
5.6.
Estimación Teórica del Espectro de Energía
Previamente a la ejecución de los ensayos en el modelo físico y al procesamiento de las
señales(ver Capítulo 6), resulta imperativo definir analíticamente las fronteras frecuenciales es-
peradas para el escurrimiento. La turbulencia en estructuras de disipación es un proceso estocás-
tico, estacionario y ergódico, cuya densidad espectral de potencia (PSD) puede regionalizarse en
bandas características regidas por la escala geométrica de los vórtices (Lopardo, 2018).
Para estimar el límite de frecuencias dominantes (fd) asociada a la inyección de energía
de la macroturbulencia en el salto de esquí, se emplea la caracterización adimensional basada
en el número de Strouhal (Sd). De acuerdo con las investigaciones experimentales de Lopardo
(2018) respecto a las fluctuaciones de presión en la base de flujos macroturbulentos, el número
de Strouhal característico de las frecuencias de máxima energía varía espacialmente en el rango
de Sd ∈[0,02, 0,08], dependiendo de la abscisa de separación de la capa límite. Esta frecuencia


=== PÁG 71 del PDF ===
59
dominante está gobernada por la velocidad media ( ¯U) y el tirante hidráulico (h), siguiendo la
relación:
fd = Sd · Uo
h0
(5.4)
Para el diseño de las obras de evacuación del Embalse Ancoa, los datos establecen que, para
el caudal de diseño de 761 m3 s−1 (T = 1.000 años), el flujo alcanza el final del segundo tramo
del rápido (inicio del salto de esquí) con una velocidad en prototipo de Up = 23,93 m s−1 y un
tirante de hp = 2,59 m (INH, 2016a).
Aplicando la ley de similitud dinámica de Froude para el modelo físico a escala λL = 40,
los parámetros cinemáticos efectivos de ingreso al salto de esquí corresponden a una velocidad
Um = Up/√λL ≈3,78 m s−1 y un tirante hm = hp/λL ≈0,0647 m. Evaluando el rango
empírico establecido para el número de Strouhal (0,02 ≤Sd ≤0,08), la banda de frecuencias
dominantes esperada en el modelo de laboratorio se sitúa en el siguiente intervalo:
fd ∈[1,17, 4,67] Hz
(5.5)
Este anclaje analítico predictivo resulta metrológicamente preciso, ya que la frecuencia de
máxima inyección de energía turbulenta registrada durante los ensayos en el modelo físico se
ubicó exactamente en el entorno de los 3 Hz, arrojando un número de Strouhal efectivo de Sd ≈
0,05. Esta convergencia valida empíricamente la parametrización de Lopardo (2018) y confirma
que el instrumental propuesto captura la macro-escala del fenómeno. A partir de esta referencia
espectral, la Densidad Espectral de Potencia (PSD) queda dividida en tres regímenes físicos:
1. Zona de Producción Energética (Macroturbulencia): Engloba la inyección primaria de
energía cinética al sistema, dominada por el peak frecuencial de los grandes vórtices cohe-
rentes (banda de 1,2 a 4,8 Hz). Esta zona concentra la mayor varianza del escurrimiento y
representa la firma hidrodinámica responsable de las fuerzas transitorias de levantamiento
(uplift) que rigen el diseño estructural de las losas de amortiguación (Fiorotto and Rinaldo,
1992; Lopardo, 2018).
2. Subrango Inercial (Cascada de Kolmogorov): Inicia inmediatamente después de la fre-
cuencia de inyección de máxima energía. En esta banda, la energía cinética se transfiere


=== PÁG 72 del PDF ===
60
desde los vórtices principales hacia escalas menores mediante un proceso inercial. Desde
el punto de vista metrológico, esta zona es la referencia teórica para validar la instrumen-
tación: si el sensor captura correctamente la dinámica turbulenta sin distorsionar la señal,
su espectro de energía debe reproducir la pendiente de −5/3 característica de un flujo
desarrollado (Pope, 2000).
3. Microturbulencia y Rango de Disipación Viscosa: De acuerdo con los fundamentos de
la turbulencia isótropa, la cascada inercial finaliza cuando las estructuras vorticosas se
reducen hasta la microescala de Kolmogorov, disipando su energía cinética en calor por
acción viscosa del fluido (Pope, 2000). En modelos hidráulicos operados bajo similitud de
Froude (λL = 40), la distorsión del número de Reynolds (λRe = λ3/2
L ) impone una penali-
zación cinemática que adelanta esta disipación (Heller, 2011). Este efecto de escala define
un umbral frecuencial que ha sido tipificado empíricamente por la literatura experimental;
investigaciones sobre el impacto de chorros de alta energía determinan que la macroturbu-
lencia dominante se concentra por debajo de los 25 Hz (Toso and Bowers, 1988; Fiorotto
and Rinaldo, 1992), mientras que el contenido espectral de alta frecuencia estructuralmen-
te crítico desaparece al cruzar la frontera de los ≈100 Hz (Bollaert and Schleiss, 2003). A
partir de este límite consensuado por el estado del arte, el espectro ingresa al rango disipa-
tivo puro, donde la amplitud física de las fluctuaciones resulta ínfima. Metrológicamente,
explorar esta banda de altísima frecuencia en modelos a escala solo adquiere justificación
para la captura de eventos transitorios extremos, tales como la cavitación incipiente regida
por depresiones instantáneas del 0,1 % (Fattor et al., 2003).
Para sintetizar la fundamentación analítica expuesta, la Figura 5.10 ilustra la topología espe-
rada del espectro en el modelo físico, definiendo las fronteras operativas para los ensayos en el
modelo físico.
Justificación del Teorema de Nyquist para el SAA: La delimitación fenomenológica de es-
tas bandas ratifica las exigencias de diseño del SAA. Para caracterizar sin distorsión matemática
(aliasing) la macroturbulencia y la cascada inercial estructuralmente relevante (hasta ≈100 Hz),
el criterio de Nyquist-Shannon exige una frecuencia de muestreo teórica mínima de fs ≥200 Hz.
Al haber estabilizado el SAA a una tasa efectiva de fs ≈300 Hz, se garantiza un margen de


=== PÁG 73 del PDF ===
61
Figura 5.10: Esquema teórico del Espectro de Densidad de Potencia (PSD) esperado para las
fluctuaciones de presión en el salto de esquí (escala Log-Log). Se delimitan analíticamente las
tres fronteras físicas fundamentales: inyección de energía primaria (fd ≈3 Hz), subrango inercial
de Kolmogorov (pendiente universal de −5/3) y el límite de disipación viscosa o piso de ruido
instrumental (> 100 Hz). Se incluye el umbral de Nyquist que ratifica la suficiencia de la tasa de
muestreo del SAA. Fuente: Elaboración propia.
sobremuestreo (oversampling) que certifica la idoneidad metrológica del SAA para capturar ín-
tegramente la macroturbulencia y el subrango inercial, cuyas magnitudes rigen las solicitaciones
críticas para la estabilidad estructural de las losas.


=== PÁG 74 del PDF ===
62
Capítulo 6
Resultados y Discusión
En este capítulo se presentan los hallazgos obtenidos tras la ejecución de los ensayos en el
modelo físico del Embalse Ancoa, lo cual comprendió 24 ensayos válidos (sintetizados en la
Tabla 6.1). Las pruebas experimentales se enmarcan en dos caudales característicos estables del
sistema de impulsión del laboratorio: un caudal Q1 ≈14,8 L/s y un caudal Q2 ≈55,0 L/s.
El análisis de los resultados se estructura en cuatro etapas secuenciales: En primer lugar, se
expone la caracterización teórica de Heller et al. (2005); Nazari et al. (2015) frente al modelo
numérico (CFD) para evaluar la estimación de las fluctuaciones de presión. En segundo lugar,
se contrasta la distribución espacial de las presiones físicas medidas frente a las formulaciones
empíricas, analizando el desfase posicional detectado. Posteriormente, se realiza una evaluación
del SAA y SCR para validar la respuesta en la medición de las fluctuaciones de presión por medio
del espectro de densidad de potencia (PSD). Finalmente, se discuten los límites operativos del
sistema implementado y se sintetizan las lecciones experimentales.


=== PÁG 75 del PDF ===
63
Tabla 6.1: Matriz operativa de los ensayos en el modelo físico del embalse Ancoa: Regímenes
de caudal y configuración de tasas de muestreo en ambos sistemas de adquisición. Fuente: Ela-
boración propia.
Caudal Bajo (Q ≈14,8 L/s)
Caudal Alto (Q ≈55,0 L/s)
Ensayo
¯Qmed (L/s)
fs SAA (Hz)
fs SCR (Hz)
Ensayo
¯Qmed (L/s)
fs SAA (Hz)
fs SCR (Hz)
P2
14,83
21
830
P1
55,18
21
830
P3
14,83
21
830
P2
55,19
21
830
P4
14,81
21
21
P3
55,22
21
830
P5
14,80
21
21
P4
55,11
327
830
P6
14,81
21
21
P6
55,11
326
327
P7
14,87
206
218
P7
55,12
205
218
P8
14,80
127
127
P8
55,13
124
127
P9
14,75
128
127
P10
55,00
301
127
P10
14,85
302
127
P11
55,12
115
127
P11
14,83
117
127
P12
55,07
183
127
P12
14,80
191
127
P13
55,08
49
127
P13
14,85
50
127
Pmax
55,00
297
3333
6.1.
Caracterización Numérica del Flujo (OE 1)
El modelo numérico WMLES con el método de volumen de fluido (VOF), se ejecutó como
herramienta de caracterización hidrodinámica (ver 1.3.2) para predecir la distribución espacial
del campo de presiones y la cinemática en torno a la geometría del salto de esquí.
El caudal mayor ensayado en el modelo físico fue de 55,0 L/s, limitado por el sistema de
impulsión del laboratorio. En contraste, la modelación numérica se escaló a un escenario superior
con un caudal de 75,2 L/s, correspondiente a la crecida de diseño milenaria (T=1000 años) (INH,
2015b). Aunque esta diferencia impide una comparación directa, el modelo numérico, con los
caudales simulados (14,8 L/s y 75,2 L/s), cumplió el propósito de caracterización preliminar
fundamental al estimar el orden de magnitud y la ubicación de la máxima fluctuación de presión.
La Figura 6.1 muestra cualitativamente que la modelación numérica reprodujo el compor-
tamiento macroscópico del flujo, capturando la deflexión de la lámina de agua al momento del


=== PÁG 76 del PDF ===
64
despegue en el salto de esquí.
Figura 6.1: Comparación del flujo del modelo numérico (izquierda) y su respectiva ejecución
sobre el modelo físico experimental (derecha). Fuente: Elaboración propia
La modelación numérica estimó el punto de máxima fluctuación de presión en torno a la
coordenada de 23,0 cm, medida horizontalmente desde el labio de despegue del salto de esquí
en dirección contraria al flujo. Específicamente, para el caudal simulado de 75,2 L/s el punto
de máxima fluctuación de presión se ubicó en Xpm = 23,4 cm, mientras que para el caudal de
14,8 L/s se situó en Xpm = 22,6 cm.
Notablemente, esta coordenada central de 23,0 cm coincide con la abscisa teórica donde
el modelo empírico de Nazari et al. (2015) ancla el punto de máxima presión dinámica media,
calculada exclusivamente a través de los parámetros geométricos de la estructura:


=== PÁG 77 del PDF ===
65
Xpm,Nazari = R · sin θ · 0, 492

sin θ
sin θ + sin α
−1,12
(6.1)
Xpm,Nazari = 44,9 cm · sin 4, 12◦· 0, 492

sin 4, 12◦
sin 4, 12◦+ sin 45, 3◦
−1,12
≈23,03 cm
(6.2)
Para evaluar visualmente esta convergencia, la Figura 6.2 expone la envolvente longitudinal
de las presiones fluctuantes extraídas de la modelación numérica, normalizadas espacialmente
respecto a la coordenada teórica central de 23,0 cm.
Figura 6.2: Desfase espacial de la fluctuación de presión (P ′) del modelo numérico y modelos
teóricos de Heller et al. (2005) y Nazari et al. (2015). Eje longitudinal normalizado respecto a
23 cm. Fuente: Elaboración propia
Para fundamentar hidrodinámicamente estos resultados y confirmar la validez inercial de
la simulación, resulta imperativo evaluar los parámetros cinemáticos incidentes. La Figura 6.3
ilustra el plano de corte geométrico empleado como sección transversal de control.


=== PÁG 78 del PDF ===
66
Figura 6.3: Sección de control en el salto de esquí del modelo numérico para la extracción e
integración espacial de los campos cinemáticos. Fuente: Elaboración propia
La modelación computacional en el salto de esquí permitió cuantificar los campos de velo-
cidad y fracción de agua, entre otros. Mediante la integración espacial de las celdas con fracción
de agua α ≥0, 5 (convención de OpenFOAM para identificar la fase líquida densa) sobre la
sección trapezoidal del salto de esquí, se extrajo el tirante promedio, el área transversal y el cau-
dal saliente, omitiendo del cálculo las fracciones menores correspondientes a la mezcla bifásica
(espumas o gotas dispersas sobre la superficie libre).
Para el régimen Q1 = 14,8 L/s, se determinó un tirante promedio de fase líquida (α ≥0, 5)
de h ≈11,6 mm y una velocidad promedio del flujo de V = 3,61 m/s (Fr = 10, 74). En la
simulación del caudal mayor (Q = 75,2 L/s), el tirante resultó en h ≈38,3 mm y V = 4,52 m/s
(Fr = 7, 47). Aunque el método VOF incompresible dispersa una fracción de la masa en celdas
de transición (α < 0, 5), penalizando la continuidad, ambos escenarios operan dentro o en la
vecindad inmediata del rango de validez cinemática estudiado por Heller et al. (2005) (3 ≤
Fr ≤10) y Nazari et al. (2015) (4, 7 ≤Fr ≤9, 5).


=== PÁG 79 del PDF ===
67
Figura 6.4: Caracterización hidrodinámica numérica en el despegue (t = 40 s). (a) Régimen de
caudal menor con tirante efectivo h ≈11,6 mm. (b) Régimen de caudal mayor (75, 2 L/s) con
tirante medio h ≈38,3 mm. Fuente: Elaboración propia
6.2.
Validación Experimental y Discusión del Desfase Espa-
cial
6.2.1.
Configuración Física y Cinemática del Flujo
A partir de la localización del punto de máxima fluctuación de presión determinado por el
modelo numérico (≈23,0 cm), se definieron las coordenadas de medición para el SAA y el SCR
en el modelo físico. En este punto inicial se instaló una toma de presión compartida mediante
una conexión con válvulas de tres vías, lo que permitió captar la señal por ambos sistemas de
adquisición de manera simultánea. Para registrar el gradiente longitudinal, el arreglo de sensores
se distribuyó de manera equiespaciada cada 10,0 cm proyectados horizontalmente respecto al
punto inicial: ubicando dos puntos de medición hacia aguas abajo (13,0 cm y 3,0 cm) y tres puntos
hacia aguas arriba (33,0 cm, 43,0 cm y 53,0 cm) a lo largo del salto de esquí (ver Figura 6.5).


=== PÁG 80 del PDF ===
68
Figura 6.5: Disposición del arreglo de sensores de presión instalados sobre la curvatura del salto
de esquí. El nodo inicial coincide con la posición del punto de máxima fluctuación de presión
determinado por el modelo numérico. Fuente: Elaboración propia
Para caracterizar el régimen de escurrimiento antes del despegue, se empleó un sensor ultra-
sónico, acoplado al DAQ del SAA que medía de forma simultánea al arreglo de seis sensores de
presión capacitivos (Figura 6.6), que midió el tirante de la lámina de agua en la zona del rápido
de descarga para ambos caudales evaluados en laboratorio.
Para el caudal Q1 ≈14,8 L/s, el sensor ultrasónico registró un tirante medio de h =
9,03 mm, lo cual corresponde a una velocidad media de V = 5,42 m/s derivada de la geometría


=== PÁG 81 del PDF ===
69
Figura 6.6: Instalación del sensor de barrido ultrasónico sobre el modelo físico de acrílico para
la medición empírica del tirante de la lámina de agua libre. Fuente: Elaboración Propia
de la sección, resultando en un Número de Froude de Fr = 18, 31. Por su parte, durante el cau-
dal mayor (Q2 ≈55,0 L/s), este mismo instrumento midió un tirante medio de h = 21,33 mm,
que se traduce en una velocidad de V = 8,42 m/s, resultando en un Número de Froude de
Fr = 18, 69. La magnitud de estas fuerzas inerciales confirma que el modelo físico operó bajo
condiciones de flujo supercríticas.
Al contrastar esta inercia real con las estimaciones de la simulación numérica de la sección
anterior, se evidencia una clara discrepancia: para el caudal menor (Q1), el modelo numérico
estimó el tirante en h ≈11,6 mm frente a los 9,03 mm medidos por el sensor ultrasónico, deri-
vando en un Fr ≈10, 74 numérico frente al Fr ≈18, 31 del modelo físico. Esta caída inercial
responde directamente a una limitación intrínseca del método VOF de interfaz nítida al extraer
parámetros unidimensionales desde un flujo bifásico (Witt et al., 2015; Bayon et al., 2016). Al
restringir la integración cinemática exclusivamente a las celdas de fase líquida (α ≥0, 5), se
excluye de la estimación del Número de Froude la inercia del fluido difuminado en la interfaz
y las gotas dispersas. Esto disminuye el caudal saliente efectivo y aumenta numéricamente el
tirante equivalente (h), resultando en una disminución artificial de la velocidad media integrada
(V ) y, consecuentemente, del Número de Froude (ver Figura 6.4).


=== PÁG 82 del PDF ===
70
6.2.2.
Registro de Fluctuaciones de Presión y Desfase Espacial
A partir del procesamiento de las series temporales para cada sensor, se extrajo la desviación
estándar (RMS) de la señal en el estado estacionario estimando la presión fluctuante. Al comparar
la magnitud y ubicación de la fluctuación de presión máxima entre el modelo numérico y físico,
se observa una diferencia significativa.
Como consecuencia directa de la discrepancia inercial analizada previamente, la Figura 6.7
expone las presiones fluctuantes máximas registradas longitudinalmente en el modelo físico y
numérico, superpuestas a la curva teórica de presión dinámica media propuesta por Heller et al.
(2005) y Nazari et al. (2015). El contraste visual es categórico: mientras las estimaciones teóricas
y la modelación numérica (gobernadas por números de Froude menores) convergieron en situar el
punto de máxima solicitación en las cercanías de Xpm = 23,0 cm (x/Xpm ≈1, 0), la modelación
física demostró que el impacto extremo real, impulsado por el Número de Froude del flujo (Fr ≈
18, 3), ocurrió desplazado hacia el labio de despegue, ubicándose en torno a la abscisa X =
13,0 cm (sensor ubicado aguas abajo del nodo central).
Además del desfase originado por las diferencias de los números de Froude, la gráfica consta-
ta una evidente sobreestimación del modelo numérico en la magnitud de la fluctuación de presión
máxima. Esta divergencia de amplitud es una consecuencia directa de la formulación matemá-
tica del solver (interFoam) acoplada a la resolución de la malla. Evaluaciones del desempeño
algorítmico del método VOF de interfaz nítida en OpenFOAM (Hirt and Nichols, 1981; Desh-
pande et al., 2012) demuestran que esta formulación presenta limitaciones intrínsecas: asume
inmiscibilidad y es incapaz de simular el atrapamiento de aire si la escala característica de la ma-
lla es mayor que el diámetro de la burbuja generada por la turbulencia (Witt et al., 2015; Bayon
et al., 2016). En este estudio, la estrategia adoptada para enfrentar la turbulencia consistió en
un enfoque WMLES, el cual posiciona el primer nodo computacional en la región logarítmica
con un valor adimensional promedio de y+ ≈30. Refinar las celdas a escalas submilimétricas
para capturar la fase dispersa (disminuyendo el y+ a valores unitarios tipo Wall-Resolved) in-
crementaría el costo computacional a niveles muy superiores. Por consiguiente, la simulación
asume inmiscibilidad a nivel de celda y omite el atrapamiento de aire a escala de subgrilla. En
la realidad física del laboratorio, esta macro-aireación induce un aumento de volumen aparente
(flow bulking) que disminuye la densidad macroscópica (Bayon et al., 2016), mientras que el aire


=== PÁG 83 del PDF ===
71
introduce compresibilidad al fluido, reduciendo drásticamente la celeridad de las ondas de pre-
sión acústica (Chanson, 2004). Esta compresibilidad hace que la mezcla actúe como un colchón
neumático (cushion effect), amortiguando la energía de las presiones de alta frecuencia, lo cual
se omite en el modelo numérico y explica la sobreestimación en la magnitud.
A la limitación espacial del modelo numérico se suma un efecto de escala inherente a la mo-
delación física. Tal como advierte la literatura (Pfister and Chanson, 2014) y corrobora el INH
para el diseño experimental del Embalse Ancoa (INH, 2015b), los modelos reducidos regidos
por la similitud de Froude subestiman el atrapamiento de aire, dado que las fuerzas viscosas y
de tensión superficial ejercen una influencia desproporcionada que inhibe la aireación a pequeña
escala. Por lo tanto, si el modelo físico ya es capaz de generar una mezcla bifásica que amorti-
gua las fluctuaciones de presión máximas frente a la rigidez incompresible del modelo numérico,
fenómeno evidenciado en la Figura 6.7 donde el solver sobreestima la solicitación máxima con
P ′
max = 1,69 cm c a frente a los valores del modelo físico medidos por el SAA y SCR (apro-
ximadamente 1,0 cm c a , ver Sección 6.3), el prototipo experimentará un aumento de volumen
aparente (flow bulking) y una atenuación elasto-neumática aún mayores (Pfister and Chanson,
2014). Este hecho confirma que la modelación física, en unión con sistemas de medición como
el SAA y SCR, constituye un requisito indispensable para el diseño estructural, permitiendo co-
rregir la sobreestimación sistemática de las herramientas computacionales sharp-interface (INH,
2016a).


=== PÁG 84 del PDF ===
72
Figura 6.7: Desplazamiento horizontal y diferencia de magnitud de las presiones fluctuantes má-
ximas. Comparación entre la modelación numérica y modelación física SAA/SCR, superpuestas
a las curvas teóricas de presión dinámica media de Heller et al. (2005) y Nazari et al. (2015).
Fuente: Elaboración propia


=== PÁG 85 del PDF ===
73
6.3.
Caracterización Comparativa del Desempeño Instrumen-
tal (OE 2)
Con el propósito de contrastar las capacidades de captura hidrodinámica de ambos sistemas
de medición, se realizó una caracterización comparativa de sus respuestas en el dominio de la
frecuencia. Este análisis permite validar la representatividad física de los registros obtenidos
tanto por el SAA como por el SCR del espectro teórico obtenido en la Sección 5.6, identificando
las potencialidades y restricciones de cada tecnología en la resolución de la turbulencia.
6.3.1.
Sincronía Temporal y Respuesta Transitoria
Como etapa inicial de la comparación, se verificó la respuesta transitoria y la sincronización
de ambos sistemas mediante la captura simultánea de un evento temporal (Figura 6.8).
Figura 6.8: Comparación temporal de las presiones capturadas por el SCR y el SAA (Q ≈
55,0 L/s). El registro evidencia una sincronía de fase que permite contrastar la respuesta de am-
bos sistemas ante eventos impulsivos de alta frecuencia.
Si bien la morfología y las amplitudes de la señal varían según el punto de medición, exis-
tiendo puntos de flujo transicional donde el SAA registra amplitudes mayores que el SCR, la


=== PÁG 86 del PDF ===
74
inspección visual de este extracto revela una sincronía de fase coincidente. Este comportamien-
to confirma que ambos sistemas detectan las fluctuaciones de manera simultánea, descartando
retrasos en el reloj del microcontrolador. Sin embargo, la clara diferencia en las amplitudes de-
muestra que el análisis en el dominio del tiempo no basta para evaluar la energía de la turbulencia.
Por ello, resulta indispensable analizar las señales mediante la Densidad Espectral de Potencia
(PSD) para determinar con exactitud qué información logra capturar cada instrumento.
6.3.1.1.
Análisis Espectral Comparativo y Cascada de Kolmogorov
Para evaluar la representatividad física de los registros obtenidos por ambos sistemas en
la captura de la fenomenología turbulenta, se recurrió a la estimación de la Densidad Espectral
de Potencia (PSD) mediante el método de Welch (Welch, 1967; BENDAT and PIERSOL, 2010).
Los resultados, expuestos en la Figura 6.9, permiten contrastar la respuesta dinámica del SAA y
del SCR bajo tres criterios fundamentales:
1. Congruencia Morfológica en Macroturbulencia: En el espectro de bajas frecuencias
(0,1 Hz ≤f ≤10 Hz), las curvas del SAA y del SCR exhiben una coincidencia de la
densidad energética, destacando una convergencia en el rango cuasi-estático (f < 1 Hz).
Ambos sistemas localizan con precisión el peak de inyección de energía en el entorno de los
3 Hz (frecuencia fundamental de macroturbulencia predicha por el Número de Strouhal)
(Lopardo, 2018). Esta coincidencia demuestra que el SAA posee una capacidad equiva-
lente al SCR para resolver la macroturbulencia y garantizar el cálculo de solicitaciones
globales.
2. Preservación de la Cascada Inercial y Variabilidad: Ambos sistemas, en todos los pun-
tos medidos, siguen la pendiente de atenuación proporcional a f −5/3, validando que tanto
el SAA como el SCR capturan la dinámica real de las transferencias de energía en el su-
brango inercial (Kolmogorov, 1991b). Adicionalmente, las áreas sombreadas (Mín-Máx)
evidencian la alta sensibilidad del SCR frente a los extremos dinámicos del flujo. Esta ma-
yor variabilidad acumulada en el espectro del SCR contrasta con la respuesta suavizada del
SAA, anticipando la divergencia entre los valores RMS que se cuantificará en la sección
estadística.


=== PÁG 87 del PDF ===
75
3. Límite de Resolución Frecuencial y Ancho de Banda: El análisis espectral define los
límites operacionales de ambos sensores introducidos por sus respectivas tasas de adquisi-
ción. La curva del SAA se interrumpe en 150 Hz, lo que corresponde a su límite de Nyquist
para una frecuencia de muestreo de 300 Hz (Figliola and Beasley, 2019), mientras que el
SCR posee alta tasa de muestreo (3333 Hz). Sin embargo, con independencia de este lími-
te matemático, el SAA manifiesta una atenuación física prematura en las zonas de flujo
transicional (como el sensor P2), comenzando a perder resolución frente al SCR entre los
10 Hz y 20 Hz. Esta caída anticipada actúa en la práctica como un filtro paso-bajo que mi-
tiga la amplitud de las vibraciones estructurales del modelo (visibles en el SCR en torno a
los 100 Hz), entregando una señal suavizada en su banda útil.


=== PÁG 88 del PDF ===
76
Figura 6.9: Densidad Espectral de Potencia (PSD) absoluta y normalizada (Q ≈55,0 L/s). El
contraste permite identificar el rango de coincidencia física y los umbrales de resolución de cada
tecnología. Fuente: Elaboración propia


=== PÁG 89 del PDF ===
77
6.4.
Evaluación Estadística y Determinación de Límites del
SAA
Para establecer empíricamente las fronteras operativas del SAA, se consolidó el análisis es-
tadístico para cada punto de medición y régimen de caudal. La Tabla 6.2 sintetiza los estadísticos
críticos evaluando la sensibilidad a la tasa de muestreo (fs). Se exponen los resultados del caudal
menor (Q ≈14,8 L/s) en los Bloques A y B y el Bloque C con los casos bajo el caudal mayor
(Q ≈55,0 L/s).
Tabla 6.2: Resultados estadísticos del SAA frente al SCR evaluando la sensibilidad a la tasa de
muestreo (fs). El Bloque A muestra los resultados en el punto de máxima fluctuación de presión
(Punto 2). El Bloque B muestra los resultados en el punto adyacente (Punto 3). El Bloque C
expone los resultados bajo el caudal máximo. Fuente: Elaboración propia
Ensayo / Punto
Tasas de Muestreo
Media Estática [cm]
Error Relativo
Rel. RMS
Morfología (S/K)
(fs SAA / fs SCR)
µSAA
µSCR
(ϵµ [ %])
(σSAA/σSCR)
SAA
SCR
Bloque A: Punto 2 - Máxima Fluctuación de Presión (Q ≈14,8 L/s)
P4 (Submuestreo)
20 Hz / 21 Hz
9,48
11,98
-20,93 %
1,18
0,07 / 2,90
0,18 / 3,05
P13 (Transición)
49 Hz / 127 Hz
8,19
14,31
-42,76 %
0,86
0,14 / 3,05
0,07 / 3,03
P8 (Banda media)
126 Hz / 127 Hz
11,33
20,50
-44,74 %
1,01
0,11 / 2,98
0,07 / 2,99
P7 (Óptimo)
206 Hz / 218 Hz
9,73
14,56
-33,16 %
1,14
-0,07 / 2,96
0,07 / 3,05
P10 (Sobremuestreo)
303 Hz / 127 Hz
8,86
14,71
-39,76 %
0,84
0,15 / 3,08
0,12 / 3,02
Bloque B: Punto 3 - Punto Adyacente (Q ≈14,8 L/s)
P4 (Submuestreo)
20 Hz / 21 Hz
7,64
6,51
+17,47 %
0,71
-0,05 / 2,91
0,00 / 2,89
P13 (Transición)
49 Hz / 127 Hz
8,27
7,48
+10,60 %
0,76
0,00 / 3,02
0,02 / 2,96
P8 (Banda media)
126 Hz / 127 Hz
7,71
10,29
-25,07 %
0,47
-0,20 / 2,86
0,04 / 2,87
P7 (Óptimo)
206 Hz / 218 Hz
6,96
7,46
-6,64 %
0,61
-0,12 / 3,00
0,04 / 3,02
P10 (Sobremuestreo)
303 Hz / 127 Hz
8,45
8,09
+4,51 %
0,62
-0,10 / 3,08
-0,03 / 2,98
Bloque C: Mediciones bajo Caudal Mayor (Q ≈55,0 L/s)
P1 (Pto. 2 - Submuestreo)
20 Hz / 830 Hz
32,78
40,36
-18,78 %
0,50
-40,49 / 1816,40
0,08 / 3,00
Pmax (Pto. 2 - Óptimo)
297 Hz / 3333 Hz
32,46
40,87
-20,58 %
1,36
-23,69 / 695,44
0,12 / 3,21
Pmax (Pto. 3 - Adyacente)
297 Hz / 3333 Hz
21,61
20,45
+5,67 %
0,65
0,15 / 2,92
0,01 / 3,01
A partir de estos resultados, se identifican las diferencias en el desempeño metrológico del
SAA frente al SCR, las cuales se explican mediante las características físicas del equipo de
medición.


=== PÁG 90 del PDF ===
78
6.4.1.
Comportamiento Metrológico en Puntos Adyacentes
En los puntos adyacentes, alejados del punto de máxima fluctuación de presión (Puntos 1, 3,
4, 5 y 6), el SAA registra valores cercanos a los obtenidos con el SCR. Como se observa en el
Bloque C de la Tabla 6.2 para el caudal mayor (Q ≈55,0 L/s), la presión estática media en el
Punto 3 indica µSAA = 21,61 cm frente a µSCR = 20,45 cm, resultando en un error relativo de
+5, 67 %. Esta similitud también se observa en los ensayos con el caudal menor (Bloque B).
Esta correspondencia se fundamenta en la distribución espectral de la energía observada en
los puntos adyacentes. Como lo evidencia la Figura 6.9, en estas ubicaciones la mayor parte de la
energía fluctuante se concentra en el espectro de bajas frecuencias (f < 10 Hz). De acuerdo con
la literatura, en los puntos adyacentes los gradientes transitorios de alta frecuencia ya se han disi-
pado, y la dinámica del flujo está gobernada por la macroturbulencia (Lopardo and Romagnoli,
2008). Dado que en este dominio de frecuencias el SAA no se ve limitado por el filtro paso-bajo
de su sensor ni por la resolución de su ADC, ambos sistemas presentan coincidencia morfológica
y energética. Al confirmar que el SAA registra de manera adecuada esta banda de frecuencias,
se valida su capacidad para cuantificar cargas estáticas medias y solicitaciones dinámicas en re-
giones donde la violencia de los gradientes transitorios del impacto ya se ha disipado (Fiorotto
and Rinaldo, 1992; Bollaert and Schleiss, 2003).
6.4.2.
Limitaciones en el Punto de Máxima Fluctuación de Presión
Los resultados en el punto de máxima fluctuación de presión (Punto 2) muestran diferencias
sistemáticas frente al SCR. Se observan subestimaciones del valor medio de hasta un −44, 74 %
(Tabla 6.2, Bloque A), lo que representa una diferencia de ≈4,8 cm c a .
Las diferencias en la captura de la señal en el Punto 2 se explican mediante dos factores
derivados de los componentes electrónicos (ver Secciones 3.4 y 3.3):
Efecto del Procesamiento Digital de Señales (DSP): El DSP del sensor capacitivo re-
quiere tiempo de cálculo para compensar matemáticamente la señal (KELLER Druckmess-
technik AG, 2023). Ante gradientes de presión rápidos generados por el impacto del flujo
supercrítico, la latencia de este cálculo hace que el sensor actúe como un filtro paso-bajo,
atenuando las fluctuaciones de mayor frecuencia. Físicamente, el instrumento no logra ras-


=== PÁG 91 del PDF ===
79
trear la tasa de cambio del transitorio y trunca los peaks máximos de presión (Figliola and
Beasley, 2019; Jentzsch et al., 2024). En consecuencia, al calcular el promedio de la serie,
el valor medio resultante (µSAA) sufre una subestimación inherente frente al registrado por
el SCR (µSCR).
Resolución del Conversor Analógico-Digital (ADC): El conversor de 10 bits del SAA
discretiza la señal continua en 1024 niveles. Al enfrentarse a variaciones abruptas de pre-
sión, este límite de resolución introduce un error de cuantización. En el procesamien-
to digital de señales, este error actúa como un ruido aditivo de banda ancha que incre-
menta artificialmente la varianza total de la serie (Proakis and Manolakis, 2007). Esto
se refleja en variaciones del estadístico RMS, como en el ensayo P4 (Bloque A) donde
σSAA/σSCR = 1, 18, o en el ensayo Pmax (Bloque C) donde la relación asciende a 1, 36.
Este aumento matemático en la desviación estándar (RMS) no corresponde a una mayor
energía física del flujo, sino a la varianza inyectada por el ruido de cuantización del ADC.
6.4.3.
Evaluación de la Asimetría y Curtosis
A pesar de las diferencias descritas en la captura de amplitud en alta frecuencia, el SAA
registra valores de asimetría (S) y curtosis (K) acordes a los medidos por el SCR en los puntos
adyacentes al impacto. En el Punto 3 (Bloque C), los valores obtenidos son SSAA = 0, 15 frente
a SSCR = 0, 01, y KSAA = 2, 92 frente a KSCR = 3, 01.
Dado que ambos parámetros estadísticos se definen como momentos centrales normalizados,
resultan matemáticamente invariantes frente a transformaciones lineales de escala (Figliola and
Beasley, 2019). Por consiguiente, a pesar de la atenuación de energía inducida por el filtro DSP
y el ADC, el SAA logra tipificar correctamente la morfología del flujo en zonas subcríticas.
Esto demuestra empíricamente que el equipo preserva la macroturbulencia y la dinámica del
subrango inercial como se observó en la Figura 6.9, registrando procesos simétricos (S ≈0) y
mesocúrticos (K ≈3).
En contraste, en el Punto 2 bajo el caudal mayor (Q ≈55,0 L/s), los estadísticos en el en-
sayo Pmax (Bloque C) alcanzan valores de S = −23, 69 y K = 695, 44. Estas cifras carecen
de significado hidrodinámico y documentan directamente el colapso de los componentes elec-


=== PÁG 92 del PDF ===
80
trónicos frente a las fluctuaciones de presión de alta frecuencia. La lectura extrema de curtosis
determina empíricamente el límite operativo del SAA, identificando el umbral físico donde la
saturación del equipo invalida por completo la morfología de la señal, fenómeno que se eviden-
cia visualmente a través de la severa amplitud de la variabilidad espectral (envolvente Min-Max)
registrada en el Punto 2 para el caudal de 55,0 L/s en la Figura 6.9.


=== PÁG 93 del PDF ===
81
Capítulo 7
Conclusiones y Recomendaciones
Esta investigación tuvo como propósito desarrollar una metodología técnico-experimental
para la caracterización de fluctuaciones de presión en modelos físicos hidráulicos, asistida por
simulación numérica (CFD) para definir los rangos de presión y fluctuaciones en la zona de
estudio, evaluando el desempeño de un Sistema de Arquitectura Abierta (SAA) mediante su
comparación independiente frente a un Sistema Comercial de Referencia (SCR) en el modelo
físico del Embalse Ancoa (INH). A partir del análisis fenomenológico, espectral y estadístico se
extraen las siguientes conclusiones fundamentales.
7.1.
Conclusiones y Límites de Aplicabilidad
Las conclusiones se estructuran en respuesta directa a los Objetivos Específicos (OE) traza-
dos al inicio de esta investigación:
1. Rol de la Prospección Numérica (OE 1): La modelación computacional (WMLES-VOF)
cumplió su objetivo como herramienta inicial de estimación, permitiendo identificar la zo-
na crítica de impacto y guiar la distribución de los sensores en el modelo físico. Sin em-
bargo, tal como se discutió en el Capítulo 6, la simulación presentó un desfase espacial
en el punto de máxima fluctuación de presión y sobreestimó la magnitud de las presiones
extremas. Este fallo es inherente a los modelos incompresibles de interfaz nítida (sharp-
interface) (Hirt and Nichols, 1981), los cuales asumen inmiscibilidad y omiten el efec-
to amortiguador (cushion effect) del aire atrapado (Chanson, 2004; Pfister and Chanson,


=== PÁG 94 del PDF ===
82
2014). Dada la naturaleza del fenómeno, refinar la malla a escalas submilimétricas para
capturar estas microburbujas incrementaría el tiempo de cómputo a órdenes de magnitud
superiores. Por lo tanto, el modelo numérico configurado como muestra el Capítulo 4 para
este caso, sirve como un estimador preliminar de la superficie libre y de los campos de
presión.
2. Validación Dinámica y Macroturbulencia (OE 2): El análisis espectral del SAA demos-
tró congruencia con la cascada de Kolmogorov (pendiente f −5/3) (Kolmogorov, 1991a),
capturando las fluctuaciones de baja frecuencia (fmodelo ≤20 Hz) que, al escalarse me-
diante la similitud de Froude (fp = fm/
√
40), cubren la banda de la macroturbulencia del
prototipo (fp ≈0,47 Hz, equivalente a ≈3 Hz en laboratorio). Esta resolución valida su
uso para evaluar la estabilidad global y el levantamiento de losas (uplift) (Fiorotto and Ri-
naldo, 1992), definiendo una envolvente de cargas conservadora. Espacialmente, se debe
considerar que la coordenada del punto de máxima fluctuación de presión en el prototi-
po sufrirá un desplazamiento debido a la mayor resistencia aerodinámica del chorro, un
efecto de escala que la similitud de Froude omite en laboratorio (Novak et al., 2007). Fi-
nalmente, en el dominio de alta frecuencia, el SAA logró caracterizar el subrango inercial
hasta los ≈100 Hz de forma equivalente al SCR, topando con su barrera física absoluta
en la frecuencia de Nyquist (≈150 Hz) por efecto del aliasing, umbral más allá del cual
es exclusivamente el SCR el que logra registrar la zona plana de disipación viscosa donde
la turbulencia remanente se transforma en calor.
3. Consolidación de una Metodología Replicable y sus Fronteras Operativas (OE 3): La
validación cruzada consolida la entrega de una matriz de decisión metodológica replicable
que trasciende la evaluación individual de los sistemas. Por un lado, se demostró que el
SAA viabiliza el mapeo espacial de alta densidad (Stanghellini et al., 2020; Rodríguez-
Juárez et al., 2018), siendo metrológicamente idóneo para determinar valores medios y
cargas globales en la macroturbulencia. Sus fronteras operativas, sin embargo, evidencian
una subestimación sistemática del RMS de hasta un ≈50 % en el punto de máxima fluc-
tuación de presión, producto del filtrado paso-bajo inducido por la latencia del DSP y el
ruido de cuantización del ADC (H. Tijdeman, 1965; Jentzsch et al., 2024). Por otro lado,


=== PÁG 95 del PDF ===
83
la metodología desmitifica al SCR como un estándar absoluto; si bien su elevado costo y
arquitectura cerrada imponen una restricción en la cantidad de puntos de medición (HR
Wallingford, 2024), su configuración con transductores piezorresistivos le otorga la exclu-
sividad técnica para medir la cinemática en la escala disipativa (KELLER AG für Druck-
messtechnik, 2024). Por consiguiente, se establece la suficiencia técnica del SAA como
una herramienta independiente para el diseño macroestructural, cuantificando la magnitud
extrema de las fluctuaciones de presión, y relegando al SCR para el diagnóstico de fatiga
de alto ciclo o cavitación incipiente (Bollaert and Schleiss, 2003).
7.1.1.
Matriz de Decisión Metrológica (Síntesis OE 3)
Como corolario del cumplimiento del tercer objetivo específico, y con el fin de consolidar
la transferencia tecnológica de esta investigación hacia la práctica profesional de la ingeniería
civil, se presenta la Tabla 7.1. Esta matriz sintetiza los límites operativos, ventajas y restriccio-
nes de cada sistema evaluado, proporcionando una guía metodológica para la caracterización de
presiones hidrodinámicas en estructuras de disipación de energía.


=== PÁG 96 del PDF ===
84
Tabla 7.1: Matriz de aplicabilidad tecnológica para la evaluación de presiones hidrodinámicas
en estructuras de alta energía. Guía metodológica para la selección de instrumentación y mode-
lación.
Herramienta
Aplicación
Rango Fr
Ventajas y Fortalezas
Limitaciones Físicas
Eq. Empíricas
(Ej. Heller,
Nazari)
Estimación
preliminar de
presión media,
máximo impacto y
posición.
4, 7 ≤Fr ≤
10
(Rango
calibrado).
Método analítico y de
costo cero. Útil para
pre-dimensionamiento
geométrico temprano.
Ciegas a turbulencia
estocástica (no predicen
RMS ni espectros). Omiten
resistencia aerodinámica.
CFD
(Numérico)
(WMLES-
VOF)
Prospección de
macroturbulencia,
lámina libre y
gradientes de
presión.
Fr ≫1
(Alta
inercia).
Resolución espacial
continua. Identifica
topológicamente zonas
críticas previo a la
instrumentación (Bayon
et al., 2016).
Sobreestima la magnitud
extrema de presiones por
incapacidad de simular la
aireación y el efecto
colchón (Witt et al., 2015;
Chanson, 2004).
SAA (Abierto)
(Arduino +
Cap.
(KELLER
Druckmess-
technik AG,
2023))
Estabilidad global
(Fiorotto and
Rinaldo, 1992),
cargas medias y
macroturbulencia.
Fr ≫1
Bajo costo DAQ
(Stanghellini et al., 2020) y
acceso total. Alta densidad
espacial. Caracteriza el
subrango inercial hasta
≈100 Hz.
Atenuación RMS
(≈50 %) por latencia del
DSP (Jentzsch et al., 2024).
Riesgo de aliasing en
límite de Nyquist (Figliola
and Beasley, 2019).
SCR
(Comercial)
(TOPS +
Piezorr.
(KELLER AG
für Druckmess-
technik, 2024))
Fatiga de alto ciclo,
cavitación
incipiente y
microturbulencia
(Bollaert and
Schleiss, 2003).
Independiente
del Fr.
Respuesta dinámica
directa (kHz). Captura la
cinemática en la escala
disipativa y la magnitud
del RMS real.
Elevado costo que restringe
la densidad espacial de
medición en el modelo.
Arquitectura cerrada.
Esta matriz evidencia que, si bien el SAA posee suficiencia técnica autónoma, la evaluación
integral de estas estructuras se optimiza al concebir las herramientas bajo un esquema de esca-
lonamiento tecnológico progresivo. El diseño se beneficia al utilizar las ecuaciones empíricas


=== PÁG 97 del PDF ===
85
(Heller et al., 2005; Nazari et al., 2015) y la estimación numérica mediante el modelo numérico
(Bayon et al., 2016) para el pre-dimensionamiento cinemático y topológico; desplegar matri-
ces del SAA para mapear las cargas de estabilidad global (uplift) en áreas extensas de las losas
(Fiorotto and Rinaldo, 1992); y, exclusivamente de ser necesario, reservar la instrumentación
del SCR para monitorear puntos críticos donde exista riesgo de cavitación incipiente o fatiga
dinámica (Fattor et al., 2003; Bollaert and Schleiss, 2003).
7.2.
Recomendaciones y Trabajo Futuro
A partir de los resultados obtenidos y los límites operativos identificados, se sugieren las
siguientes líneas de desarrollo para futuras investigaciones:
1. Protocolo de Muestreo y Mitigación de Aliasing: Para estudios estándar de macroturbu-
lencia, la plataforma actual requiere configurar el DAQ del SAA con una tasa de muestreo
mínima de 200 Hz para satisfacer el criterio de Nyquist-Shannon (Figliola and Beasley,
2019). Para futuras implementaciones orientadas a capturar íntegramente el subrango iner-
cial de interés estructural (hasta ≈100 Hz) con mayor holgura frente al plegamiento de
energía (aliasing), se recomienda transitar hacia microcontroladores de mayor frecuencia
de reloj y arquitectura de 32 bits (como Arduino Due, ESP32 o Raspberry Pi Pico), permi-
tiendo estabilizar tasas de muestreo superiores a los 300 Hz sin saturación del bus serial.
2. Evolución del Hardware Sensorial: Se recomienda transitar desde transductores capaci-
tivos con DSP interno hacia transductores piezorresistivos de salida analógica directa. La
eliminación del procesamiento digital intermedio y la reducción de la impedancia elasto-
hidráulica de la manguera constituyen el requerimiento fenomenológico principal para
extender el ancho de banda dinámico del SAA hacia las escalas disipativas (H. Tijdeman,
1965; Jentzsch et al., 2024). Asimismo, se sugiere implementar conversores Analógico-
Digitales (ADC) externos de 16 bits (por ejemplo ADS1115) para erradicar el ruido de
cuantización del microcontrolador ante variaciones rápidas de presión, corrigiendo así la
desviación leptocúrtica observada en las distribuciones estadísticas.
3. Refinamiento Multifásico del Modelo Numérico: Para acortar la brecha cuantitativa en-


=== PÁG 98 del PDF ===
86
tre la simulación y el modelo físico en zonas de alto impacto, se sugiere incorporar modelos
Eulerianos multifásicos compresibles en futuros modelos numéricos. Esto permitirá mode-
lar el aumento de volumen aparente (flow bulking) y el fundamental efecto amortiguador
(cushion effect) que ejerce la disipación acústica de la lámina aerada sobre las presiones
extremas (Pfister and Chanson, 2014; Bayon et al., 2016).
4. Estandarización y Ciencia Abierta: Se propone consolidar las rutinas de adquisición de-
sarrolladas en C++ (Arduino) y los algoritmos de post-procesamiento espectral y estadís-
ticos programados en Python en repositorios de código abierto. Esta transferencia tecnoló-
gica facilitará la reproducibilidad de la metodología (Stanghellini et al., 2020; Rodríguez-
Juárez et al., 2018).
7.3.
Síntesis Global
En síntesis, el principal aporte de esta investigación es la consolidación de una metodología
técnico-experimental híbrida y escalonada para la caracterización de presiones hidrodinámicas
fluctuantes en modelos físicos. Este marco metodológico demuestra que la evaluación de estruc-
turas de disipación de alta energía se optimiza al no depender de un único instrumento, sino de la
integración sinérgica de tecnologías: la estimación numérica inicial mediante CFD (LES/VOF)
para identificar topológicamente las zonas críticas de impacto y gradientes adversos (Bayon et al.,
2016; Deshpande et al., 2012); el despliegue de instrumentación del SAA para el mapeo espacial
de alta densidad de la macroturbulencia y las cargas de estabilidad global (Stanghellini et al.,
2020; Fiorotto and Rinaldo, 1992); y la focalización del SCR en los puntos sometidos a riesgos
de microturbulencia disipativa (KELLER AG für Druckmesstechnik, 2024; Fattor et al., 2003).
Al definir explícitamente los límites metrológicos y operativos de cada una de estas etapas, esta
tesis entrega a la práctica de la ingeniería hidráulica un protocolo de medición moderno, eco-
nómicamente viable, reproducible y fundamentado en los principios de la mecánica de fluidos
y el procesamiento digital de señales (Kolmogorov, 1991a; Figliola and Beasley, 2019; Welch,
1967).


=== PÁG 99 del PDF ===
87
Bibliografía
Bayon, A., Valero, D., García-Bartual, R., Vallés-Morán, F. ., and López-Jiménez, P. A. (2016).
Performance assessment of OpenFOAM and FLOW-3D in the numerical modeling of a low
Reynolds number hydraulic jump. Environmental Modelling & Software, 80:322–335.
BENDAT, JULIUS. and PIERSOL, ALLAN. (2010). Random Data: Analysis and Measurement
Procedures, Fourth Edition. Wiley Series in Probability and Statistics. John Wiley & Sons,
Erscheinungsort nicht ermittelbar, 1st edition edition.
Bollaert, E. and Schleiss, A. (2003). Scour of rock due to the impact of plunging high velocity
jets Part II: Experimental results of dynamic pressures at pool bottoms and in one- and two-
dimensional closed end rock joints. Journal of Hydraulic Research, 41(5):465–480.
Breuer, M., Jovičić, N., and Mazaev, K. (2003). Comparison of DES, RANS and LES for the
separated flow around a flat plate at high incidence. International Journal for Numerical
Methods in Fluids, 41(4):357–388.
Buffon, F. T., Buffon, F. T., Marques, M. G., and Marques, M. G. (2016). Método de determinação
de pressões em bacias de dissipação a jusante de vertedores tipo salto esqui. null.
Castillo, L. G., Carrillo, J. M., and Marco, F. (2018). Advances in the characterization of pres-
sures and velocities in the overtopping of arch and gravity dams.
Chanson, H., editor (2004). The Hydraulics of Open Channel Flow: An Introduction ; Basic
Principles, Sediment Motion, Hydraulic Modelling, Design of Hydraulic Structures. Elsevier
Butterworth Heinemann, Amsterdam Boston, 2nd ed edition.


=== PÁG 100 del PDF ===
88
de Borja, J. G., de Borja, J. G., Sanagiotto, D. G., Sanagiotto, D. G., Sanagiotto, D. G., Marques,
M. G., Marques, M. G., Canellas, A. V. B., Canellas, A. V. B., Canellas, A. V. B., Palauro, C.,
and Palauro, C. (2019). Scale effect on mean pressures : Study of two reduced models of a ski
jump spillway. RBRH.
Deshpande, S., Anumolu, L., and Trujillo, M. (2012). Evaluating the performance of the two-
phase flow solver interFoam. Computational Science & Discovery, 5.
Deutscher Kalibrierdienst and Physikalisch-Technische Bundesanstalt (2014). Calibración De
Instrumentos Medidores De Presión. Directriz DKD-R 6-1, DKD (Servicio Alemán de Cali-
bración).
Diligent (2026).
Referencia de Digilent para TracerDAQ® y TracerDAQ® Pro.
https://digilent.com/reference/software/tracerdaq/start.
Eder, M., Eder, M., Hillman, G., Hillman, G., Tarrab, L., Tarrab, L., Pagot, M., Pagot, M., Ro-
dríguez, A., and Rodríguez, A. (2019). Modelación física de erosión en estructuras de baja
altura con saltos esquí. Tecnologia y Ciencias del Agua.
Ettema, R., editor (2000). Hydraulic Modeling: Concepts and Practice. Number 97 in ASCE
Manuals and Reports on Engineering Practice. ASCE, American Society of Civil Engineers,
Reston, Virginia.
Fattor, C. A., Lopardo, M. C., Casado, J. M., and Lopardo, R. A. (2003). CAVITATION BY
MACROTURBULENT PRESSURE FLUCTUATIONS IN HYDRAULIC JUMP STILLING
BASINS.
Ferziger, J., Perić, M., and Street, R. (2019). Computational Methods for Fluid Dynamics. Sprin-
ger International Publishing.
Figliola, R. and Beasley, D. (2019). Theory and Design for Mechanical Measurements. Wiley.
Fiorotto, V. and Rinaldo, A. (1992). Fluctuating Uplift and Lining Design in Spillway Stilling
Basins. Journal of Hydraulic Engineering, 118(4):578–596.


=== PÁG 101 del PDF ===
89
Galli, A., Peruzzi, C., Gangi, F., and Masseroni, D. (2024). ArduHydro: A low-cost device for
water level measurement and monitoring. Journal of Agricultural Engineering.
H. Tijdeman (1965). Theoretical and experimental results for the dynamic response of pressure
measuring systems by H.Bergh and H.Tijdeman.
Heller, V. (2011). Scale effects in physical hydraulic engineering models. Journal of Hydraulic
Research, 49(3):293–306.
Heller, V., Hager, W. H., and Minor, H.-E. (2005). Ski Jump Hydraulics. Journal of Hydraulic
Engineering, 131(5):347–355.
Hirt, C. and Nichols, B. (1981). Volume of fluid (VOF) method for the dynamics of free boun-
daries. Journal of Computational Physics, 39(1):201–225.
HR Wallingford (2024).
High Performance Pressure Sensors (Datasheet EQ-006 R6).
HR
Wallingford Ltd, Oxfordshire, UK.
INH (2015a). Embalse Ancoa: Esquema General Proyecto General BVP. Technical report, Ins-
tituto Nacional de Hidráulica.
INH (2015b). Modelación Física y Matemática de las Obras de Evacuación del Embalse Ancoa,
Región del Maule. Informe Final, Instituto Nacional de Hidráulica, Peñaflor, Chile.
INH (2016a). Modelación Física y Matemática de las Obras de Evacuación del Embalse Ancoa,
Región del Maule. Informe Final, Instituto Nacional de Hidráulica, Peñaflor, Chile.
INH (2016b).
Render del Modelo Físico del Embalse Ancoa en Verge3D Web Interactive.
https://theluisesquivel.github.io/Ancoa_SoporteRapido_v02/index.html.
INH (2020). Plano Eléctrico: Sistema de Adquisición de Datos (DAQ) basado en Arduino. Tech-
nical report, Instituto Nacional de Hidráulica.
INH (2024). Modelo Físico de Emergencia Embalse Ancoa - VII Región: Informe Etapa 1:
Revisión B. Informe Técnico, Instituto Nacional de Hidráulica, Peñaflor, Chile.


=== PÁG 102 del PDF ===
90
INH and Peña, C. (2020). Manual de Instrucciones para el Uso del Adquisidor de Datos MEGA
(DAQ-MEGA). Minuta Técnica Rev A, Instituto Nacional de Hidráulica (INH), Peñaflor,
Chile.
INH and Peña Bozo, C. (2024). Informe de calibración de sensores de nivel Microsonic ZWS-
15/CD/QS. Technical report, Instituto Nacional de Hidráulica, Peñaflor, Región Metropolita-
na.
Jentzsch, M., Lechner, W., Woszidlo, R., Nayeri, C. N., and Paschereit, C. O. (2024). The dy-
namic response of a pressure transducer for measurements in water. Experiments in Fluids,
65(8):125.
Júnior, R. S., Kipper, P. M., Ferreira, L., Teixeira, E. D., Prá, M. D., and Marques, M. G. (2023).
Turbulent pressures at the position of maximum pressure fluctuation in hydraulic jump stilling
basins. RBRH.
KELLER AG für Druckmesstechnik (2024). Series 25Y Piezoresistive Pressure Transmitters
Absolute and Gauge Pressure.
KELLER Druckmesstechnik AG (2023). Datenblatt Series 41X / 41X-Ei: Capacitive Pressure
Transmitter. KELLER Druckmesstechnik AG, Winterthur, Switzerland.
Kolmogorov, A. N. (1991a). Dissipation of Energy in the Locally Isotropic Turbulence. Procee-
dings: Mathematical and Physical Sciences, 434(1890,):15–17.
Kolmogorov, A. N. (1991b).
The Local Structure of Turbulence in Incompressible Viscous
Fluid for Very Large Reynolds Numbers. Proceedings: Mathematical and Physical Sciences,
434(1890,):9–13.
Kumcu, Ş. Y., Kumcu, S. Y., and Kumcu, S. Y. (2017). Investigation of flow over spillway
modeling and comparison between experimental data and CFD analysis. Ksce Journal of
Civil Engineering.
Li, G., editor (2001). XXIX IAHR Congress ”21st Century: The New Era for Hydraulic Re-
search and Its Applications”, Beijing, China, September 16-21, 2001: Proceedings of John F.
Kennedy Student Paper Competition. Tsinghua University Press, Beijing.


=== PÁG 103 del PDF ===
91
Lopardo, R. A. (2018). DESCRIPCIÓN DE ALGUNAS CARACTERÍSTICAS MACRO TUR-
BULENTAS DEL RESALTO HIDRÁULICO A PARTIR DE LAS PRESIONES EN SU BA-
SE.
Lopardo, R. A. and Romagnoli, M. (2008). Pressure and Velocity Fluctuations in Stilling Ba-
sins. In Advances in Water Resources and Hydraulic Engineering, pages 2093–2098, Berlin,
Heidelberg. Springer Berlin Heidelberg.
Moghadam, M. F., Moghadam, M. K., Amini, A., Malek, M. A., Mohammad, T. A., and Hoseini,
H. (2019). Physical Modeling of Ski-Jump Spillway to Evaluate Dynamic Pressure. Water.
Moghadam, M. K., Moghadam, M. K., Amini, A., Amini, A., Hosseini, H. A., and Hosseini,
H. (2020). Experimental evidence dynamic pressures reduction on plunge pool floors downs-
tream flip bucket for increasing downstream face slopes. Water supply.
Mousavi, S. N., Mousavi, S. N., Bocchiola, D., and Bocchiola, D. (2020). A Novel Comparative
Statistical and Experimental Modeling of Pressure Field in Free Jumps along the Apron of
USBR Type I and II Dissipation Basins. Mathematics.
Muhanad Mohammed Abbas (2013). Experimental Investigation of Pressure Distribution Along
Makhool Dam Spillway. Diyala Journal of Engineering Sciences, 6(2):122–138.
Nazari, O., Nazari, O., Jabbari, E., Jabbari, E., Sarkardeh, H., and Sarkardeh, H. (2015). Dynamic
pressure analysis at chute flip buckets of five dam model studies. International Journal of Civil
Engineering.
Negrete, F., Cotroneo, J., Zamorano, L., Osorio, C., Niño, Y., and Tamburrino, A. (2016). Com-
parison between physical and numerical models of the velocity measurement in the lateral
channel of the ancoa reservoir. RHMA.
Novak, P., Moffat, A., Nalluri, C., and Narayanan, R. (2007). Hydraulic Structures, Fourth
Edition. Taylor & Francis.
OpenCFD Ltd (2023). OpenFOAM v2312 User Guide. https://doc.openfoam.com/2312/.


=== PÁG 104 del PDF ===
92
Peltier, Y., Dewals, B., Archambeau, P., Pirotton, M., and Erpicum, S. (2017a). Pressure and
velocity on an ogee spillway crest operating at high head ratio: Experimental measurements
and validation. Journal of Hydro-environment Research, 19.
Peltier, Y., Peltier, Y., Dewals, B., Dewals, B., Archambeau, P., Archambeau, P., Pirotton, M.,
Pirotton, M., Erpicum, S., and Erpicum, S. (2017b). Pressure and velocity on an ogee spillway
crest operating at high head ratio: Experimental measurements and validation. Journal of
Hydro-environment Research.
Pfister, M. and Chanson, H. (2014). Two-phase air-water flows: Scale effects in physical mode-
ling. Journal of Hydrodynamics, 26(2):291–298.
Pope, S. B. (2000). Turbulent Flows. Cambridge University Press, Cambridge, 1. publ., 12. print
edition.
Proakis, J. and Manolakis, D. (2007). Digital Signal Processing. Prentice Hall International
Editions. Pearson Prentice Hall.
Rafael Santiago Seoane and Raúl Antonio Lopardo (2006). Evolución en los criterios hidroló-
gicos e hidráulicos de los aliviaderos para el control de crecidas en Argentina. Buenos Aires,
Argentina.
Rodríguez-Juárez, P., Júnez-Ferreira, H., González Trinidad, J., Zavala, M., Burnes-Rudecino, S.,
and Bautista-Capetillo, C. (2018). Automated Laboratory Infiltrometer to Estimate Saturated
Hydraulic Conductivity Using an Arduino Microcontroller Board. Water, 10(12):1867.
Rusche, H. (2002). Computational Fluid Dynamics of Dispersed Two-Phase Flows at High
Phase Fractions. PhD thesis, Imperial College London.
Smagorinsky, J. (1963). GENERAL CIRCULATION EXPERIMENTS WITH THE PRIMITI-
VE EQUATIONS: I. THE BASIC EXPERIMENT*. Monthly Weather Review, 91(3):99–164.
Stanghellini, G., Del Bianco, F., and Gasperini, L. (2020). OpenSWAP, an Open Architecture,
Low Cost Class of Autonomous Surface Vehicles for Geophysical Surveys in the Shallow
Water Environment. Remote Sensing, 12(16):2575.


=== PÁG 105 del PDF ===
93
Thorat, S., Thorat, S., Thorat, S., Nale, A., Nale, A., Vyavahare, Y., Vyavahare, Y., Shaikh, S.,
and Shaikh, S. (2020). Hydraulic Analysis of Ski Jump as An Energy Dissipator. International
journal of engineering research and technology.
Toso, J. W. and Bowers, C. E. (1988). Extreme Pressures in Hydraulic-Jump Stilling Basins.
Journal of Hydraulic Engineering, 114(8):829–843.
Welch, P. (1967). The use of fast Fourier transform for the estimation of power spectra: A method
based on time averaging over short, modified periodograms. IEEE Transactions on Audio and
Electroacoustics, 15(2):70–73.
Witt, A., Gulliver, J., and Shen, L. (2015). Simulating air entrainment and vortex dynamics in a
hydraulic jump. International Journal of Multiphase Flow, 72:165–180.
Yoshizawa, A. (1986). Statistical theory for compressible turbulent shear flows, with the appli-
cation to subgrid modeling. Physics of Fluids, 29(7):2152–2164.
