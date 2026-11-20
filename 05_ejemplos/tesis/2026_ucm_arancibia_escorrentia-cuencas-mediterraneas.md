<!-- Texto extraído automáticamente de 2026_ucm_arancibia_escorrentia-cuencas-mediterraneas.pdf (original: Ejemplo_tesis_2.pdf). Solo para lectura por IA; puede tener errores de extracción. NO copiar texto a la tesis. -->

=== PÁG 1 del PDF ===
UNIVERSIDAD CATÓLICA DEL MAULE
FACULTAD DE CIENCIAS DE LA INGENIERÍA
ESCUELA DE INGENIERÍA CIVIL
“PROCESOS DE GENERACIÓN DE ESCORRENTÍA y UMBRALES EN CUENCAS
MEDITERRANEAS”
CHRISTIAN RENÉ ARANCIBIA CÉSPEDES
PROFESOR GUÍA: GUILLERMO BARRIENTOS ANDRÉS ALARCÓN
Proyecto de Título presentado en conformidad a los requisitos para obtener el título de
Ingeniero Civil
TALCA, Abril 2026


=== PÁG 2 del PDF ===
UNIVERSIDAD CATÓLICA DEL MAULE
FACULTAD DE CIENCIAS DE LA INGENIERÍA
ESCUELA DE INGENIERÍA CIVIL
Proyecto de Título presentado en conformidad a los requisitos para obtener el título de
Ingeniero Civil
“PROCESOS DE GENERACIÓN DE ESCORRENTÍA Y UMBRALES EN CUENCAS
MEDITERRANEAS”
CHRISTIAN RENÉ ARANCIBIA CÉSPEDES
PROFESOR GUÍA: GUILLERMO ANDRÉS BARRIENTOS ALARCÓN
COMISIÓN EXAMINADORA
FIRMA
Dr. Guillermo Barrientos Alarcón / Dr. Ecosis-
temas Forestales y Recursos Naturales
Dr. Guillermo Barrientos Alarcón
Dr. Ismael Vera Puerto / Dr. Ciencias Ambienta-
les mención Sistemas Acuáticos Continentales
Dr. Ismael Vera Puerto
Dr. Marco Quiroz Valeria / Dr. Ciencias de la
Ingeniería
Dr. Marco Quiroz Valeria
NOTA FINAL EXAMEN DE TÍTULO
TALCA, Abril 2026


=== PÁG 3 del PDF ===
I
Abstract
Existe un vacío en la literatura respecto al análisis de alta resolución de eventos de crecida
en cuencas agrícolas mediterráneas de la Región del Maule, Chile. La extracción y el proce-
samiento de series temporales de alta resolución permiten examinar los mecanismos internos e
inferir los procesos de activación y su eficiencia frente a eventos de precipitación, lo que a su
vez contribuye a profundizar en sus implicaciones para la modelación hidrológica. Por lo tanto,
para suplir este vacío en la literatura, el presente estudio tuvo el objetivo de analizar los procesos
de activación, condiciones pre-evento y eficiencia hidrológica en tres cuencas mediterráneas de
la región del Maule (Robles, Chagres y Damas). Se procesaron 63 eventos de precipitación con
HydRun y regresión segmentada para evaluar la respuesta del sistema frente a distintas varia-
bles meteorológicas y de cobertura de suelo. Al analizar los resultados, las métricas pre-evento
muestran que la cobertura forestal en la cuenca Robles sostiene un mayor caudal base debido a
una alta conductividad hidráulica. En contraste, la predominancia agrícola en la cuenca Chagres
restringe el flujo base profundo y registra la mayor eficiencia de escorrentía directa. Esta cuenca
agrícola exhibe, además, un umbral de intensidad máxima de precipitación de 14.6 mm/h aso-
ciado a un flujo superficial por exceso de infiltración. Por otro lado, la cuenca Damas tuvo un
comportamiento similar a la Robles debido a su menor uso agrícola. Se presentó una ausencia
de umbrales exclusivos a la precipitación del evento aislado en las tres cuencas, por lo que la ge-
neración de escorrentía está gobernada por una memoria hidrológica a corto plazo de 3 a 5 días.
Se identificaron umbrales combinados que evalúan precipitación total y humedad antecedente
del suelo (Ptot +ASM100 ) en un rango de 505 a 522 mm para las tres cuencas. Se concluye que
la caracterización precisa del estado de humedad inicial del suelo es un control de primer orden
para evitar errores y simplificaciones en la modelación hidrológica.


=== PÁG 4 del PDF ===
II
Agradecimientos
Este trabajo fue financiado por el gobierno de Chile a través de ANID/FONDECYT/11250081
y ANID/BASAL/FB210015 (CENAMAD). Agradecemos el apoyo y la infraestructura propor-
cionados por el Departamento de Obras Civiles y la Vicerrectoría de Investigación y Postgrado
de la Universidad Católica del Maule, y el Centro Nacional de Excelencia para la Industria de la
Madera (CENAMAD) de la Pontificia Universidad Católica de Chile. Agradecemos a la Escuela
de Ingeniería Civil de la Universidad Católica del Maule


=== PÁG 5 del PDF ===
III
Índice general
Pág.
Resumen
I
Agradecimientos
II
Índice de figuras
VIII
Índice de tablas
X
1
Introducción
1
1.1
Contexto Teórico . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
1.2
Contexto de la Zona . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
1.3
Objetivo General . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
1.4
Objetivos Específicos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
2
Marco Teórico
5
2.1
Procesos Atmosféricos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
2.1.1
Circulación Atmosférica . . . . . . . . . . . . . . . . . . . . . . . . .
5
2.1.2
Generación de Precipitación . . . . . . . . . . . . . . . . . . . . . . .
6
2.2
Procesos de Superficie y Subsuperficie . . . . . . . . . . . . . . . . . . . . . .
8
2.2.1
Propiedades del Suelo
. . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.2.1.1
Textura del Suelo
. . . . . . . . . . . . . . . . . . . . . . .
8
2.2.1.2
Conductividad Hidráulica . . . . . . . . . . . . . . . . . . .
9
2.2.1.3
Capacidad de Almacenamiento de Humedad . . . . . . . . .
10
2.2.2
Infiltración . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10


=== PÁG 6 del PDF ===
2.2.3
Escorrentía Superficial . . . . . . . . . . . . . . . . . . . . . . . . . .
10
2.2.3.1
Flujo Hortoniano
. . . . . . . . . . . . . . . . . . . . . . .
11
2.2.3.2
Flujo por Exceso de Saturación . . . . . . . . . . . . . . . .
12
2.2.4
Escorrentía Subsuperficial . . . . . . . . . . . . . . . . . . . . . . . .
13
2.3
Conectividad Hidrológica . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
2.3.1
Hipótesis Llenado y Derrame (Fill and Spill)
. . . . . . . . . . . . . .
15
2.3.2
Umbrales Hidrológicos . . . . . . . . . . . . . . . . . . . . . . . . . .
17
2.3.3
Tipos de Umbrales . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
2.3.4
Identificación de Umbrales . . . . . . . . . . . . . . . . . . . . . . . .
19
2.3.5
Criterios para la aceptación de umbrales . . . . . . . . . . . . . . . . .
19
2.4
Fluviometría . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
2.5
Separación de eventos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
2.5.1
Separación del flujo base . . . . . . . . . . . . . . . . . . . . . . . . .
21
2.5.2
Extracción de eventos
. . . . . . . . . . . . . . . . . . . . . . . . . .
22
3
Materiales y Métodos
27
3.1
Área de Estudio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
3.1.1
Uso de Suelo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
3.1.2
Tipo de suelo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
3.2
Adquisición de Datos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
3.2.1
Datos Fluviométricos . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
3.2.2
Datos Pluviométricos . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
3.2.3
Datos de Humedad . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
3.3
Extracción de Eventos
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
3.4
Variables Predictoras y de Respuesta . . . . . . . . . . . . . . . . . . . . . . .
38
3.5
Implementación de Regresión Segmentada . . . . . . . . . . . . . . . . . . . .
41
3.6
Correlación entre características de la cuenca y respuesta hidrológica . . . . . .
42
4
Resultados
43
4.1
Análisis de Eventos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
43
4.2
Análisis De Umbrales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49


=== PÁG 7 del PDF ===
4.3
Análisis de Correlación . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
56
5
Discusión
60
5.1
Condiciones Pre-evento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
60
5.2
Activación y Memoria del Sistema . . . . . . . . . . . . . . . . . . . . . . . .
61
5.3
Umbral por Intensidad
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
62
5.4
Respuesta y Eficiencia de las Cuencas . . . . . . . . . . . . . . . . . . . . . .
63
5.5
Implicaciones para la Modelación Hidrológica . . . . . . . . . . . . . . . . . .
64
6
Conclusión
66
Bibliografía
67
Anexos
75
I
Datos Brutos
76


=== PÁG 8 del PDF ===
VI
Índice de figuras
Pág.
2.1
Diagrama latitudinal de circulación atmosférica general. Fuente: Extraido de
Chow et al. (1994). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.2
Diagrama de formación de precipitación. Fuente: Extraido de Chow et al. (1994).
7
2.3
Pirámide de texturas de suelo aplicado a suelos con varias fracciones de arena,
limo y arcilla. Fuente: Extraido de Dingman (2015). . . . . . . . . . . . . . . .
8
2.4
Proceso de Flujo Hortoniano. Fuente: Extraido de Beven (2011). . . . . . . . .
12
2.5
Proceso de Flujo por Exceso de Saturación. Fuente: Extraido de Beven (2011).
13
2.6
Proceso de Flujo Subsuperficial. Fuente: Extraido de Beven (2011).
. . . . . .
14
2.7
Esquema conceptual del mecanismo de Llenado y Derrame. Fuente: Extraido de
McDonnell et al. (2021). . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
2.8
Proceso de llenado y derrame a diferentes escalas. Se visualiza que la activación
de un umbral a miscroescala (Escala x=1) no garantiza la activación de umbrales
a escalas mayores (Escala x=2 y x=3). Fuente: Extraido de McDonnell et al. (2021). 16
2.9
Esquemas conceptuales de relaciones no lineales lluvia-escorrentía reportados
frecuentemente en la literatura. Fuente: Adaptado de Ali et al., 2013. . . . . . .
18
2.10 Diagrama de funcionamiento de HydRun. Fuente: Adaptado de Tang and Carey
(2017). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
3.1
Cartografía del área de estudio, se muestran las tres cuenca de interés y su posi-
ción en Chile y la región del Maule. Fuente: Elaboración propia. . . . . . . . .
28
3.2
Esquema de sensor HOBO MX20L. Fuente: Extraido de Onset Computer Cor-
poration (2024). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33


=== PÁG 9 del PDF ===
3.3
Serie temporal continua de caudales (Q) para las cuencas (a) Damas, (b) Chagres
y (c) Robles. El área sombreada resalta la magnitud del caudal durante el período
de registro. Fuente: Elaboración propia.
. . . . . . . . . . . . . . . . . . . . .
34
3.4
Serie temporal continua de precipitación (Pacum) para las cuencas (a) Damas, (b)
Chagres y (c) Robles. Fuente: Elaboración propia. . . . . . . . . . . . . . . . .
35
3.5
Serie temporal continua de precipitación acumulada (P) para las cuencas (a) Da-
mas, (b) Chagres y (c) Robles. Fuente: Elaboración propia. . . . . . . . . . . .
36
4.1
Hidrogramas de crecida junto a nivel de humedad para distintas profundidades.
Se detallan métricas hidrológicas correspondientes para eventos consecutivos en
las 3 cuencas de estudio. Fuente: Elaboración propia. . . . . . . . . . . . . . .
47
4.2
Relación entre Escorrentía total del evento RTOT y su precipitación total PTOT
asociada. La linea RC indica un transformación equivalente de precipitación en
escorrentía. Fuente: Elaboración propia. . . . . . . . . . . . . . . . . . . . . .
50
4.3
Umbrales para las métricas PTOT + PA3 (a), PTOT + ASM100 (b) y PA3 (c) para
las las tres cuencas. Fuente: Elaboración propia. . . . . . . . . . . . . . . . . .
53
4.4
Umbral de intensidad máxima en 10 minutos (Imax(10)) para la cuenca Chagres.
54
4.5
Análisis de Criterio de Información de Akaike corregido para las métricas con
al menos un resultado de R2
adj >0,45 en las tres cuencas de estudio. Fuente: Ela-
boración propia. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
4.6
Mapa de calor de correlación de Pearson (r) entre las respuestas hidrológicas y
los porcentajes de cobertura de uso de suelo. Fuente: Elaboración propia.
. . .
57
4.7
Mapa de calor de correlación de Pearson (r) entre las respuestas hidrológicas y
las métricas topográficas. Fuente: Elaboración propia. . . . . . . . . . . . . . .
58
4.8
Mapa de calor de correlación de Pearson (r) entre las respuestas hidrológicas y
las propiedades físicas del suelo (perfil 0-200 cm). Fuente: Elaboración propia.
59
I.1
Relación entre escorrentía total RTOT y métricas predictoras meteorológicas para
la cuenca Chagres. Fuente: Elaboración propia. . . . . . . . . . . . . . . . . .
83
I.2
Relación entre escorrentía total RTOT y métricas predictoras meteorológicas para
la cuenca Damas. Fuente: Elaboración propia. . . . . . . . . . . . . . . . . . .
84


=== PÁG 10 del PDF ===
I.3
Relación entre escorrentía total RTOT y métricas predictoras meteorológicas para
la cuenca Robles. Fuente: Elaboración propia. . . . . . . . . . . . . . . . . . .
85


=== PÁG 11 del PDF ===
IX
Índice de tablas
Pág.
2.1
Valores representativos de conductividad hidráulica saturada (Ks) según la clase
textural del suelo. Fuente: Adaptado de Dingman (2015) con base en datos de
Clapp y Hornberger (1978). . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
3.1
Métricas morfométricas y topográficas de las cuencas de estudio. Fuente: Ela-
boración propia a partir de DEM ALOS PALSAR. . . . . . . . . . . . . . . . .
28
3.2
Métricas morfológicas de los cauces principales. . . . . . . . . . . . . . . . . .
28
3.3
Distribución de uso de suelo y área para las cuencas Chagres, Robles y Damas.
Fuente: Elaboración propia a partir de Infraestructura de Datos Espaciales (IDE)
de Chile. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
3.4
Propiedades del suelo y conductividad hidráulica (Ks) por profundidad para las
cuencas Robles, Chagres y Damas. Fuente: Elaboración propia a partir de datos
de Dinamarca et al. (2023). . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
3.5
Comparación de la conductividad hidráulica mínima de las cuencas con los cri-
terios del Grupo Hidrológico de Suelo (HSG) tipo C. Fuente: Elaboración propia. 32
3.6
Estadísticas de registros de caudal para las cuencas Damas, Chagres y Robles.
Fuente: Elaboración propia. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
3.7
Ecuaciones de las curvas de descarga y coeficientes de determinación (R2) para
las cuencas Damas, Chagres y Robles. Fuente: Elaboración propia. . . . . . . .
33
3.8
Estadísticas y registros de precipitación para las cuencas Damas, Chagres y Ro-
bles. Fuente: Elaboración propia. . . . . . . . . . . . . . . . . . . . . . . . . .
36
3.9
Parámetros de calibración utilizados en la herramienta HydRun para la extrac-
ción de eventos en las cuencas de estudio. Fuente: Elaboración propia. . . . . .
38


=== PÁG 12 del PDF ===
3.10 Caracterización de las variables predictoras para cada evento. Fuente: Elabora-
ción propia en base a métricas utilizadas por Ross et al. (2021). . . . . . . . . .
39
3.11 Métricas hidrológicas (variables de respuesta) extraídas para caracterizar el com-
portamiento de la cuenca en cada evento. Fuente: Elaboración propia.
. . . . .
39
3.12 Métricas de humedad antecedente del suelo y precipitación combinada. Fuente:
Elaboración propia. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
3.13 Descripción de los parámetros del modelo lineal y segmentado para el cálculo
del AICc. Fuente: Elaboración propia. . . . . . . . . . . . . . . . . . . . . . .
41
3.14 Variables predictoras estáticas utilizadas en el análisis de correlación.
. . . . .
42
4.1
Estadísticas descriptivas de los eventos de precipitación y la escorrentía generada
por cuenca. Fuente: Elaboración propia. . . . . . . . . . . . . . . . . . . . . .
44
4.2
Precipitación antecedente (PA) promedio acumulada para distintas ventanas
temporales previas a los eventos. Fuente: Elaboración propia. . . . . . . . . . .
44
4.3
Estadísticas de caudales absolutos: máximo, caudal base y caudal directo por
evento. Fuente: Elaboración propia.
. . . . . . . . . . . . . . . . . . . . . . .
45
4.4
Estadísticas de caudales específicos (normalizados por área) y coeficiente de
escorrentía. Fuente: Elaboración propia. . . . . . . . . . . . . . . . . . . . . .
45
4.5
Comparativa de los índices IV R y constante de recesión K por evento y cuenca.
Fuente: Elaboración propia. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
4.6
Resultados de métricas estadísticas (R2
Adj, BP y BP 95 %) para las trece variables
predictoras por cuenca. N.A indica que el modelo no convergió. Fuente: Elabo-
ración propia. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
51
4.7
Evaluación de pendientes y validación de umbrales para las variables predictoras
con R2
adj > 0, 45 por cuenca. Fuente: Elaboración propia. . . . . . . . . . . . .
52
I.1
Estadísticas de parámetros de suelo por capa y cuenca. Fuente: Elaboración pro-
pia a partir de datos de Dinamarca et al. (2023). . . . . . . . . . . . . . . . . .
76
I.2
Porcentaje de textura de suelo y conductividad hidráulica promedio Ks para
cada cuenca y profundidad específica. Fuente: Elaboración propia a partir de
datos Dinamarca et al. (2023).
. . . . . . . . . . . . . . . . . . . . . . . . . .
82


=== PÁG 13 del PDF ===
CAPÍTULO 1. INTRODUCCIÓN
1
Capítulo 1
Introducción
1.1.
Contexto Teórico
La alta heterogeneidad en las propiedades de las cuencas, tales como las topográficas y de
suelo, provocan un comportamiento no lineal en la generación de escorrentía como respuesta a
los eventos de precipitación (Zehe and Sivapalan, 2009). Esto implica que la homogenización de
estas características ignora información crítica asociada a los comportamientos emergentes a es-
cala (McDonnell et al., 2021). Omitir esta variabilidad conduce a una conceptualización errónea
sobre el funcionamiento del sistema. Según Beven (2011), cada cuenca posee particularidades
producto de su heterogeneidad, por lo tanto, la aplicación directa de métodos generalizados para
describir procesos hidrológicos puede generar resultados erróneos, especialmente en la genera-
ción de escorrentía, donde las propiedades del suelo son variables. Además, la dependencia de
los mecanismos respecto a la escala determina que no sea posible extrapolar directamente la
información local a zonas de mayor extensión (Ali et al., 2013).
El análisis de eventos a escala lluvia-escorrentía es un método validado y frecuentemente
usado para evaluar el comportamiento hidrológico frente a las entradas meteorológicas (Rodríguez-
Blanco et al., 2012). Las series temporales de salida contienen implícitamente la física de la cuen-
ca (Blume et al., 2007). Además estas series de tiempo capturan las propiedades emergentes que
se manifiestan a la escala de análisis (McDonnell et al., 2007). Por lo tanto, la evaluación de estos
datos entrega información valiosa para comprender las peculiaridades de un sistema específico.
Esta caracterización puede provenir directamente del análisis de los datos brutos, tales como las


