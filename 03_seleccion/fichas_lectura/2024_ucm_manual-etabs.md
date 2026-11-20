# Morales y Venegas (2024) — Manual de modelación, análisis y diseño estructural en ETABS v9.7.4 (UCM)

- **Clave BibTeX:** — (**NO citar ni mencionar ETABS en la tesis**: instrucción del autor, 2026-11-20; ETABS no se usó)
- **Referencia:** Morales Matamala, J. (elab.) y Venegas Zurita, J. P. (aprob.) (2024). *Manual de modelación, análisis y diseño estructural en ETABS v.9.7.4*, Rev. 0. Escuela de Ingeniería Civil, Universidad Católica del Maule. Documento interno.
- **PDF:** `02_material_bruto/papers/2024_ucm_manual-etabs-v9.7.4_rev0.pdf` (54 págs.)
- **Tipo:** manual docente interno (no es fuente citable según la normativa: solo apoyo de método).
- **Relevancia para la tesis:** media — sirve para **entender el método** (cargas, diafragma, sismo, combinaciones) del cálculo estructural hecho a mano / en Python; las fuentes que se citan son las normas que el manual nombra.

## En una frase

Guía paso a paso de modelación en ETABS; lo útil para la tesis son sus resúmenes de estados de carga, diafragma rígido, sismo estático (NCh433/DS 61) y combinaciones LRFD/ASD de la **NCh3171 Of.2017**.

## Ideas útiles (pág. del PDF)

1. **Estados de carga** (p. 29): peso propio (D1), carga permanente (D2: elementos no estructurales permanentes, instalaciones), sobrecarga de uso (L), de techo (Lr), viento, sismo.
2. **Diafragma rígido** (p. 29–30): si la losa/cubierta cumple los requisitos (ASCE 7, cap. 12.3), todos los puntos del nivel tienen el mismo desplazamiento y la fuerza sísmica se reparte entre los elementos verticales según su rigidez; un diafragma semirrígido "puede considerarse equivalente a no utilizar ninguno". → **Base para la pregunta 1** (¿los 6 pilares comparten el sismo?): depende de que el tablero + vigas formen un diafragma rígido en su plano (conexiones, arriostramiento horizontal). Respaldar con la norma (NCh2369 / NCh433), no con el manual.
3. **Sismo estático** (p. 31–32): corte basal con coeficiente sísmico C (NCh433 6.2.3.1 y DS 61 art. 15.1), acotado por C_min (DS 61 15.2) y C_max (NCh433 tabla 6.4); aplicado en el centro de masa, con excentricidad accidental. Para la plataforma corresponde la NCh2369 (estructura industrial): verificar cuál aplica (pregunta 1).
4. **Masa sísmica** (p. 34): carga permanente + 25 % o 50 % de la sobrecarga de uso (NCh433 5.5). En la plataforma el agua de los estanques es carga de operación (100 % en NCh2369): confirmar.
5. **Combinaciones LRFD, NCh3171 Of.2017** (p. 35): 1) 1,4D; 2) 1,2D + 1,6L + 0,5(Lr o S o R); 3a) 1,2D + 1,6(Lr o S o R) + L; 3b) 1,2D + 1,6(Lr o S o R) + 0,8W; 4) 1,2D + 1,6W + L + 0,5(Lr o S o R); 5) 1,2D + 1,4E + L + 0,2S; 6) 0,9D + 1,6W; **7) 0,9D + 1,4E**. ASD: D; D+L; …; D+E; D+0,75E+0,75L+0,75S; 0,6D±W; **0,6D+E**.

## Consecuencias para la tesis

- Confirma la marca `\revisar` del cap. 2: las combinaciones vienen de la **NCh3171** (Of.2017), no de la NCh427/1 → agregar la NCh3171 a la bibliografía (con la norma a la vista).
- La tabla de combinaciones de la tesis (1,4D; 1,2D+1,6L; 1,2D+1,0L+1,4E) **omite 0,9D + 1,4E**, que es la que gobierna el **volcamiento y el levantamiento de las zapatas** (menos peso estabilizante). Revisar la verificación de zapatas con esa combinación.
- Si el agua de los estanques se trata como carga de operación (NCh2369) y no como sobrecarga de uso, cambia qué factor se le aplica (pregunta pendiente al co-guía).

## Qué NO hacer

- No mencionar ETABS ni modelos computacionales en la tesis (no se usaron).
