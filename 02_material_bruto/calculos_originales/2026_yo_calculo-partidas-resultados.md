# 

# 1.- Calculo de la Estructura:

Más que en los calculos necesito la revisión de las conclusiones y de la tabla de valores aproximados, para confirmar la elección de los materiales para empezar a detallar la construccion en los planos.

## <span class="smallcaps">MÓDULO I: ANÁLISIS DE CARGAS DE ESTANQUES Y DISEÑO DEL SUELO DE MADERA</span>

<span class="mark">--- 1. CONTROL DE CARGAS DE LOS ESTANQUES ---</span>

<span class="mark">-\> Volumen de agua por estanque: 0.785 m³</span>

<span class="mark">-\> Peso de agua por estanque: 785.4 kg</span>

<span class="mark">-\> Peso TOTAL de 1 estanque lleno: 825.4 kg</span>

<span class="mark">-\> Fuerza puntual equivalente por estanque: 8.10 kN</span>

<span class="mark">--- 2. VERIFICACIÓN DE SERVICIABILIDAD DEL SUELO (OGUC / NCh1198) ---</span>

<span class="mark">-\> Distancia entre costaneras de apoyo (Luz de la madera): 40 cm</span>

<span class="mark">-\> Restricción de deformación máxima permitida (L/300): 1.33 mm</span>

<span class="mark">Probando plancha de 15 mm -\> Deflexión proyectada a largo plazo: 1.85 mm</span>

<span class="mark">==============================================================================</span>

<span class="mark">CONCLUSIÓN DEL MÓDULO I:</span>

<span class="mark">==============================================================================</span>

<span class="mark">\[CUMPLE\] Una plancha de madera de 15 mm.</span>

## MÓDULO II: ANÁLISIS DE LA VIGA CONTINUA DE ACERO (5.5 m)

<span class="mark">--- 1. CARGAS DE DISEÑO FACTORIZADAS (LRFD) ---</span>

<span class="mark">-\> Carga muerta lineal de servicio (w_D): 0.75 kN/m</span>

<span class="mark">-\> Carga viva lineal de servicio (w_L): 4.42 kN/m</span>

<span class="mark">-\> Carga última distribuida de diseño (w_u): 7.97 kN/m</span>

<span class="mark">--- 2. DIAGRAMA DE SOLICITACIONES MÁXIMAS (BARRAS DE ACERO) ---</span>

<span class="mark">-\> Momento Flector Positivo Máximo (en el tramo): 4.24 kN-m</span>

<span class="mark">-\> Momento Flector Negativo Máximo (Peak sobre pilar central): 7.53 kN-m</span>

<span class="mark">-\> Esfuerzo de Corte Máximo de Diseño (Vu): 13.70 kN</span>

<span class="mark">-\> Razón de momentos (M_neg / M_pos): 1.78 (El momento sobre el pilar es 1.77 veces mayor)</span>

<span class="mark">--- 3. TRASPASO DE CARGAS HACIA LAS FUNDACIONES (Fuerzas Axiales en Pilares) ---</span>

<span class="mark">-\> Fuerza de servicio en Pilares de las Esquinas (4 unidades): 5.33 kN</span>

<span class="mark">-\> Fuerza de servicio en Pilares Centrales (2 unidades): 17.77 kN</span>

<span class="mark">==============================================================================</span>

<span class="mark">CONCLUSIÓN DEL MÓDULO II:</span>

<span class="mark">==============================================================================</span>

<span class="mark">-\> El Pilar Central absorbe el 62.5% de la carga total de la estructura.</span>

<span class="mark">-\> Para el diseño de las barras en el Módulo III, se deben utilizar los siguientes valores de demanda:</span>

<span class="mark">\* Viga de Acero: Flexión de Diseño (Mu) = 7.53 kN-m</span>

<span class="mark">\* Viga de Acero: Corte de Diseño (Vu) = 13.70 kN</span>

<span class="mark">\* Columna (Pilar Central): Carga Axial de Compresión de Servicio (Pu) = 17.77 kN</span>

## MÓDULO III: VERIFICACIÓN Y DISEÑO DEL PERFIL DE LA VIGA (25x25 cm)

<span class="mark">--- 1. PROPIEDADES GEOMÉTRICAS Y CONTROL DE PANDEO LOCAL ---</span>

<span class="mark">-\> Razón ancho/espesor del ala flectada (b/e): 39.67</span>

<span class="mark">-\> Límite normativo para ala compacta: 32.46</span>

<span class="mark">-\> Clasificación de la sección: \[ALERTA\] Sección ESBELTA. Se requiere factor de reducción Q.</span>