=== PÁG 14 del PDF ===
CAPÍTULO 1. INTRODUCCIÓN
2
magnitudes de caudal y las propiedades del hidrograma, o por otro lado, mediante un análisis
acoplado. El análisis acoplado permite la evaluación entre métricas predictivas y de respuesta
abriendo la posibilidad de evaluar múltiples configuraciones para parametrizar el sistema (Ali
et al., 2013). La literatura compara frecuentemente métricas volumétricas y de almacenamiento
frente a la escorrentía del evento, por otro lado, métricas como la intensidad son menos habituales
(Ross et al., 2021).
El análisis lluvia-escorrentía y la comparación cruzada de métricas son fundamentales para
jerarquizar los controles hidrológicos y determinar su grado de influencia en la generación de
escorrentía (Merz and Blöschl, 2009). Esta categorización facilita la identificación de aquellas
variables que no gobiernan el proceso, permitiendo aislar los resultados útiles reales frente al
ruido del sistema.
Por lo tanto, es ideal transitar desde supuestos basados en generalizaciones hacia un análisis
que aborde la complejidad individual del sistema, utilizando registros de terreno que contengan
la firma hidrológica local (Beven, 2000). Una de las propiedades emergentes más documentadas
bajo este enfoque corresponde a los umbrales de generación de escorrentía (McDonnell et al.,
2021). Estos representan momentos críticos donde el sistema experimenta un cambio abrupto y
no lineal en la producción de escorrentía como respuesta a métricas de entradas meteorológicas
(Spence, 2010; Ali et al., 2013). La aplicación de este esquema sobre diferentes métricas de entra-
da permite caracterizar tanto el estado de activación de la cuenca como su memoria hidrológica
a corto, mediano y largo plazo (Ross et al., 2021).
Aunque la complejidad e incertidumbre de la naturaleza limita la obtención de umbrales
exactos, la identificación de estos y de varios tipos, a pesar de no ser perfectos, proporciona una
mejor comprensión sobre las tendencias de comportamiento de la cuencas (Beven, 2000).


=== PÁG 15 del PDF ===
CAPÍTULO 1. INTRODUCCIÓN
3
1.2.
Contexto de la Zona
Existe un análisis extensivo de eventos y umbrales en cuencas mediterráneas (Rodríguez-
Blanco et al., 2012; Nanda and Safeeq, 2023) y con suelos agrícolas (Vreugdenhil et al., 2022;
Han et al., 2012; Saffarpour et al., 2016) a nivel internacional, sin embargo, la mayoría de los
estudios en Chile se enfocan en las cuencas forestales de la zona sur del país (Iroumé et al.,
2021; Rivera et al., 2021; Little et al., 2009; Iroumé et al., 2006). Específicamente en la Región
del Maule, los estudios orientados a cuencas mediterráneas suelen limitarse a escalas temporales
diarias, modelación hidrológica o desarrollo de curvas IDF (Pizarro-Tapia et al., 2014; Pizarro
et al., 2009; Pizarro T. et al., 2005). Esta resolución temporal es insuficiente para capturar los
detalles que suceden rápidamente y caracterizan de los procesos de generación de escorrentía,
tendiendo a promediar estos procesos que operan a escala subhoraria.
La extracción y procesamiento de series temporales de alta resolución en cuencas medite-
rráneas y agrícolas de esta región representa un vacío importante en la literatura de la zona. Por
lo tanto, profundizar en esa temática genera una oportunidad para examinar los mecanismos hi-
drológicos de la cuenca, permitiendo observar dinámicas complejas como la dependencia de la
humedad antecedente, los procesos de conectividad del flujo y la eficiencia de las métricas hidro-
lógicas. Esto es de especial relevancia considerando el actual escenario climático que afecta a la
zona central de Chile, el cual altera las condiciones hídricas previas a los eventos de precipitación
(Alvarez-Garreton et al., 2021; Garreaud et al., 2020).


=== PÁG 16 del PDF ===
CAPÍTULO 1. INTRODUCCIÓN
4
1.3.
Objetivo General
Caracterizar los procesos de activación hidrológica y los umbrales de escorrentía en tres
cuencas mediterráneas de la Región del Maule, utilizando series temporales de alta resolución
para comprender la influencia de las condiciones antecedentes, la no linealidad en la generación
de escorrentía y los mecanismos internos que provocan la activación.
1.4.
Objetivos Específicos
1. Caracterizar los eventos de lluvia-escorrentía en las cuencas de estudio provenientes de
las series temporales de alta resolución.
2. Cuantificar la magnitud de escorrentía directa mediante la separación del flujo base obte-
niendo métricas hidrológicas para cada evento.
3. Identificar la existencia de umbrales hidrológicos no lineales mediante algoritmos de re-
gresión segmentada y criterios de información (AICc), evaluando el rol de la humedad del
suelo antecedente y la precipitación en la activación de la cuenca.
4. Relacionar las características estáticas de las cuencas con las métricas de respuesta diná-
micas para determinar la influencia de estas sobre la generación de escorrentía.


=== PÁG 17 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
5
Capítulo 2
Marco Teórico
2.1.
Procesos Atmosféricos
2.1.1.
Circulación Atmosférica
La tierra recibe constantemente calor desde el sol a través de radiación solar y emite una parte
de este calor al espacio a través de radiación. El calentamiento de la tierra no es homogéneo, el
ecuador recibe más radiación que los polos, por lo que la atmosfera funciona como un motor que
transfiere energía entre estas secciones de la tierra (Chow et al., 1994).
El patrón de circulación atmosférica se muestra en la Figura 2.1. De acuerdo con Chow et al.
(1994) este patrón se divide en tres celdas convectivas principales por hemisferio (tropical, media
y polar) debido a la rotación de la Tierra, la cual desvía los vientos mediante el efecto Coriolis.
En este sistema, las diferencias térmicas y de presión movilizan masas de aire que actúan como
reservas de humedad.
El desplazamiento de estas masas genera zonas de convergencia y de baja presión. Cuando
masas de aire con distintas temperaturas colisionan, forman límites llamados frentes. La interac-
ción de estos frentes y de los sistemas de baja presión fuerza físicamente al aire a ascender hacia
capas superiores de la troposfera. Al elevarse, la presión disminuye, lo que provoca que el aire
se expanda y se enfríe, provocando que el vapor de agua se condense.


=== PÁG 18 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
6
Figura 2.1: Diagrama latitudinal de circulación atmosférica general. Fuente: Extraido de Chow
et al. (1994).
2.1.2.
Generación de Precipitación
La precipitación considera todos los procesos mediante los cuales el agua cae a la superficie
terrestre, incluyendo lluvia, nieve, granizo y aguanieve. Su formación requiere el ascenso de una
masa de aire en la atmósfera, lo que provoca su enfriamiento y la condensación de su humedad
Existen tres mecanismos principales que impulsan este ascenso, entre ellos el levantamiento
frontal, donde el aire cálido es empujado por encima del aire más frío al paso de un frente, el
levantamiento orográfico, en el cual una masa de aire se ve forzada a elevarse para sobrepasar
una cadena montañosa y el levantamiento convectivo, donde el aire es arrastrado hacia arriba
por acción convectiva. Las celdas convectivas son iniciadas por el calentamiento de la superficie
terrestre, lo que genera inestabilidad vertical en el aire húmedo, y son sostenidas por el calor
latente de vaporización liberado a medida que el vapor de agua asciende y se condensa.
Como se visualiza en la Figura 2.2, a medida que el aire asciende y se enfría, el agua pasa del
estado gaseoso al líquido. Este proceso de condensación requiere una zona alrededor del cual las
moléculas de agua puedan adherirse o nuclearse. Estas partículas microscópicas, conocidas como
aerosoles, incluyen polvo, sales derivadas de la evaporación marina y compuestos de azufre y
nitrógeno resultantes de la combustión.
Las gotas pequeñas crecen por condensación e impacto con las gotas vecinas mientras son


=== PÁG 19 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
7
transportadas por las corrientes de aire turbulento. Al alcanzar un tamaño suficiente, la fuerza de
gravedad supera la fricción y comienzan a caer, incrementando su masa al colisionar con otras
gotas durante la trayectoria. Sin embargo, durante la caída, parte del agua se evapora, reduciendo
su tamaño, por lo que puede volver a ser arrastrada hacia arriba por la acción de la nube. Este
ciclo de condensación, caída, evaporación y ascenso ocurre en promedio unas diez veces antes
de que la gota alcance un tamaño crítico de aproximadamente 0.1 mm, suficiente para atravesar
la base de la nube. Las gotas de lluvia normales miden entre 0.1 y 3 mm de diámetro, al superar
este tamaño se aplanan en su base, se vuelven inestables y se fragmentan en gotas más pequeñas.
El agua en las nubes puede existir en estado líquido subenfriado hasta los -35°C, temperatura
a la cual las gotas se congelan incluso sin núcleos de congelación. A estas temperaturas, la presión
de vapor de saturación es menor sobre el hielo que sobre el agua líquida. En consecuencia, si
se mezclan partículas de hielo con gotas subenfriadas, el hielo crece por la evaporación de las
gotas y la posterior condensación sobre los cristales de hielo. Estos cristales suelen agruparse por
colisión y coalescencia para caer como copos de nieve, o crecer individualmente lo suficiente
como para precipitar directamente a la tierra en forma de granizo o aguanieve (Chow et al., 1994).
Figura 2.2: Diagrama de formación de precipitación. Fuente: Extraido de Chow et al. (1994).


=== PÁG 20 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
8
2.2.
Procesos de Superficie y Subsuperficie
2.2.1.
Propiedades del Suelo
2.2.1.1.
Textura del Suelo
El suelo actúa como un sistema poroso donde su capacidad para almacenar y transmitir agua
depende de su distribución de tamaño de poros. De acuerdo con Dingman (2015), la geometría
de vacíos depende de la distribución granulométrica de las partículas, lo que define la textura
del suelo. Siguiendo el sistema de clasificación del Departamento de Agricultura de los Estados
Unidos (Dingman, 2015; Soil Science Division Staff, 2017), los suelos se categorizan según su
proporción másica de arcilla (d < 0,002 mm), limo (0,002 ≤d < 0,05 mm) y arena (0,05 ≤
d < 2 mm). La la proporción de limo, arenas y arcilla y la categorización de la textura del suelo
se resumen en la pirámide de texturas de suelo en la Figura 2.3.
Figura 2.3: Pirámide de texturas de suelo aplicado a suelos con varias fracciones de arena, limo
y arcilla. Fuente: Extraido de Dingman (2015).


=== PÁG 21 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
9
2.2.1.2.
Conductividad Hidráulica
La textura y la distribución del tamaño de poros determinan el valor de la conductividad hi-
dráulica saturada (Ks). Esta variable mide la facilidad con la que el medio poroso permite el flujo
de agua. Suelos con texturas gruesas, como arenas, presentan macroporos asociados a una alta
Ks, favoreciendo la infiltración rápida. Por el contrario, suelos finos, como las arcillas, poseen
una baja Ks, aumentando la capacidad de generar escorrentía superficial por flujo Hortoniano
(Dingman, 2015). Valores representativos de Ks se muestran en la Tabla 2.1.
Tabla 2.1: Valores representativos de conductividad hidráulica saturada (Ks) según la clase tex-
tural del suelo. Fuente: Adaptado de Dingman (2015) con base en datos de Clapp y Hornberger
(1978).
Categoría de Suelo
Ks (cm/s)
Arena
1,76 × 10−2
Arena franca
1,56 × 10−2
Franco arenoso
3,47 × 10−3
Franco limoso
7,20 × 10−4
Franco
6,95 × 10−4
Franco arcillo-arenoso
6,30 × 10−4
Franco arcilloso
2,45 × 10−4
Arcillo-arenoso
2,17 × 10−4
Franco arcillo-limoso
1,70 × 10−4
Arcilla
1,28 × 10−4
Arcillo-limoso
1,03 × 10−4
La medición directa de la Ks a escala de cuenca suele ser inviable, por lo que se utilizan
funciones de pedotransferencia (PTF). De acuerdo con Dingman (2015), las PTF son modelos
empíricos que estiman parámetros hidráulicos complejos a partir de propiedades del suelo dispo-
nibles en bases de datos espaciales, como la distribución granulométrica (porcentajes de arena,
limo y arcilla) y la densidad aparente. El uso de PTFs permite generar grillas continuas de Ks
que definen las propiedades del suelo en la cuenca.


=== PÁG 22 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
10
2.2.1.3.
Capacidad de Almacenamiento de Humedad
Además de la capacidad de transmisión de flujo, representada por la conductividad hidráulica
Ks, el suelo funciona como un reservorio que retiene agua contra la fuerza de gravedad debido
a las fuerzas de succión capilar y matricial. Estos límites de almacenamiento se definen con
términos estáticos de estados de humedad (Dingman, 2015).
La capacidad de campo (FC) es uno de los términos de capacidad de almacenamiento de
humedad y representa el contenido de agua que el suelo puede retener tras haber sido saturado
y haber drenado por gravedad. El punto de marchitez permanente (PWP) corresponde al límite
inferior de humedad práctica, donde el agua remanente está retenida por tensiones matriciales
que resulta inaccesible para la extracción radicular de la vegetación. Por su parte, la capacidad
de agua disponible (AWC) es la diferencia entre la capacidad de campo y el punto de marchitez
permanente (FC −PWP) y representa el volumen máximo de agua dinámicamente activa que
el perfil del suelo puede almacenar.
2.2.2.
Infiltración
La infiltración es el proceso físico en el cual el agua proveniente de la precipitación ingresa
al suelo a través de su superficie. Este movimiento vertical descendente depende de las fuerzas
de gravedad y el gradiente de presión matricial o succión capilar en la ecuación de Richards.
De acuerdo con Dingman (2015), cuando el agua ingresa a un suelo seco al inicio de un even-
to de lluvia, el gradiente de presión en la superficie es significativamente mayor que el gradiente
gravitacional, resultando en tasas de infiltración iniciales elevadas. A medida que el evento con-
tinúa y el contenido de humedad superficial aumenta, las fuerzas de succión capilar disminuyen
drásticamente. Esto provoca que la tasa de infiltración decaigan a lo largo del tiempo hasta al-
canzar un valor constante, el cual depende solo de la gravedad y equivale a la conductividad
hidráulica (Ks).
2.2.3.
Escorrentía Superficial
La escorrentía superficial ocurre cuando la lluvia se acumula sobre una superficie inclinada
y comienza a fluir hacia los cauces. Este proceso comienza cuando la capa superficial del suelo


=== PÁG 23 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
11
se satura. Existen dos mecanismos principales mediante los cuales ocurre esta saturación, por
exceso de infiltración y exceso de saturación (Dingman, 2015).
Antes que el agua fluya libremente por la superficie, este debe superar el almacenamiento
en depresiones. Las superficies topográficas presentan micro relieves donde el agua se acumula
inicialmente. Durante un evento de precipitación, estas depresiones se llenan, se desbordan y
se fusionan. Este proceso retrasa el inicio de la escorrentía y reduce su volumen total, ya que
proporciona mayor tiempo para que el agua acumulada se infiltre o se evapore.
2.2.3.1.
Flujo Hortoniano
El flujo superficial por exceso de infiltración, o flujo Hortoniano, se genera cuando la in-
tensidad (i) asociada al evento de precipitación P, supera la capacidad de infiltración del suelo
(f), generando un exceso de escorrentía q0 que se distribuye al cauce (Figura 2.4). La tasa de
infiltración disminuye exponencialmente en el tiempo a medida que el suelo se satura. El proceso
se describe por la ecuación empírica de Horton:
f(t) = fc + (f0 −fc)e−kt
(2.1)
donde f0 es la tasa de infiltración inicial, fc es la capacidad de infiltración de equilibrio y k
es la constante de decaimiento temporal (Chow et al., 1994).
Este mecanismo es dominante en regiones áridas y semiáridas, donde las lluvias suelen ser
intensas y la conductividad superficial es baja debido a la escasa vegetación. También es el pro-
ceso principal en áreas urbanas o impermeables, y en zonas donde la actividad humana o el
congelamiento han compactado el suelo. Sin embargo, este tipo de mecanismo rara vez sucede
de manera independiente y en la cuenca en su totalidad, ya que depende de la complejidad del
suelo y la topografía (Dingman, 2015).


=== PÁG 24 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
12
Figura 2.4: Proceso de Flujo Hortoniano. Fuente: Extraido de Beven (2011).
2.2.3.2.
Flujo por Exceso de Saturación
El flujo por exceso de saturación ocurre cuando el nivel freático asciende hasta la superfi-
cie, impidiendo cualquier infiltración adicional. Este ascenso suele estar condicionado por un
nivel freático superficial preexistente, una capa impermeable poco profunda, o una disminución
repentina de la conductividad hidráulica con la profundidad (Dunne and Black, 1970).
Como se visualiza en la Figura 2.5, cuando el nivel freático sube hasta la superficie se genera
escorrentía producto del aumento de qr de manera independiente a la escorrentía proveniente del
exceso de infiltraación q0. Por otro lado, una porción del nivel freático qs ingresa al cauce desde
la subsuperficie.
Las áreas que generan escorrentía no son estáticas, ya que la extensión de las zonas saturadas
cambia significativamente con el tiempo, expandiéndose durante las tormentas y contrayéndose
en periodos secos (Dunne and Black, 1970). La propensión de un área específica a saturarse desde
la zona baja depende de la topografía local, áreas que convergen el flujo subsuperficial y presen-
tan índices topográficos altos son las más propensas a generar escorrentía por este mecanismo
(Dingman, 2015).


=== PÁG 25 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
13
Figura 2.5: Proceso de Flujo por Exceso de Saturación. Fuente: Extraido de Beven (2011).
2.2.4.
Escorrentía Subsuperficial
La escorrentía subsuperficial, también conocida como flujo subsuperficial, consiste en el
movimiento lateral del agua a través del perfil del suelo hacia el cauce del río qs, sin llegar a
emerger a la superficie (Hewlett and Hibbert, 1967). La respuesta rápida del cauce producto de
este proceso, sin necesidad de escorrentía superficial, es por el desplazamiento del agua subsu-
perficial. Como se muestra en la Figura 2.6, cuando el agua de una nueva tormenta se infiltra,
una fracción contribuye al almacenamiento temporal del suelo, mientras que otra fracción ejerce
presión y desplaza el agua previa al evento almacenada en la ladera. Esta agua pre-evento es
liberada en grandes cantidades hacia el canal una vez que el suelo alcanza o supera su capacidad
de campo.
La velocidad de este flujo depende de la estructura topográfica y profundidad. El agua puede
moverse lentamente o desplazarse de forma rápida mediante rutas preferenciales y macroporos
(Dingman, 2015).


=== PÁG 26 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
14
Figura 2.6: Proceso de Flujo Subsuperficial. Fuente: Extraido de Beven (2011).


=== PÁG 27 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
15
2.3.
Conectividad Hidrológica
2.3.1.
Hipótesis Llenado y Derrame (Fill and Spill)
El concepto de llenado y derrame (fill and spill) proporciona un marco conceptual para agru-
par los procesos de generación de escorrentía a escala de evento (McDonnell et al., 2021). Esta
hipótesis plantea que las entradas verticales y laterales en una unidad de análisis a una escala
específica; ya sea escala de poros, ladera o cuenca; se deben almacenar y solo cuando este al-
macenamiento Si alcanza un nivel crítico S∗
i se activa una vía de flujo de salida previamente
inactiva. En la Figura 2.7 se puede visualizar que, para una escala x, solo si el almacenamien-
to Si(x) supera el almacenamiento crítico Si(x)∗, este generará escorrentía qi(x) producto del
desbordamiento (Ecuación 2.2). Este flujo qi(x) depende de la cantidad del almacenamiento por
sobre el límite Si(x)∗durante un periodo de tiempo T y modulado por una función fi(x). Por
otro lado, de ser Si(x) menor a Si(x)∗, la escorrentía será 0 (Ecuación 2.3).
Figura 2.7: Esquema conceptual del mecanismo de Llenado y Derrame. Fuente: Extraido de
McDonnell et al. (2021).
Si Si(x) > S∗
i(x) entonces qi(x) = 1
T
∫T
0
fi(x)
(
Si(x) −S∗
i(x), . . .
)
dt
(2.2)
Si Si(x) ≤S∗
i(x) entonces qi(x) = 0
(2.3)


