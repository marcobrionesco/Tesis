# Manual ETABS v9.7.4 (UCM, 2024) — texto extraído

> Copia en texto (pymupdf). No mencionar ETABS en la tesis.

```text

=== PÁG 1 ===
                                                                                                
 
 
 
 
 
 
 
 
MANUAL DE MODELACIÓN, ANÁLISIS Y DISEÑO 
ESTRUCTURAL EN ETABS v.9.7.4 
 
 
 
INGENIERÍA CIVIL 
DEPARTAMENTO DE OBRAS CIVILES 
 
UNIVERSIDAD CATÓLICA DEL MAULE 
 
 
REV 
Fecha 
Emitido para 
Elaborado por 
Aprobado por 
0 
15/03/2024 
Utilización 
Javiera Morales Matamala 
Juan Pablo Venegas Zurita 

=== PÁG 2 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
2 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
Índice 
1. 
Introducción ................................................................................................................................ 5 
2. 
Empezar un Nuevo Modelo ......................................................................................................... 6 
2.1 Definir la Grilla Horizontal (Planta) ......................................................................................... 7 
2.2 Definir la Grilla Vertical (Elevación) ........................................................................................ 9 
2.3 Editar Grilla Horizontal ......................................................................................................... 11 
2.4 Editar Grilla Vertical .............................................................................................................. 11 
2.5 Insertar Nivel ........................................................................................................................ 11 
2.6 Borrar Nivel ........................................................................................................................... 12 
2.7 Editar y Agregar: Planos de Referencia ................................................................................. 12 
2.8 Editar y Agregar: Líneas de Referencia ................................................................................. 12 
3. 
Herramientas Principales ........................................................................................................... 13 
3.1 Vista Renderizada del Modelo .............................................................................................. 14 
3.2 Código de diseño .................................................................................................................. 14 
4. 
Opciones de Visualización del Modelo ...................................................................................... 15 
5. 
Herramientas Gráficas ............................................................................................................... 16 
6. 
Definir Materiales ...................................................................................................................... 17 
7. 
Definir Elementos Lineales ........................................................................................................ 18 
8. 
Definir Secciones de Muros y Losas ........................................................................................... 21 
9. 
Herramientas De Dibujo ............................................................................................................ 22 
9.1 Snap To ................................................................................................................................. 22 
9.2 Puntos ................................................................................................................................... 23 
9.3 Elementos lineales ................................................................................................................ 23 
9.4 Ajuste de Propiedades de Frames ........................................................................................ 24 
9.4.1 End (Length) Offsets – Cachos rígidos ............................................................................. 24 
9.4.2 Insertion Point ................................................................................................................. 24 
9.4.3 Local Axes ........................................................................................................................ 25 
9.5 Elementos de área ................................................................................................................ 25 
9.5.1 Vigas Como Elemento de Área ........................................................................................ 26 
9.6 Consejos Para Dibujar ........................................................................................................... 26 
9.6.1 Similar Stories .................................................................................................................. 26 
9.6.2 Replicate .......................................................................................................................... 26 

=== PÁG 3 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
3 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
10. Definir Apoyos ........................................................................................................................... 27 
11. Definir Condiciones de Borde .................................................................................................... 28 
11.1 Condición de Borde de Vigas ................................................................................................ 28 
11.2 Condición de Borde de Muros .............................................................................................. 28 
12. Estados De Carga Gravitacional ................................................................................................. 29 
13. Definir y Asignar Diafragmas ..................................................................................................... 29 
14. Estados de Carga Sísmicos ......................................................................................................... 31 
14.1 Análisis Estático Equivalente ................................................................................................ 31 
14.2 Por Gravedad o Coeficiente .................................................................................................. 31 
14.3 Análisis Modal Espectral ....................................................................................................... 32 
14.3.1 Definir el Espectro de Diseño........................................................................................ 32 
14.3.2 Ingresar los Estados de Carga Sísmicos ......................................................................... 33 
14.3.3 Definir Mass Source ...................................................................................................... 34 
15. Combinaciones De Carga ........................................................................................................... 35 
16. Asignar Cargas ........................................................................................................................... 36 
16.1 Visualización de Cargas Aplicadas ........................................................................................ 37 
16.2 Asignar y Visualizar Cargas Inclinadas .................................................................................. 37 
17. Mesh .......................................................................................................................................... 38 
17.1 Mesh en Losas ...................................................................................................................... 38 
17.2 Mesh en Muros .................................................................................................................... 39 
18. Identificación de Elementos: Piers y Spandrels ......................................................................... 41 
18.1 Asignación de Pier ................................................................................................................ 41 
18.2 Asignación de Spandrel ........................................................................................................ 41 
18.3 Notación recomendada ........................................................................................................ 41 
19. Definir Tipo De Análisis y Checkear El Modelo .......................................................................... 42 
20. Análisis y Resultados .................................................................................................................. 43 
20.1 Obtención de Tablas de Resultados ...................................................................................... 43 
20.2 Resultados debido al Análisis Dinámico ............................................................................... 44 
20.2.1 Modos de vibrar y Períodos de la estructura ................................................................ 44 
20.2.2 Peso sísmico y Corte basal directo ................................................................................ 44 
20.2.3 Centro de masa y Centro de rigidez .............................................................................. 45 
20.2.4 Desplazamiento Lateral ................................................................................................ 45 

=== PÁG 4 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
4 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
20.3 Calibración Sismo para Método Modal Espectral ................................................................ 46 
20.4 Vigas en ETABS ...................................................................................................................... 47 
20.4.1 Diseño de Vigas a Flexión – Carga Axial (Frames) ......................................................... 47 
20.4.2 Diseño de Vigas a Corte (Frames) ................................................................................. 48 
20.4.3 Diseño de Vigas a Flexión – Carga Axial y Corte (Spandrel) .......................................... 48 
20.4.4 Presentación de Gráficos .............................................................................................. 49 
20.4.5 Extracción de Tablas ...................................................................................................... 49 
20.5 Verificación Columna Fuerte – Viga Débil ............................................................................ 50 
20.6 Muros en ETABS .................................................................................................................... 50 
20.6.1 Diseño de Muros a Flexión – Carga Axial ...................................................................... 50 
20.6.2 Diseño de Muros a Corte .............................................................................................. 51 
20.6.3 Presentación de Gráficos .............................................................................................. 51 
20.6.4 Extracción de Tablas ...................................................................................................... 52 
20.7 Curva Interacción .................................................................................................................. 52 
21. Referencias ................................................................................................................................ 54 
 
 
 
 

=== PÁG 5 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
5 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
1. 
Introducción 
El Manual que se presenta a continuación, tiene la finalidad de entregar el paso a paso en la modelación y obtención de resultados 
a partir del análisis estructural de problemas físicos. 
El uso de este manual de modelación, análisis y diseño estructural con ETABS, está dirigido a estudiantes de último año de 
Ingeniería Civil de la Universidad Católica del Maule, especialmente a aquellos que cursan las siguientes asignaturas:  
✓ Diseño en Hormigón Armado. 
✓ Fundamentos del Diseño Estructural en Acero. 
✓ Ingeniería Antisísmica. 
✓ Diseño en Acero. 
✓ Diseño en Madera. 
ETABS, por sus siglas: Extended Three Dimensional Analysis of Building Systems, es un programa que ha sido desarrollado para 
un análisis estático y dinámico de edificaciones y naves industriales, lo que permite realizar modelos con una aproximación a la 
realidad. Además, ofrece una interfaz gráfica fácil y completa. 
Por último, tiene la capacidad de importar el modelo desde Autocad y exportar los resultados a diferentes programas como: 
SAP2000, SAFE, Microsoft Excel, entre otros. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

=== PÁG 6 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
6 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
2. 
Empezar un Nuevo Modelo 
Al abrir el archivo ejecutable (.EDB), aparece una ventana con “tips”, los cuales son recomendaciones para la utilización del 
programa, como se muestra en la imagen 1. Cabe mencionar, que cada vez que se inicie el programa aparecerá un 
consejo/sugerencia diferente. 
 
Imagen 1.  
Al presionar “Ok o X”, aparece la ventana de trabajo, donde lo primero es definir las unidades de medidas para el trabajo en la 
esquina inferior derecha de la pantalla. Se consideran las unidades para el análisis y diseño en sistema internacional (ton-m ó 
kg-cm), como se presenta en la imagen 2.  
Luego, para crear un nuevo modelo se presiona “File” → “New Model” o el icono 
 que aparece en la barra de herramientas 
principal en la esquina superior izquierda. 
 
Imagen 3. 
En la ventana de New Model Initialization, se presentan 3 opciones distintas para comenzar con el proyecto: 
   
Imagen 4. 
La opción “Choose.edb” permite crear un archivo 
nuevo en el que se utilizan propiedades previamente 
definidas en un modelo anterior (materiales, secciones, 
combinaciones de carga) y preferencias necesarias para 
hacer el análisis. Este podría elegirse si se trabaja con 
proyectos similares. 
La opción “Default.edb” es elegida cuando se quiere 
trabajar con las condiciones por default que vienen con el 
software.  
Por último, la opción “No”, permite que el usuario 
defina y edite todos los parámetros según la necesidad del 
proyecto a ejecutar. Se recomienda utilizar esta opción. 
 
 
 
 
Imagen 2. 

=== PÁG 7 ===
 
2.1 
Definir la Grilla Horizontal (Planta) 
Al presionar la opción “No” en el apartado anterior, aparece la ventana de Building Plan Grid System and Story Data Definition, 
la cual permite crear las dimensiones de la grilla (planta) y pisos (elevación).  
✓ Si el modelo cuenta con un proyecto arquitectónico, se recomienda utilizar la misma numeración de ejes en planta; 
mientras que, si no cuenta, se recomienda generar ejes que coincidan con los centroides de los elementos 
estructurales verticales ya que es beneficioso para el dibujo del modelo luego. De todas formas, se puede trabajar sin 
ella. 
Para definir la grilla horizontal se trabaja con la parte izquierda de la ventana, como se muestra en la imagen 5. Esta nos permite 
determinar cuál será el espacio de trabajo en el plano cartesiano.  
 → Se tienen dos opciones de definición de grilla:  
 
Imagen 5. 
 
 La primera es Uniform Grid Spacing, esta permite 
definir la cantidad de ejes en X y en Y, además del 
espaciamiento que existe entre ellos. Esta opción se utiliza 
solo cuando la distancia entre ejes es igual, y ocurre para 
ambas direcciones, independiente que sea o no el mismo 
valor. 
 La segunda opción, Custom Grid Spacing, permite 
definir cada una de las distancias entre ejes en ambas 
direcciones cuando no se tiene la misma separación entre 
ellos, se selecciona la alternativa “Grid Labels” que se 
muestra en la imagen 6: 
 
Imagen 6. 
 
Imagen 7. 
Luego, al presionar la alternativa “Edit Grid” aparece una nueva ventana que 
presenta donde se ingresarán los datos para la definición de la grilla horizontal 
tanto para X como en Y: 
Esta ventana permite 
definir 
la 
identificación 
que 
tendrá 
en 
cada 
dirección la malla, 
además 
de 
la 
dirección por la que 
comenzará la etiqueta 
de identificación. 
Etiqueta del eje X-X, en este caso comienza con la 
letra A. 
 
Etiqueta comienza de izquierda a derecha. 
Etiqueta comienza de derecha a izquierda. 
 
Etiqueta del eje Y-Y, en este caso comienza con el 
número 1. 
 
Etiqueta comienza de abajo hacia arriba. 
Etiqueta comienza de arriba hacia abajo. 
 
Imagen 8. 

=== PÁG 8 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
8 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
En el apartado de Display Grids as se tienen dos opciones con las que trabajar: Ordinates, realiza la separación entre ejes con 
distancias acumuladas desde el origen en X,Y = 0,0; mientras que la opción Spacing, trabaja con el espaciamiento entre ejes. Se 
recomienda realizar el modelo con la última alternativa.  
En el apartado de Units, se puede editar la unidad de medida con la que se ingresa la información.  
 
Imagen 9. 
✓ Para definir si el eje consistirá en una línea primaria o secundaria, se debe editar en Line Type (Tipo de Línea). Por 
defecto se establece que son primarias, pero basta con hacer doble click en la casilla para cambiarla a secundaria. 
✓ La columna de Visiability (Visibilidad) permite definir si el eje de esa fila aparecerá o no en el modelo. 
✓ Para el eje X de la grilla, las burbujas con la identificación de cada eje vienen arriba por defecto; pero si se quisiera 
cambiar de orientación, basta con hacer doble click en la casilla de Bubble loc (localización de la burbuja) y estas se 
presentarán abajo. Lo mismo ocurre con los elementos en la dirección Y de la grilla, solo que cambiarán de ubicación 
moviéndose de izquierda a derecha. 
✓ En la última columna, Grid Color (Color del eje), se puede definir un color para cada eje.  
✓ En la esquina inferior derecha, se puede definir el tamaño de la burbuja de identificación del eje en Bubble Size. 
Cuando se ingresa la información necesaria, se selecciona “Ok” para dejar la planta de la estructura lista y se continúa con la 
elevación. 
 
 
 
 
 
 
X
Y
Además del ID y 
espaciamiento, 
se 
permite modificar el 
color, posición de la 
burbuja 
de 
identificación del eje y 
propiedades de la 
malla 
(color, 
por 
ejemplo). 
Unidades 

=== PÁG 9 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
9 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
2.2 
Definir la Grilla Vertical (Elevación) 
Para definir los niveles de piso, se trabaja con el lado derecho de la ventana de Building Plan Grid System and Story Data 
Definition.  
Para establecer las características que tendrá la grilla vertical, se puede trabajar con las dos opciones que se presentan en 
Story Dimensions. 
 
Imagen 10. 
 
 
Imagen 12. 
✓ Para el caso de labels, generalmente se trabaja con la siguiente notación:  
CPi;  
donde C = cielo,  
P = piso/S = subterráneo, 
 i = nivel (N°). 
✓ En Height se agrega la altura entre pisos que existe (según las unidades de medidas establecidas anteriormente se 
agrega en metros), mientras que el programa en Elevation va sumando automáticamente la atura total.  
 La primera es Simple Story Data. Aquí el programa pide 
ingresar el número de niveles, la altura del primer piso (que 
por lo general es diferente a los siguientes) y la altura del 
piso típico (que es la altura de entrepiso). 
 La segunda es Custom Story Data. Aquí se permite 
modificar cada nivel por separado con sus respetivas alturas. 
Al seleccionar la última opción y presionar “Edit Story Data”, 
se abre la ventana que se muestra en la imagen 12. 
 
Imagen 11. 
Nombre de cada piso 
Altura de cada piso 
Altura del nivel 
base 
Definir nivel de 
referencia 
Definir pisos 
similares 
Unidades 

=== PÁG 10 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
10 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
✓ Determinar un Master Story como Yes (Sí), significa considerarlo como nivel de referencia, donde cualquier cambio 
en él se realiza en los considerados similares (Similar To). 
✓ Similar To establece que es similar a un piso considerado como Maestro.  
Se recomienda que cada nivel tenga autonomía en su respectiva edición. Entonces, según lo expuesto anteriormente, se debe 
considerar cada piso como Master Story (Yes). 
Por último, el apartado de Add Structural Objects permite generar modelos con formas y elementos predefinidos por el software.  
 
 
Imagen 13. 
De las opciones dadas, se decide trabajar con la opción “Grid Only”, ya que le da autonomía en cuanto a la forma, propiedades, 
elementos y espacio de trabajo. Luego de dar “Ok”, se aprecian dos ventanas en la imagen 14: la que se encuentra a la izquierda 
es una vista en planta, mientras que la de la derecha es una vista en 3D. 
 
 
Imagen 14. 
 
 
 
Estructura de 
pórtico en acero 
Estructura de acero con 
armadura especial 
Losas macizas de hormigón 
armado sobre capiteles 
Losas macizas de hormigón armado sobre 
capiteles y vigas perimetrales 
Losas reticuladas de hormigón 
armado sobre capiteles 
Estructura con vigas en ambas 
direcciones y losa nervada 
Solo grilla 
Ventana de vista en 
planta de la grilla 
Ventana de vista 3D 
Sistema de 
coordenadas 
Barra de 
herramientas de 
dibujo 
Barra de herramientas 
principales 
Barra de comandos 
Unidades  
Activación de replicado de dibujo por 
niveles 
Coordenadas de la 
posición del cursor 

=== PÁG 11 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
11 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
✓ Se recomienda guardar el modelo antes de comenzar con los puntos siguientes.  
El modelo se guarda de la siguiente manera: “File” → “Save As” o presionando el icono 
 en la esquina superior izquierda. 
 
El archivo EDB debe ser guardado en una carpeta destinada para el modelo, ya que al ser ejecutado despliega una serie de 
archivos que pueden llegar a ocupar el espacio. Estos desaparecen cuando el modelo deja de ejecutarse. 
En el caso de que sea necesario modificar la malla horizontal y la vertical se debe modificar desde la 
barra de herramientas principal. 
“Edit” →”Edit Grid Data” 
“Edit” → “Edit Story Data” 
 
2.3 
Editar Grilla Horizontal 
Para modificar la grilla horizontal, se selecciona la opción “Edit Grid” que aparece en la imagen 17. Luego, se selecciona 
“Modify/Show System” para ingresar a la ventana que se presenta en el punto 2.1 de este manual en la imagen 9. 
             
 
Imagen 17.                                                                               Imagen 18. 
2.4 
Editar Grilla Vertical 
Para modificar la elevación del modelo se selecciona “Edit Story Data” y después “Edit Story”, como se muestra en la imagen 19. 
Con este procedimiento se obtiene la ventana de edición presentada anteriormente en la imagen 12. 
 
Imagen 19. 
2.5 
Insertar Nivel 
Este comando, presentado en la imagen 19 como “Insert Story”, permite incorporar pisos nuevos al modelo. Para hacerlo se 
define el nombre del piso nuevo, la altura y cantidad.  
Imagen 15. 
Imagen 16. 

=== PÁG 12 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
12 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
            
 
                           Imagen 20.  
2.6 
Borrar Nivel 
 
                  Imagen 21. 
2.7 
Editar y Agregar: Planos de Referencia 
Esta alternativa permite agregar planos de niveles que no se consideran dentro de la grilla vertical establecida originalmente 
pero que permiten dibujar en elevación y planta elementos. Además, permite editar los planos en altura que fueron creados. 
 
 
2.8 
Editar y Agregar: Líneas de Referencia 
 
✓ New Story Location, permite definir donde será ubicado el piso a insertar, los 
cuales pueden quedar entre los pisos ya propuestos. En el caso de que sean 
posicionados sobre uno ya existente, se desplazarán cuando se dupliquen. 
✓ La alternativa Replicate New Story permite hacer una réplica de nivel a alguno 
que se haya definido anteriormente. Esto es beneficioso para incluir los pisos 
tipo en el modelo. 
✓ En la imagen 19, se tiene la opción de “Delete Story”, con la cual aparece la 
ventana presentada en la imagen 21. 
✓ Esta opción, Select Story to Delete, permite eliminar uno o más pisos completos 
de modelo de una vez. Esto se logra seleccionando el piso y presionando “Ok”. 
✓ Clickear en “Edit Reference Planes”, que se muestra en la imagen 19, abre una 
ventana donde se permite ingresar la altura (en la casilla bajo Z-Ord) a la que se 
requiere insertar un plano de referencia en las unidades de trabajo (
), Luego 
se presiona “Add” y “Ok” para que sea agregado al modelo. 
✓ Para editar el plano de referencia se selecciona el que se desea modificar y se 
escribe en la casilla bajo Z-Ord la nueva altura que se tendrá, dando por último 
click en “Modify”. 
✓ Para eliminar el plano de referencia se selecciona el que quiere borrarse y luego 
se clickea en “Delete”. 
Imagen 22. 
✓ Ingresando una coordenada en X y en Y, permite crear 
líneas en puntos específicos que requieran de atención. 
Imagen 23. 
Nombre del nivel a 
incorporar 
Número de niveles a 
incorporar 
Altura del nivel 
Agregar 
Modificar 
Borrar 
Borrar todos 

=== PÁG 13 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
13 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
3. 
Herramientas Principales 
Antes de comenzar con el dibujo del modelo a diseñar, es importante tener en consideración cuales son las herramientas 
principales proporcionadas por ETABS para el dibujo, edición y asignación de propiedades, perfiles, condiciones de borde, etc. 
Estas, que se presentan en el cuadro a continuación, están agrupadas por: barra principal, editar, definir, dibujar, asignación de 
áreas y mostrar. 
Main 
Edit 
 
Modelo Nuevo 
 
Cortar 
 
Abrir modelo existente 
 
Copiar 
 
Guardar modelo 
 
Pegar 
 
Imprimir gráficas 
 
Borrar (supr) 
 
Imprimir tablas de datos 
 
Replicar 
 
Deshacer/Rehacer 
 
Editar grilla 
 
Refresh 
 
Editar elevación 
 
Desbloquear/bloquear modelo 
 
Unir puntos 
 
Correr Modelo/Run Analysis 
 
Alinear puntos/líneas/bordes 
 
Correr Modelo de secuencia constructiva 
 
Mover punto/líneas/áreas 
 
Correo Modelo No Lineal 
 
Expandir/encoger áreas 
 
Zoom área seleccionada 
 
Unir áreas 
 
Deshacer zoom/vista completa 
 
Mesh de áreas 
 
Zoom previo 
 
Unir líneas 
 
Acercar 
 
Dividir líneas 
 
Alejar 
 
Extruir puntos a líneas 
 
Mover con mouse 
 
Extruir líneas a áreas 
 
Vista 3D 
Define 
 
Vista en planta 
 
Propiedades de materiales 
 
Vista en elevación 
 
Secciones frame (vigas, columnas, diagonales) 
 
Rotar vista 3D 
 
Secciones área (losas, muros) 
 
Perspectiva 
 
Espectro de pseudoaceleración 
 
Mover Arriba/Abajo, Izquierda/Derecha 
 
Funciones de historia en el tiempo 

=== PÁG 14 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
14 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
 
Modificar herramientas en panel 
 
Estados de carga 
 
Opciones de vista/visualización del modelo 
 
Casos de respuesta al espectro 
Draw 
 
Casos de historia en el tiempo 
 
Seleccionar objeto 
 
Combinaciones de carga 
 
Remodelar objeto 
 
Definir Mass Source/Masas 
 
Dibujar líneas (Plan, Elev, 3D) 
Shell and Area Assigns 
 
Crear líneas con un click o en región (Plan, Elev, 3D) 
 
Asignar muro o losa 
 
Crear columnas con un click o en región (Plan) 
 
Asignar diafragma rígido 
 
Crear vigas secundarias con un click o en región (Plan) 
 
Asignar carga uniforme 
 
Dibujar diagonales con un click o en región (Elev) 
 
Etiqueta de Pier 
 
Dibujar áreas (Plan, Elev, 3D) 
 
Etiqueta de Spandrel 
 
Dibujar áreas rectangulares (Plan, Elev, 3D) 
Display 
 
Dibujar áreas con un click (Plan, Elev) 
 
Modelo no deformado 
 
Dibujar muros (Plan) 
 
Modelo deformado 
 
Dibujar muros en una región o con un click (Plan) 
 
Formas modales 
 
Dibujar ventanas 
 
Diagramas de esfuerzos 
 
Dibujar puertas 
 
Diagrama de energía y trabajo virtual 
 
3.1 
Vista Renderizada del Modelo 
ETABS permite crear y mostrar una vista renderizada del modelo en construcción, la cual es útil 
para insertar en memorias de cálculo o anexos. Esta se obtiene en “View” → “Create OpenGL View”, 
lo cual abre una ventana con la imagen, que puede ser guardada en el computador como archivo jpg.  
3.2 
Código de diseño 
Para realizar cambios en códigos de diseño del programa, se selecciona “Options” → “Preferences”. Lo anterior, despliega la 
opción de diseño de acero, hormigón, vigas compuestas y muros a corte. 
                          
 
Imagen vista completa 
de ventana 
Imagen solo del modelo 
Solo de la región 
del usuario 
Imagen 24. 
Imagen 26. 
Imagen 25. 

=== PÁG 15 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
15 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
4. 
Opciones de Visualización del Modelo 
Se debe hacer click en la casilla celeste con un tick (
) o ir a “View” → “Set Building View Options” para que aparezca el 
cuadro. Esta ventana, permite seleccionar todas las casillas de la información que se quiera aplicar para ver u ocultar en el 
modelo, y están separadas por grupos de vista. 
 
Imagen 27. 
Cada uno de estos ítems permite distintas cosas: 
✓ Ver elementos del modelo de acuerdo con el color de la alternativa elegida (por objetos, secciones, materiales). 
✓ Ver efectos especiales (separación de objetos, relleno del objeto, eje de los objetos y objetos con volumen, la cual 
considera las dimensiones de la sección ingresada). 
✓ Ver en pantalla los objetos seleccionados (áreas, líneas, puntos) 
✓ Ver etiquetas y ejes locales de los elementos. 
✓ Vista de piers y spandrels. 
✓ Opciones de visualización de elementos del modelo (grilla, planos de referencia, líneas de referencia). 
✓ Elementos especiales de las líneas (cachos rígidos, rótulas). 
✓ Otros elementos especiales (diafragma, auto area mesh, masas adicionales). 
 
 
 
 
 
 
Algunas de las opciones en la casilla pueden utilizar muchos recursos para el programa y 
afectar al refresh si se las tiene activadas sin necesidad. Esto ocurre con el Auto Area 
Mesh o con la opción Extrusion, esta última da una vista consolidada de la estructura, pero 
es recomendable trabajar con la opción Object Fill si se quiere un modelo en sólido.  

=== PÁG 16 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
16 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
5. 
Herramientas Gráficas 
También, se permite modificar las dimensiones de la letra y la cantidad de decimales que 
tendrán los resultados del modelo como las fuerzas, deformaciones, etc. Para esto es 
necesario clickear en “Options” y luego en “Preferences”, se debe elegir alguna de las dos 
opciones: Dimensiones/Tolerancias o Decimales en Resultados.  
 
 
 
 
 
 
 
 
 
 
Además, el programa permite modificar tanto los colores del fondo, de la grilla, de 
elementos y texto, como los colores con los que se presentarán los resultados 
obtenidos del modelo. Para esto, uno debe dirigirse a “Options” → “Colors” y presionar 
la opción que requiera ver: Display (Del modelo propiamente tal) y Output (Resultados). 
 
 
 
 
 
 
 
 
. 
Imagen 27. 
Imagen 33. 
Imagen 29. 
Imagen 30. 
       La opción “Windows”, permite 
definir con cuantas ventanas y en 
que disposición de ellas se 
trabajará en el modelo. 
Imagen 32. 

=== PÁG 17 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
17 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
6. 
Definir Materiales 
Con la grilla horizontal y vertical definida para modelar la estructura, es importante 
determinar las propiedades mecánicas de los materiales con los que se trabajará. 
Para eso, se selecciona “Define” y luego “Material Properties” como se muestra en la imagen 
34. 
 
 
Imagen 35. 
Para agregar un nuevo material se debe hacer click en “Add New 
Material”, lo cual abre una ventana en la que hay que modificar 
propiedades mecánicas como: densidad (kg/m3), peso específico 
en unidades de kgf (kgf/m3), módulo elástico (kg/cm2), tensiones 
máximas de trabajo (kg/cm2), entre otros.  
 
 
 
 
✓ Weight per unit Volume: peso específico del material (kgf/m3). 
✓ Mass per unit Volume: densidad específica del material (kg/m3). Como aproximación se puede dividir el anterior por 
10 m2/s. 
✓ Modulus of Elasticity: Modulo de elasticidad del material (kg/cm2). 
✓ Poisson’s Ratio: coeficiente de Poisson del material. 
 
 
 
 
 
Imagen 34. 
El programa viene con Hormigón (Conc) y Acero (Steel) como 
materiales por defecto con sus respectivas propiedades, pero estas 
pueden modificarse si no se trabaja con las mismas calidades, al igual 
que agregar otros materiales siempre y cuando se conozcan sus 
respectivas propiedades mecánicas. 
Hormigón 
Acero 
Imagen 36. 
          La alternativa Orthotropic, permite establecer 
las propiedades mecánicas individuales según cada eje 
local. Esto sirve para materiales como la Madera. 

=== PÁG 18 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
18 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
7. 
Definir Elementos Lineales 
Una vez definidos los materiales (acero, madera, hormigón, etc), se pueden crear las 
secciones transversales de los elementos estructurales que se pueden modelar como 
elementos Frame. 
Los elementos lineales de dibujo son considerados elementos tipo Frame, los cuales pueden ser: vigas, columnas y diagonales. 
Por lo tanto, para definir una sección se debe seleccionar “Define” → “Frame Sections”. 
 
 
Imagen 38. 
Para añadir, por ejemplo, una sección rectangular como una viga de hormigón armado, se debe presionar 
la flecha que aparece en “Add I/Wide Flange” y elegir “Add Rectangular”. Se abrirá una ventana que 
permitirá agregar las dimensiones que tendrá la viga con la que se requiera trabajar, donde: Depth = Altura 
(H) y Width = Ancho (B), como se muestra en la imagen 40. 
 
 
Imagen 40. 
Imagen 37. 
ETABS trae consigo varias secciones definidas previamente en 
una gran lista que se aprecia al aparecer la ventana Define Frame 
Properties, como se muestra en la imagen 38.  
Además, se pueden añadir elementos de tipo: tubular, I, 
rectangular, círculos y perfiles comerciales, entre otros. 
En el caso de que una sección no exista, es posible definirla en la 
opción Add SD Section, donde se dibuja el elemento en la ventana de 
Section Designer. 
Imagen 39. 
Material 
Nombre de la sección 
Modificadores de propiedades 
Propiedades de la sección 
Datos armadura de refuerzo 
La notación que se recomienda utilizar 
es: 
✓ Viga: “V.” + “ancho”/”alto” 
centímetros. (V.20/20, V.25/30, 
entre otros) 
✓ Columna: “C.” + “ancho”/”alto” 
centímetros. (C.30/30, C.40/40, 
entre otros) 

=== PÁG 19 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
19 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
 
Imagen 41. 
 
 
 
 
 
 
 
 
 
 
       Las secciones que vienen por defecto en ETABS y no se usarán en el modelo 
a diseñar, se deben borrar de la lista ya que no serán de utilidad.  
       Se puede crear la cantidad de secciones que se necesiten para construir 
el modelo. Estas, al irse guardando, se mostrarán en la ventana de Define Frame 
Properties.  
Columna 
Viga 
Imagen 42. 
Para ingresar a la información de la armadura de refuerzo 
de la viga rectangular que tendrá la viga de hormigón, se 
selecciona “Reinforcement” y la ventana que aparece indica 
primeramente la elección entre columna y viga. Es 
importante definir correctamente esta selección ya que 
tiene incidencia en el diseño que realiza el programa. 
 
Luego, permite ingresar el recubrimiento que tendrá y por 
último se clickea en “Ok” para guardar la sección creada. 
Para el caso de columnas de hormigón, hay que definir si es una 
columna rectangular o circular, además si el refuerzo transversal es 
por estribos o espiral (zunchos). 
En el caso de columnas rectangulares, se requiere agregar el 
recubrimiento, el número de barras longitudinales y el diámetro que 
existirá en cada dirección. 
Por último, se tienen dos opciones para tipo de análisis sobre estos 
elementos: 
✓ Barras de refuerzo para ser verificadas. 
✓ Barras de refuerzo para ser diseñadas. 

=== PÁG 20 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
20 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
Además, para crear secciones transversales de acero, tales como perfiles tubulares rectangulares o perfiles I, se debe 
seleccionar la flecha de la imagen 39 y elegir la opción Box/Tube Section o I/Wide Flange Section. Los perfiles de acero se 
nombran con su alto en mm X el peso por metro, anteponiendo a esto el tipo de perfil que se está ingresando al listado. 
 
 
Imagen 43. 
 
Imagen 44. 
 
 
 
 
 
 
Sección tubular 
rectangular 
Alto 
Ancho 
Espesor ala 
Espesor alma 
Sección I 
Alto 
Ancho ala superior 
Espesor ala superior 
Espesor alma 
Ancho ala inferior 
Espesor ala inferior 

=== PÁG 21 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
21 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
8. 
Definir Secciones de Muros y Losas 
Los elementos de superficie, como losas y muros, deben ser creados en presionando 
Define, como se muestra en la imagen 45, Estos se definen según el material y el 
espesor, el cual depende de la arquitectura y los requerimientos de acuerdo con la 
normativa vigente. 
Imagen 45. 
Por lo tanto, para definir una sección de losa o muro se debe seleccionar “Define” → “Wall/Slab/Deck Sections”.  
 
Imagen 46. 
 
Si se requiere crear una losa, se selecciona la opción “Add 
New Slab”. Esta abrirá una ventana donde nos permite 
ingresar el material de la sección, el espesor y el tipo de 
elemento finito a considerar en la modelación. 
 
 
 
 
 
 
 
 
Imagen 47. 
          Existe la opción de cambiar la distribución de cargas de la losa para que esta distribuya en una sola dirección. Esto se 
realiza marcando la casilla Use Special One-Way Load Distribution. 
 
Para definir la sección transversal, se tienen 3 opciones disponibles: 
✓ Deck: es una losa colaborante nervada como elemento de área y tipo 
membrane, que transmite sus acciones en una sola dirección por 
ancho tributario a sus apoyos.  
✓ Slab: sección de área tipo Shell, Membrane o Plate. Su asignación es 
exclusiva para losas de piso. 
✓ Wall: sección de área tipo Shell, Membrane o Plate. Su asignación es 
exclusiva para muros. 
Nombre de la sección 
Espesor para deformación axial 
Espesor para deformación 
a flexión y corte 
Distribución de cargas en 
una sola dirección 
Modificadores de propiedades 
Membrane: considera transmisión de cargas solo en su 
plano mediante el método de área tributaria y presentan 
rigidez infinita frente a flexión y corte. 
Plate: este considera que transmite cargas fuera de su 
plano. Se utilizan cuando solo se somete el elemento a flexión 
y corte. 
Shell: es la representación de la suma de Membrane y 
Plate. Se utiliza para secciones bajo esfuerzos de flexión, 
corte y fuerza axial. Se elige esta opción ya que se utiliza en 
la mayoría de los casos. 

=== PÁG 22 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
22 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
 
Imagen 48.         
Para el caso de la creación de muros, se trabaja de la misma manera que losas: considerando 
el elemento tipo Shell, agregando el material y espesor con el que se trabajará para el 
modelo. 
 
 
 
 
 
Imagen 49. 
9. 
Herramientas De Dibujo 
Las herramientas que presenta ETABS permiten dibujar las secciones tanto en planta como en elevación. Por ejemplo, los 
elementos lineales como vigas se pueden dibujar en planta y elevación, mientras que las columnas solo se dibujan en elevación 
de punto inicial a punto final. Existe la opción de dibujar los pilares en planta, pero debe realizarse con la herramienta por click. 
Algo similar ocurre con los elementos de área, ya que muros y losas se dibujan en planta, pero los primeros pueden dibujarse 
en elevación de igual manera. 
9.1 
Snap To 
Estas son distintas opciones que da el software para que el puntero actúe al dibujar en el modelo. Para definir las alternativas 
a utilizar se selecciona “Draw” → “Snap To” o se seleccionan los iconos en el extremo inferior del lado izquierdo de la ventana 
de trabajo. 
  Imagen 50. 
✓ Para hacer que la losa trabaje fisurada se puede modificar en Set 
Modifiers sus propiedades de inercia fuera del plano según lo 
indicado en 6.6.3 de ACI 318-14.  
La notación que se recomienda utilizar es: 
✓ Losa: “L” + espesor en centímetros. (L20, L30, entre otros) 
✓ Muros de hormigón armado: “MHA” + espesor en centímetros. 
(MHA15, MHA20, entre otros) 
Intersección de grilla y puntos 
Punto final de líneas y puntos medios 
Intersecciones 
Proyección perpendicular 
Líneas y ejes 
Alta precisión en grilla 

=== PÁG 23 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
23 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
9.2 
Puntos  
                 
 
Para dibujar puntos sobre la grilla de trabajo se selecciona “Draw” → “Draw Point Objects”, eso abrirá una ventana que permite 
definir en ambos ejes en planta la ubicación del punto desde uno de referencia (unión entre ejes, generalmente; pero puede ser 
otro punto creado anteriormente). 
9.3 
Elementos lineales 
 
Imagen 53. 
Para dibujar elementos lineales se tienen varias herramientas distintas según como se esté visualizando el modelo, las cuales 
se muestran en la imagen 53, 
 
Imagen 54. 
 
 
 
Imagen 55. 
 
 
Imagen 56. 
 
Vigas en planta y elevación 
Columnas en elevación 
Columnas en planta por click 
Vigas secundarias en planta por click 
Se elige la sección según las creadas: columna o viga 
Tipo de línea: Frame 
Condición de borde: unión empotrada o rótula  
Para dibujar con esta herramienta se debe 
seleccionar el punto inicial de la viga o columna 
y luego el punto final.  
Se puede indicar condición de borde y algún 
control específico para el dibujo. 
Para dibujar con esta herramienta basta con 
hacer click en los espacios entre ejes de la 
grilla.  
Lo anterior no resulta muy útil si las 
dimensiones de la columna son distintas al 
espaciamiento entre ejes. 
Se elige la sección según las creadas: vigas o columnas 
Columnas en elevación 
Vigas en planta y elevación 
✓ Se dibuja automáticamente hasta que se 
encuentre otro punto o línea de grilla. 
Para dibujar columnas con esta opción basta 
con hacer click en algún punto designado en 
planta. El punto puede ser la unión entre dos 
líneas de grilla o creado con la opción Draw 
Point Objects.  
La columna se dibujará en el cielo de piso que 
este posicionado la vista en planta. 
Se elige la sección según las creadas: solo columnas 
Distancia por el eje x e y desde el punto seleccionado 
Imagen 51. 
Imagen 52. 

=== PÁG 24 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
24 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
9.4 
Ajuste de Propiedades de Frames 
Cuando se trabaja con líneas (Frames), ETABS proporciona herramientas fundamentales para su ajuste de propiedades, con las 
cuales se permite definir elementos estructurales que no podrían simplemente dibujarse, como son las vigas invertidas. Se hace 
hincapié en 3 herramientas principales a continuación. 
 
9.4.1 
End (Length) Offsets – Cachos rígidos 
 
9.4.2 
Insertion Point 
 
La representación de una viga invertida o semi invertida mediante la herramienta Insertion Point, se visualiza solo cuando el 
modelo se encuentra con la opción de “Extrusion”. 
 
 
Imagen 60. 
Imagen 57. 
Si se requiere definir un frame como viga invertida o semi 
invertida, ya que por defecto viene en posición normal, 
primero se define el punto de referencia que viene en Cardinal 
Point, que tiene relevancia en la interacción que existirá entre 
frames. 
Luego, se determina la colocación final del elemento ajustando 
los valores en Frame Joint Offsets from Cardinal Point. 
Imagen 59. 
Imagen 58. 
Esta alternativa permite definir sectores de rigidez infinita en 
encuentros de elementos frame y disminuir la luz libre. Lo anterior, 
corresponde a una aproximación de la realidad debido a que los 
elementos frame se intersecan solo en sus centroides.  
La longitud de cacho rígido se determina según el capítulo 2 de 
Guendelman T (2004). 
✓ Se debe hacer click en todos los elementos y luego definir la 
longitud de rigidez. 
✓ También se puede ingresar un factor de zona de rigidez. 
Viga 
Viga Invertida 
Viga Semi invertida 

=== PÁG 25 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
25 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
9.4.3 
Local Axes 
 
Imagen 61. 
9.5 
Elementos de área 
 
Imagen 62. 
Para dibujar secciones como muros y losas definidas, se tienen las 5 herramientas mostradas en la imagen 62. Estas se utilizan 
de acuerdo con la vista en la que se está trabajando y dependiendo del elemento que se requiera según los creados 
anteriormente. 
 
Imagen 63. 
 
Imagen 64. 
 
Imagen 65. 
Esta opción permite rotar los eje locales de los 
elementos frente a su posición original (opción: Angle) o 
la posición actual (opción: Rotate by Angle) utilizando 
grados. 
Esta herramienta sirve de gran manera para la posición 
final que tendrá el pilar que se dibujará en el diseño. 
Dibujo de losas irregulares en planta 
Dibujo de losas rectangulares en planta 
Dibujo de muros rectangulares en elevación 
Dibujo de losas en planta por click 
Dibujo de muros en elevación por click 
Dibujo de muros en planta por click 
Dibujo de muros en planta  
Con esta opción se pueden dibujar losas de formas 
geométricas distintas a la rectangular. Estas pueden ser: 
triangulares, trapezoidales, entre otras. 
Además, de todas las herramientas de área, esta es la única 
que dibuja en 3D. 
Esta herramienta permite dibujar elementos de área de forma 
rectangular. En el apartado de X e Y se pueden agregar las 
dimensiones que se tendrá y solo hacer click en el punto. 
✓ En este caso, dibuja las losas en planta y los muros en 
elevación. 
Este comando permite dibujar muros en planta, donde se debe 
marcar un punto de inicio y uno final. 
✓ Esta herramienta funciona como las que se presentaron en 
el apartado de elementos lineales. 

=== PÁG 26 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
26 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
9.5.1 
Vigas Como Elemento de Área 
Generalmente las vigas se dibujan como líneas utilizando frames, pero existe el caso donde deben 
dibujarse en el modelo como elemento de área tipo Shell al igual que los muros. Esto ocurre 
cuando estas se encuentran entre muros y reciben cargas sísmicas, afectándolas ya que 
trabajan a corte.  
✓ De acuerdo con el capítulo 2.5 del Manual de Diseño en ETABS (Computers & Structures INC, 2010), el diseño de los 
Spandrel modelados como Shell o Frame no contempla la carga axial. Dado lo anterior, el post proceso debe ser 
realizado por el ingeniero y no por la herramienta de diseño del programa. 
9.6 
Consejos Para Dibujar  
ETABS tiene dos herramientas que permite el dibujo más rápido cuando se trabaja con elementos estructurales de similar 
disposición. Estas sirven cuando se trabaja con un edificio donde más de un piso repite las características estructurales o 
cuando un elemento se repite en el mismo nivel. 
9.6.1 
Similar Stories 
Como se mostró anteriormente en la imagen 14, existe una opción en la ventana inicial del programa que permite definir 
el dibujo para los pisos que sean similares. Esta opción se encuentra en la esquina inferior derecha y se activa cuando 
esta seleccionada la herramienta con la que se trabajará. De “One Story” → “Similar Stories” o se utiliza la opción “All 
Stories” si es un elemento que se repite por toda la estructura. 
✓ Similar Stories debe definirse antes que todo en la grilla vertical para que funcione la herramienta, donde se 
considera el piso de dibujo como Master Story. 
9.6.2 
Replicate 
La herramienta de replicado permite repetir elementos en la estructura con 4 opciones distintas. Para utilizarla, se debe 
seleccionar el o los elementos que se quieren replicar y luego se hace click en “Edit” → “Replicate”, lo cual abrirá una ventana 
con las distintas opciones de reproducción. 
 
                   
 
Imagen 68.                                                               Imagen 69. 
 
Imagen 67. 
Tipo de Replicado: Lineal 
Distancia en X 
Distancia en Y 
Número de elementos a 
replicar 
Borrar elementos originales replicados  
Tipo de Replicado: Radial 
Rotar alrededor de un punto determinado: 
✓ 
Centro del modelo 
✓ 
Punto específico 
Borrar elementos originales replicados  
 
Ángulo de rotación de los elementos 
replicados 
Número de elementos a replicar 
Imagen 66. 

=== PÁG 27 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
27 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
                        
 
Imagen 70.                                                                   Imagen 71.  
 
 Los elementos verticales como muros o columnas se dividen automáticamente cuando existe un cambio de piso, mientras 
que los elementos horizontales como losas y vigas se deben dibujar con sus llegadas a muros y columnas, desde inicio a fin para 
que se considere el tramo real de sección ya que no presenta división automática. 
10. Definir Apoyos  
Los apoyos se definen en los nodos de cada uno de los elementos estructurales que estén conectados a la base. Para el caso de 
las secciones frame, estas corresponden a los extremos del elemento; mientras que, para las secciones de área, los apoyos 
estarán en los vértices de cada elemento. 
Para modificarlos, se debe seleccionar el punto del nodo a cambiar e ir a “Assign” → “Joint/Point” → “Restraints (Supports)”. 
Lo anterior, abrirá una ventana con las alternativas de apoyo y restricciones que ofrece ETABS. 
 
Imagen 72. 
 
 
 
 
Tipo de Replicado: Espejo 
Línea de simetría con 
respecto a la que se 
hará el replicado. Se 
necesitan dos puntos 
con coordenadas (X,Y) 
Borrar elementos originales replicados  
Borrar elementos originales replicados  
 
Tipo de Replicado: Por Piso 
Selección de pisos donde se 
replicará el o los elementos 
Restricciones en las direcciones globales  
Restricciones predefinidas  
Apoyo empotrado 
Apoyo fijo 
Apoyo móvil 
Nodo simple 

=== PÁG 28 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
28 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
11. 
Definir Condiciones de Borde 
El programa permite definir condiciones de borde para distintos casos y dependiendo del elemento estructural con el que se 
esté trabajando para el diseño. 
11.1 
Condición de Borde de Vigas 
Existe la opción de rotular las vigas como elementos frame en los bordes. Para esto, se 
selecciona la sección y luego se hace click en “Assign” → “Frame/Line” → “Frame 
Releases/Partial Fixity”. Las rotulas aparecerán como unos círculos sobre los extremos 
de las vigas. 
Esto se realiza en distintos casos como: 
✓ Conexión perpendicular con un muro. 
✓ No desarrollan una longitud de empotramiento debido a una falta de continuidad. 
✓ Las armaduras longitudinales no alcanzan su longitud de desarrollo según ACI 318-08.  
                                  
 
 
11.2 
Condición de Borde de Muros 
Los muros pueden considerarse con apoyo fijo o empotrado en la base. En el caso de que los muros posean rigidez fuera de su 
plano y no presenten problemas de inestabilidad lateral, y a su vez posean armadura longitudinal superior a la requerida y que, 
además el sistema de fundación sea consistente con las restricciones al giro y laterales, se permite considerar la base como 
empotrada. Si no es así, se define el nodo como apoyo fijo. 
De todas formas, el apoyo fijo restringe los desplazamientos en las tres direcciones y proporciona el par tracción-compresión 
debido a la flexión en el plano del muro, haciendo que este actúe como empotrado en la dirección 3-3 de este. 
 
 
 
 
 
 
Imagen 75. 
Imagen 74. 
Imagen 73. 
Rótula 
Rótula 
Rótula 
Rótula 

=== PÁG 29 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
29 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
12. Estados De Carga Gravitacional 
Esta opción, permite definir los estados de carga gravitacionales que actuarán en el modelo, Estos contienen 
los estados de carga muerta, sobrecargas de uso, sobrecargas de techo, las que son debido al viento y otras 
que sean necesarias.  
 
 
 
Imagen 77.  
 El tipo de carga, Type, permite clasificarlas y separarlas, lo cual favorece luego al cargarlas en las combinaciones de carga 
o con información predefinida por normas y en distribuciones. 
 Self Weight Multiplier, establece cuanto y en cual estado se considera el peso propio de las secciones del modelo. Este valor 
puede variar entre 0 y 1. 
 La opción de Auto Lateral Load se activa solo cuando se selecciona un tipo de carga que actúe de forma lateral, como de 
sismo o viento. 
✓ Para peso propio (D1), el programa calcula automáticamente el valor de este para cada uno de los elementos. 
✓ La carga permanente o muerta (D2), incluye el peso de elementos que no son estructurales y que estarán de forma 
permanente en la estructura, como lo es: recubrimientos, terminaciones, instalaciones sanitarias, eléctricas, clima y 
gas. 
✓ En las cargas vivas, las cuales son temporales, se encuentran las sobrecargas de uso (L) y las sobrecargas de techo 
(Lr). 
13. Definir y Asignar Diafragmas  
Los edificios que poseen masas concentradas (como las losas), que tienen 3 grados de libertad por 
nivel y que cumplen con lo requerido en el capítulo 12.3 de la norma ASCE 7, se puede considerar 
que las losas de piso pueden trabajar bajo la hipótesis de un diafragma rígido, donde los puntos de 
un nivel tengan todo el mismo desplazamiento. 
Para hacer que las losas del edificio se comporten como un diafragma rígido, este debe definirse 
en el modelo y agregarle la condición de rígido. Al agregar diafragmas en los pisos, se debe tener 
en consideración que poseen una gran rigidez lo que provoca menores desplazamientos laterales 
en la estructura. 
       Solo para la carga de peso 
propio (PP) se considera el valor de 
uno (1) en Self Weight Multiplier. 
Tipo de carga 
Factor multiplicador de 
peso propio 
Nombre de la carga 
Opción de carga 
lateral 
Agregar nueva carga 
Modificar carga 
Modificar carga lateral 
Borrar carga 
Imagen 76. 
Imagen 78. 

=== PÁG 30 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
30 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
Para crear un diafragma, se debe seleccionar “Define” → “Diaphragms”. Esto abrirá una ventana que permite definir el o los 
diafragmas con los que se trabajará en el modelo.  
                                                 
 
Imagen 79.                                                                                                 Imagen 80. 
En la imagen 80 se permite elegir el tipo de diafragma: Rígido o Semi Rígido (este da la opción de que cada punto de la estructura 
pueda desplazarse según su rigidez flexural).  
Luego de definir el diafragma, se debe asignar a la losa correspondiente. Esto se hace seleccionando 
el área y haciendo click en “Assign” → “Shell/Area” → “Diaphragms”. Esto abre una nueva ventana 
donde nos permite asignar a la losa el diafragma previamente creado, la cual se muestra en la imagen 
81, y se muestra la aplicación del diafragma en la imagen 82.  
 
 
 
 
 
 
 
 
 
Agregar nuevo diafragma 
Modificar/Mostrar diafragma 
Borrar diafragma 
Nombre del diafragma 
Semi Rígido 
Rígido 
Imagen 81. 
Imagen 82. 
       Si se habla de rigidez, asignar un 
diafragma semi rígido puede considerarse 
equivalente a no utilizar ninguno. 
✓ Un mismo diafragma creado puede asignarse a más de una losa 
y a varios niveles distintos. Para esto, puede utilizarse el 
comando Select → by Wall/Slab/Deck Sections, el cual permite 
seleccionar todos los elementos de un mismo nombre, haciendo 
más fácil la asignación de características como los diafragmas. 
 
✓ Se recomienda utilizar el mismo nombre de los diafragmas para 
todos los niveles. Esto debido a que la asignación de uno permite 
la obtención del centro de masa y el centro de rigidez. 
 
✓ El declarar un diafragma permite aplicar cargas laterales y 
conocer la posición del centro de masa y centro de rigidez de la 
estructura. 

=== PÁG 31 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
31 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
14. Estados de Carga Sísmicos 
Para ingresar las cargas laterales de sismo al modelo se tienen 3 opciones distintas: mediante fuerzas puntuales laterales, con 
un coeficiente de corte basal o ingresando un espectro de pseudo aceleraciones. Cada una de las opciones que se mostrarán a 
continuación y los cálculos se basan en la norma chilena NCh433 y el D.S N°61. 
14.1 
Análisis Estático Equivalente 
El análisis estático equivalente se realiza calculando las fuerzas sísmicas horizontales que actuarán en cada nivel con la fórmula 
planteada en el punto 6.2.5 de la norma chilena NCh433. Donde el período de la 
estructura en cada dirección de análisis se obtiene mediante el análisis modal 
espectral. Para ingresar las fuerzas estáticas laterales a ETABS se debe 
seleccionar “Define” → “Static Load Cases” y agregar como “Load” el sismo 
en X (Ex) y en Y (Ey), respectivamente 
Para utilizar este tipo de análisis, el tipo, type, de carga tendrá la clasificación 
de Quake, lo que activará la columna de Auto Lateral Load. Esta nos da distintas 
opciones de como considerar la fuerza sísmica, pero aquí se utiliza ”User 
Loads”, la cual es mediante fuerzas laterales.  
 
Imagen 84. 
✓ Para las fuerzas sísmicas horizontales en el eje Y, se realiza el mismo procedimiento, pero se trabaja con la columna 
FY. 
✓ Las fuerzas estáticas solo pueden ser utilizadas en diafragmas declarados como rígidos. 
14.2 
Por Gravedad o Coeficiente 
La definición de este sismo se realiza considerando el coeficiente sísmico C 
calculado según 6.2.3.1 de NCh 433 y 15.1 de DS61, el cual se encuentra limitado 
por un Cmin según 15.2 de DS61 y Cmax por la tabla 6.4 de NCh 433.   
 
Imagen 85. 
Imagen 83. 
Los resultados de las fuerzas sísmicas se agregan en 
la ventana que se abre al presionar ”Modify Lateral 
Load”.  
Para el sismo en dirección X, se selecciona el 
diafragma que actuará por piso, el cual debe estar 
definido anteriormente, y se ingresa en la columna de 
FX los valores de las fuerzas sísmicas. Además, se 
considera que actúa en el centro de masa (Apply at 
Center of Mass), pero si se tiene la excentricidad de 
trabajo, esta puede agregarse considerando la opción 
User Specifed Application Point. 

=== PÁG 32 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
32 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
En este caso, el tipo, type, de carga tendrá la clasificación de Quake, lo que activará la columna de Auto Lateral Load. Esta nos 
da distintas opciones de como considerar la fuerza sísmica, pero para este caso se utiliza ”User Coefficient”, la cual es mediante 
un coeficiente de corte basal. 
Al seleccionar la carga EX, en el lado derecho de la ventana, Click To, se activa la opción ”Modify Lateral Load”. Al hacer click en 
ella, se abre la ventana de la imagen 86, la cual permite definir: la dirección y excentricidad de la fuerza, los factores y el rango 
de niveles donde actuará. 
 
Imagen 86. 
14.3 
Análisis Modal Espectral 
14.3.1 
Definir el Espectro de Diseño 
En el caso de que se quiera trabajar con un espectro de pseudo aceleraciones, el programa permite 
ingresarlo para que actúe sobre la estructura. Primero se debe obtener el espectro de diseño según 
lo expuesto en el apartado 12.1 del Decreto Supremo 61, sin considerar la corrección de I/R*.   
 
Este debe guardarse en un archivo con formato .txt, donde existirán dos columnas: el período Tn (0 
a 3 segundos aproximadamente, con incrementos de 0.05s) y el valor de Ao*S* para cada período. 
 
 
Imagen 88. 
 
 
Para el caso del sismo en la dirección en X, se selecciona ”X Dir” y se ingresa 
el coeficiente sísmico de corte basal calculado según el tipo de estructura que 
se tenga. Además, es importante definir el piso donde comienza y donde termina 
la aplicación del sismo, la cual es generalmente desde la BASE al último piso. 
✓ Para el sismo en dirección Y, con EY, se realiza el mismo procedimiento, 
pero considerando la dirección como ”Y Dir”. 
✓ K, según el capítulo 2.15 del Manual de Carga Laterales, es el coeficiente de 
altura de la edificación y se utiliza como un exponente que determina la 
distribución del corte basal sobre la altura del edificio (Computers & 
Structures INC, 2009). 
Para ingresar el espectro de diseño al programa, se debe seleccionar 
”Define” → “Response Spectrum Functions”. Lo anterior, abre una 
ventana que permite definir un espectro elástico de diseño. Para esto, se 
pueden utilizar dos opciones: 
 User Spectrum: deben agregarse los puntos de la curva de diseño 
de uno en uno. 
 Spectrum from File: esta alternativa permite ingresar el espectro de 
diseño que fue almacenado en el archivo .txt anteriormente. Para este 
caso, hay que tener cuidado en el ingreso de números: con coma o con 
punto, lo cual depende de la configuración del programa y el computador. 
ETABS podría lanzar un error de lectura si no se ingresa bien el archivo. 
Se recomienda trabajar con la segunda opción. 
Imagen 87. 

=== PÁG 33 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
33 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
 
 
Imagen 89.                                                                                               Imagen 90. 
✓ Para que considere bien el espectro de diseño, se debe seleccionar la opción ”Period vs Value2 en el apartado de 
Values are. 
 
Imagen 91. 
        El programa no guarda los espectros de diseño cargados en él después de leerlos, por lo que puede ser un problema si el 
proyecto se cambia a otra carpeta o de computador; ahí se requiere que el espectro sea actualizado de forma manual. Pero, al 
seleccionar la opción “Convert to User Defined”, la curva de diseño puede almacenarse en el modelo. 
14.3.2 
Ingresar los Estados de Carga Sísmicos 
Debido a que la función del espectro sísmico ya fue ingresada, es posible definir el estado de carga sísmico 
en ambas direcciones, como respuesta del espectro de diseño.  
El estado de carga sísmico en X y en Y, se debe ingresar en “Define → Response Spectrum Cases”. 
 
Se escribe el nombre de la función de 
acuerdo con la notación recomendada y 
luego se sube el archivo.  
Para ingresar el espectro se hace click en 
”Browse” y se busca el archivo como Text 
Files en el computador. 
Notación: “S” + Letra del tipo de suelo + “Z” + N° de zona sísmica 
Factor de  
Amortiguación 
Si se selecciona ”Display Graph”, ETABS muestra 
el gráfico de la curva de diseño ingresada, y 
moviendo el cursor por sobre ella puede verse los 
valores de la función en cada punto. 
Para ingresar un caso de respuesta al espectro 
de diseño, se debe hacer click en “Add New 
Spectrum”, en la ventana emergente de Define 
Response Spectra. 
Como notación se utilizará Ex y Ey para las 
direcciones de trabajo. 
Imagen 92. 
Imagen 93. 

=== PÁG 34 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
34 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
 
Imagen 94. 
14.3.3 
Definir Mass Source  
Es importante, cuando se hace un análisis modal espectral, que se ingrese al programa los estados de carga gravitacionales que 
serán parte de la masa sísmica concentrada por nivel. Esto se permite en ETABS gracias al comando Mass Source. 
“Define” → “Mass Source” 
✓ Según lo que se expone en la NCh433, las sobrecargas de uso tendrán porcentajes de participación de 25% o 50%, 
dependiendo de las consideraciones que se establecen en el punto 5.5 de la norma. 
La ventana emergente que aparece al seleccionar Mass Source, trae consigo 3 opciones 
distintas para considerar la masa sísmica. 
 From Self and Specified Mass: considera solamente la masa brindada por el pedo propio 
de los elementos del modelo y masa sísmica adicional que se haya agregado. (“Assign” 
→”Shell/Area” → “Aditional Area Mass”) 
 From Loads: en este caso, las masas se definen de acuerdo con los estados de carga 
independientes agregados anteriormente, al igual que el peso propio ya que se define con un 
Self Weight = 1. 
 From Self and Specified Mass and Loads: esta es una combinación de las dos alternativas 
anteriores. 
✓ Se recomienda aplicar la segunda opción con los respectivos porcentajes según 
análisis. 
Factor de 
Amortiguación 
Las direcciones que presentan los casos sísmicos están descritas como U1, U2 y UZ. 
Estas se definen como un sistema cartesiano típico con X, Y y Z, respectivamente, 
solo cuando el ángulo de excitación ingresado es igual a 0. 
Para ingresar el sismo en la dirección X, debe tenerse en consideración que en el 
apartado Input Response Spectra solo se considerará la dirección U1 con un ángulo 
de excitación 0. En este caso, el factor de escala (Scale Factor) corresponderá al 
factor de reducción definido según la normativa chilena y la función (Function) 
seleccionada será la del espectro de diseño ingresada en el punto anterior.  
✓ De momento solo debe considerarse como valor 1 en la casilla de Scale Factor, 
indicando un sismo de diseño elástico. Más adelante, se presentará la 
calibración que es necesario realizar. 
✓ Exitation Angle, es el ángulo en el que actuará el sismo de acuerdo con la 
dirección principal establecida. (Si se trabaja en la dirección U2 con un ángulo 
de 90°, significa que el sismo actuará en el eje X) 
Override, permite considerar en el modelo el efecto causado por la torsión 
accidenta ingresándolo como una excentricidad por piso al modelo. 
Para el sismo en el sentido Y, se realiza el mismo procedimiento, pero considerando 
la dirección U2. 
Imagen 95. 

=== PÁG 35 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
35 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
15. Combinaciones De Carga 
Cuando se definen todos los estados de carga estáticos y dinámicos con los que se 
trabajará, se deben ingresar al programa las combinaciones de carga para el análisis y 
diseño de la estructura modelada. 
✓ La función de las combinaciones de carga es llevar la estructura a los máximos 
efectos para lograr un diseño seguro. 
Para ingresarlas, se debe hacer click en “Define” → “Load Combinations”, esto abrirá una 
ventana emergente que permite definir los combos seleccionando en Add New Combo, como 
se presenta en la imagen 96.  
 
Imagen 97. 
✓ Usualmente se ingresan las combinaciones presentadas en la norma chilena NCh 
3171 Of 2017. 
 
 
         Los combos se aplican al modelo en su totalidad a través 
del análisis, no a los elementos en sí. Las cargas, en cambio, 
si se aplicar directamente a las secciones como se muestra 
en el punto siguiente. 
 
 
Imagen 96. 
Notación recomendada: “LRFD” ó “ASD” 
+ N° de la combinación. 
Tipo de combinación de carga: 
✓ 
ADD: suma algebraica. 
✓ 
ENVE: envolvente. 
✓ 
ABS: valores absolutos. 
✓ 
SRSS: raíz cuadrada de la suma de 
valores al cuadrado. 
Factor de escala: este puede tomar 
valores positivos o negativos (±). 
Estados de carga 
seleccionados 
NCh 3171 – Combinaciones LRFD 
1) 1,4 D  
2) 1,2 D + 1,6 L + 0,5 (Lr o S o R)  
3a) 1,2 D + 1,6 (Lr o S o R) + L  
3b) 1,2 D + 1,6 (Lr o S o R) + 0,8 W  
4) 1,2 D + 1,6 W + L + 0,5 (Lr o S o R)  
5) 1,2 D + 1,4 E + L + 0,2 S  
   5.1) 1,2 D ± 1,4 EX ± 1,4 TAX + L  
   5.2) 1,2 D ± 1,4 EY ± 1,4 TAY + L  
6) 0,9 D + 1,6 W 
7) 0,9 D + 1,4 E  
   7.1) 0,9 D ± 1,4 EX ± 1,4 TAX  
   7.2) 0,9 D ± 1,4 EY ± 1,4 TAY  
NCh 3171 – Combinaciones ASD 
1) D  
2) D + L  
3) D + Lr  
4) D + 0,75L + 0,75Lr  
5) D ± W  
6) D + E 
   6.1) D ± EX ± TAX 
   6.2) D ± EY ± TAY 
7) D ± 0,75W + 0,75L + 0.75Lr 
8) D + 0,75E + 0,75L + 0,75S 
   8.1) D ± 0,75EX ± 0,75TAX + 0,75L + 0,75S 
   8.2) D ± 0,75EY ± 0,75TAY + 0,75L + 0,75S 
9) 0,6D ± W 
10) 0,6D + E 
   10.1) 0,6 ± EX ± TAX 
   10.2) 0,6D ± EY ± TAY 

=== PÁG 36 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
36 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
16. Asignar Cargas 
ETABS permite asignar 3 tipos de carga dependiendo del elemento: sobre nodos, sobre líneas y sobre 
áreas. Para esto, hay que seleccionar el elemento al que se requiera agregar una carga externa y 
se hace click en Assign y, luego, cualquiera de las 3 opciones: Joint/Point Loads, Frame/Line Loads 
o Shell/Area Loads, como se muestra en la imagen 98. 
 
 
 
Imagen 99. 
  
Imagen 100. 
 
 
 
 
 
Imagen 101. 
 
Imagen 102. 
 
Imagen 103. 
 
Imagen 98. 
Esta opción permite agregar cargas puntuales en los 
nodos, indicando el valor de esta y la dirección en la que 
se aplicará.  
Sobre líneas, se puede agregar cargas puntuales y distribuidas.  
✓ Las cargas puntuales se utilizan generalmente cuando se quiere agregar 
efectos de cargas muertas localizadas, las cuales se presentan en 
relación con los ejes globales. 
✓ Las cargas lineales, se pueden añadir como una distribución regular o 
como una irregular, definida con 4 puntos del elemento. 
✓ En Load se agrega el valor de la carga en sus unidades respectivas, 
generalmente: ton ó kg, cuando es puntual; ton/m ó kg/m, cuando es 
distribuida. 
Usualmente, asignar cargas en áreas es la alternativa más 
común para la mayoría de los modelos estructurales. 
Para esto, se seleccionan las áreas a las que se les agregará 
una carga, las cuales son losas generalmente, y se define el valor 
y dirección que tendrá, la cual estará en unidades de peso por 
área (ton/m2 ó kgf/m2). 
✓ Tener cuidado con las unidades de ingreso de la carga. 
✓ Se puede utilizar el comando Select, explicado en el punto 12, 
para que el ingreso de cargas no sea tedioso. 
✓ Definir la dirección de la carga correctamente, ya que no 
todas actúan en gravedad. 

=== PÁG 37 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
37 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
16.1 
Visualización de Cargas Aplicadas 
Para visualizar las cargas aplicadas, se debe seleccionar el comando “Display” → “Show Loads”. Esto permite saber si las 
cargas fueron ingresadas correctamente al modelo. 
 
Imagen 104. 
    
                                                           
 
    Imagen 105.                                                                                                Imagen 106. 
Imagen 107. 
16.2 
Asignar y Visualizar Cargas Inclinadas 
En casos donde las superficies presentan inclinación y se requiere ingresar cargas, tales como el viento, ETABS permite hacerlo 
al igual que las que se presentaron anteriormente, pero debe realizarse en los ejes locales del elemento. De esa forma, 
presentará la inclinación requerida para simular una carga en la realidad. 
           
 
Puntuales 
Lineales 
Superficie 
Para visualizar las cargas 
puntuales, se clickea en 
“Joint/Point” y se elige el 
estado 
de 
carga 
que 
contiene la asignada. 
Para visualizar las cargas 
lineales, se clickea en 
“Frame/Line” y se elige el 
estado 
de 
carga 
que 
contiene la asignada. 
Para visualizar las cargas 
de superficie, se clickea en 
“Shell/Area” y se elige el 
estado 
de 
carga 
que 
contiene la asignada. 
Estado de 
carga 
Dirección en 
ejes locales 
Carga 
Imagen 108. 
Imagen 109. 

=== PÁG 38 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
38 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
17. Mesh  
La finalidad del realizar Mesh o discretización de áreas, tanto en muros como en losas, es lograr que exista una conectividad 
entre los nodos de los elementos que conforman la estructura modelada, y así, se pueda traspasar los esfuerzos internos y 
deformaciones. 
✓ Se recomienda aplicar el Mesh, tanto en losas como en muros, luego de que la estructura esté dibujada por completo. 
✓ Se debe tener en consideración que el Mesh manual, el que se realiza en muros, es de forma permanente; por lo que 
es mejor guardar un modelo sin este y otro con sus modificaciones, ya que no se podrá volver atrás. En cambio, el 
Automesh, utilizado en losas, divide los elementos únicamente cuando el programa ha desarrollado el análisis 
estructural. 
17.1 
Mesh en Losas 
Para discretizar la losa y asegurar que existe conectividad con los muros, es necesario utilizar vigas NONE (elementos lineal 
frame), ya que esto permite guiar como será el mesh automático que se aplicará luego a las losas. 
 
Imagen 110. 
Para visualizar las vigas NONE agregadas, se debe seleccionar el icono de opción de visualización 
del modelo (
) y hacer click en ”Object Present in View” → “All Null Lines”. 
Luego de lo anterior, se deben seleccionar todas las losas a las que se les dibujó frames nulos, 
para aplicar un mesh de forma automática. Se debe presionar “Assign” → “Shell/Area” → “Area 
Object Mesh Options”, esto abrirá una ventana que contiene múltiples opciones de trabajo. 
 
Imagen 112. 
Las vigas nulas deben dibujarse cortando la losa orientándose hacia la dirección en la que 
se encuentran las vigas o elementos estructurales importantes que generan separación y 
perpendicular a vanos de puertas y ventanas, como en puntas de muros. 
Lo ideal, es que las divisiones creadas crucen la losa de comienzo a fin ya que esto 
permitirá que al aplicar el auto mesh, se provoque una discretización acorde y coincidente 
con esas separaciones. 
Mesh solo a elementos Membrane 
Mesh solo a áreas con diafragma rígido 
Utiliza secciones de área solo como 
elementos estructurales 
Mesh automático de elementos de área con 4 
opciones distintas: 
✓ 
En vigas y líneas existentes. 
✓ 
En muros y rampas existentes. 
✓ 
En las líneas de grilla visibles. 
✓ 
Dividir en un tamaño máximo (se 
trabaja en metros generalmente, 
donde las losas se dividen en 1 metro) 
Imagen 111. 
El mesh automático y el mesh manual son 
procedimientos que trabajan juntos, no son 
sustitutos del otro.  Esto debido a que se 
tendrá que realizar un ajuste manual 
siempre en las zonas donde exista un interés 
mayor. 
Se puede ir revisando el auto mesh en 
 
→ Other Special Items → Auto Area Mesh.  
✓ Si la conectividad no es la deseada, se 
debe ir iterando en la ubicación de las 
vigas nulas o ir agregando más para 
lograr concordancia entre las divisiones. 

=== PÁG 39 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
39 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
        Aquí se agrupan las opciones automáticas de mesh en muros, pero se prefiere realizar esta división de manera manual 
como se mostrará en el apartado siguiente. 
                           
 
Imagen 113.                                                            Imagen 114. 
✓ El mesh automático utiliza muchos recursos computacionales, por lo que se recomienda que no se tenga visible cuando 
no se necesita, así se evita que el refresh sea lento debido a la gran cantidad de información que genera. 
✓ El mesh automático entrega resultados aceptables cuando se realiza entre 50cm y 100cm, por lo que la decisión queda 
a criterio del ingeniero. 
17.2 
Mesh en Muros 
En muros, se prefiere realizar un mesh manual con una herramienta llamada Mesh Areas, debido a las perforaciones de vanos 
de puertas y ventanas. Para llegar a esta, se debe seleccionar el muro al que se le requiere hacer mesh y luego, “Edit” → “Mesh 
Areas”. Esto abrirá la ventana que se muestra a continuación, que nos permitirá dividir las áreas.  
 
Imagen 115. 
✓ Se aconseja que las subdivisiones realizadas generen cuadrados o rectángulos cuya razón sea inferior a 2. 
✓ Estas divisiones se deben realizar idealmente en encuentros con muros perpendiculares, vigas apoyados en ellos o 
columnas. Estos se deben localizar donde se sepa que exista un traspaso de carga complejo (dinteles o muros cortos) 
de manera de mejorar la descarga en la estructura. 
Visualización de 
vigas NONE en 
losas. 
Visualización de 
Auto Mesh en 
losas debido a las 
vigas 
nulas 
generadas. 
División de áreas considerando los 
objetos lineales elegidos en el plano 
horizontal. 
División de áreas considerando un 
ángulo de rotación entre la selección 
de puntos. 
División 
de 
áreas 
considerando 
cuadrados/rectángulos de X por Y. 
División de áreas considerando 1 o todos los 
puntos de las opciones: 
✓ 
Intersección con líneas de grilla 
visible. 
✓ 
Puntos y ejes seleccionados. 
✓ 
Intersección con líneas seleccionadas. 

=== PÁG 40 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
40 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
Cuando se dibuja viga o columnas como elementos Shell, se espera que el mesh manual se realice en base a la relación 2:1 
de H:L, donde H se considera como la altura de la sección que resiste la solicitación por flexión; mientras que L, es la altura del 
elemento Shell discretizado en elevación. 
Las vigas ingresadas al programa como Shell deben dividirse en partes con números par no menor a 4, ya que esto 
discretizará al elemento y generará que se comporten de manera flexible. 
Para aplicar mesh en la base de los muros, se puede realizar de manera automático cada 1 metro sin considerar la condición 
de “Add Restraints/Constraints..” ya que esta opción considera apoyos ficticios en la base, cuyas reacciones solo se aprecian 
de forma visual en el programa. Al hacer la subdivisión manual, se pueden exportar las reacciones de cada uno de los nodos a 
una base de datos.  
                                
 
Imagen 116.                                                      Imagen 117. 
Por último, cuando el modelo se tiene dibujado por completo, se debe ir a “Assign” → “Shell/Area” → “Auto Line Constraint”. 
Esto permite asegurar la correcta conectividad entre todos los elementos del modelo creando una unión lineal entre objetos. 
 
Imagen 118. 
 
 
 
 
 
 
Mesh Manual en la 
base cada 1 metro, 
con sus respectivos 
apoyos generados. 
Mesh Automático en 
los muros y en la base 
cada 1 metro. 
V/S 

=== PÁG 41 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
41 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
18. Identificación de Elementos: Piers y Spandrels 
La numeración de los elementos de área Piers y Spandrel es necesaria, ya que permite obtener la integración de los esfuerzos 
internos y diseñar como elementos de hormigón armado. Cuando se asigna un label, ETABS integra automáticamente los 
elementos de área que conforman la sección, generando los diagramas de esfuerzos (axiales, cortes y momentos). 
Existen dos tipos de identificación:  
✓ Pier: Muros. 
✓ Spandrel: Vigas. 
18.1 
Asignación de Pier 
Estas pueden agregarse a secciones de área verticales (muros) y a secciones de línea verticales 
(columnas). Cuando se asigne su identificación, se debe tener en consideración que los que pertenecen 
al mismo piso y tienen el mismo pier label, serán considerados por el programa como parte del mismo 
elemento. 
Para crear las identificación y asignar los nombres a los muros, se selecciona el área que quiere 
identificarse, luego “Assign” → “Shell/Area” → “Pier Labels”, lo cual permite agregar todos los ID. 
18.2 
Asignación de Spandrel 
A diferencia de la anteriores, estas se agregan a vigas que son dibujadas como área 
y a las líneas horizontales, aunque la identificación contiene las misma propiedades 
que los piers. 
En este caso, se tiene que todas las vigas deben dividirse en dos tramos, a excepción 
de las vigas de acople (L/H<2), ya que estas presentan sus esfuerzos máximos en los 
extremos. 
Para crear las identificación y asignar los nombres a las áreas, se selecciona la que 
quiere identificarse, luego “Assign” → “Shell/Area” → “Spandrel Labels”, lo cual 
permite definir los nombres. 
18.3 
Notación recomendada 
Se sugiere que se utilice la siguiente notación para un correcto orden de los elementos presentados: 
✓ En Muros: Eje – Nro de orden. 
✓ En Pilares frame: Eje _ Nro de orden.  
✓ En Vigas Frame: Eje  .  Nro de orden (A o B) 
✓ En Vigas Shell: Eje  /  Nro de orden (A o B) 
 
 
 
Imagen 119. 
Imagen 120. 
El número de orden se 
recomienda con comienzo 
de izquierda a derecha. 
Imagen 121. 

=== PÁG 42 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
42 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
19. Definir Tipo De Análisis y Checkear El Modelo 
Antes de ejecutar el código que resuelve el análisis matricial del modelo, es necesario definir 
las características y parámetros que se le concederán inicialmente. Para esto, existe un 
comando llamado Set Analysis Options, que permite definir los ejes en los que se actuará (full 
3D o por planos), los modos del análisis sísmico e incluso incluir un efecto P-Delta. 
Al seleccionar ”Analyze” y luego “Set Analysis Options”, esto abrirá una ventana a la cual se le definirán los parámetros iniciales 
de modelación. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Lo primero, es definir cuantos grados de libertad actuarán en el análisis del 
modelo.  
✓ Si se está realizando el diseño de un marco o una cercha isoestático, se 
deben analizar en 2D, es importante considerar un análisis de tipo Plane. De 
otra forma, el programa detectará inestabilidad.  
✓ En cambio, cuando se modelan estructuras hiperestáticas, es posible 
considerar la opción Full 3D. 
Al ingresar parámetros dinámicos mediante un espectro de diseño al modelo, es posible definir 
la cantidad de modos de vibrar a los que se quiere llegar y, además, permite definir el tipo de 
análisis sísmico en Set Dynamic Parameters, los cuales pueden ser por: 
✓ Vectores propios (eigenvectors). 
✓ Vectores de Ritz: si se elige esta opción, se debe agregar la aceleración en x y en y. 
        La cantidad mínima de modos de vibrar se puede calcular como 3 grados de libertad por 
cada nivel (movimiento en X, Y y Torsión). 
        EL porcentaje de masa traslacional que deberá alcanzar el análisis modal espectral tendrá 
que ser de al menos 90%; si esto no se logra, se tendrán que agregar más modos de vibrar. 
        Solo en casos justificados se agregar el efecto P-Delta.  
Imagen 122. 
Imagen 123. 
Imagen 124. 
Imagen 125. 
Por último, antes de ejecutar el análisis, es importante verificar que no exista 
ninguna advertencia o Warning. Para esto, ETABS trae consigo la ventana Check 
Model, la cual se encuentra bajo Set Analysis Options en Analyze.  
✓ Se seleccionan todas las casillas presentes y se espera para saber si se 
debe modificar algo del modelo. 
Luego de esto, se selecciona “Run Analysis” o F5 y los resultados estarán listos 
para utilizarse en el diseño. 

=== PÁG 43 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
43 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
20. Análisis y Resultados 
Primeramente, al ejecutar el modelo, se puede obtener desde el software un archivo que despliega toda la información relevante 
al análisis estructural realizado, el cual muestra la cantidad de nodos, elementos de línea, elementos de área, resumen de la 
iteración que se realiza en el análisis sísmico, y los warning asociados a errores de modelación y posibles mecanismos. Para 
esto, se debe ir a “File” → “Last Analysis Run Log”, lo cual abrirá un WordPad con la información. 
 
20.1 
Obtención de Tablas de Resultados 
Luego de que el programa ejecute el análisis estructural, se puede procesar la información a partir de tablas de datos 
exportables a Excel. Lo que se realiza es dirigirse a “Display” → “Show Tables”. Al seleccionar lo anterior, aparecerá una ventana 
con distintos puntos importantes.  
✓ Primero se debe definir que tablas se necesita procesar haciendo click en las casillas. Estas pueden ser de resultados 
del modelo o de la construcción de este. 
✓ Para extraer la información de Pier Forces y Spandrel Forces, en necesario seleccionar las combinaciones LRFD 
ingresadas. Mientras que para Story Shears solo basta con los estados de carga de peso propio, carga muerta, 
sobrecarga y sismo en dirección X e Y. 
✓ En cuanto al Center Mass Rigidity, Modal Participating Mass Ratios, Diaphragm Drifts, Diaphragm CM Displacements, 
Stoy Datam no dependen de los estados de carga. 
               
 
Imagen 127.                                                                                          Imagen 128. 
Imagen 126. 

=== PÁG 44 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
44 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
Mientras el candado este cerrado en el modelo, se puede ingresar todas las veces que se quiera Show Tables. Esto debido a que 
el modelo se encuentra protegido a las modificaciones hasta que voluntariamente se quiete el seguro.  
 
También, como se expresó anteriormente, se recomienda guardar los archivos de ETABS en carpetas, ya que después de echarlo 
a correr, generan muchos documentos los cuales pueden llenar el escritorio. Además, siempre que se cierre el modelo, es 
preferible hacerlo con el candado abierto para que los archivos que se generan por la modelación no ocupen memoria de forma 
innecesaria en el computador. 
✓ En este caso, para poder calibrar el sismo, se extraen solo algunas tablas, las cuales serán importantes al brindarnos 
información para obtener el factor de escala (I/R*) que luego será ingresado al estado de carga del espectro en X y 
en Y. 
20.2 
Resultados debido al Análisis Dinámico 
20.2.1 
Modos de vibrar y Períodos de la estructura 
La tabla Modal Participating Mass Ratios, nos entrega los modos elegidos con su respectivo periodo, porcentaje de masa 
traslacional y la sumatoria de esta mientras avanza.  
 
Imagen 130. 
✓ En estructuras que están acopladas y que los porcentajes de masa están repartidos en los modos, es necesario 
evaluar la estructura en más de un período en cada dirección. 
20.2.2 
Peso sísmico y Corte basal directo 
Según los expresado en la NCh433, el peso sísmico corresponderá a la sumatoria de D + %SC. Por lo tanto, se acuerdo a lo 
anterior, es posible obtener el peso sísmico total del edificio considerando el valor de PP + CM como D y el valor de la sobrecarga 
de uso multiplicado por su respectivo porcentaje de participación, donde todos los resultado están en la columna 4 (P) de la 
tabla de Story Shears. 
Si la participación de masa acumulada en X y en Y llega 
o supera el 90%, significa que los resultados del 
modelo pueden utilizarse para el diseño. Esto se ve en 
las columnas SumUX y SumUY. 
Cuando lo anterior se comprueba, se busca en las 
columnas 3 y 4 (UX y UY) la que tenga el mayor valor 
de masa traslacional en cada dirección. 
Lo anterior es debido a que de esa forma se determina 
cual será el período de la estructura en cada dirección. 
Candado cerrado 
Imagen 129. 

=== PÁG 45 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
45 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
 
Imagen 131. 
20.2.3 
Centro de masa y Centro de rigidez 
Al definir el diafragma rígido se obtiene: XCM, YCM, XCR e YCR; mientras que si se considera diafragma flexible solo se entrega 
XCM e YCM. Debería obtenerse algo similar si es que se realiza de manera manual.  
Estos valores se encuentran en conjunto en la tabla de Center Mass Rigidity, donde CM es centro de masa; mientras que, CR es 
centro de rigidez.  
 
Imagen 132. 
20.2.4 
Desplazamiento Lateral 
Según lo expuesto en la NCh 433, el desplazamiento relativo máximo entre dos pisos consecutivos, medido en el centro de masa 
de cada una de las direcciones de análisis, no debe ser mayor que la altura de entrepiso multiplicado por 0,002.  
 
Imagen 133. 
 
Además, las cargas EX y EY, nos dan el corte 
sísmico directo que hay en la base. Un valor 
que sirve directamente en la calibración del 
método modal espectral. 
Para EX se considera la columna de Vx; 
mientras que, para EY, se considera la 
columna de Vy. 
 
✓ En todos estos casos, se trabaja con el 
valor ubicado en la localización de 
Bottom, ya que esta incluirá todo el piso. 
Con la tabla Diaphragm CM Displacements, se obtienen los 
desplazamientos laterales en el centro de masa en cada 
dirección debido al sismo en X y en Y.  
De debe tener en consideración los desplazamientos en la tabla 
son acumulativos con respecto al piso inferior; por lo que, para 
trabajar con el resultado por piso, debe restársele la 
deformación que presentó el piso de abajo. 

=== PÁG 46 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
46 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
 
Imagen 134. 
Además, es posible visualizar gráficamente las deformaciones si se selecciona “Display” → “Show Story Response Plots”.  
 Imagen 135. 
20.3 
Calibración Sismo para Método Modal Espectral 
Inicialmente, el valor del factor de escala para la calibración es I/R*, donde I viene dado de acuerdo con la categoría del edificio 
y R* es una ecuación que depende del período obtenido en cada dirección. 
Pero si la reducción del corte directo no es suficiente para ser menor al Qmáx (Cmáx x Psís x I) o mayor al Qmín (Cmín x Psís x 
I), el factor de escala tendrá que incluir el ajuste a los extremos de la siguiente manera: 
𝑄𝑚á𝑥
𝑄𝑟𝑒𝑑𝑢𝑐𝑖𝑑𝑜∗
𝐼
𝑅∗      ó       
𝑄𝑚í𝑛
𝑄𝑟𝑒𝑑𝑢𝑐𝑖𝑑𝑜∗
𝐼
𝑅∗ 
Cuando ya se tiene el ajuste en cada una de las direcciones, se desbloquea el candado del modelo ya que se tendrá que realizar 
una modificación. Luego, se hace click en “Define” → “Response Spectrum Cases”, donde se modificará tanto EX como EY 
seleccionando “Modify/Show Spectrum”. 
Con la tabla Story Drifts, se obtienen los 
desplazamientos laterales en cada dirección 
debido al sismo en X y en Y.  
Donde se tiene que el desplazamiento relativo 
máximo entre dos pisos consecutivos, medido en 
cualquier punto de la planta en ambas 
direcciones, no debe exceder en más de 0,001 h, 
h como altura de entrepiso, al desplazamiento 
relativo medido en el centro de masas. 
Piso superior 
Piso inferior 
Fuerza lateral para evaluar 
Selección de Diafragma 
Color en dirección X 
Color en dirección Y 
Opciones para mostrar gráficamente 

=== PÁG 47 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
47 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
                                                                                                       
 
Imagen 136.                                                                                                                                          Imagen 137. 
✓ Se debe tener en consideración que cualquier cambio significativo en cuanto a la masa y rigidez de la estructura que 
afecte al período, provocará que se vuelva a calibrar el sismo modal espectral. 
20.4 
Vigas en ETABS 
ETABS permite diseñar los elementos frame que se presenten en el proyecto modelado. En este caso, se explicará como se 
realiza el diseño para flexión y carga axial, además del diseño a corte. 
20.4.1 
Diseño de Vigas a Flexión – Carga Axial (Frames) 
Lo primero que debe hacerse, es definir las combinaciones de carga que participarán en el diseño que queremos realizar. Si se 
esta diseñando solo para cargas gravitacionales (diseño estático), no es necesario considerar las combinaciones que incluyan 
sismo en el diseño de frames. Pero en el caso de que sea un diseño dinámico, deben incluirse. 
✓ Se incluyen las combinaciones sísmicas para un diseño a flexión con carga axial.  
Para definir las combinaciones del diseño, se selecciona “Design” → “Concrete Frame Design” → “Select Design Combo”. Esto 
llevará a una ventana que nos permitirá añadir las combinaciones con las que queremos analizar y diseñas los elementos de 
línea. 
 
Imagen 138. 
 
Después de agregar el factor de escala, tanto en 
X como en Y, el modelo estaría calibrado para 
sismo y los resultados podrían tomarse en 
consideración para el diseño dinámico de los 
elementos. 
ETABS trae consigo distintas combinaciones por defecto para el 
diseño, pero se considera seleccionar solo las que se presentan en la 
normativa chilena para el diseño de esfuerzos últimos, LRFD. 
Para agregarlas a Design Combos, se debe hacer click sobre el o los 
combos a agregar y luego presionar Add. De igual manera, si una 
combinación desea eliminarse, debe seleccionarse de la columna 
Design Combos, para luego hacer click en Remove. 

=== PÁG 48 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
48 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
Luego, es necesario ejecutar el ítem de diseño, ya que de otra manera no se podrá hacer el diseño automático. Cuando la 
modelación haya terminado, se debe hacer click en “Design” → “Concrete Frame Design” → “Start Design/Check of Structure”. 
 
Imagen 139. 
 
 
 
 
 
20.4.2 
Diseño de Vigas a Corte (Frames) 
El diseño de refuerzo a corte se muestra seleccionando “Design” → “Concrete Frame Design” → “Display Design Info”. 
Aparecerá una casilla, que permitirá definir qué resultados se deben mostrar en el modelo, ahí se elige “Shear Reinforcing”. 
Cabe mencionar, que Rebar Percentage indica la cuantía en los elementos. 
                    
 
Imagen 141.                                                                                                            Imagen 142. 
✓ El procedimiento para ver el cuadro resumen de diseño es igual al punto anterior. 
✓ La armadura a corte se muestra en unidades de área/longitud. 
20.4.3 
Diseño de Vigas a Flexión – Carga Axial y Corte (Spandrel) 
El procedimiento para este diseño, trabajando con ETABS, es similar a lo 
que se realiza con elementos frames, solo que esta vez el diseño se realiza 
mediante los muros con asignación de tipo Spandrel. Primero debe 
hacerse click en “Design” y luego seleccionar “Shear Wall Design” 
→”Select Design Combos”, para agregar las combinaciones con las que 
se quiere trabajar. Luego de esto, el programa debe estar funcionando 
con sus resultados para que se obtenga el diseño automático. 
Para el diseño de refuerzo longitudinal (As y As’), el programa 
muestra las áreas que se necesitan en los extremos y el centro.  
Para que el número no se vea tan pequeño, hay que cambiar las 
unidades a Ton-cm. 
✓ Este resultado sirve para compararlo con el diseño que se 
realiza por planillas de Excel como un punto de partida. 
Al hacer click derecho sobre cualquiera de las vigas, aparece 
una ventana con la información de su diseño.  
Las casillas de la parte inferior permiten ver las 
consideraciones que se tomaron para el acero de refuerzo 
en el diseño, además de un resumen. 
✓ Se puede ver, que el diseño se realiza en base a ACI 
318-08. 
 
Imagen 140.  

=== PÁG 49 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
49 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
Se deben seleccionar las áreas discretizadas que compongan la viga en tipo Shell, para luego seleccionar “Design” → “Shear 
Wall Design” → “Start Design/Check of Structure”. Luego de que termina el diseño, se debe seleccionar “Display Design Info” 
lo cual abrirá un cuadro con las opciones Design Output y Design Input, considerando la primer casilla se busca: Spandrel 
Longitudinal Reinforcing, para el acero longitudinal en la viga, y Pier/Spandrel Shear Reinforcing, para el refuerzo a corte. 
20.4.4 
Presentación de Gráficos 
ETABS nos permite ver los resultados para fuerza axial, corte y momento en diagramas que pueden ser solo rellenos, como 
diagramas que pueden tener los valores máximos. Para llegar a ellos, se debe seleccionar “Display” → “Show Member 
Forces/Stress Diagram” → “Frame/Pier/Spandrel Forces”.  
Lo anterior abrirá una ventana que permitirá definir: la combinación que se quiere ver, que tipo de esfuerzo (generalmente Shear 
2-2 y Moment 3-3), la escala del diagrama, el tipo de diagrama (relleno o con números) y el tipo de elemento a incluir (elementos 
frame y/o elementos área, pier y spandrel). 
 
Imagen 144. 
Si se hace click derecho sobre el elemento, uno puede moverse dentro del diagrama viendo los valores extremo e intermedios 
de los elementos. Esto resultado también se presentan en tablas para un mejor análisis para el diseño mediante planillas Excel. 
20.4.5 
Extracción de Tablas 
De las tablas, es importante la extracción de los esfuerzos y de las propiedades de los elementos ya que estas servirán para un 
diseño posterior de forma manual guiándose de la normativa requerida. 
Se recomienda descargar las tablas: 
✓ Properties Definitions → Frame Section (dimensiones y propiedades de la sección). 
✓ Properties Definitions → Pier/Spandrel Section Properties (dimensiones de las vigas shell discretizadas: ancho, 
largo, etc). 
✓ Frame Output → Frame Forces (Para vigas y columnas: esfuerzos de carga axial, corte y momento en unidades 
seleccionadas) 
✓ Wall Output  Spandrel Forces (esfuerzos de carga axial, corte y momento en unidades seleccionadas). 
Diagrama relleno de Momento 3-
3 para viga tipo frame 
Diagrama relleno de Corte 2-2 
para viga tipo Shell (Spandrel) 
Imagen 145. 
Imagen 146. 

=== PÁG 50 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
50 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
 
 
20.5 
Verificación Columna Fuerte – Viga Débil 
El diseño debido al análisis estructural del modelo permite obtener la verificación de Columna Fuerte – Viga Débil, según lo 
expuesto en ACI 318-08. Para esto, se debe seleccionar la opción “(6/5) Beam/Column Capacity Ratios” en la imagen 141.  
 
20.6 
Muros en ETABS 
ETABS permite diseñar los elementos Shell (Wall) que se presenten en el proyecto modelado. En este caso, se explicará cómo se 
realiza el diseño para flexión y carga axial, además del diseño a corte. 
20.6.1 
Diseño de Muros a Flexión – Carga Axial 
Lo primero que debe hacerse, es definir las combinaciones de carga que 
participarán en el diseño que queremos realizar. Si se está diseñando solo 
para cargas gravitacionales (diseño estático), no es necesario considerar las 
combinaciones que incluyan sismo en el diseño de muros. Pero en el caso de 
que sea un diseño dinámico, deben incluirse.  
Para definir las combinaciones del diseño, se selecciona “Design” → “Shear 
Wall Design” → “Select Design Combo”. Esto llevará a una ventana que nos 
permitirá añadir las combinaciones con las que queremos analizar y diseñas los elementos de línea. Este procedimiento será 
similar al que se realizó para vigas. 
Imagen 147. 
Imagen 148. 
Imagen 150. 
El diseño arrojará un resultado de acuerdo con la relación que 
se cumpla entre los elementos evaluados. Pero, en el caso de 
que no se cumpla la relación en cuestión, el análisis 
estructural destacará la columna con las letras “N/A”, lo cual 
indicaría modificar las dimensiones de la columna. 
Imagen 149. 

=== PÁG 51 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
51 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
Luego, se deben definir las secciones Pier con las que se quiere trabajar. Se debe definir el nombre, material y la opción Start 
from Existing Wall Pier, indicando el piso y el pier a analizar (el cual debe estar designado anteriormente). Esto abrirá la opción 
de Section Designer, la cual es útil cuando se calcula en base a los esfuerzos el refuerzo manualmente que debe tener el muro 
ya que nos permite sacar la curva minorizada de interacción. 
✓ En este caso, se considera la sección predefinida ya que el diseño nos dará la cantidad de armadura necesaria, la cual 
debe verificarse luego por cálculos manuales. 
Con los Pier de diseño definidos, se debe echar a correr el modelo para que pueda ocurrir el análisis. Cuando la modelación haya 
terminado, se debe hacer click en “Design” → “Shear Wall Design” → “Start Design/Check of Structure”. 
 
Imagen 151. 
20.6.2 
Diseño de Muros a Corte 
El diseño de refuerzo a corte se muestra seleccionando “Design” → “Concrete Frame Design “→ “Display Design Info”. 
Aparecerá una casilla, que permitirá definir qué resultados se deben mostrar en el modelo, ahí se elige “Pier/Spandrel Shear 
Reinforcing”. 
 
Imagen 152. 
20.6.3 
Presentación de Gráficos 
ETABS nos permite ver los resultados para fuerza axial, corte y momento en diagramas que pueden ser solo rellenos, como 
diagramas que pueden tener los valores máximos. Para llegar a ellos, se debe seleccionar “Display” → “Show Member 
Forces/Stress Diagram” → “Frame/Pier/Spandrel Forces”.  
Lo anterior abrirá una ventana que permitirá definir: la combinación que se quiere ver, que tipo de esfuerzo (generalmente Shear 
2-2 y Moment 3-3), la escala del diagrama, el tipo de diagrama (relleno o con números) y el tipo de elemento a incluir (elementos 
frame y/o elementos área, pier y spandrel). 
Para el diseño de refuerzo longitudinal, el programa muestra las 
áreas que se necesitan como radios con respecto a la sección 
creada.  
✓ Este resultado sirve para compararlo con el diseño que se 
realiza por planillas de Excel como un punto de partida. 

=== PÁG 52 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
52 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
 
20.6.4 
Extracción de Tablas 
De las tablas, es importante la extracción de los esfuerzos y de las propiedades de los elementos ya que estas servirán para un 
diseño posterior de forma manual guiándose de la normativa requerida. 
Se recomienda descargar las tablas: 
✓ Properties Definitions → Pier/Spandrel Section Properties (dimensiones de las vigas shell discretizadas: ancho, 
largo, etc). 
✓ Wall Output  Pier Forces (esfuerzos de carga axial, corte y momento en unidades seleccionadas). 
20.7 
Curva Interacción  
Para obtener la curva interacción de elementos estructurales como muros o columnas, se debe seleccionar la flecha del icono 
 y luego dar click en “Define Pier Sections for Checking”. Esto lanzará una ventana emergente de Pier Sections, donde se 
debe reingresar en Add Pier Section las identificaciones antes propuestas, pero solo de los elementos que se quieren evaluar. 
                                       
 
Imagen 155.                                                                                  Imagen 156. 
Se debe dar un nombre, definir el material del elemento y considerar la alternativa “Start form Existing Wall Pier”, ya que las 
secciones ya fueron identificadas anteriormente con Piers Name. Se selecciona el nivel en el que esta el elemento estructural y 
su ID, para luego hacer click en “Section Designer”. 
 
 
Diagrama relleno de Corte 2-2 
para muro tipo Shell (Pier) 
Imagen 153. 
Imagen 154. 

=== PÁG 53 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
53 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
La ventana emergente de CSISD, donde se permite modificar la forma y la armadura de refuerzo que tendrá el elemento que se 
está analizando, haciendo click sobre el acero. Para obtener la curva interacción del programa se debe seleccionar sobre el 
siguiente icono: 
. 
                             
 
Imagen 157.                                                                                                              Imagen 158. 
La curva interacción se muestra por carga axial, momento M3-3 y momento M2-2. Además, se puede seleccionar si se desea 
visualizar con minoración debido a phi, sin minoración o sin minoración con aumento en el valor de fy. Para procesarla, se 
considera la curva minorizada con phi y se copian todos los resultados en “Edit” → “Copy All”.  
✓ Al pegar los resultados en Excel, hay que tener en consideración que cuando se analizan Muros, solo será útil la curva 
con 0° y 180°, solo la dirección fuera del plano M3-3; mientras que cuando se analizan columnas, se mantienen los 
resultados de 0°, 90°, 180°y 270°, debido a que se analiza para ambas direcciones de momento (M2-2 y M3-3). 
✓ También, se debe tener en consideración que ETABS entrega los valores de esfuerzos axiales con signo distinto al que 
se analiza comúnmente, siento el valor negativo: compresión y el positivo: tracción. 
Luego de procesar los resultados, se debe cambiar el signo del esfuerzo axial para luego graficar los resultados, como se 
muestra en la imagen 160. Donde, el momento (M3-3) será parte de las abscisas (X), mientras que la compresión y tracción 
serán la ordenada del gráfico (Y). 
 
Imagen 159.                                                                                   
 
 
Imagen 160. 
 

=== PÁG 54 ===
Manual de Modelación, Análisis y Diseño Estructural en ETABS v.9.7.4 
Página 
54 de 54 
                                                                                                
 
Este documento es propiedad intelectual de la Escuela de Ingeniería Civil de la Universidad Católica del Maule. 
Se prohíbe su reproducción sin su consentimiento. 
 
21. Referencias  
American Concrete Institute. (2008). Requisitos de Reglamento para Concreto Estructural (ACI 318S-08). ISBN: 978-0-87031-
264-9. Farmington Hill. Michigan. USA. 
American Concrete Institute. (2014). Requisitos de Reglamento para Concreto Estructural (ACI 318SUS-14). ISBN: 978-0-87031-
960-0. Farmington Hill. Michigan. USA. 
Computers & Structures INC. (2009). Automated Lateral Loads Manual For ETABS. Berkeley. California. USA. 
Computers & Structures INC. (2010). Concrete Frame Design Manual – ACI 318-08/IBC 2009 For ETABS. Berkeley. California. 
USA. 
Guendelman, T. (2004). Análisis Estático y Dinámico de Estructuras. ISBN: 978-956-7393-92-3. Editorial MIDAS IT. La Serena. 
Chile. 
Instituto Nacional de Normalización. (2009). Norma Chilena Oficial: 433 – Diseño Sísmico de Edificios. Santiago. Chile. 
Instituto Nacional de Normalización. (2017). Norma Chilena Oficial: 3171 – Diseño Estructural – Disposiciones Generales y 
Combinaciones de Cargas. Santiago. Chile. 
Ministerio de Vivienda y Urbanismo. (2011). Decreto Supremo 61. Santiago. Chile. 
American Society of Civil Engineers. (2016). ASCE 7 – Minimum Design Loads and Associated Criteria for Buildings and Other 
Structures. ISBN: 978-0-7844-7996-4. Reston. Virginia. USA. 
 
 
 
 
 
 
 
```