<span class="mark">--- 2. EVALUACIÓN DE CAPACIDADES REALES (LRFD) ---</span>

<span class="mark">-\> Resistencia de Diseño a la Flexión (Phi\*Mn): 104.66 kN-m</span>

<span class="mark">-\> Momento Flector Máximo Solicitante (Mu): 7.53 kN-m</span>

<span class="mark">-\> Resistencia de Diseño al Esfuerzo de Corte (Phi\*Vn): 405.00 kN</span>

<span class="mark">-\> Esfuerzo de Corte Máximo Solicitante (Vu): 13.70 kN</span>

<span class="mark">==============================================================================</span>

<span class="mark">CONCLUSIÓN DEL MÓDULO III:</span>

<span class="mark">==============================================================================</span>

<span class="mark">-\> Razón de Trabajo por Flexión (Mu / Phi\*Mn): 0.072</span>

<span class="mark">-\> Razón de Trabajo por Corte (Vu / Phi\*Vn): 0.034</span>

<span class="mark">\[CUMPLE\] El perfil cuadrado de 25x25 cm x 6 mm es aceptable estructuralmente.</span>

<span class="mark">\* Posee una tasa de utilización por flexión del 7.2%.</span>

<span class="mark">\* Posee una tasa de utilización por corte del 3.4%.</span>

## MÓDULO IV: ANÁLISIS DE CARGA SÍSMICA INDUSTRIAL Y DISEÑO DE PILARES

<span class="mark">--- 1. PARÁMETROS SÍSMICOS INDUSTRIALES (NCh2369:2025) ---</span>

<span class="mark">-\> Coeficiente Sísmico de Diseño Industrial (C): 0.360</span>

<span class="mark">-\> Esfuerzo de Corte Sísmico Horizontal del Marco: 10.80 kN</span>

<span class="mark">-\> Momento de Volcamiento Sísmico inducido en la base del pilar: 12.15 kN-m</span>

<span class="mark">--- 2. VERIFICACIÓN DE ESTABILIDAD Y PANDEO GLOBAL DE LA COLUMNA ---</span>

<span class="mark">-\> Esbeltez efectiva del pilar (KL/r): 47.42 (Límite máximo normativo: 200)</span>

<span class="mark">-\> Esfuerzo actuante por compresión axial (fc): 3640.50 kN/m²</span>

<span class="mark">-\> Esfuerzo admisible límite al pandeo (Fcr_adm): 129577.76 kN/m²</span>

<span class="mark">-\> Esfuerzo actuante por flexión sísmica (fm): 26121.27 kN/m²</span>

<span class="mark">==============================================================================</span>

<span class="mark">CONCLUSIÓN DEL MÓDULO IV:</span>

<span class="mark">==============================================================================</span>

<span class="mark">-\> Índice / Razón de Interacción por Flexocompresión Combinada: 0.188</span>

<span class="mark">\[CUMPLE\] El perfil cuadrado de 25x25 cm resiste las fuerzas sísmicas industriales de la Zona 3.</span>

<span class="mark">\* Razón de trabajo final: 18.8% de la capacidad última de la barra.</span>

<span class="mark">\* Nota: El gran tamaño del perfil (25x25 cm) absorbe el momento volcante sin peligro de inestabilidad estructural.</span>

## MÓDULO V: DISEÑO DE FUNDACIONES Y DETALLES DE CONEXIÓN

<span class="mark">--- 1. DISEÑO DE FUNDACIÓN AISLADA DE HORMIGÓN ARMADO ---</span>

<span class="mark">-\> Lado mínimo teórico de la zapata: 0.34 m</span>

<span class="mark">-\> Dimensión en planta especificada en memoria: 0.80 m x 0.80 m</span>

<span class="mark">-\> Espesor o peralte total de la zapata (H): 0.40 m (40 cm)</span>

<span class="mark">-\> Presión real transmitida al suelo en servicio: 27.76 kN/m² (\< q_adm = 150.0 kN/m²???)</span>

<span class="mark">--- 2. VERIFICACIÓN DE CONEXIÓN SOLDADA (VIGA-PILAR) ---</span>

<span class="mark">-\> Tamaño del filete de soldadura propuesto (s): 6 mm</span>

<span class="mark">-\> Garganta efectiva del cordón (t): 4.24 mm</span>

<span class="mark">-\> Resistencia última de diseño de la soldadura: 916.27 kN/m</span>

<span class="mark">-\> Longitud lineal mínima requerida por cálculo de corte: 1.5 cm</span>

<span class="mark">-\> Longitud perimetral real disponible en el perfil de 25x25 cm: 100.0 cm</span>