=== PÁG 28 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
16
Este enfoque no reemplaza las ecuaciones físicas de flujo, sino que aborda el problema de
la heterogeneidad espacial, teorizando que la respuesta a macroescala depende de la superación
de umbrales a microescala (Figura 2.8).
Figura 2.8: Proceso de llenado y derrame a diferentes escalas. Se visualiza que la activación de
un umbral a miscroescala (Escala x=1) no garantiza la activación de umbrales a escalas mayores
(Escala x=2 y x=3). Fuente: Extraido de McDonnell et al. (2021).
La existencia de otros procesos físicos se describen en la Ecuación 2.4, en donde el cambio
del almacenamiento Si(x) en el tiempo t, no solo depende de la salida de flujo qi(x) asociado a
la activación de una vía preferencial, si no que mecanismos paralelos pueden aumentar (Ii(x)) o
disminuir (Li(x)) el almacenamiento.
dSi(x)
dt
= Ii(x) −qi(x) −Li(x)
(2.4)
El esquema de llenado y derrame explica cómo los mecanismos teóricos de generación de
escorrentía interactúan en una zona espacialmente heterogénea. Por ejemplo, para el flujo Hor-
toniano, el agua no infiltrada interactúa dentro de una dinámica de “charco a charco”, producto
de las depresiones del relieve superficial, lo cual retrasa el flujo continuo hasta superar el al-
macenamiento en estas depresiones. Por otra parte, para el flujo por exceso de saturación y el
flujo subsuperficial, la topografía del lecho rocoso, los horizontes del suelo y los cambios en
la conductividad hidráulica actúan como reservorios que exigen una conectividad hidrológica


=== PÁG 29 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
17
completa antes de contribuir significativamente al caudal de salida.
2.3.2.
Umbrales Hidrológicos
La activación no lineal del mecanismo de llenado y derrame se expresa en propiedades
emergentes conocidas como umbrales hidrológicos, los cuales representan los momentos críti-
cos donde el comportamiento de la escorrentía cambia significativamente. Para identificar estos
momentos de cambio, se evalúan las relaciones entre métricas de respuesta hidrológica y métri-
cas predictoras. Las métricas predictoras establecidas por Ross et al. (2021) están vinculadas a
la precipitación y a su intensidad.
Las métricas de precipitación se dividen entre la cantidad que cae durante un evento especí-
fico y la que se acumula en el sistema previamente. La métrica principal dentro de esta categoría
es la precipitación total del evento (PTOT), la cual mide la cantidad de lluvia registrada durante
un evento lluvia-escorrentía específico; mientras que las métricas acumuladas corresponden a la
suma de la precipitación durante una ventana de tiempo específica x (PAx), así como a la suma
de la precipitación total y la antecedente (PTOT + PAx). Por su parte, las métricas de intensidad
están relacionadas con la máxima intensidad durante el evento de precipitación para una ventana
móvil de tiempo x (Imax(x)).
Además de las métricas meteorológicas, otra categoría de métrica predictora está asociada a
la humedad antecedente presente en las capas del suelo antes del evento de precipitación (ASM,
por sus siglas en inglés) a una profundidad específica. Este tipo de predictor ha sido utilizado,
por ejemplo, en el trabajo de Nanda and Safeeq (2023).
Las métricas de respuesta hidrológica evaluadas en relación con estos predictores se catego-
rizan en métricas de magnitud y métricas de tiempo (Ross et al., 2021). Las métricas de magnitud
miden el volumen generado, incluyendo la escorrentía total del evento (RTOT), el caudal máximo
(Qmax), el coeficiente de escorrentía (RC) y la abstracción inicial (Ia). Por otro lado, las métricas
de tiempo caracterizan la velocidad del movimiento del agua a través del sistema, abarcando el
tiempo de respuesta o rezago (Lag) y el tiempo de concentración (Tc).


=== PÁG 30 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
18
2.3.3.
Tipos de Umbrales
De acuerdo con Ali et al. (2013), en la literatura hidrológica se identifican cuatro tipos de
respuestas no lineales asociadas a la activación de umbrales. El modelo más frecuente se asimila
a la forma de un “palo de hockey”, descrito como una función lineal por tramos. Este sistema
exhibe una respuesta nula hasta que el almacenamiento de la cuenca supera un límite crítico. Una
vez sobrepasado este umbral de activación, la magnitud de la escorrentía aumenta de manera
proporcional. También existen casos donde la zona anterior al umbral presenta pendientes no
nulas (m1 > 0) (Ross et al., 2021).
El comportamiento de la cuenca puede caracterizarse mediante otros modelos (Figura 2.9).
Entre estos se incluyen umbrales de función escalón, que representan una activación repentina y
constante de una vía de flujo; funciones de impulso de Dirac, asociadas a respuestas instantáneas
y de corta duración; y funciones sigmoides, que modelan una transición gradual hacia la gene-
ración de escorrentía, alcanzando un límite asintótico debido a la saturación total del sistema.
Figura 2.9: Esquemas conceptuales de relaciones no lineales lluvia-escorrentía reportados fre-
cuentemente en la literatura. Fuente: Adaptado de Ali et al., 2013.


=== PÁG 31 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
19
2.3.4.
Identificación de Umbrales
Tradicionalmente, la presencia de umbrales hidrológicos en el análisis a nivel de eventos se
evaluaba de forma empírica mediante la inspección visual de gráficos de dispersión (Tromp-van
Meerveld and McDonnell, 2006; Detty and McGuire, 2010a). Para solucionar la subjetividad
de este enfoque y determinar con precisión el punto exacto en el que las variables predictoras
activan un cambio no lineal en la respuesta de la cuenca se ha propuesto el análisis de regresión
segmentada, como el algoritmo propuesto por Muggeo (2003).
Este enfoque analítico trata el punto de quiebre como un parámetro adicional a estimar. Para
lograrlo, utiliza una expansión de Taylor de primer orden que transforma un problema matemáti-
camente no lineal y no diferenciable en un proceso iterativo que ajusta modelos lineales estándar.
La ventaja de este método radica en que, además de calcular el valor del umbral, permite obtener
de forma directa los errores estándar y establecer los intervalos de confianza asociados al punto
de cambio.
2.3.5.
Criterios para la aceptación de umbrales
La identificación matemática de un punto de quiebre no garantiza, por sí sola, que este re-
presente una característica hidrológica del sistema, por lo que es necesario aplicar criterios de
bondad de ajuste y parsimonia para distinguir el comportamiento hidrológico de ruido prove-
niente de los datos de entrada.
Se han propuesto métricas cuantitativas para validar la robustez de estos umbrales. Por ejem-
plo Ross et al. (2021) sugiere el uso del coeficiente de determinación (R2) derivado de modelos
segmentados como el algoritmo de Muggeo (2003), estableciendo empíricamente valores de has-
ta 0,45 para considerar el ajuste como aceptable en respuestas a nivel de cuenca.
Para evitar el sobreajuste, se evalúa la parsimonia del modelo empleando el Criterio de In-
formación de Akaike corregido para muestras pequeñas (AICc) de Hurvich and Tsai (1989),
siendo este una modificación del AIC de Akaike (1974). La ecuación del AICc se describe en
la Ecuación 2.5. Los términos k y n representan el número de parámetros en el modelo y el nú-
mero de muestras, respectivamente, mientras que RSS es la suma de cuadrados residuales. Este
último representa la sumatoria de las diferencias al cuadrado entre los valores observados (yi) y


=== PÁG 32 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
20
los valores predichos por la regresión (ˆyi), como se muestra en la Ecuación 2.6.
AICc = n ln
(RSS
n
)
+ 2k + 2k(k + 1)
n −k −1
(2.5)
RSS =
n
∑
i=1
(yi −ˆyi)2
(2.6)
Se busca comparar la complejidad del modelo segmentado frente a su contraparte lineal
simple requiriendo que AICc,segmentado sea menor que AICc,lineal. Para el estudio de activación
de cuencas de Ross et al. (2021), se estableció que la diferencia entre ambos modelos en la
Ecuación 2.7 debe ser superior a dos unidades para justificar el aumento de complejidad que
implica añadir un punto de cambio, respaldando este valor en base a los ejemplos de Sakamoto
et al. (1986).
∆AICc = AICc,lineal −AICc,segmentado
(2.7)
Finalmente se evalúan las pendientes de los segmentos pre-umbral (m1) y post-umbral (m2).
Los criterios exigen que la tasa de respuesta post-umbral sea positiva y supere a la inicial en un
margen significativo, por ejemplo 10 % según Ross et al. (2021), para confirmar que efectiva-
mente se ha superado el umbral y activado nuevos mecanismos de escorrentía en la cuenca.
2.4.
Fluviometría
La fluviometría es la rama de la hidrología dedicada a la acción de medir los caudales que
fluyen sobre un cauce en una sección específica de este (Stowhas B., 2016). De no contar con
monitoreo continuo por una agencia nacional en la sección de interés del cauce, los datos del
nivel del agua (h) y de caudal (Q) se deben obtener mediante un posprocesamiento de los datos
brutos provenientes de un sensor sumergido. Los sensores entregan la presión total Psumergido
que incluyen los valores de la presión atmosférica Patmosfrica más la columna de agua Pcolumna,
por lo que es necesario restar los valores asociados a la atmosférica (Ecuación 2.8).
Pcolumna = Psumergido −Patmosfrica
(2.8)


=== PÁG 33 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
21
El nivel del agua h se obtiene convirtiendo la presión a unidades de largo (Ecuación 2.9).
h = Psumergido −Patmosfrica
ρg
(2.9)
Para transformar la altura h a caudal Q es necesario una relación que asocie ambas variables.
En secciones naturales se deben realizar aforos mediante mediciones sucesivas e independientes
del nivel del agua h y caudal Q durante un mismo periodo. Para la obtención de Q se debe utilizar
un instrumento de medición hidrométrico tal como un correntómetro, midiendo la velocidad en
intervalos igualmente espaciados de la sección del cauce. Los valores de velocidad y su área
asociada se multiplican para obtener el valor de caudal. Mientras que para la medición de h se
utiliza un regla limnimétrica. Luego de registrar un conjunto de datos representativos, es posible
ajustar una curva de descarga, siendo esta una función potencia simple (Ecuación 2.10) con
coeficientes a y b que deben ajustarse.
Q = a(H)b
(2.10)
2.5.
Separación de eventos
Para evaluar e identificar los umbrales hidrológicos se deben aislar las respuestas directas
que produce la cuenca ante los eventos de precipitación. Para ello es necesario separar el flujo
base de los eventos de crecida que generan escorrentía directa. Este proceso se realizaba tradi-
cionalmente mediante métodos gráficos, principalmente el de la línea recta (Stowhas B., 2016).
La calibración de este tipo de métodos incluye una alta subjetividad y sesgo, además, su aplica-
ción no es eficiente para series de datos de gran tamaño. Para superar estas limitaciones, en la
separación de eventos moderna se utilizan algoritmos automatizados con filtros numéricos (Tang
and Carey, 2017).
2.5.1.
Separación del flujo base
La automatización de este proceso mediante filtros numéricos implica tratar la serie de caudal
como una señal continua compuesta por distintas frecuencias en el dominio del tiempo. En base


=== PÁG 34 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
22
a Lyne and Hollick (1979), la escorrentía directa (Qd,t) representa la señal de alta frecuencia,
ya que responde rápidamente a los eventos de precipitación y muestra una alta variabilidad en
intervalos de tiempo cortos. Por el contrario, el flujo base (Qb,t) se comporta como una señal de
baja frecuencia, caracterizada por una respuesta lenta, suave y estable a largo plazo.
La Ecuación 2.11 describe el filtro digital recursivo de Lyne and Hollick (1979). En ella se
observa que la escorrentía directa en el instante actual (Qd,t) depende del caudal total observado
(Qt) y de las condiciones en el paso de tiempo anterior (Qt−1 y Qd,t−1). El término de la dife-
rencia (Qt −Qt−1) permite calcular la tasa de cambio en el hidrograma. Un valor alto implica
un aumento significativo del caudal producto de la lluvia, lo que significa una mayor contribu-
ción de escorrentía directa. Por el contrario, un valor cercano a cero o negativo indica el cese de
la precipitación y el inicio de la recesión del sistema. Por su parte, el parámetro α es un factor
de calibración que representa la amortiguación del aumento de la escorrentía directa. Una vez
obtenida la escorrentía directa (Qd,t), es posible calcular el flujo base mediante la Ecuación 2.12.
Qd,t = αQd,t−1 + 1 + α
2
(Qt −Qt−1)
(2.11)
Qb,t = Qt −Qd,t
(2.12)
Para que el algoritmo presente consistencia física, se imponen restricciones al flujo base Qb,t.
Este no puede ser cero ni tampoco mayor a Qt.
Los filtros recursivos aplicados unidireccionalmente introducen un desfase temporal en los
resultados de la señal (Nathan and McMahon, 1990). Para corregir este error, el filtro debe eje-
cutarse en múltiples pasadas en ambas direcciones y en valores pares. Esto logra que la curva
del flujo base quede alineada con el evento meteorológico.
2.5.2.
Extracción de eventos
Como se visualiza en la Figura 2.10, en la categoría de Streamflow Data, la herramienta
HydRun, desarrollada para MATLAB por Tang and Carey (2017), implementa el filtro recursivo
descrito en la Subsección 2.5.1 para aislar el flujo base y, posteriormente, separar los eventos de
lluvia-escorrentía.


=== PÁG 35 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
23
Figura 2.10: Diagrama de funcionamiento de HydRun. Fuente: Adaptado de Tang and Carey
(2017).
Con el hidrograma de escorrentía directa ya aislado, se procede a identificar y extraer los
eventos individuales. Para definir el punto de inicio de cada hidrograma, el algoritmo detecta los
mínimos locales de la serie temporal calculando la primera derivada de la curva de caudal (Q)
con respecto al tiempo (t) e identificando los puntos donde esta se anula (Ecuación 2.13).
dQ
dt = 0
(2.13)
Para evitar la detección de falsos mínimos generados por el ruido de los instrumentos, se
aplica un filtro de media movil a la señal antes de generar el analisis. Para determinar el punto
final del evento, HydRun implementa un umbral de retorno (ReTh). Este parámetro establece
la diferencia máxima tolerable entre el caudal al inicio de la crecida y el caudal en la etapa de
recesión, permitiendo delinear el evento completo cuando se cumple esta condición.
Para filtrar las respuestas hidrológicas significativas de las pequeñas perturbaciones del sis-
tema, se aplica un umbral de caudal máximo (PKThreshold). Este parámetro permite descartar
automáticamente los eventos extraídos con una magnitud máxima no superior al límite predefini-
do. Por su parte, para determinar el punto final del evento, se utiliza un parámetro que representa


=== PÁG 36 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
24
un umbral de retorno (ReRa). Este parámetro establece la proporción máxima entre el caudal en
la zona de recesión (Qfin) y el caudal al inicio del hidrograma crecida (Qinicio), finalizando el
evento cuando se cumple la condición de la Ecuación 2.14.
Qfin
Qinicio
≤ReRa
(2.14)
Dentro de la categoría Precipitation Data, en la Figura 2.10, se identifican los eventos de
lluvia. Se debe especificar una duración máxima de periodo sin lluvia para identificar un evento
único. Tras esto, es necesario asociar cada evento de lluvia con su respectivo evento de esco-
rrentía, para ello, el algoritmo aplica una ventana de búsqueda asociado a un valor de horas (n)
predefinido antes del inicio de la crecida.
Con los eventos de lluvia-escorrentía ya identificados y emparejados, los módulos de pos-
procesamiento se encargan de calcular métricas hidrológicas y meteorológicas de interés. Como
se visualiza en la Figura 2.10, el software determina métricas temporales tanto del hidrograma
como del hietograma, tales como la duración de la lluvia (Tw), la duración de la crecida (D), el
retardo de respuesta (Lag), el tiempo de incremento hasta el pico (Tr) y el tiempo de concen-
tración (Tc). Además, calcula diversos retardos asociados a los centroides en la distribución de
parámetros del tiempo (TLP, TLPC, TLC).
Ademas de las métricas temporales, la librería calcula métricas de magnitud y volumen,
incluyendo la precipitación total del evento (PTOT), la escorrentía total (RTOT) y el coeficiente
de escorrentía (RC). La escorrentía total se calcula integrando el caudal directo (Qd) generado
durante la crecida, desde su inicio (tinicio) hasta el final del evento (tfin), y normalizando este
volumen por el área de la cuenca (A), tal como se muestra en la Ecuación 2.15.
RTOT =
∫tfin
tinicio
Qd(t) dt
A
(2.15)
Por su parte, el coeficiente de escorrentía evalúa la eficiencia de la cuenca, calculándose
como la proporción directa entre la escorrentía total y la precipitación total del evento (Ecua-
ción 2.16).
Rc = RTOT
PTOT
(2.16)


=== PÁG 37 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
25
También se evalúan las condiciones previas del sistema mediante el cálculo de la precipita-
ción antecedente para ventanas de tiempo predefinidas (PAx), definida como la sumatoria de las
precipitaciones (Pi) registradas en los x días previos al inicio del evento (Ecuación 2.17).
PAx =
x
∑
i=1
Pi
(2.17)
Tras el procesamiento de los datos, se extraen métricas de magnitud directamente del hidro-
grama de crecida, por ejemplo el caudal máximo (Qmax) y el flujo base (Qb), considerando este
último como equivalente al caudal registrado al inicio del evento (Qinicial). A partir de estas va-
riables, se determina el caudal directo (∆Q), definido como la diferencia entre el caudal máximo
y el flujo base (Ecuación 2.18).
∆Q = Qmax −Qb
(2.18)
La constante de recesión describe la curva de recesión del hidrograma y permite caracterizar
el almacenamiento de la cuenca y su interacción con el drenaje de las crecidas (Tallaksen, 1995).
Su valor se obtiene calibrando el parámetro K para que la Ecuación 2.19 se ajuste a la curva de
recesión del hidrograma real, esta calibración se realiza aplicando el logaritmo natural a todos
los términos de la Ecuación 2.20 y calibrando K linealmente. Sus valores varían entre 0 y 1,
siendo los valores más altos representativos de un drenaje lento y los valores cercanos a cero
indicativos de un drenaje más rápido.
Qt = Q0Kt
(2.19)
ln(Qt) = ln(Q0) + t ln(K)
(2.20)
Adicionalmente, se calculó un Índice de Tasa de Recesión (IV R) para cada crecida (Guy,
1964). Este índice representa la velocidad con la que disminuye el caudal en la zona de recesión
del evento y se define como la pendiente entre el caudal específico máximo (qmax ) y el caudal
específico al final del evento (qfinal ), dividida por el tiempo transcurrido entre el peak (tpeak ) y
el final de la crecida (tfinal ). El cálculo se muestra en la Ecuación 2.21.


=== PÁG 38 del PDF ===
CAPÍTULO 2. MARCO TEÓRICO
26
IV R = qmax −qfinal
tfinal −tpeak
(2.21)
La utilización de caudales específicos para el cálculo del IV R permite una comparación
entre cuencas.


=== PÁG 39 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
27
Capítulo 3
Materiales y Métodos
3.1.
Área de Estudio
El área de estudio se encuentra en la región del Maule, zona central de Chile, localizada
entre los 35° y 36°S (Figura 3.1). Su distribución espacial está determinada orográficamente
por la topografía de la Cordillera de la Costa y los Andes. Las subcuencas se delinearon con
el modelo de elevación digital (DEM) global ALOS PALSAR de 12 metros de resolución utili-
zando la extensión ArcSWAT en ArcGIS (ESRI, 2025). El área está compuesta por tres cuencas
mediterráneas: Robles, Chagres y Damas, las cuales cubren una extensión total de 144,2 km2.
Esta superficie equivale al 51,4 % de la cuenca del río Las Chilcas (280,3 km2) y al 4,9 % de la
cuenca del río Claro (2923,1 km2). La cuenca más extensa es Robles (70,8 km2), seguida por
Chagres (37,0 km2) y Damas (36,4 km2). Topográficamente, la elevación varía entre un mínimo
de 167 m s. n. m. en Damas y un máximo de 848 m s. n. m. en Robles. Durante los eventos de
precipitación, estas cuencas de elevaciones relativamente bajas suelen estar cubiertas por nubes.
Por su parte, la pendiente media varía desde un 11,0 % en Damas hasta un 14,9 % en Robles.
Caracteristicas morfométricas extraídas para cada cuenca se resume en la Tabla 3.1, mientras
que las propiedades de su red de drenaje principal se detallan en la Tabla 3.2.


=== PÁG 40 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
28
Figura 3.1: Cartografía del área de estudio, se muestran las tres cuenca de interés y su posición
en Chile y la región del Maule. Fuente: Elaboración propia.
Tabla 3.1: Métricas morfométricas y topográficas de las cuencas de estudio. Fuente: Elaboración
propia a partir de DEM ALOS PALSAR.
Cuenca
Área
Elevación media
Pendiente media
MRN
HI
TPI medio
TWI medio
SPI medio
Curvatura media
Orientación media
[km2]
[m]
[ %]
-
-
-
-
-
[1/m]
[deg]
Chagres
37,0
261,3
11,1
35,2
0,5
-0,005
7,6
592,9
0,2
192,6
Robles
70,8
375,1
14,9
81,3
0,3
0,020
7,3
1320,5
-0,2
177,9
Damas
36,4
232,5
11,0
32,5
0,4
-0,002
7,6
670,1
0,0
193,2
Tabla 3.2: Métricas morfológicas de los cauces principales.
Cuenca
Longitud (L)
Pendiente (S)
Ancho (W)
Profundidad (D)
[km]
[ %]
[m]
[m]
Chagres
25,2
0,8
11,3
0,6
Robles
41,7
1,5
16,6
0,7
Damas
22,8
0,8
11,2
0,5


=== PÁG 41 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
29
3.1.1.
Uso de Suelo
La caracterización del uso y cobertura del suelo se obtuvo de la Infraestructura de Datos
Espaciales (IDE) de Chile. Las áreas respectivas se calcularon en relación con la superficie total
para derivar la contribución de cada uso de suelo y tipo de vegetación por cuenca. El uso de
suelo principal en las tres áreas de estudio es agrícola, siendo Chagres la que presenta la mayor
proporción con un 82,0 %, mientras que Damas y Robles poseen un 65,5 % y 53,5 %, respec-
tivamente. La categoría de bosques es el segundo uso predominante, abarcando un 14,3 % en
Chagres, 27,6 % en Damas y 40,3 % en Robles (Tabla 3.3).
Tabla 3.3: Distribución de uso de suelo y área para las cuencas Chagres, Robles y Damas. Fuente:
Elaboración propia a partir de Infraestructura de Datos Espaciales (IDE) de Chile.
Cuenca
Categoría
Área (km2)
% del total de cuenca
Chagres
Bosques
5,3
14,28
Cuerpos de Agua
0,0
0,07
Praderas y Matorrales
1,2
3,27
Terrenos Agrícolas
30,2
81,97
Áreas Urbanas e Industriales
0,2
0,41
Robles
Bosques
28,5
40,29
Cuerpos de Agua
0,1
0,08
Praderas y Matorrales
3,7
5,25
Terrenos Agrícolas
37,8
53,46
Áreas Urbanas e Industriales
0,6
0,92
Damas
Bosques
10,0
27,57
Cuerpos de Agua
0,1
0,21
Praderas y Matorrales
2,2
6,05
Terrenos Agrícolas
23,8
65,45
Áreas Urbanas e Industriales
0,3
0,71


=== PÁG 42 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
30
3.1.2.
Tipo de suelo
Las propiedades del suelo se extrajeron de la base de datos grillada chilena CLSoilMaps
(Dinamarca et al., 2023). Los datos provenientes de este producto fueron validados con resul-
tados solidos por los autores de los datos grillados, obteniendo un coeficiente de determinación
de hasta 0, 84 para el contenido de arena y 0, 88 para la densidad aparente. Para alinearse con
el modelo de elevación digital (DEM), los datos de CLSoilMaps se remuestrearon de 100 m a
12 m utilizando el método de nearest neighbour en ArcGisPRO (ESRI, 2025), y posteriormente
se calculó un promedio espacial a nivel de cuenca para obtener un valor representativo para ca-
da una de las seis capas de suelo (0-5, 5-15, 15-30, 30-60, 60-100 y 100-200 cm). Para las tres
cuencas, el tipo de suelo predominante en las primeras capas (0-30 cm) se compone principal-
mente de suelo franco (52, 2 % −59, 7 %), seguido por franco arcilloso (28, 4 % −35, 1 %). Por
otro lado, las capas más profundas (30-200 cm) se componen principalmente de franco arcilloso
(54, 6 %−76, 6 %), seguido por franco (20, 8 %−40, 6 %) (Tabla 3.4). La conductividad hidráuli-
ca promedio disminuye a mayor profundidad, estando las capas superficiales asociadas a valores
de 9,0, 10,5 y 29,6 cm/día para Damas, Chagres y Robles, mientras que las capas profundas están
asociadas a valores de 6,6, 7,7 y 17,9 cm/día, respectivamente.


=== PÁG 43 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
31
Tabla 3.4: Propiedades del suelo y conductividad hidráulica (Ks) por profundidad para las cuen-
cas Robles, Chagres y Damas. Fuente: Elaboración propia a partir de datos de Dinamarca et al.
(2023).
Cuenca
Profundidad
Franco
Franco
Franco arcillo
Ks
(cm)
arcilloso ( %)
( %)
arenoso ( %)
(cm/día)
Robles
0-5
32,79
65,06
1,68
33,56
5-15
52,45
19,48
28,07
15,80
15-30
1,92
94,43
0,14
39,55
30-60
42,96
54,47
1,99
27,46
60-100
57,01
39,29
3,65
13,85
100-200
63,97
27,93
7,93
12,42
Chagres
0-5
39,09
58,57
1,48
10,96
5-15
45,60
17,31
37,09
8,25
15-30
0,52
96,68
0,00
12,29
30-60
51,52
46,15
2,30
10,25
60-100
73,09
22,28
4,64
6,83
100-200
57,20
28,97
12,32
5,93
Damas
0-5
47,26
52,32
0,17
9,45
5-15
57,25
6,54
36,22
6,37
15-30
0,64
97,75
0,00
11,10
30-60
59,22
40,39
0,39
8,36
60-100
88,51
10,68
0,81
6,21
100-200
82,20
11,24
6,26
5,23
Utilizando CLSoilMaps se extrajeron propiedades hidráulicas del suelo adicionales, tales
como la capacidad de campo (FC), punto de marchitez permanente (PWP), conductividad hi-
dráulica (Ks, cm/d), contenido de agua (AWC, mm), capacidad total de Agua (AWC, mm),
humedad disponible (AvMoist, cm3/cm3), contenido de agua residual (θr), contenido de agua
a saturación (θs), parámetro de forma alfa (α) y parámetro de forma (n) (Tabla I.1).
Utilizando la clasificación del HSG (Hydrologic Soil Group), el suelo de las tres cuencas se
clasifica como tipo C (Tabla 3.5). Estos suelos se caracterizan por tener un potencial modera-


=== PÁG 44 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
32
damente alto para generar escorrentía cuando se encuentran completamente húmedos, ya que la
transmisión de agua a través del suelo es algo restrictiva. Físicamente, este tipo de suelos tiene
entre 20 % y 40 % de arcilla y menos de 50 % de arena (US Department of Agriculture, Natural
Resources Conservation Service, 2009).
Tabla 3.5: Comparación de la conductividad hidráulica mínima de las cuencas con los criterios
del Grupo Hidrológico de Suelo (HSG) tipo C. Fuente: Elaboración propia.
Cuenca /
Capa imper-
Nivel
Ks mínima
Rango Ks HSG
Criterio
meable (cm) freático (cm)
(cm/día)
(cm)
Criterio USDA
>100
>100
>3,5 a <34,6
0 a 100
C
Chagres
>100
>100
6,8
0 a 100
C
Damas
>100
>100
6,2
0 a 100
C
Robles
>100
>100
15,8
0 a 100
C
3.2.
Adquisición de Datos
3.2.1.
Datos Fluviométricos
Para estimar el caudal en las salidas de las tres cuencas, se instalaron sensores de nivel de
agua HOBO MX20 (Figura 3.2). Se registraron datos desde mediados de julio continuamente
hasta finales de diciembre de 2025 (Tabla 3.6). Dado que estos instrumentos registran la presión
absoluta (Patm + Pcolumna), se instaló un sensor HOBO adicional en el exterior con la finalidad
de medir la presión barométrica y compensar los registros de los sensores sumergidos.


=== PÁG 45 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
33
Figura 3.2: Esquema de sensor HOBO MX20L. Fuente: Extraido de Onset Computer Corpora-
tion (2024).
Tabla 3.6: Estadísticas de registros de caudal para las cuencas Damas, Chagres y Robles. Fuente:
Elaboración propia.
Cuenca
Inicio
Fin
Qmax
Qmin
Qprom
Qmed
σ
Q95
Q5
(m3/s)
(m3/s)
(m3/s)
(m3/s)
(m3/s)
(m3/s)
(m3/s)
Damas
2025-07-17
2025-12-23
12,61
0,12
0,63
0,62
0,60
1,01
0,16
Chagres
2025-07-17
2025-12-23
23,19
0,18
0,58
0,43
0,98
1,00
0,29
Robles
2025-07-17
2025-12-23
28,39
0,16
2,03
2,05
1,59
3,67
0,30
Una vez obtenida la presión neta, esta se convirtió a nivel de agua y, posteriormente, a caudal
continuo mediante la aplicación de curvas de descarga. Estas curvas fueron actualizadas men-
sualmente a partir de aforos realizados en terreno (Tabla 3.7). Los registros originales, tomados
en intervalos de 5 minutos, fueron remuestreados a una resolución temporal de 10 minutos cal-
culando el promedio de cada intervalo (Figura 3.3).
Tabla 3.7: Ecuaciones de las curvas de descarga y coeficientes de determinación (R2) para las
cuencas Damas, Chagres y Robles. Fuente: Elaboración propia.
Cuenca
Ecuación de la curva
R2
Damas
Q = 4712, 6 · H2,02
0,7517
Chagres
Q = 7316, 3 · H2,7249
0,9616
Robles
Q = 4204, 4 · H2,2915
0,9602


=== PÁG 46 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
34
Figura 3.3: Serie temporal continua de caudales (Q) para las cuencas (a) Damas, (b) Chagres
y (c) Robles. El área sombreada resalta la magnitud del caudal durante el período de registro.
Fuente: Elaboración propia.
3.2.2.
Datos Pluviométricos
Los datos pluviométricos se obtuvieron mediante dos pluviómetros de tipo tipping bucket,
uno instalado en la salida de la cuenca Damas y el otro asociado a las cuencas Chagres y Ro-
bles debido a proximidad espacial (Figura 3.1). Estos sensores registraron información con una
resolución de 0,2 mm desde mediados de julio hasta finales de diciembre de 2025 (Tabla 3.8).
Los registros originales, tomados en intervalos de 5 minutos, fueron remuestreados a una resolu-
ción temporal de 10 minutos sumando la precipitación acumulada en cada nuevo intervalo. Los
gráficos de precipitación instantánea y acumulada durante el periodo de la serie de tiempo se
muestran en la Figura 3.4 y Figura 3.5 respectivamente.


=== PÁG 47 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
35
Figura 3.4: Serie temporal continua de precipitación (Pacum) para las cuencas (a) Damas, (b)
Chagres y (c) Robles. Fuente: Elaboración propia.


=== PÁG 48 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
36
Figura 3.5: Serie temporal continua de precipitación acumulada (P) para las cuencas (a) Damas,
(b) Chagres y (c) Robles. Fuente: Elaboración propia.
Tabla 3.8: Estadísticas y registros de precipitación para las cuencas Damas, Chagres y Robles.
Fuente: Elaboración propia.
Cuenca
Inicio
Fin
PTOT
Registros
Frecuencia
(mm)
con lluvia
( %)
Damas
2025-07-17
2025-12-23
237,6
473
2,07
Chagres
2025-07-17
2025-12-23
244,4
466
2,04
Robles
2025-07-17
2025-12-23
244,4
466
1,93


=== PÁG 49 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
37
3.2.3.
Datos de Humedad
Para estimar la humedad del suelo, se utilizó la fracción volumétrica de agua extraída del
reanálisis ERA5-Land (Muñoz Sabater, 2019), el cual cuenta con una resolución espacial de 9
km y una resolución temporal horaria, utilizando el período comprendido entre el 1 de abril de
2025 y el 31 de marzo de 2026. Los datos se remuestrearon a 12 m utilizando el método de nearest
neighbour, y posteriormente se calculó un promedio espacial a nivel de cuenca para obtener un
valor representativo. Finalmente, la fracción de agua se multiplicó por el espesor de cada capa
nativa del modelo para obtener los valores de humedad del suelo (ASM) correspondientes a las
cuatro profundidades de ERA5-Land (7, 28, 100 y 289 cm).
3.3.
Extracción de Eventos
Los eventos de lluvia-escorrentía se identificaron a partir de las series temporales de pre-
cipitación y caudal de cada cuenca utilizando la herramienta HydRun, ejecutada en el entorno
MATLAB (The MathWorks Inc., 2023). Los parámetros del filtro se ajustaron de manera inde-
pendiente (Tabla 3.9). Se utilizaron coeficientes de atenuación (α) entre 0,985 y 0,990, ejecutan-
do un número par de pasadas (4 y 6).
Para aislar exclusivamente las crecidas significativas, se aplicó un umbral de caudal máximo
(PKThreshold) variable entre 0,30 y 0,40 mm/h, y un umbral de retorno (ReRa) entre 0,15 y
0,20 para identificar el evento completo en el punto de recesión.


=== PÁG 50 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
38
Tabla 3.9: Parámetros de calibración utilizados en la herramienta HydRun para la extracción de
eventos en las cuencas de estudio. Fuente: Elaboración propia.
Parámetro
Chagres
Robles
Damas
Área de drenaje (km2)
36,95
70,84
36,43
Ventana de búsqueda de precipitación, n (horas)
5
5
5
Período sin lluvia mínimo (horas)
4
4
4
Coeficiente del filtro, α
0,985
0,990
0,985
Número de pasadas del filtro
4
6
4
Umbral de caudal máximo, PKThreshold (mm/h)
0,30
0,40
0,30
Umbral de retorno, ReRa
0,20
0,15
0,15
Pendiente de inicio del evento, beg_slope
0,001
0,001
0,001
Pendiente de recesión final, end_slope
0,0001
0,0001
0,0001
Coeficiente de suavizado, smooth_coef
17
7
5
Los eventos de lluvia que no generaron escorrentía también se consideraron en el análisis.
Se estableció un intervalo mínimo de 4 horas sin precipitación para clasificar los eventos como
independientes. Finalmente, el emparejamiento entre cada evento de escorrentía y su evento
de lluvia se realizó mediante una ventana de búsqueda de n = 5 horas. Los parámetros de
calibración detallados para las cuencas de Chagres, Robles y Damas se presentan en la Tabla 3.9.
3.4.
Variables Predictoras y de Respuesta
Siguiendo la metodología de Ross et al. (2021), se definieron cuatro variables principales
para caracterizar cada evento de precipitación (Tabla 3.10). Estas métricas permiten evaluar tanto
la magnitud y la intensidad del evento aislado como la influencia de la precipitación antecedente
en diferentes ventanas temporales (3, 5, 7, 10, 13, 30 días).


=== PÁG 51 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
39
Tabla 3.10: Caracterización de las variables predictoras para cada evento. Fuente: Elaboración
propia en base a métricas utilizadas por Ross et al. (2021).
Variable
Descripción
PTOT
Lluvia total del evento
Imax10
Intensidad de lluvia máxima durante 10 minutos
PAx
Lluvia antecedente a los x días
PTOT + PAx
Suma de la lluvia del evento y antecedente sobre cada ventana
Por otro lado, para caracterizar la respuesta del sistema, se definieron las variables hidroló-
gicas (Tabla 3.11). Estas métricas se dividieron en aquellas relacionadas con las magnitudes y
características del hidrograma, y las métricas de tiempo de respuesta, adoptando la nomenclatura
de Dingman (2015).
Tabla 3.11: Métricas hidrológicas (variables de respuesta) extraídas para caracterizar el compor-
tamiento de la cuenca en cada evento. Fuente: Elaboración propia.
Variable
Descripción
Características del hidrograma
Qmax
Caudal máximo del evento
Qb
Flujo base
qb
Flujo base específico
RTOT
Escorrentía total del evento
qmax
Caudal máximo específico
∆Q
Diferencia entre el caudal máximo y el flujo base
RC
Coeficiente de escorrentía
Métricas de tiempo de respuesta
Lag
Retardo de respuesta
D
Duración de la crecida
IV R
Índice de tasa de recesión
K
Constante de recesión
Para representar las condiciones de humedad iniciales de la cuenca (ASM), se extrajeron mé-
tricas correspondientes a cuatro profundidades acumuladas, derivadas de la estructura de ERA5-


=== PÁG 52 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
40
Land (0-7, 0-28, 0-100 y 0-289 cm). Estos valores se registraron exactamente una hora antes del
inicio de cada evento de precipitación. Dado que el reanálisis proporciona la humedad por capas
discretas, los valores para las profundidades acumuladas se estimaron calculando un promedio
ponderado según el espesor de cada estrato, para luego multiplicar este resultado por la profundi-
dad total de la columna de interés. Adicionalmente, se generaron variables combinadas sumando
la precipitación total del evento (PTOT ) con la humedad antecedente de cada perfil (Tabla 3.12).
Tabla 3.12: Métricas de humedad antecedente del suelo y precipitación combinada. Fuente: Ela-
boración propia.
Variable
Descripción
ASM7
Humedad del suelo antecedente acumulada en la capa 0-7 cm
ASM28
Humedad del suelo antecedente acumulada en la capa 0-28 cm
ASM100
Humedad del suelo antecedente acumulada en la capa 0-100 cm
ASM289
Humedad del suelo antecedente acumulada en la capa 0-289 cm
PTOT + ASM7
Precipitación total del evento más humedad antecedente (0-7 cm)
PTOT + ASM28
Precipitación total del evento más humedad antecedente (0-28 cm)
PTOT + ASM100
Precipitación total del evento más humedad antecedente (0-100 cm)
PTOT + ASM289
Precipitación total del evento más humedad antecedente (0-289 cm)


=== PÁG 53 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
41
3.5.
Implementación de Regresión Segmentada
La identificación de umbrales hidrológicos se realizó aplicando el algoritmo iterativo de
Muggeo (2003) mencionado en la Subsección 2.3.4. La posición de los puntos de quiebre (BP)
y los modelos de los segmentos lineales se calcularon en Python utilizando la librería piecewise-
regression de Pilgrim (2021). Se aplicó la regresión segmentada entre la variable de respues-
ta (RTOT) y las variables predictoras de la Sección 3.4 para identificar el umbral, obteniendo
además los valores de RSS, los coeficientes de determinación (R2 y R2adj) y los intervalos de
confianza al 95 % (BP95 %) asociados. Adicionalmente, se extrajeron los valores de significancia
estadística (valor p) para las pendientes de los segmentos lineales y para la estimación del punto
de quiebre. Finalmente, para aceptar la validez de los umbrales detectados por el algoritmo, se
aplicaron los mismos criterios de selección propuestos por Ross et al. (2021), los cuales fueron
descritos previamente en la Subsección 2.3.5. En la tabla Tabla 3.13 se mencionan la cantidad
de parámetros k utilizados en el cálculo de AICc para el modelo lineal y segmentado.
Tabla 3.13: Descripción de los parámetros del modelo lineal y segmentado para el cálculo del
AICc. Fuente: Elaboración propia.
Parámetro
Descripción
Modelo Lineal (k = 2)
β0
Intercepto de la recta
β1
Pendiente de la recta
Modelo Segmentado (k = 4)
β0
Intercepto del primer segmento
β1
Pendiente del primer segmento
β2
Pendiente del segundo segmento
γ
Punto de quiebre


=== PÁG 54 del PDF ===
CAPÍTULO 3. MATERIALES Y MÉTODOS
42
3.6.
Correlación entre características de la cuenca y respuesta
hidrológica
Para evaluar la influencia de las propiedades físicas estáticas de las cuencas sobre la caracte-
rización de las crecidas, se realizó un análisis de correlación lineal de Pearson (r). La selección
de las variables predictoras (Tabla 3.14) se basó en criterios de representatividad y variabilidad
espacial. Para el uso de suelo se escogieron las tres coberturas de mayor extensión porcentual en
el área de estudio, mientras que para las métricas topográficas y de tipo de suelo se excluyeron
aquellas que presentan valores constantes en las tres cuencas.
El comportamiento del sistema fue caracterizado mediante métricas de respuesta de magni-
tud, escorrentía total y flujo base, tanto en sus valores absolutos como específicos (Qmax, qmax,
RTOT, Qb y qb). Se aplicó una agregación temporal a los datos al calcular el valor promedio de
las métricas de respuesta considerando todos los eventos de escorrentía registrados por cuenca.
Tabla 3.14: Variables predictoras estáticas utilizadas en el análisis de correlación.
Variable
Descripción
Métricas Topográficas
Area
Área de drenaje de la cuenca (km2)
Elevmed
Elevación media de la cuenca (m)
Smed
Pendiente media de la cuenca ( %)
MRN
Número de Rugosidad Morfométrica (Adimensional)
Métricas de Uso de Suelo
LUForest
Cobertura de bosque ( %)
LUGrasslands
Cobertura de praderas y matorrales ( %)
LUAgricultural
Cobertura agrícola ( %)
Métricas de Suelo (Perfil 0-200 cm)
AWC
Capacidad de retención de agua disponible
FC
Capacidad de campo
Ksat
Conductividad hidráulica saturada