<span class="mark">==============================================================================</span>

<span class="mark">CONCLUSIÓN DEL MÓDULO V:</span>

<span class="mark">==============================================================================</span>

<span class="mark">\[CUMPLE\] Fundación de 0.8x0.8x0.4 m es estructuralmente correcta.</span>

<span class="mark">\[CUMPLE\] La soldadura de filete perimetral continua de 6 mm es plenamente capaz.</span>

<span class="mark">\* Nota: Se dispone de 100 cm de longitud real frente a los 1.5 cm exigidos por corte.</span>

<span class="mark">\* Especificación en plano: Cordón continuo en todo el contorno de la unión viga-columna.</span>

## MÓDULO EXTRA: DISEÑO DE VIGAS SECUNDARIAS (COSTANERAS DE 150x50x3 mm)

<span class="mark">--- 1. VERIFICACIÓN DE RESISTENCIA ÚLTIMA (ACERO 150x50x3 mm) ---</span>

<span class="mark">-\> Momento Flector de Diseño (Mu): 5.13 kN-m</span>

<span class="mark">-\> Resistencia Admisible a Flexión (Phi\*Mn): 11.96 kN-m</span>

<span class="mark">-\> Esfuerzo de Corte de Diseño (Vu): 3.60 kN</span>

<span class="mark">-\> Resistencia Admisible a Corte (Phi\*Vn): 121.50 kN</span>

<span class="mark">--- 2. VERIFICACIÓN DE FLECHA (SERVICIABILIDAD) ---</span>

<span class="mark">-\> Deflexión máxima real en el centro de la costanera: 3.81 mm</span>

<span class="mark">-\> Deflexión máxima permitida por norma (L/300): 10.00 mm</span>

<span class="mark">==============================================================================</span>

<span class="mark">CONCLUSIÓN DEL MÓDULO EXTRA:</span>

<span class="mark">==============================================================================</span>

<span class="mark">\[CUMPLE\] El perfil trabaja al 42.9% de su capacidad a flexión.</span>

<span class="mark">\[CUMPLE\] La costanera es suficientemente rígida.</span>

<span class="mark">El perfil 150x50x3 mm instalado de canto cada 40 cm es ideal para el proyecto.</span>

<img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image4.png" style="width:7.84786in;height:5.87808in" />

<img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image5.png" style="width:7.84252in;height:5.875in" />

## Tabla de costos

| **Ítem**          | **Cantidad a Comprar** | **Unidad** | **Valor Unitario (\$)** | **Valor Total (\$)** | **Especificación Técnica Sugerida**                                             |
|-------------------|------------------------|------------|-------------------------|----------------------|---------------------------------------------------------------------------------|
| Pilar 250x250x6mm | 14                     | m          | \$55.000                | \$770.000            | Para los 6 pilares                                                              |
| Viga 250x250x6mm  | 17                     | m          | 55.000                  | \$935.00             | Para las vigas principales que van montadas en los pilares por todo el contorno |
| Viga 150x50x3mm   | 39                     | m          | \$11.000                | \$429.000            | Para las vigas secundarias que van ir trnasversalmente.                         |
| Plancha de 15mm   | 6                      | und        | \$22.000                | \$132.000            | Para la superficie superior, será el suelo.                                     |

#  

# 2.- Calculo de Excavaciónes

Los calculos fueron realizados con una inclinación de un 2% lo que asegura que no vamos a tener obstrucción por poca pendiente o separación de liquido/solidos.

El valor que mas nos importa en la tabla es la **Excavación Total** en metros y cuantos metros va estar **Tapada** por debajo del nivel del suelo en el punto más bajo del trayecto.

<img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image3.jpg" style="width:6.30364in;height:6.69707in" />

## Camara Aguas Quimicas - Camara Nueva (107m lineales)

<img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image9.png" style="width:7.85079in;height:5.98306in" />

## Camara Aguas Sanitarias Oficina - Camara Nueva (37m lineales)

<img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image8.png" style="width:7.84252in;height:6.45833in" />

## Tabla de costos

| **Ítem**     | **Cantidad** | **Unidad** | **Valor Unitario (\$)** | **Valor Total (\$)** | **Especificación Técnica Sugerida** |
|--------------|--------------|------------|-------------------------|----------------------|-------------------------------------|
| Excavación 1 | 14           | m3         | \$55.000                | \$770.000            | Cubicación                          |
| Excavación 2 | 17           | m3         | 55.000                  | \$935.00             | Cubicación                          |

#  

# 3.- Calculo de Bombas