=== PÁG 55 del PDF ===
CAPÍTULO 4. RESULTADOS
43
Capítulo 4
Resultados
4.1.
Análisis de Eventos
La Tabla 4.1 muestra los eventos de precipitación y sus características para las tres cuencas
de estudio. Se observó un total de 63 eventos de precipitación, 23 en la cuenca Damas y 20 en las
cuencas Chagres y Robles. La precipitación total (Ptot) promedio alcanzó 12,2 mm en Chagres y
Robles, con valores que oscilaron entre 0,2 y 59,4 mm, mientras que Damas registró un promedio
de 10,4 mm, con un rango entre 0,2 y 43,5 mm. La intensidad máxima en 10 minutos (Imax10)
registró un valor de 21,6 mm/h en Chagres y Robles, mientras que en Damas fue de 19,2 mm/h.
El promedio de intensidad más alto se observó en Damas (8,2 mm/h), mientras que el valor
mínimo para las tres cuencas fue de 1,2 mm/h. De los eventos analizados, se observó generación
de escorrentía (Rtot > 0) en 6 eventos correspondientes a la cuenca Robles, 5 a Chagres y 5 a
Damas. El valor máximo de escorrentía total (Rtot) se registró en la cuenca Chagres (17,4 mm),
mientras que en Robles y Damas alcanzó 14,6 mm y 13,2 mm, respectivamente. La escorrentía
promedio osciló entre 4,0 y 6,4 mm, y el valor mínimo varió de 0,3 a 0,9 mm entre las tres
cuencas.


=== PÁG 56 del PDF ===
CAPÍTULO 4. RESULTADOS
44
Tabla 4.1: Estadísticas descriptivas de los eventos de precipitación y la escorrentía generada por
cuenca. Fuente: Elaboración propia.
Cuenca
Eventos
Ptot (mm)
Imax10 (mm/h)
Eventos con
Rtot (mm)
(n)
Max
Min
Prom
Max
Min
Prom
Rtot > 0
Max
Min
Prom
Chagres
20
59,4
0,2
12,2
21,6
1,2
7,9
5
17,4
0,6
6,4
Damas
23
43,6
0,2
10,4
19,2
1,2
8,2
5
13,2
0,9
5,6
Robles
20
59,4
0,2
12,2
21,6
1,2
7,9
6
14,6
0,3
4,0
La precipitación antecedente (PA) promedio aumentó progresivamente entre las ventanas
de 3 y 30 días, con valores que oscilaron en un rango de 6,9 a 70,1 mm (Tabla 4.2).
Tabla 4.2: Precipitación antecedente (PA) promedio acumulada para distintas ventanas tempo-
rales previas a los eventos. Fuente: Elaboración propia.
Cuenca
Precipitación Antecedente Promedio (mm)
PA3
PA5
PA7
PA10
PA13
PA15
PA30
Chagres
6,9
13,8
19,6
23,3
25,9
32,3
69,8
Damas
8,0
13,1
18,1
22,1
25,4
32,3
70,1
Robles
6,9
13,8
19,6
23,3
25,9
32,3
68,8
Se evidenciaron diferencias en los patrones de respuesta al comparar los valores de magnitud
absoluta frente a los específicos (Tabla 4.3 y Tabla 4.4). La Tabla Tabla 4.3 muestra que los
valores máximos absolutos de caudal se registraron en la cuenca Robles, con un caudal máximo
(Qmax) de 28,4 m3/s, seguida por Chagres con 23,2 m3/s y Damas con 12,6 m3/s. Este mismo
orden de magnitud se mantuvo para el caudal base (Qb) y el caudal directo (∆Q), alcanzando
máximos de 2,9 y 25,5 m3/s en Robles, 1,6 y 21,6 m3/s en Chagres, y 0,5 y 12,1 m3/s en Damas,
respectivamente. En cuanto a los promedios, los valores más altos para Qmax y Qb se observaron
en Robles (8,8 y 2,2 m3/s), seguida por Chagres (8,5 y 0,7 m3/s) y finalmente Damas (4,8 y
0,3 m3/s); sin embargo, este comportamiento se invirtió para el caudal directo promedio (∆Q),
donde el valor más alto se registró en Chagres (7,9 m3/s) y el mínimo en Robles (4,0 m3/s).


=== PÁG 57 del PDF ===
CAPÍTULO 4. RESULTADOS
45
Tabla 4.3: Estadísticas de caudales absolutos: máximo, caudal base y caudal directo por evento.
Fuente: Elaboración propia.
Cuenca
Qmax (m3/s)
Qb (m3/s)
∆Q (m3/s)
Max
Min
Prom
Max
Min
Prom
Max
Min
Prom
Chagres
23,2
1,0
8,5
1,6
0,3
0,7
21,6
0,5
7,9
Damas
12,6
1,0
4,8
0,5
0,1
0,3
12,1
0,6
4,5
Robles
28,4
1,9
8,8
2,9
1,4
2,2
25,5
0,5
4,0
Al analizar las magnitudes específicas, la tendencia observada en los caudales absolutos
se invirtió (Tabla 4.4). La cuenca Chagres registró el valor más alto para el caudal específico
máximo (qmax) con 0,63 m3/s/km2, seguida por Robles con 0,40 m3/s/km2 y Damas con 0,34
m3/s/km2. Este comportamiento se mantuvo en el caudal directo específico (∆q), alcanzando
0,59, 0,36 y 0,33 m3/s/km2 para Chagres, Robles y Damas, respectivamente. Para el caudal base
específico (qb), los valores máximos correspondieron a 0,04 m3/s/km2 en Chagres y Robles, y
0,01 m3/s/km2 en Damas. Finalmente, la eficiencia en la generación de escorrentía, representada
por el coeficiente de escorrentía (RC), presentó su valor máximo en la cuenca Chagres (42 %),
mientras que en Robles y Damas se registraron valores de 35 % y 41 %, respectivamente.
Tabla 4.4: Estadísticas de caudales específicos (normalizados por área) y coeficiente de esco-
rrentía. Fuente: Elaboración propia.
Cuenca
qmax (m3/s/km2)
qb (m3/s/km2)
∆q (m3/s/km2)
RC ( %)
Max
Min
Prom
Max
Min
Prom
Max
Min
Prom
Max
Min
Prom
Chagres
0,63
0,03
0,23
0,04
0,01
0,02
0,59
0,01
0,21
42
3
22
Damas   
0,34
0,03
0,13
0,01
0,01
0,01
0,33
0,02
0,12
41
4
20
Robles 
0,40
0,03
0,12
0,04
0,02
0,03
0,36
0,01
0,06
35
5
15
Respecto a los valores promedio de las magnitudes absolutas, los registros más altos de
caudal máximo (Qmax) y caudal base (Qb) se mantuvieron en Robles (8,8 y 2,2 m3/s), seguidos
por Chagres (8,5 y 0,7 m3/s) y Damas (4,8 y 0,3 m3/s). Sin embargo, este patrón no se observó
para el caudal directo (∆Q); por ejemplo, la cuenca Chagres registró el valor promedio más alto
(7,9 m3/s), seguida por Damas (4,5 m3/s) y Robles (4,0 m3/s). Esta predominancia del caudal


=== PÁG 58 del PDF ===
CAPÍTULO 4. RESULTADOS
46
directo en Chagres se mantuvo en los promedios específicos, registrando el mayor ∆q (0,21
m3/s/km2) y la mayor eficiencia promedio mediante el RC (22 %), contrastando con Robles, que
presentó el RC promedio más bajo (15 %). Por el contrario, no se identificó ninguna tendencia
clara en los valores mínimos, ni para las variables de magnitud ni para las de eficiencia.
La Figura 4.1 muestra los hidrogramas de crecidas registrados consecutivamente en las tres
cuencas de estudio junto a la variación de humedad antecedente (ASM) durante el evento el ini-
cio del evento de lluvia hasta el termino de la crecida para cuatro profundidades de suelo. En los
eventos 1 y 2, asociados a las tormentas más intensas, se evidenció una dominancia de la cuenca
Chagres en la generación de escorrentía. Durante el evento 1, se registró en esta cuenca un coefi-
ciente de escorrentía (RC) de 14,6 % y el caudal máximo (Qmax) más alto (13,8 m³/s), mientras
que en Robles y Damas se observaron valores de RC de 8,4 % y 11,8 %, respectivamente. En
el evento 2 se evidenció el efecto de la precipitación antecedente (PA3), la cual osciló entre
43,6 y 59,4 mm, sobre la eficiencia de la cuenca para generar escorrentía. Esta saturación previa
incrementó el valor de RC en todas las cuencas, alcanzando un máximo de 42,3 % en Chagres,
mientras que el valor más alto de Qmax se registró esta vez en Robles (28,4 m3/s). El mismo
patrón se repite en el evento 3, en donde las cuencas con mayor PA3 (18,2 mm) registraron los
valores más altos de RC de 13,7 y 18,4 % en Chagres y Robles respectivamente, mientras que
en Damas se observó un valor de 7,8 % con una métrica de PA3 de 1,6 mm. El evento 4 con-
tinúa registrando la dominancia de RC en Chagres (23,2 %) por sobre Robles (10,9 %) incluso
en condiciones sin precipitación antecedente (PA3 = 0), sin embargo, en Damas se generó un
aumento inusual de RC (41,3 %), coincidiendo con el tiempo de retardo (Lag) más largo de los
4 eventos. La métrica Lag varió entre 0,5h y 17,2h, sin embargo, no presentó ninguna tendencia
con relación a los eventos.


=== PÁG 59 del PDF ===
CAPÍTULO 4. RESULTADOS
47
Figura 4.1: Hidrogramas de crecida junto a nivel de humedad para distintas profundidades. Se
detallan métricas hidrológicas correspondientes para eventos consecutivos en las 3 cuencas de
estudio. Fuente: Elaboración propia.


=== PÁG 60 del PDF ===
CAPÍTULO 4. RESULTADOS
48
En la Figura 4.1 se observa que, durante los eventos de precipitación, las capas más superfi-
ciales del suelo (7 y 28 cm de profundidad) exhiben una respuesta rápida. Las series temporales
de ASM7 y ASM28 presentan respuestas abruptas y con alta variabilidad. En contraste, para los
eventos 1, 3 y 4, las capas más profundas (ASM100 y ASM289) presentan un aumento gradual de
la humedad, sin mostrar un drenaje significativo durante el desarrollo de la crecida. Por ejemplo,
en el Evento 1, la humedad aumentó de 464 a 502 mm en ASM100 y de 1242 a 1290 mm en
ASM289. Este patrón también se observa durante el Evento 3 (457-493 mm y 1300-1335 mm,
respectivamente) y en el Evento 4 (450-484 mm y 1311-1347 mm). Sin embargo, este compor-
tamiento difiere durante el Evento 2 para la capa ASM100. En este caso, la serie temporal no
presentan un aumento gradual, sino que muestra una respuesta abrupta que caracteriza a las ca-
pas superficiales. Este cambio de patrón coincide con un aumento de la precipitación antecedente
(PA3) producto del Evento 1. Por su parte, la capa más profunda (ASM289) mantuvo su patrón
de aumento gradual, al igual que en los eventos 1, 3 y 4.
La humedad para profundidades entre ASM100 y ASM289, para los eventos 1, 2 y 3 y a
diferencia de las profundidades superiores, respondieron tardíamente al ascenso y peak de las
crecidas, notando un aumento solo luego de suceder la mayor parte del evento. Para el caso del
Evento 2, este aumento también fue tardío en relación a las capas superiores, pero esta vez el
ascenso de humedad sucedió durante el ascenso de la crecida.
La Tabla 4.5 muestra que en la cuenca Chagres se registraron los índices de tasa de recesión
(IV R) más altos y las constantes de recesión (K) más bajas, con valores que oscilaron entre
0,003 y 0,267 para el IV R, y entre 0,838 y 0,929 para K, durante los tres eventos de mayor
caudal máximo (Qmax). En contraste, para el evento de menor magnitud se observaron valores
de 0,0006 para el IV R y 0,972 para K. Por el contrario, en la cuenca Robles se registraron los
menores valores de IV R y los mayores valores de K durante los eventos 1, 3 y 4, correspon-
dientes a 0,008, 0,0004 y 0,001 para el IV R, y a 0,926, 0,996 y 0,983 para K, respectivamente.
En la cuenca Damas los valores se mantuvieron dentro del rango de las otras cuencas, a excep-
ción del Evento 3, asociado al Qmax menor, en donde se registró el menor K (0,958) y el mayor
IV R (0,0012). Finalmente, el promedio de IV R para Chagres (0,011) es el más alto, seguido
por Robles (0,0059) y Damas (0,0053), mientras que el promedio de K presenta los valores más


=== PÁG 61 del PDF ===
CAPÍTULO 4. RESULTADOS
49
altos en Damas (0,975), luego Robles (0,937) y Chagres (0,915).
Tabla 4.5: Comparativa de los índices IV R y constante de recesión K por evento y cuenca.
Fuente: Elaboración propia.
Evento
Chagres
Robles
Damas
IV R
K
IV R
K
IV R
K
1
0,026697
0,84
0,007996
0,90
0,008320
0,93
2
0,015955
0,92
0,014309
0,94
0,008862
1,00
3
0,000647
0,97
0,000423
0,96
0,001215
0,98
4
0,003270
0,93
0,001013
0,95
0,003111
0,98
Promedio
0,011642
0,9150
0,005935
0,9375
0,005377
0,9725
4.2.
Análisis De Umbrales
La Figura 4.2 muestra el comportamiento no lineal en la transformación de precipitación a
escorrentía. Todos los eventos observados se distribuyen por debajo del límite teórico de RC = 1,
el cual equivale a una conversión total de la precipitación (PTOT) en escorrentía (RTOT). La
relación entre los eventos de escorrentía y todas las variables predictoras meteorológicas para
las tres cuencas se encuentran en la Figura I.1, Figura I.2 y Figura I.3.


=== PÁG 62 del PDF ===
CAPÍTULO 4. RESULTADOS
50
Figura 4.2: Relación entre Escorrentía total del evento RTOT y su precipitación total PTOT aso-
ciada. La linea RC indica un transformación equivalente de precipitación en escorrentía. Fuente:
Elaboración propia.
La Tabla 4.6 muestra los resultados del coeficiente de determinación ajustado (R2
adj), la mag-
nitud de los umbrales de activación (BP) y el intervalo absoluto asociado al 95 % de confianza
del umbral (BP95 %). Para la métrica combinada Ptot +PA3, los valores de R2
adj correspondieron
a 0,55, 0,83 y 0,92 en Damas, Chagres y Robles, con umbrales BP de 41,4, 53,3 y 54,4 mm, res-
pectivamente. Por otro lado, para el índice PA3 de forma individual, se obtuvo un R2
adj de 0,64,
0,70 y 0,87, y un BP de 30,7, 22,5 y 16,8 mm, respectivamente. Esto evidencia que el índice
PA3 por sí solo presenta un mejor ajuste en la cuenca Damas, pero un rendimiento inferior en
Chagres y Robles en comparación con la métrica combinada.
Se registró un patrón similar para la métrica Ptot + ASM0−100, con valores de R2
adj de 0,66,
0,92 y 0,97, y umbrales de activación de 505,6, 512,1 y 522,6 mm para las mismas cuencas,
respectivamente. Por el contrario, las variables ASM0−100 y Ptot evaluadas de forma individual
no alcanzaron un R2
adj mayor a 0,45 en ninguna de las tres áreas de estudio. Este mismo patrón
de bajo ajuste se identificó en las métricas de precipitación antecedente de largo plazo (7 a 30
días).
Por su parte, la métrica Ptot+PA5 obtuvo valores de R2
adj > 0, 45 únicamente en las cuencas
de Robles (0,78) y Chagres (0,90), mientras que en Damas el modelo no convergió. Los intervalos
de confianza (BP95 %) asociados a Ptot + PA5 (11,5 y 6,7 mm) resultaron menores que los de


=== PÁG 63 del PDF ===
CAPÍTULO 4. RESULTADOS
51
Ptot + PA3 (21,2 y 11,3 mm) en sus respectivas cuencas, lo que indica una mayor precisión
estadística en la estimación de la posición del umbral al utilizar la ventana de 5 días. Finalmente,
para la métrica de intensidad máxima (Imax10), el R2
adj superó el umbral de 0,45 solo en la cuenca
Chagres.
Tabla 4.6: Resultados de métricas estadísticas (R2
Adj, BP y BP 95 %) para las trece variables
predictoras por cuenca. N.A indica que el modelo no convergió. Fuente: Elaboración propia.
Métrica
R2
Adj
BP
BP 95 %
Chagres
Damas
Robles
> 0, 45
Chagres
Damas
Robles
Prom.
Chagres
Damas
Robles
Ptot
0,42
0,31
0,28
0
10,5
5,6
15,2
10,4
28,9
75,8
56,6
PA3
0,70
0,64
0,83
3
22,5
30,7
16,8
23,3
11,8
3,9
11,0
PA5
0,70
-0,12
0,88
2
56,3
11,5
56,3
41,4
1,1
31,4
0,7
PA7
-0,17
-0,14
N.A
0
7,9
2,5
N.A
5,2
36,4
11,8
N.A
PA10
-0,18
N.A
N.A
0
23,9
N.A
N.A
23,9
130,7
N.A
N.A
PA13
N.A
-0,18
N.A
0
N.A
2,9
N.A
2,9
N.A
15,5
N.A
PA30
-0,17
-0,06
0,02
0
6,3
9,0
121,8
45,7
N.A
16,5
133,1
Ptot + PA3
0,83
0,55
0,92
3
53,3
41,4
54,4
49,7
21,2
19,7
11,3
Ptot + PA5
0,78
N.A
0,90
2
52,0
N.A
53,3
52,6
11,5
N.A
6,7
Ptot + PA7
0,15
0,04
N.A
0
17,8
10,4w
N.A
14,1
80,4
84,1
N.A
Ptot + PA10
0,24
0,03
0,29
0
56,8
17,0
64,2
46,0
54,4
93,0
40,0
Ptot + PA13
0,10
0,10
N.A
0
27,1
84,8
N.A
55,9
92,5
5,4
N.A
Ptot + PA30
-0,20
-0,09
N.A
0
84,4
83,1
N.A
83,7
94,1
46,0
N.A
Imax10
0,51
N.A
0,40
1
14,6
N.A
13,1
13,9
5,4
N.A
10,0
ASM7
N.A
N.A
N.A
0
N.A
N.A
N.A
N.A
N.A
N.A
N.A
ASM28
-0,18
-0,20
-0,20
0
134,8
134,5
137,8
135,7
15,6
19,3
0,0
ASM100
N.A
-0,16
N.A
0
N.A
442,0
N.A
442,0
N.A
180,2
N.A
ASM289
0,37
0,30
0,32
0
1247,8
1256,8
1274,2
1259,6
21,8
28,8
37,1
Ptot + ASM7
0,34
0,27
0,23
0
36,6
36,0
41,0
37,9
23,8
21,5
41,1
Ptot + ASM28
0,31
0,16
0,20
0
132,9
129,0
135,4
132,5
26,7
28,7
31,1
Ptot + ASM100
0,92
0,66
0,97
3
512,1
505,6
522,6
513,4
4,3
8,8
2,8
Ptot + ASM289
N.A
-0,13
-0,14
0
N.A
1263,5
1323,1
1293,3
N.A
65,8
74,0
La Tabla 4.7 muestra que, para las tres cuencas, todos los parametros R2
Adj mayores a 0,45
cumplen los criterios establecidos en Sección 3.5. La cuenca Chagres obtuvo la mayor cantidad
de umbrales (7), seguido por Robles (5) y finalmente Damas (3). El umbral de intensidad Imax10
solo se presentó en Chagres, mientras que las métricas asociadas a PA5 solo en Chagres y Robles.