## CÁLCULO BOMBA TRANSVERSAL 

<span class="mark">¿Cuántos litros deseas llenar?: 1000 Lts</span>

<span class="mark">¿En cuántos minutos deseas llenarlo?: 30 m</span>

<span class="mark">Altura de succión (Metros desde el agua hasta la bomba): 6 m</span>

<span class="mark">Altura de impulsión (Metros hacia arriba desde la bomba al destino final): 5 m</span>

<span class="mark">Distancia horizontal de impulsión (Metros): 100 m</span>

<span class="mark">Diámetro interno de la tubería (en milímetros): 30 mm</span>

<span class="mark">Presión requerida al final (0 si es descarga libre): 0 bar</span>

<span class="mark">==============================================================================</span>

<span class="mark">RESULTADOS BOMBA TRANSVERSAL</span>

<span class="mark">==============================================================================</span>

<span class="mark">Caudal requerido: 0.56 Litros/segundo (2.00 m3/hora)</span>

<span class="mark">Pérdidas por fricción en tubería: 3.07 metros</span>

<span class="mark">Altura Dinámica Total (ADT) requerida: 14.07 metros</span>

<span class="mark">-\> Necesito buscar una bomba que levante al menos 14.07 metros a un caudal de 0.56 l/s o 2 m3/h.</span>

## CÁLCULO BOMBA SUMERGIBLE MÁS DESFAVORABLE

<span class="mark">¿Cuántos litros deseas llenar?: 1000 Lts</span>

<span class="mark">¿En cuántos minutos deseas llenarlo?: 30</span>

<span class="mark">Altura de impulsión (Metros hacia arriba, desde la bomba al destino final): 5 m</span>

<span class="mark">Distancia horizontal de impulsión (Metros): 100 m</span>

<span class="mark">Diámetro interno de la tubería (en milímetros): 30 mm</span>

<span class="mark">Presión requerida al final (0 si es descarga libre): 0</span>

<span class="mark">==============================================================================</span>

<span class="mark">RESULTADOS BOMBA SUMERGIBLE</span>

<span class="mark">==============================================================================</span>

<span class="mark">Caudal requerido: 0.56 Litros/segundo (2.00 m3/hora)</span>

<span class="mark">Pérdidas por fricción en tubería: 2.90 metros</span>

<span class="mark">Altura Dinámica Total (ADT) requerida: 7.90 metros</span>

<span class="mark">-\> Necesito buscar una bomba sumergible que entregue 7.90 metros a un caudal de 0.56 l/s o 2 m3/h.</span>

- CÁLCULO BOMBA SUMERGIBLE PARA RIEGO

Número de plantas: 10

Número de goteros por planta: 8

Caudal de cada gotero en Litros/hora: 2 Lts

Altura de impulsión (Metros hacia arriba desde la bomba al terreno): 0.5 M

Distancia horizontal total de la tubería principal (Metros): 65 m

Diámetro interno de la tubería: 30 mm y 16 mm

Presión de trabajo de los goteros: 1 bar

<span class="mark">==============================================================================</span>

RESULTADOS BOMBA DE RIEGO

<span class="mark">==============================================================================</span>

Caudal total requerido del sistema: 160.00 Litros/hora (0.0444 Litros/segundo)

Pérdidas por fricción estimadas: 0.02 metros

Presión necesaria para abrir los goteros: 10.20 metros (1.0 Bar)

Altura Dinámica Total (ADT) requerida: 10.71 metros

-\> Necesito buscar una bomba sumergible que entregue 10.71 metros de altura a un caudal de 160.00 l/h o 0.16 m3/h.

## Bombas Transversales Posibles

<img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image7.jpg" style="width:7.84375in;height:9.5438in" /><img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image1.png" style="width:1.03777in;height:1.04167in" /><img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image1.png" style="width:1.04474in;height:1.04474in" />

## Bombas Sumergibles Posibles

<img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image2.jpg" style="width:7.84375in;height:7.77994in" /><img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image1.png" style="width:1.04474in;height:1.04474in" /><img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image1.png" style="width:1.03777in;height:1.04167in" /><img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image1.png" style="width:1.03777in;height:1.04167in" />

<img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image1.png" style="width:1.03777in;height:1.04167in" />

<img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image6.jpg" style="width:7.84375in;height:8.38755in" /><img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image1.png" style="width:1.04474in;height:1.04474in" /><img src="/tmp/claude-0/-home-user-Tesis/0c9ab8c1-e540-5bc1-a1dc-ca79c816e29f/scratchpad/partidas_media/media/image1.png" style="width:1.04474in;height:1.04474in" />