=== PÁG 64 del PDF ===
CAPÍTULO 4. RESULTADOS
52
Tabla 4.7: Evaluación de pendientes y validación de umbrales para las variables predictoras con
R2
adj > 0, 45 por cuenca. Fuente: Elaboración propia.
Variable
Análisis de Pendientes
Criterios de Validación
m1
m2
∆m ( %)
∆m > 10 %
m2 > 0
Umbral Válido
Chagres
PA3
-0,0492
0,4766
1069,3
Sí
Sí
Sí
PA5
-0,0311
5,8148
18824,3
Sí
Sí
Sí
Ptot + PA3
0,0552
0,3164
473,2
Sí
Sí
Sí
Ptot + PA5
0,0134
0,3480
2500,8
Sí
Sí
Sí
Imax10
0,0144
1,8082
12418,9
Sí
Sí
Sí
Ptot + ASM100
0,0034
0,5856
16882,9
Sí
Sí
Sí
Damas
PA3
-0,0545
1,0830
2086,7
Sí
Sí
Sí
Ptot + PA3
0,0251
0,2660
958,1
Sí
Sí
Sí
Ptot + ASM100
0,0018
0,4088
23102,7
Sí
Sí
Sí
Robles
PA3
-0,0932
0,3621
488,3
Sí
Sí
Sí
PA5
-0,0202
4,8741
24259,1
Sí
Sí
Sí
Ptot + PA3
0,0263
0,2888
1000,2
Sí
Sí
Sí
Ptot + PA5
0,0018
0,3060
17145,0
Sí
Sí
Sí
Ptot + ASM100
0,0002
0,7272
416798,9
Sí
Sí
Sí
Se observó que solo tres métricas predictoras, vinculadas a la humedad antecedente de corto
plazo (PA3, Ptot + PA3 y Ptot + ASM0−100), presentaron un R2
adj superior a 0,45 de forma
simultánea en las tres cuencas de estudio (Figura 4.3). Se puede visualizar que la cuenca Robles
presentó el mayor ajuste entre las tres cuencas, con valores de 0,97, 0,92 y 0,83 para Ptot +
ASM0−100, Ptot + PA3 y PA3, respectivamente. Por el contrario, la variable PA3 evaluada
de forma individual obtuvo los valores más bajos de ajuste y los intervalos de confianza más
extensos.


=== PÁG 65 del PDF ===
CAPÍTULO 4. RESULTADOS
53
Figura 4.3: Umbrales para las métricas PTOT + PA3 (a), PTOT + ASM100 (b) y PA3 (c) para las
las tres cuencas. Fuente: Elaboración propia.
El umbral de intesidad de Imax(10) se presentó solo en la cuenca Chagres con los valores
más bajos de ajuste (0,51) y los intervalos de confianza del umbral más largos (Figura 4.4).


=== PÁG 66 del PDF ===
CAPÍTULO 4. RESULTADOS
54
Figura 4.4: Umbral de intensidad máxima en 10 minutos (Imax(10)) para la cuenca Chagres.
Los resultados del análisis del Criterio de Información de Akaike corregido (∆AICc) en la
Figura 4.5 evidenciaron que las métricas PA3, PA5, Ptot + PA3, Ptot + PA5, Ptot + ASM0−100
e Imax10 superan el umbral de dos unidades, lo que justifica la segmentación en aquellas cuen-
cas asociadas a valores de R2
adj > 0, 45. Los valores de ∆AICc más altos correspondieron al
índice Ptot + ASM0−100 en Robles (61,7), seguido por Chagres (41,9), mientras que en Damas
correspondió a PA3 (18,8). Se observó que en la cuenca Damas se presentaron los valores más
bajos para las métricas de precipitación antecedente, con un ∆AICc de 2,7 para el índice de 3
días Ptot + PA3 y una ausencia de convergencia del modelo para el de 5 días Ptot + PA5. En
contraste, en las cuencas Chagres y Robles se registraron valores de 7,0 y 14,8 para Ptot + PA3,
y de 24,8 y 41,9 para Ptot + PA5, respectivamente. Finalmente, para la métrica de intensidad
Imax10, se observaron valores de ∆AICc superiores al umbral de dos solo en la cuenca Chagres.


=== PÁG 67 del PDF ===
CAPÍTULO 4. RESULTADOS
55
Figura 4.5: Análisis de Criterio de Información de Akaike corregido para las métricas con al
menos un resultado de R2
adj >0,45 en las tres cuencas de estudio. Fuente: Elaboración propia.


=== PÁG 68 del PDF ===
CAPÍTULO 4. RESULTADOS
56
4.3.
Análisis de Correlación
La Figura 4.6 presenta los coeficientes de correlación de Pearson (r) entre las respuestas
hidrológicas y las métricas de uso de suelo. Los datos muestran la relevancia de normalizar el
caudal máximo absoluto (Qmax) por el área de la cuenca para aislar el caudal pico específi-
co (qmax). Mientras que Qmax no registró correlación con LUForest (0,04) ni con LUAgricultural
(0,04), qmax exhibió correlaciones fuertes para ambas variables (-0,90 y 0,93, respectivamente),
además de una alta asociación negativa con LUGrasslands (-0,94). 
Los resultados muestran valores inversos entre las coberturas boscosas (LUForest) y agrícolas
(LUAgricultural) para todas las métricas de respuesta. Este patrón se evidencia en la escorrentía to-
tal (RTOT), con correlaciones de -0,98 y 0,96 respectivamente, y se mantiene en el flujo base (Qb)
con valores de 0,76 y -0,70. Por otro lado, la cobertura de praderas y matorrales (LUGrasslands)
presenta una alta asociación negativa con qmax (-0,94) y moderada con RTOT (-0,55), sin embar-
go, su correlación con la generación de flujo base (Qb) es nula (0,07), contrastando con el efecto
de la cobertura boscosa (0,76). La tendencias que presentó Qb también se muestran en qb con
valores  de 0,58, -0,18 y -0,51 para LUForest, LUGrasslands y LUAgricultural respectivamente.


=== PÁG 69 del PDF ===
CAPÍTULO 4. RESULTADOS
57
Figura 4.6: Mapa de calor de correlación de Pearson (r) entre las respuestas hidrológicas y los
porcentajes de cobertura de uso de suelo. Fuente: Elaboración propia.
En la Figura 4.7 se visualiza una fuerte correlación positiva entre el flujo base absoluto (Qb)
y todas las métricas topográficas, con valores oscilando entre 0,99 y 1,00. Esta asociación se
mantiene alta incluso cuando el caudal se normaliza por el área de la cuenca (qb), registrando
coeficientes de 0,92 a 0,97. Por el contrario, se observa una inversión de signos al comparar
las correlaciones del caudal máximo, mientras la métrica absoluta (Qmax) presenta asociaciones
positivas (0,55 a 0,69), el caudal específico (qmax) muestra valores negativos (-0,38 a -0,54) para


=== PÁG 70 del PDF ===
CAPÍTULO 4. RESULTADOS
58
las variables topográficas. Finalmente, al igual que qmax, la escorrentía total (RTOT) exhibe una
marcada tendencia negativa para todas las variables topográficas, con coeficientes que varían
entre -0,86 y -0,94.
Figura 4.7: Mapa de calor de correlación de Pearson (r) entre las respuestas hidrológicas y las
métricas topográficas. Fuente: Elaboración propia.
La Figura 4.8 muestra una fuerte correlación positiva del flujo base (Qb y qb) con las pro-
piedades del suelo (AWC, FC y Ksat), alcanzando coeficientes que oscilan entre 0,91 y 1,00.
Asimismo, se replica el patrón de inversión de signos previamente descrito para los caudales má-
ximos donde la métrica absoluta (Qmax) presenta asociaciones positivas (0,54 a 0,70) y el caudal


=== PÁG 71 del PDF ===
CAPÍTULO 4. RESULTADOS
59
específico (qmax) muestra correlaciones negativas (-0,37 a -0,55). Finalmente, la escorrentía total
(RTOT) muestra una marcada tendencia negativa para todas las propiedades de suelo, con valores
que varían entre -0,85 y -0,94.
Figura 4.8: Mapa de calor de correlación de Pearson (r) entre las respuestas hidrológicas y las
propiedades físicas del suelo (perfil 0-200 cm). Fuente: Elaboración propia.


=== PÁG 72 del PDF ===
CAPÍTULO 5. DISCUSIÓN
60
Capítulo 5
Discusión
5.1.
Condiciones Pre-evento
La respuesta del caudal base de las cuencas está controlada fuertemente por las caracterís-
ticas topográficas, propiedades del suelo y por el uso de la superficie. Las cuencas con mayor
porcentaje de cobertura boscosa, como Robles (40 %), presentaron valores promedio de caudal
base más altos (2, 2 m3/s) previos a los eventos de crecida. Por el contrario, la dominancia de co-
bertura agrícola en Chagres (82 %) se asocia a un caudal base menor (0, 7 m3/s). Esta reducción
es consistente con la literatura sobre la alteración hidrológica producto de la agricultura (Price,
2011; Roa-García et al., 2011). La alteración agrícola se presenta físicamente en la cuenca a tra-
vés de una menor conductividad hidráulica en las capas profundas del suelo (5, 93 cm/dia en
Chagres frente a 12, 42 cm/dia en Robles para 100 −200 cm), restringiendo la capacidad del
sistema para mover caudal subsuperficial de manera sostenida (Zimmermann et al., 2006).
Además de los parámetros superficiales, la capacidad total del sistema para mantener el
caudal base está influenciada por sus características topográficas y eso se refleja en la marcada
correlación entre el caudal base absoluto (Qb) y métricas como el área, la elevación media y la
pendiente. La influencia de la topografía genera que la pendiente y la elevación proporcionan el
empuje necesario para que el agua subsuperficial hacia la red de drenaje durante los periodos de
recesión (Smakhtin, 2001).
Es esperable que una cuenca de mayor extensión superficial genere un mayor caudal base
debido a la mayor área de drenaje (Smakhtin, 2001). Sin embargo, la fuerte correlación posi-


=== PÁG 73 del PDF ===
CAPÍTULO 5. DISCUSIÓN
61
tiva del caudal base específico (qb) con todas las variables topográficas, incluido el tamaño de
la cuenca, indica que, en la zona de estudio, la cuenca de mayor dimensión (Robles) produce
desproporcionadamente más caudal base por unidad de área. Este comportamiento se debe a que
la cuenca de mayor extensión es, además, la de mayor altitud media. La elevación actúa como
una variable sustituta que covaría fuertemente con las propiedades del suelo y la cobertura te-
rrestre (Merz et al., 2009). En este caso, el incremento de altitud hacia la cuenca Robles se asocia
con una mayor cobertura boscosa (40 %), lo que implica una alta conductividad hidráulica y un
aumento en la Capacidad de Retención de Agua Disponible (AWC).
5.2.
Activación y Memoria del Sistema
Para las tres cuencas, no se encontró ningún umbral de activación considerando la precipi-
tación total por sí sola. La cantidad de escorrentía generada por una tormenta depende principal-
mente de las condiciones de humedad previas y de la distribución temporal de la lluvia, no solo
de su volumen total (Sittner et al., 1969). La literatura muestra que los umbrales dependientes
exclusivamente del evento aislado son inusuales (Ross et al., 2021; Ali et al., 2013). Esta in-
suficiencia demuestra que la magnitud de la respuesta hidrológica local no está dictada por el
volumen del evento, sino que está condicionada por la memoria del sistema.
La existencia de los umbrales basados en la precipitación antecedente (PA) y su combina-
ción con la lluvia del evento (Ptot +PA) para las tres cuencas de estudio demuestra la necesidad
de analizar una ventana temporal para describir adecuadamente los mecanismos de generación
de escorrentía. Esta dependencia temporal evidencia que la conectividad hidrológica de la cuenca
está condicionada por los eventos pasados. La literatura documenta que la memoria del sistema
actúa como un control de primer orden en la activación de diversos tipos de cuencas (Detty and
McGuire, 2010b; Nanda and Safeeq, 2023; James and Roulet, 2007).
El umbral Ptot+ASM100 concuerda con los procesos de saturación descritos por Vreugdenhil
et al. (2022) en cuencas agrícolas con perfiles de suelo restrictivos y está acorde a los umbrales
observados en cuencas mediterráneas (Nanda and Safeeq, 2023). En sistemas dominados por
limos con moderado a alto contenido de arcilla, similares a los suelos del Grupo Hidrológico C
presentes en Chagres, Robles y Damas, donde el suelo franco arcilloso se convierte en el tipo


=== PÁG 74 del PDF ===
CAPÍTULO 5. DISCUSIÓN
62
de suelo predominante en las capas inferiores (54,6 % - 76,6 %), la baja permeabilidad de las
capas inferiores genera un estancamiento del agua percolada y restricción vertical que provoca
la formación de niveles freáticos colgados que limitan el almacenamiento efectivo al estrato
superficial e intermedio (Silasari et al., 2017). Esto está acorde al aumento de humedad a una
profundidad de 100 cm durante el inicio del evento y el ascenso tardío de humedad entre las
capas ASM100 y ASM289 tras la crecida, indicando el estancamiento de flujo producto de la
menor conductividad hidráulica.
Por lo tanto, el estado de humedad del suelo, así como se ha observado en varios sistemas
hidrológicos, controla la conectividad de la cuenca (Nanda and Safeeq, 2023; Detty and McGui-
re, 2010b). Mientras que la capa superior (0-100 cm) posea capacidad de almacenamiento, la
lluvia genera una escorrentía nula o mínima, ya que el agua es absorbida por la capa sin saturar.
Sin embargo, una vez que el volumen combinado supera la capacidad de retención (el umbral
de 505-522 mm), el nivel freático se eleva hasta intersectar la superficie o las vías de flujo pre-
ferencial subsuperficiales. Esta dinámica concuerda con el comportamiento de umbral descrito
por Vreugdenhil et al. (2022), en el cual el sistema experimenta un cambio de estado abrupto,
transformando la precipitación adicional en escorrentía (Han et al., 2012).
La detección de umbrales para precipitación antecedente entre 3 y 5 días, y su ausencia para
ventanas de mayor duración temporal, indica que la cuenca funciona con una memoria de corto
plazo. En este sistema, los eventos ocurridos hace más de 5 días no afectan los procesos de gene-
ración de escorrentía. Este comportamiento en las tres cuencas concuerda con las observaciones
de Ross et al. (2021), donde los umbrales de memoria corta resultaron ser los más frecuentes.
5.3.
Umbral por Intensidad
La coexistencia de un umbral de intensidad de 14, 6 mm/h con los umbrales de precipitación
antecedente y humedad en Chagres evidencia una alta complejidad en los procesos de genera-
ción de escorrentía de la cuenca. La literatura documenta la activación de múltiples mecanismos
hidrológicos en cuencas mediterráneas (Lana-Renault et al., 2014) y cuencas sometidas a un uso
agrícola intensivo (Saffarpour et al., 2016). El umbral permite teorizar que el sistema opera bajo
un régimen mixto: bajo eventos de alta intensidad ocurre la escorrentía superficial por exceso


=== PÁG 75 del PDF ===
CAPÍTULO 5. DISCUSIÓN
63
de infiltración, proceso documentando en cuencas agrícolas (García-Ruiz et al., 2008; Rogger
et al., 2017), y el flujo lateral rápido a través de redes de macroporos, mecanismos que actúan
en conjunto con el flujo subsuperficial y el exceso de saturación controlados por la humedad
del perfil. La existencia de este umbral está acorde al uso agrícola en la cuenca Chagres (81 %),
la cual es significativamente mayor que en Damas (65 %) y Robles (53 %). La literatura docu-
menta que las prácticas agrícolas intensivas inducen la compactación del suelo y degradan la
estructura superficial, lo que reduce drásticamente la capacidad de infiltración inicial respecto
a suelos forestales (Navas et al., 2008). Por lo tanto, cuando la intensidad de la precipitación
supera esta conductividad hidráulica superficial, el sistema genera una respuesta de escorrentía
rápida por exceso de infiltración, independientemente del volumen total acumulado (Saffarpour
et al., 2016).
5.4.
Respuesta y Eficiencia de las Cuencas
La cuenca Robles es la que produce las crecidas y el caudal directo más extremos en prome-
dio, lo que está asociado a un mayor área de drenaje (Smakhtin, 2001), sin embargo, la cuenca
Chagres, a pesar de presentar menores caudales máximos, es la más eficiente transformando
la precipitación en crecidas, seguida por la cuenca Damas. Este comportamiento se refleja en
los mayores promedios de RC y ∆Q. Esto está acorde al mayor porcentaje de suelo agrícola
(81 %) y la menor conductividad hidráulica en las capas más profundas, lo que limita el alma-
cenamiento de humedad y fomenta la aparición de flujo por exceso de infiltración, implicando
un mayor coeficiente de escorrentía (RC) (Rogger et al., 2017). La cuenca Damas, debido a su
menor uso agrícola, está asociada a un coeficiente de escorrentía menor que Chagres, a pesar
de presentar una conductividad hidráulica inferior. Por otro lado, la cuenca Robles muestra la
menor eficiencia en la generación de escorrentía con una conductividad hidráulica alta (entre
17, 9 % y 29, 6 %). Esto se debe a su mayor cobertura forestal (40 %). La literatura documenta
que los suelos forestales presentan una menor alteración antropogénica por labranza o maquina-
ria pesada, conservando una red de macroporos y dinámicas radiculares (de Moraes et al., 2026).
Esto incrementa significativamente la conductividad hidráulica (Zimmermann et al., 2006). Esta
mayor capacidad de infiltración amortigua la respuesta hidrológica, disminuyendo la proporción


=== PÁG 76 del PDF ===
CAPÍTULO 5. DISCUSIÓN
64
de precipitación que se transforma en caudal directo en comparación con cuencas intervenidas
(Neary et al., 2009).
Los valores más altos para el índice de recesión (IV R) y más bajos de K en la cuenca Cha-
gres están asociados a ramas descendentes pronunciadas, junto a una capacidad de drenaje tras
la crecida más rápida en relación a las cuencas Damas y Robles. Un valor bajo de K indica una
recesión rápida, producto de una cuenca con menor retención y circulación de agua (Tallaksen,
1995), lo que está acorde a la degradación de la conductividad hidráulica en el suelo producto del
uso agrícola (Lana-Renault et al., 2014). La rápida recesión también se presenta para un valor
alto de IV R (Rodríguez-Blanco et al., 2012). Por otro lado, las cuencas Damas y Robles están
asociadas a un mayor porcentaje de uso de bosques (27–40 %), por lo que presentaron valores
mayores de K y menores de IV R. A diferencia de la cuenca Chagres, estas presentan mayor
capacidad de almacenamiento, por lo que son más lentas en descargar las crecidas.
5.5.
Implicaciones para la Modelación Hidrológica
La identificación de umbrales no lineales para las métricas de humedad e intensidad confir-
ma que la utilización de modelos hidrológicos lineales no es suficiente para representar fielmente
la complejidad de los mecanismos de la cuenca. La literatura ha documentado extensamente las
críticas hacia las estructuras de modelación lineales y la problemática de emplear ecuaciones
aditivas (Kirchner, 2006; Fenicia et al., 2014). Estas simplificaciones suelen conducir a la so-
breparametrización de los modelos, forzando los términos de calibración para lograr un ajuste
artificial con los datos observados (Beven, 2011). Los resultados obtenidos en las cuencas de
estudio respaldan el uso de modelos que justifiquen su base en la existencia de dinámicas de
umbrales y activación a nivel de cuenca, lo que está acorde a la teoría de llenado y derrame de
McDonnell et al. (2021).
La disparidad en la identificación de umbrales específicos, como la intensidad de precipi-
tación, entre las distintas cuencas confirma la problemática de emplear modelos hidrológicos
simplificados. Que la cuenca Chagres muestre un umbral de activación mientras que Damas no
lo haga, ilustra el riesgo de asumir comportamientos hidrológicos basándose tan solo en clasi-
ficaciones simplificadas de uso de suelo. Asumir un mecanismo de escorrentía por exceso de


=== PÁG 77 del PDF ===
CAPÍTULO 5. DISCUSIÓN
65
infiltración bajo la premisa de que una cuenca pertenece a la categoría agrícola puede provocar
errores importantes de modelación en sistemas donde este proceso no ejerce un control de pri-
mer orden (Lyon et al., 2006). Esto es especialmente riesgoso considerando que este mecanismo
suele utilizarse comúnmente en suelos áridos o severamente compactados (Dunne, 1983).
La identificación del umbral combinado (P[TOT] +ASM100 ) entre 505 y 522 mm demuestra
que la estimación de la humedad antecedente en el perfil de 100 cm constituye el parámetro más
relevante para la predicción de crecidas. Si un modelo hidrológico inicia un evento con un estado
de humedad erróneo, el volumen de la escorrentía simulada también lo será, independientemente
de la resolución de los datos de entrada (Minet et al., 2011). Por lo tanto, la utilidad práctica de
este umbral está en su capacidad para y definir los rangos de valores para activar sistemas de
alerta temprana, en donde ya se han demostrado que su capacidad para predecir correctamente
una crecida depende de la humedad del suelo (Norbiato et al., 2008). Para capturar la activación
no lineal de la cuenca, la modelación debe incorporar la asimilación continua de datos de hu-
medad del suelo, integrando observaciones empíricas para actualizar constantemente el estado
de almacenamiento del reservorio previo al desarrollo de una tormenta, como por ejemplo en el
estudio de Brocca et al. (2010), donde se utilizó información satelital de humedad para mejorar
los modelación de crecidas.


=== PÁG 78 del PDF ===
CAPÍTULO 6. CONCLUSIÓN
66
Capítulo 6
Conclusión
La generación de escorrentía en las cuencas mediterráneas de Robles, Chagres y Damas
está regida por procesos no lineales dependientes de la memoria hidrológica a corto plazo. La
activación de la cuenca necesita de la superación de un umbral combinado de precipitación y
humedad antecedente en los primeros 100 cm del suelo. Este umbral marca el punto crítico en que
la percolación se estanca debido a la menor permeabilidad de los estratos profundos, generando
un nivel freático que satura el perfil superior, produciendo así escorrentía rápida.
La eficiencia con la que esta activación se transforma en caudal directo está dictada por las
alteraciones físicas del uso del suelo. La cuenca con dominancia forestal exhibe la menor efi-
ciencia de escorrentía directa, esto debido a su mayor conductividad hidráulica, lo cual actúa
como amortiguador favoreciendo la infiltración profunda y generando mayor caudal base. En
contraste, la cuenca de predominancia agrícola presenta perfiles de suelo degradados que res-
tringen el drenaje profundo, incrementando significativamente la cantidad de lluvia convertida
en caudal directo y generando hidrogramas de recesión rápida. Esta alteración agrícola intro-
duce un régimen hidrológico mixto, la cuenca presenta un segundo umbral de activación por
intensidad máxima, a partir del cual se detona escorrentía superficial por exceso de infiltración,
independientemente del nivel de saturación previa del suelo.
La complejidad de estos mecanismos confirma que la respuesta del sistema no puede utilizar
un enfoque de modelación lineal o categorizaciones de suelo estáticas. Considerar la humedad
antecedente del perfil y los umbrales son necesarios para representar la generación de caudal y
evitar errores conceptuales en las simulaciones hidrológicas.


=== PÁG 79 del PDF ===
BIBLIOGRAFÍA
67
Bibliografía
Akaike, H. (1974). A new look at the statistical model identification. In Parzen, E., Tanabe, K.,
and Kitagawa, G., editors, Selected Papers of Hirotugu Akaike, Springer Series in Statistics.
Springer, New York, NY.
Ali, G., Oswald, C. J., Spence, C., Cammeraat, E. L. H., McGuire, K. J., Meixner, T., and Reaney,
S. M. (2013). Towards a unified threshold-based hydrological theory: necessary components
and recurring challenges. Hydrological Processes, 27(2):313–318.
Alvarez-Garreton, C. et al. (2021). The impacts of the central Chile megadrought on regional
hydrology. Hydrology and Earth System Sciences, 25(1):125–140.
Beven, K. (2000). Uniqueness of place and process representations in hydrological modelling.
Hydrology and Earth System Sciences, 4(2):203–213.
Beven, K. J. (2011). Rainfall-Runoff Modelling: The Primer. Wiley-Blackwell, Chichester, UK,
2nd edition.
Blume, T., Zehe, E., and Bronstert, A. (2007). Streamflow response to precipitation as an indi-
cator of catchment properties. Journal of Hydrology, 339(3-4):208–222.
Brocca, L., Melone, F., Moramarco, T., Wagner, W., Naeimi, V., Bartalis, Z., and Hasenauer,
S. (2010). Improving runoff prediction through the assimilation of the ascat soil moisture
product. Hydrology and Earth System Sciences, 14(10):1881–1893.
Chow, V. T., Maidment, D. R., and Mays, L. W. (1994). Hidrología aplicada. McGraw-Hill
Interamericana, Bogotá, Colombia.


=== PÁG 80 del PDF ===
BIBLIOGRAFÍA
68
de Moraes, M. T., Grande, L. H. Q., de Moura, G. A., Bieluczyk, W., Alvarez, D. O., de Souza,
L. F., Tsai, S. M., and de Camargo, P. B. (2026). Impacts of forest-to-pasture conversion on
soil water retention in the amazon biome. Forests, 17(2):157.
Detty, J. M. and McGuire, K. J. (2010a). Threshold changes in storm runoff generation at a
till-mantled headwater catchment. Water Resources Research, 46(7):W07525.
Detty, J. M. and McGuire, K. J. (2010b). Threshold changes in storm runoff generation at a
till-mantled headwater catchment. Water Resources Research, 46(7):W07525.
Dinamarca, D. I., Galleguillos, M., Seguel, O., and Faúndez Urbinas, C. (2023). Clsoilmaps: A
national soil gridded database of physical and hydraulic soil properties for Chile. Scientific
Data, 10(1):627.
Dingman, S. L. (2015). Physical Hydrology. Waveland Press, Inc., Long Grove, Illinois, third
edition.
Dunne, T. (1983). Relation of field studies and modeling in the prediction of storm runoff.
Journal of Hydrology, 65:25–48.
Dunne, T. and Black, R. D. (1970). Partial area contributions to storm runoff in a small new
england watershed. Water Resources Research, 6(5):1296–1311.
ESRI (2025). ArcGIS Pro. ESRI, Redlands, California, USA.
Fenicia, F., Kavetski, D., Savenije, H. H. G., Clark, M. P., Schoups, G., Pfister, L., and Freer,
J. (2014). Catchment properties, function, and conceptual model representation: is there a
correspondence? Hydrological Processes, 28:2451–2467.
García-Ruiz, J. M., Regüés, D., Alvera, B., Lana-Renault, N., Serrano-Muela, P., Nadal-Romero,
E., Navas, A., Latron, J., Martí-Bono, C., and Arnáez, J. (2008). Flood generation and sediment
transport in experimental catchments affected by land use changes in the central pyrenees.
Journal of Hydrology, 356:245–260.
Garreaud, R. D. et al. (2020). The central Chile mega drought (2010–2018): A climate dynamics
perspective. International Journal of Climatology, 40(1):421–439.


=== PÁG 81 del PDF ===
BIBLIOGRAFÍA
69
Guy, H. P. (1964). An analysis of some storm-period variables affecting stream sediment trans-
port. Professional Paper 462, US Geological Survey, Washington, DC.
Han, S., Xu, D., and Wang, S. (2012). Runoff formation from experimental plot, field, to small
catchment scales in agricultural north huaihe river plain, china. Hydrology and Earth System
Sciences, 16(9):3115–3125.
Hewlett, J. D. and Hibbert, A. R. (1967). Factors affecting the response of small watersheds to
precipitation in humid areas. pages 275–290.
Hurvich, C. M. and Tsai, C.-L. (1989). Regression and time series model selection in small
samples. Biometrika, 76(2):297–307.
Iroumé, A. et al. (2021). High-frequency monitoring of hydrological and biogeochemical fluxes
in forested catchments of southern Chile. Hydrological Processes, 35(5).
Iroumé, A., Mayen, O., and Huber, A. (2006). Runoff and peak flow responses to timber harvest
and forest age in southern Chile. Hydrological Processes, 20(1):37–50.
James, A. L. and Roulet, N. T. (2007). Investigating hydrologic connectivity and its association
with threshold change in runoff response in a temperate forested watershed. Hydrological
Processes, 21(25):3391–3408.
Kirchner, J. W. (2006).
Getting the right answers for the right reasons: Linking measure-
ments, analyses, and models to advance the science of hydrology. Water Resources Research,
42(W03S04).
Lana-Renault, N., Regüés, D., Serrano, P., and Latron, J. (2014). Spatial and temporal varia-
bility of groundwater dynamics in a sub-mediterranean mountain catchment. Hydrological
Processes, 28:3288–3299.
Little, C., Lara, A., McPhee, J., and Urrutia, R. (2009). Revealing the impact of forest exotic
plantations on water yield in large scale watersheds in south-central Chile. Journal of Hydro-
logy, 374(1-2):162–170.


=== PÁG 82 del PDF ===
BIBLIOGRAFÍA
70
Lyne, V. and Hollick, M. (1979). Stochastic time-variable rainfall-runoff modelling. In Insti-
tute of Engineers Australia National Conference, pages 89–93, Perth, Australia. Institute of
Engineers Australia.
Lyon, S. W., McHale, M. R., Walter, M. T., and Steenhuis, T. S. (2006). The impact of runoff
generation mechanisms on the location of critical source areas. Journal of the American Water
Resources Association, 42(3):793–804.
McDonnell, J. J., Sivapalan, M., Vaché, K., Dunn, S., Grant, G., Haggerty, R., Hinz, C., Hooper,
R., Kirchner, J., Roderick, M. L., Selker, J., and Weiler, M. (2007). Moving beyond hete-
rogeneity and process complexity: A new vision for watershed hydrology. Water Resources
Research, 43(7):W07301.
McDonnell, J. J., Spence, C., Karran, D. J., van Meerveld, H. J. I., and Harman, C. J. (2021).
Fill-and-spill: A process description of runoff generation at the scale of the beholder. Water
Resources Research, 57(5):e2020WR027514.
Merz, R. and Blöschl, G. (2009). A regional analysis of event runoff coefficients with respect to
climate and catchment characteristics in austria. Water Resources Research, 45(1).
Merz, R., Parajka, J., and Blöschl, G. (2009). A regional analysis of event runoff coefficients
with respect to climate and catchment characteristics in austria. Water Resources Research,
45(1):W01405.
Minet, J., Laloy, E., Lambot, S., and Vanclooster, M. (2011). Effect of high-resolution spatial
soil moisture variability on simulated runoff response using a distributed hydrologic model.
Hydrology and Earth System Sciences, 15:1323–1338.
Muggeo, V. M. R. (2003). Estimating regression models with unknown break-points. Statistics
in Medicine, 22(19):3055–3071.
Muñoz Sabater, J. (2019). ERA5-Land hourly data from 1950 to present. https://doi.org/
10.24381/cds.e2161bac.
Nanda, A. and Safeeq, M. (2023). Threshold controlling runoff generation mechanisms in me-
diterranean headwater catchments. Journal of Hydrology, 620:129532.


=== PÁG 83 del PDF ===
BIBLIOGRAFÍA
71
Nathan, R. and McMahon, T. (1990). Evaluation of automated techniques for base flow and
recession analyses. Water Resources Research, 26(7):1465–1473.
Navas, A., Machín, J., Beguería, S., López-Vicente, M., and Gaspar, L. (2008). Soil properties
and physiographic factors controlling the natural vegetation re-growth in a disturbed catch-
ment of the central spanish pyrenees. Agroforestry Systems, 72:173–189.
Neary, D. G., Ice, G. G., and Jackson, C. R. (2009). Linkages between forest soils and water
quality and quantity. Forest Ecology and Management, 258(10):2269–2281.
Norbiato, D., Borga, M., Degli Esposti, S., Gaume, E., and Anquetin, S. (2008). Flash flood
warning based on rainfall thresholds and soil moisture conditions: An assessment for gauged
and ungauged basins. Journal of Hydrology, 362(3-4):274–290.
Onset Computer Corporation (2024). HOBO MX20L Water Level Logger User Guide. Onset
Computer Corporation. Document Number: 29140-A.
Pilgrim, C. (2021). piecewise-regression (aka segmented regression) in python. Journal of Open
Source Software, 6(68):3859.
Pizarro, R., Ausensi, P., Aravena, D., Sangüesa, C., León, L., and Balocchi, F. (2009). Evalua-
ción de métodos hidrológicos para la completación de datos faltantes de precipitación en las
estaciones de la región del maule, Chile. Aqua-LAC, 1(2):172–185.
Pizarro T., R., Soto B., M., Farias D., C., and Jordan D., C. (2005). Aplicación de dos modelos
de simulación integral hidrológica, para la estimación de caudales medios mensuales, en dos
cuencas de Chile central. Bosque, 26(2):123–129.
Pizarro-Tapia, R., Valdés-Pineda, R., Olivares, C., and González, P. A. (2014). Development
of upstream data-input models to estimate downstream peak flow in two mediterranean river
basins of Chile. Open Journal of Modern Hydrology, 4(4):132–143.
Price, K. (2011). Effects of watershed topography, soils, land use, and climate on baseflow
hydrology in humid regions: A review. Progress in Physical Geography, 35(4):465–492.


=== PÁG 84 del PDF ===
BIBLIOGRAFÍA
72
Rivera, D. et al. (2021). Comparison of three daily rainfall-runoff hydrological models using
four evapotranspiration models in four small forested watersheds with different land cover in
south-central Chile. Water, 13(22):3191.
Roa-García, M. C., Brown, S., Schreier, H., and Lavkulich, L. M. (2011). The role of land use and
soils in regulating water flow in small headwater catchments of the andes. Water Resources
Research, 47(5):W05510.
Rodríguez-Blanco, M. L., Taboada-Castro, M. M., and Taboada-Castro, M. T. (2012). Rainfall-
runoff response and event-based runoff coefficients in a humid area (northwest spain). Hy-
drological Sciences Journal, 57(3):445–459.
Rogger, M., Agnoletti, M., Alaoui, A., Bathurst, J. C., Bodner, G., Borga, M., Chaplot, V., Gallart,
F., Glatzel, G., Hall, J., Holden, J., Holko, L., Horn, R., Kiss, A., Kohnová, S., Leitinger, G.,
Lennartz, B., Parajka, J., Perdigão, R., Peth, S., Plavcová, L., Quinton, J. N., Robinson, M.,
Salinas, J. L., Santoro, A., Szolgay, J., Tron, S., van den Akker, J. J. H., Viglione, A., and
Blöschl, G. (2017). Land use change impacts on floods at the catchment scale: Challenges
and opportunities for future research. Water Resources Research, 53:5209–5219.
Ross, C. A., Ali, G. A., Spence, C., and Courchesne, F. (2021).
Evaluating the ubiquity of
thresholds in rainfall-runoff response across contrasting environments. Water Resources Re-
search, 57(1):e2020WR027498. Received 11 MAR 2020, Accepted 7 DEC 2020.
Saffarpour, S., Western, A. W., Adams, R., and McDonnell, J. J. (2016). Multiple runoff pro-
cesses and multiple thresholds control agricultural runoff generation. Hydrology and Earth
System Sciences, 20:4525–4545.
Sakamoto, Y., Ishiguro, M., and Kitagawa, G. (1986). Akaike Information Criterion Statistics.
Mathematics and Its Applications (Japanese Series). D. Reidel Publishing Company, Dor-
drecht, Holland. Translation of: Johoryo tokeigaku.
Silasari, R., Parajka, J., Ressl, C., Strauss, P., and Blöschl, G. (2017). Potential of time-lapse
photography for identifying saturation area dynamics on agricultural hillslopes. Hydrological
Processes, 31(20):3610–3627.


=== PÁG 85 del PDF ===
BIBLIOGRAFÍA
73
Sittner, W. T., Schauss, C. E., and Monro, J. C. (1969). Continuous hydrograph synthesis with
an API-type hydrologic model. Water Resources Research, 5(5):1007–1022.
Smakhtin, V. U. (2001). Low flow hydrology: a review. Journal of Hydrology, 240(3-4):147–
186.
Soil Science Division Staff (2017). Soil Survey Manual. USDA Handbook No. 18. United States
Department of Agriculture (USDA), Washington, D.C.
Spence, C. (2010). A paradigm shift in hydrology: storage thresholds across scales influence
catchment runoff generation. Journal of Hydrology, 381(3-4):353–365.
Stowhas B., L. (2016). Fundamentos de Hidrología Aplicada. Sello Editorial USM, Valparaíso,
Chile.
Tallaksen, L. M. (1995).
A review of baseflow recession analysis.
Journal of Hydrology,
165:349–370.
Tang, W. and Carey, S. K. (2017). Hydrun: A matlab toolbox for rainfall-runoff analysis. Hy-
drological Processes. Accepted for publication.
The MathWorks Inc. (2023). MATLAB. The MathWorks Inc., Natick, Massachusetts, USA.
Tromp-van Meerveld, H. J. and McDonnell, J. J. (2006).
Threshold relations in subsurfa-
ce stormflow: 1. a 147-storm analysis of the panola hillslope. Water Resources Research,
42(2):W02410.
US Department of Agriculture, Natural Resources Conservation Service (2009). Chapter 7:
Hydrologic Soil Groups. National Engineering Handbook, Part 630 Hydrology. USDA-NRCS,
Washington, DC. (210-VI-NEH, issued January 2009).
Vreugdenhil, M., Széles, B., Parajka, J., Strauss, P., and Blöschl, G. (2022). Non-linearity in event
runoff generation in a small agricultural catchment. Hydrological Processes, 36(8):e14675.
Zehe, E. and Sivapalan, M. (2009). Threshold behaviour in hydrological systems as (human) geo-
ecosystems: manifestations, controls, implications. Hydrology and Earth System Sciences,
13(7):1273–1297.


=== PÁG 86 del PDF ===
BIBLIOGRAFÍA
74
Zimmermann, B., Elsenbeer, H., and De Moraes, J. M. (2006). The influence of land-use changes
on soil hydraulic properties: Implications for runoff generation. Forest Ecology and Manage-
ment, 222(1-3):29–38.


=== PÁG 87 del PDF ===
75
Anexos


=== PÁG 88 del PDF ===
ANEXO I. DATOS BRUTOS
76
Anexo I
Datos Brutos
Tabla I.1: Estadísticas de parámetros de suelo por capa y cuenca.
Fuente: Elaboración propia a partir de datos de Dinamarca et al.
(2023).
Cuenca
Capa
Variable
Min
P10
P25 Mediana
Media
P75
P90
Chagres 0-5cm
alpha
0,005
0,006
0,007
0,008
0,008
0,009
0,009
Chagres 0-5cm
AvMoist
0,131
0,140
0,143
0,150
0,152
0,160
0,168
Chagres 0-5cm
AWC
6,548
6,994
7,164
7,521
7,615
8,013
8,385
Chagres 0-5cm
FC
0,278
0,292
0,296
0,303
0,304
0,311
0,318
Chagres 0-5cm
ksat
5,644
7,843
9,023
10,713
10,962
12,512
14,466
Chagres 0-5cm
n
1,291
1,334
1,345
1,365
1,368
1,391
1,405
Chagres 0-5cm
PWP
0,122
0,140
0,145
0,152
0,152
0,158
0,162
Chagres 0-5cm
theta_r
0,080
0,091
0,094
0,097
0,097
0,100
0,103
Chagres 0-5cm
theta_s
0,382
0,394
0,399
0,405
0,406
0,412
0,420
Chagres 5-15cm
alpha
0,006
0,007
0,008
0,009
0,009
0,011
0,012
Chagres 5-15cm
AvMoist
0,111
0,120
0,125
0,132
0,134
0,143
0,151
Chagres 5-15cm
AWC
11,070
11,961
12,541
13,212
13,407
14,330
15,113
Chagres 5-15cm
FC
0,260
0,276
0,282
0,290
0,291
0,299
0,308
Chagres 5-15cm
ksat
3,123
4,987
6,267
7,984
8,254
9,993
11,784
Continúa en la siguiente página...
1


=== PÁG 89 del PDF ===
ANEXO I. DATOS BRUTOS
77
Tabla I.1 – Continuación de la página anterior
Cuenca
Capa
Variable
Min
P10
P25 Mediana
Media
P75
P90
Chagres 5-15cm
n
1,254
1,294
1,307
1,324
1,326
1,348
1,361
Chagres 5-15cm
PWP
0,138
0,149
0,153
0,157
0,157
0,161
0,165
Chagres 5-15cm
theta_r
0,089
0,095
0,097
0,099
0,099
0,101
0,103
Chagres 5-15cm
theta_s
0,355
0,369
0,378
0,388
0,390
0,402
0,413
Chagres 15-30cm
alpha
0,005
0,006
0,006
0,007
0,007
0,008
0,009
Chagres 15-30cm
AvMoist
0,137
0,144
0,148
0,154
0,156
0,164
0,173
Chagres 15-30cm
AWC
20,589
21,665
22,175
23,170
23,470
24,555
25,915
Chagres 15-30cm
FC
0,274
0,285
0,291
0,298
0,299
0,306
0,313
Chagres 15-30cm
ksat
6,834
9,256
10,370
11,855
12,285
13,738
16,278
Chagres 15-30cm
n
1,348
1,365
1,373
1,385
1,390
1,405
1,426
Chagres 15-30cm
PWP
0,127
0,136
0,138
0,143
0,142
0,146
0,149
Chagres 15-30cm
theta_r
0,083
0,088
0,090
0,092
0,092
0,094
0,096
Chagres 15-30cm
theta_s
0,375
0,391
0,395
0,403
0,403
0,408
0,415
Chagres 30-60cm
alpha
0,005
0,006
0,007
0,008
0,008
0,009
0,009
Chagres 30-60cm
AvMoist
0,129
0,136
0,140
0,146
0,149
0,158
0,168
Chagres 30-60cm
AWC
38,658
40,898
41,998
43,828
44,796
47,260
50,409
Chagres 30-60cm
FC
0,278
0,290
0,295
0,303
0,303
0,309
0,316
Chagres 30-60cm
ksat
4,766
6,935
7,982
9,564
10,246
12,007
14,767
Chagres 30-60cm
n
1,313
1,333
1,338
1,349
1,360
1,379
1,405
Chagres 30-60cm
PWP
0,131
0,144
0,149
0,154
0,153
0,158
0,162
Chagres 30-60cm
theta_r
0,086
0,093
0,096
0,098
0,098
0,101
0,102
Chagres 30-60cm
theta_s
0,379
0,389
0,394
0,404
0,404
0,411
0,420
Chagres 60-100cm
alpha
0,006
0,007
0,008
0,009
0,009
0,010
0,010
Chagres 60-100cm
AvMoist
0,110
0,126
0,130
0,135
0,136
0,141
0,146
Chagres 60-100cm
AWC
44,024
50,322
52,003
54,083
54,213
56,322
58,462
Chagres 60-100cm
FC
0,267
0,285
0,290
0,296
0,296
0,302
0,307
Chagres 60-100cm
ksat
2,887
4,898
5,658
6,584
6,826
7,616
8,978
Chagres 60-100cm
n
1,261
1,299
1,309
1,323
1,326
1,341
1,360
Continúa en la siguiente página...
1


=== PÁG 90 del PDF ===
ANEXO I. DATOS BRUTOS
78
Tabla I.1 – Continuación de la página anterior
Cuenca
Capa
Variable
Min
P10
P25 Mediana
Media
P75
P90
Chagres 60-100cm
PWP
0,134
0,149
0,155
0,162
0,160
0,166
0,169
Chagres 60-100cm
theta_r
0,085
0,095
0,098
0,102
0,101
0,104
0,105
Chagres 60-100cm
theta_s
0,354
0,374
0,381
0,388
0,388
0,395
0,402
Chagres 100-200cm
alpha
0,006
0,007
0,008
0,009
0,009
0,010
0,011
Chagres 100-200cm
AvMoist
0,103
0,118
0,123
0,129
0,129
0,134
0,140
Chagres 100-200cm
AWC 103,183 117,835 123,122 129,146 128,998 134,481 139,823
Chagres 100-200cm
FC
0,255
0,276
0,281
0,288
0,288
0,295
0,301
Chagres 100-200cm
ksat
2,281
4,177
4,809
5,691
5,935
6,798
7,851
Chagres 100-200cm
n
1,239
1,280
1,297
1,316
1,316
1,333
1,350
Chagres 100-200cm
PWP
0,126
0,145
0,153
0,160
0,159
0,166
0,172
Chagres 100-200cm
theta_r
0,081
0,092
0,096
0,100
0,099
0,103
0,106
Chagres 100-200cm
theta_s
0,338
0,363
0,370
0,378
0,378
0,385
0,391
Chagres 0-200cm
Total_AWC 228,571 252,025 260,525 271,331 272,500 283,861 295,210
Damas
0-5cm
alpha
0,005
0,006
0,007
0,008
0,008
0,008
0,009
Damas
0-5cm
AvMoist
0,131
0,139
0,141
0,146
0,148
0,152
0,162
Damas
0-5cm
AWC
6,555
6,949
7,071
7,289
7,405
7,616
8,115
Damas
0-5cm
FC
0,273
0,288
0,294
0,302
0,302
0,308
0,315
Damas
0-5cm
ksat
5,649
6,980
7,748
8,929
9,446
10,619
12,403
Damas
0-5cm
n
1,290
1,335
1,345
1,355
1,358
1,370
1,386
Damas
0-5cm
PWP
0,127
0,145
0,149
0,153
0,154
0,158
0,162
Damas
0-5cm
theta_r
0,083
0,093
0,096
0,098
0,098
0,101
0,103
Damas
0-5cm
theta_s
0,377
0,388
0,393
0,399
0,401
0,408
0,415
Damas
5-15cm
alpha
0,006
0,008
0,008
0,009
0,010
0,011
0,012
Damas
5-15cm
AvMoist
0,108
0,114
0,119
0,124
0,126
0,131
0,145
Damas
5-15cm
AWC
10,768
11,422
11,878
12,357
12,646
13,118
14,530
Damas
5-15cm
FC
0,258
0,274
0,280
0,286
0,287
0,293
0,303
Damas
5-15cm
ksat
2,745
3,812
4,691
5,759
6,373
7,458
9,603
Damas
5-15cm
n
1,259
1,281
1,289
1,301
1,307
1,319
1,347
Continúa en la siguiente página...
1


=== PÁG 91 del PDF ===
ANEXO I. DATOS BRUTOS
79
Tabla I.1 – Continuación de la página anterior
Cuenca
Capa
Variable
Min
P10
P25 Mediana
Media
P75
P90
Damas
5-15cm
PWP
0,139
0,153
0,157
0,161
0,161
0,165
0,168
Damas
5-15cm
theta_r
0,089
0,096
0,098
0,100
0,100
0,102
0,104
Damas
5-15cm
theta_s
0,347
0,359
0,366
0,376
0,379
0,386
0,403
Damas
15-30cm
alpha
0,005
0,006
0,007
0,007
0,007
0,008
0,008
Damas
15-30cm
AvMoist
0,135
0,144
0,146
0,151
0,153
0,159
0,167
Damas
15-30cm
AWC
20,186
21,530
21,930
22,657
23,011
23,853
25,095
Damas
15-30cm
FC
0,269
0,280
0,286
0,293
0,294
0,301
0,308
Damas
15-30cm
ksat
6,572
8,266
9,507
10,718
11,099
12,354
14,034
Damas
15-30cm
n
1,348
1,368
1,375
1,384
1,388
1,400
1,417
Damas
15-30cm
PWP
0,124
0,134
0,137
0,141
0,141
0,144
0,148
Damas
15-30cm
theta_r
0,081
0,087
0,089
0,091
0,091
0,093
0,095
Damas
15-30cm
theta_s
0,376
0,385
0,388
0,394
0,396
0,402
0,410
Damas
30-60cm
alpha
0,005
0,007
0,007
0,008
0,008
0,009
0,009
Damas
30-60cm
AvMoist
0,126
0,133
0,136
0,141
0,144
0,147
0,161
Damas
30-60cm
AWC
37,654
39,910
40,883
42,281
43,078
44,063
48,412
Damas
30-60cm
FC
0,278
0,287
0,292
0,299
0,299
0,304
0,311
Damas
30-60cm
ksat
4,250
5,876
6,528
7,528
8,356
9,285
12,120
Damas
30-60cm
n
1,301
1,324
1,331
1,342
1,348
1,355
1,388
Damas
30-60cm
PWP
0,138
0,148
0,151
0,155
0,155
0,159
0,163
Damas
30-60cm
theta_r
0,090
0,095
0,096
0,099
0,099
0,101
0,103
Damas
30-60cm
theta_s
0,372
0,383
0,387
0,393
0,395
0,401
0,412
Damas
60-100cm
alpha
0,006
0,007
0,008
0,008
0,009
0,009
0,010
Damas
60-100cm
AvMoist
0,099
0,121
0,128
0,133
0,133
0,138
0,144
Damas
60-100cm
AWC
39,519
48,544
51,177
53,180
53,209
55,277
57,600
Damas
60-100cm
FC
0,267
0,286
0,291
0,297
0,297
0,304
0,309
Damas
60-100cm
ksat
1,998
4,034
4,998
6,056
6,214
7,172
8,423
Damas
60-100cm
n
1,243
1,290
1,302
1,314
1,316
1,330
1,346
Damas
60-100cm
PWP
0,142
0,154
0,160
0,165
0,164
0,169
0,173
Continúa en la siguiente página...
1


=== PÁG 92 del PDF ===
ANEXO I. DATOS BRUTOS
80
Tabla I.1 – Continuación de la página anterior
Cuenca
Capa
Variable
Min
P10
P25 Mediana
Media
P75
P90
Damas
60-100cm
theta_r
0,090
0,097
0,100
0,103
0,103
0,105
0,107
Damas
60-100cm
theta_s
0,332
0,368
0,379
0,387
0,387
0,395
0,402
Damas
100-200cm
alpha
0,006
0,008
0,008
0,009
0,009
0,010
0,011
Damas
100-200cm
AvMoist
0,100
0,116
0,121
0,126
0,126
0,131
0,136
Damas
100-200cm
AWC
99,930 115,802 121,048 125,758 125,883 131,100 135,724
Damas
100-200cm
FC
0,258
0,279
0,284
0,290
0,290
0,295
0,301
Damas
100-200cm
ksat
2,012
3,549
4,307
5,124
5,234
6,123
6,964
Damas
100-200cm
n
1,236
1,276
1,288
1,302
1,303
1,318
1,331
Damas
100-200cm
PWP
0,135
0,154
0,160
0,165
0,164
0,169
0,173
Damas
100-200cm
theta_r
0,085
0,096
0,099
0,102
0,102
0,104
0,106
Damas
100-200cm
theta_s
0,337
0,361
0,369
0,377
0,376
0,383
0,390
Damas
0-200cm
Total_AWC 218,261 247,049 255,365 263,588 265,231 274,806 284,810
Robles
0-5cm
alpha
0,004
0,006
0,006
0,007
0,007
0,008
0,009
Robles
0-5cm
AvMoist
0,126
0,142
0,150
0,160
0,172
0,200
0,213
Robles
0-5cm
AWC
6,278
7,095
7,506
7,999
8,609
10,006
10,654
Robles
0-5cm
FC
0,275
0,293
0,301
0,313
0,327
0,358
0,372
Robles
0-5cm
ksat
4,500
8,827
10,482
13,184
33,562
52,627
90,598
Robles
0-5cm
n
1,292
1,341
1,359
1,384
1,385
1,409
1,429
Robles
0-5cm
PWP
0,120
0,143
0,149
0,155
0,155
0,161
0,165
Robles
0-5cm
theta_r
0,079
0,092
0,095
0,098
0,098
0,101
0,104
Robles
0-5cm
theta_s
0,366
0,397
0,404
0,416
0,441
0,488
0,512
Robles
5-15cm
alpha
0,005
0,007
0,008
0,009
0,009
0,010
0,011
Robles
5-15cm
AvMoist
0,114
0,127
0,134
0,144
0,149
0,167
0,176
Robles
5-15cm
AWC
11,387
12,677
13,360
14,368
14,938
16,707
17,644
Robles
5-15cm
FC
0,259
0,283
0,290
0,302
0,308
0,329
0,339
Robles
5-15cm
ksat
3,828
6,469
7,782
10,225
15,796
22,268
33,187
Robles
5-15cm
n
1,277
1,310
1,326
1,345
1,346
1,366
1,384
Robles
5-15cm
PWP
0,137
0,150
0,154
0,159
0,159
0,164
0,168
Continúa en la siguiente página...
1


=== PÁG 93 del PDF ===
ANEXO I. DATOS BRUTOS
81
Tabla I.1 – Continuación de la página anterior
Cuenca
Capa
Variable
Min
P10
P25 Mediana
Media
P75
P90
Robles
5-15cm
theta_r
0,088
0,095
0,098
0,100
0,100
0,103
0,106
Robles
5-15cm
theta_s
0,359
0,383
0,390
0,403
0,418
0,452
0,467
Robles
15-30cm
alpha
0,004
0,005
0,006
0,007
0,007
0,008
0,008
Robles
15-30cm
AvMoist
0,127
0,147
0,154
0,166
0,178
0,207
0,221
Robles
15-30cm
AWC
19,047
22,056
23,034
24,846
26,689
31,071
33,114
Robles
15-30cm
FC
0,266
0,287
0,295
0,306
0,323
0,359
0,374
Robles
15-30cm
ksat
4,820
10,268
12,020
15,045
39,552
63,502 106,033
Robles
15-30cm
n
1,331
1,370
1,383
1,408
1,409
1,431
1,450
Robles
15-30cm
PWP
0,123
0,134
0,139
0,144
0,145
0,151
0,157
Robles
15-30cm
theta_r
0,081
0,087
0,090
0,093
0,093
0,096
0,099
Robles
15-30cm
theta_s
0,359
0,394
0,401
0,411
0,438
0,488
0,512
Robles
30-60cm
alpha
0,004
0,006
0,007
0,007
0,007
0,008
0,009
Robles
30-60cm
AvMoist
0,127
0,140
0,147
0,159
0,168
0,190
0,208
Robles
30-60cm
AWC
38,228
42,125
44,044
47,827
50,451
57,060
62,447
Robles
30-60cm
FC
0,276
0,294
0,301
0,312
0,322
0,347
0,361
Robles
30-60cm
ksat
5,002
8,353
9,853
13,069
27,461
37,763
73,526
Robles
30-60cm
n
1,312
1,335
1,349
1,374
1,382
1,415
1,434
Robles
30-60cm
PWP
0,127
0,141
0,148
0,154
0,154
0,159
0,167
Robles
30-60cm
theta_r
0,083
0,091
0,095
0,098
0,098
0,101
0,105
Robles
30-60cm
theta_s
0,374
0,396
0,403
0,415
0,434
0,471
0,495
Robles
60-100cm
alpha
0,005
0,006
0,007
0,008
0,008
0,009
0,010
Robles
60-100cm
AvMoist
0,099
0,122
0,128
0,137
0,146
0,157
0,187
Robles
60-100cm
AWC
39,790
48,744
51,357
54,983
58,217
62,793
74,669
Robles
60-100cm
FC
0,257
0,281
0,289
0,297
0,305
0,314
0,345
Robles
60-100cm
ksat
1,752
4,252
5,462
7,378
13,845
13,684
34,369
Robles
60-100cm
n
1,236
1,289
1,307
1,331
1,340
1,373
1,407
Robles
60-100cm
PWP
0,129
0,145
0,152
0,161
0,159
0,166
0,173
Robles
60-100cm
theta_r
0,083
0,092
0,097
0,101
0,100
0,103
0,107
Continúa en la siguiente página...
1


=== PÁG 94 del PDF ===
ANEXO I. DATOS BRUTOS
82
Tabla I.1 – Continuación de la página anterior
Cuenca
Capa
Variable
Min
P10
P25 Mediana
Media
P75
P90
Robles
60-100cm
theta_s
0,337
0,365
0,378
0,392
0,404
0,423
0,469
Robles
100-200cm
alpha
0,005
0,007
0,008
0,009
0,009
0,010
0,010
Robles
100-200cm
AvMoist
0,099
0,116
0,122
0,132
0,140
0,153
0,185
Robles
100-200cm
AWC
99,499 115,696 121,980 131,699 140,350 153,127 184,527
Robles
100-200cm
FC
0,248
0,275
0,282
0,292
0,301
0,316
0,345
Robles
100-200cm
ksat
1,974
3,615
4,639
6,344
12,421
13,009
32,986
Robles
100-200cm
n
1,225
1,280
1,297
1,320
1,328
1,352
1,391
Robles
100-200cm
PWP
0,129
0,148
0,155
0,161
0,161
0,167
0,173
Robles
100-200cm
theta_r
0,081
0,093
0,097
0,100
0,100
0,104
0,107
Robles
100-200cm
theta_s
0,327
0,357
0,367
0,382
0,398
0,423
0,468
Robles
0-200cm
Total_AWC 222,649 252,198 262,230 281,676 299,254 331,974 377,255
Tabla I.2: Porcentaje de textura de suelo y conductividad hidráulica promedio Ks para cada
cuenca y profundidad específica. Fuente: Elaboración propia a partir de datos Dinamarca et al.
(2023).
Basin
Depth_Lay %_Cl %_ClLo %_Lo %_LoSa %_Sa %_SaCl %_SaClLo %_SaLo %_SiCl %_SiClLo %_SiLo Kc_promed
Chagres 0-5cm
0
39,09
58,57
0
0
0
1,48
0
0
0
0,85
10,9622
Chagres 5-15cm
0
45,6
17,31
0
0
0
37,09
0
0
0
0
8,2536
Chagres 15-30cm
0
0,52
96,68
0
0
0
0
0
0
0
2,8
12,285
Chagres 30-60cm
0
51,52
46,15
0
0
0
2,3
0
0
0
0,03
10,2461
Chagres 60-100cm
0
73,09
22,28
0
0
0
4,64
0
0
0
0
6,8264
Chagres 100-200cm
0
57,2
28,97
0
0
1,51
12,32
0
0
0
0
5,9349
Damas
0-5cm
0
47,26
52,32
0
0
0
0,17
0
0
0
0,25
9,4458
Damas
5-15cm
0
57,25
6,54
0
0
0
36,22
0
0
0
0
6,3735
Damas
15-30cm
0
0,64
97,75
0
0
0
0
0
0
0
1,61
11,0988
Damas
30-60cm
0
59,22
40,39
0
0
0
0,39
0
0
0
0
8,356
Damas
60-100cm
0
88,51
10,68
0
0
0
0,81
0
0
0
0
6,2142
Damas
100-200cm
0,14
82,2
11,24
0
0
0,17
6,26
0
0
0
0
5,234
Robles
0-5cm
0,01
32,79
65,06
0
0
0
1,68
0
0
0
0,46
33,5618
Robles
5-15cm
0
52,45
19,48
0
0
0
28,07
0
0
0
0
15,7963
Robles
15-30cm
0
1,92
94,43
0
0
0
0,14
0
0
0
3,51
39,5523
Robles
30-60cm
0
42,96
54,47
0
0
0
1,99
0
0
0
0,57
27,461
Robles
60-100cm
0
57,01
39,29
0
0
0
3,65
0
0
0
0,04
13,8453
Robles
100-200cm
0,06
63,97
27,93
0
0
0,11
7,93
0
0
0
0
12,4207


=== PÁG 95 del PDF ===
ANEXO I. DATOS BRUTOS
83
Figura I.1: Relación entre escorrentía total RTOT y métricas predictoras meteorológicas para la
cuenca Chagres. Fuente: Elaboración propia.


=== PÁG 96 del PDF ===
ANEXO I. DATOS BRUTOS
84
Figura I.2: Relación entre escorrentía total RTOT y métricas predictoras meteorológicas para la
cuenca Damas. Fuente: Elaboración propia.


=== PÁG 97 del PDF ===
ANEXO I. DATOS BRUTOS
85
Figura I.3: Relación entre escorrentía total RTOT y métricas predictoras meteorológicas para la
cuenca Robles. Fuente: Elaboración propia.
