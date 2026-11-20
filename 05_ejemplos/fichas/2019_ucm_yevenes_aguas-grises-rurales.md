# Ejemplo: Tratamiento y reutilización de aguas grises en sectores rurales (Yévenes, 2019)

- **Archivo:** `05_ejemplos/tesis/2019_ucm_yevenes_aguas-grises-rurales_parte1.pdf` y `_parte2.pdf` (texto en `…aguas-grises-rurales.md`)
- **Tipo:** tesis de pregrado (Ingeniería Constructor, UCM, enero 2019)
- **Autor / institución / año:** Diego Esteban Yévenes Valdés · Universidad Católica del Maule · 2019 · **profesor guía: Ismael L. Vera Puerto**
- **Tema:** estimación de la producción de aguas grises en 3 viviendas rurales (Talca) con fichas de registro de uso y aforos; diseño y costo de una fosa séptica + alternativa convencional (Ecostep Pro) frente a un humedal de flujo vertical.
- **Relación con mi tesis:** **alta**. Es el "trabajo de Diego" que el profesor guía indicó como modelo (revisión del 16-11-2026):
  "Debe ligarse con anexos donde se muestren las fichas que se utilizaron… Fíjate cómo está ahí redactado".
  Sirve para el cap. 3 (caracterización y producción de aguas), el cap. 2 (balance de oxígeno) y los anexos.
- **¿Es fuente citable según la normativa?** Dudoso (tesis de pregrado). Usarla como **modelo de redacción y de método**;
  para valores técnicos citar la fuente original que ella cita (p. ej. Platzer, 1999).

## Qué hace bien (para imitar la forma, no el texto)

| Aspecto | Dónde (pág. del PDF) | Cómo aplicarlo en mi tesis | Archivo destino |
|---|---|---|---|
| Metodología en orden: ubicación del proyecto → estimación de producción → diseño → comparación | Parte 1, cap. 3 (pp. 14–19 numeradas) | Mismo orden ya adoptado: área de estudio → caracterización → diseño | `capitulos/03_metodologia.tex` |
| Explica **cómo se usaron las fichas**: qué artefactos, por qué esos, cuánto tiempo, dónde se pegaron, cada cuánto se renovaron, con foto de la ficha instalada | Parte 1, §3.2 | Describir igual las fichas de oficinas (WC, lavamanos, lavaplatos) y remitir al anexo | `capitulos/03_metodologia.tex` + anexo de fichas |
| Explica el **aforo**: llave abierta un tiempo medido con cronómetro, agua recogida y medida con probeta; tiempo por uso preguntado a los usuarios | Parte 1, §3.2 | Describir el aforo de los artefactos de oficinas (caudal y tiempo por uso) | `capitulos/03_metodologia.tex` |
| **Anexos con las fichas en blanco** (Anexos 1–3) y con los **registros tabulados** (Anexos 10–11) | Parte 1 pp. 47–49; Parte 2 | Anexo con la ficha usada + anexo con el registro semanal de usos | `anexos/anexo_fichas_registro.tex` |
| Resultados: tabla de usos/día por artefacto (media ± desviación) y luego caudal diario | Parte 1, §4.1, tablas 5–9 | Presentar usos por artefacto y escenario, luego volumen diario | `capitulos/04_resultados.tex` |
| **Anexo 9**: balance de oxígeno con **cada término explicado** y sus unidades, ecuaciones numeradas y luego el cálculo | Parte 2, pp. 8–11 (numeradas 57–60) | Es "lo que te falta arriba" que pidió el profesor: explicar cada término | `capitulos/02_marco_teorico.tex`, `anexos/anexo_calculos_humedal.tex` |

## Métodos, criterios o valores útiles

| Elemento | Pág. | Fuente original que cita el ejemplo | ¿Verificado? |
|---|---|---|---|
| OD_DQO = 0,85 × 0,7 g O₂/g DQO × carga DQO (0,7 g O₂/g DQO; **0,85 = eficiencia media de eliminación de DQO** en HC-FV) | Parte 2, Anexo 9 | Platzer (1999) | Coincide con el anexo de cálculo del proyecto; verificar en el original |
| OD_nitrificación = 4,3 g O₂/g NTK × carga NTK (nitrificación completa) | Anexo 9 | Platzer (1999) | Ídem |
| **OD_desnitrificación = 0,10 × 2,9 g O₂/g N × carga NTK** (≈ 10 % de desnitrificación) — el cálculo del proyecto lo omite (lado seguro) | Anexo 9 | Platzer (1999) | Ídem (el ejemplo escribe por error "g O₂/g CQO") |
| OI_difusión = 1 g O₂/(h·m²) × A × (24 − 1,5·n_cargas); **1,5 h sin difusión después de cada carga** | Anexo 9 | Platzer (1999) | Ídem |
| OI_convección = 0,3 g O₂/L × volumen cargado; **0,3 g/L = contenido de O₂ del aire (300 mg/L)** | Anexo 9 | Platzer (1999) | Ídem |
| Parámetros de diseño de HC-FV: carga orgánica (g DQO/m²·d), área por persona equivalente (m²/PE), oferta y demanda de O₂ | Anexo 9 | — | — |

## Qué NO imitar

- Títulos de anexos en minúscula inconsistente ("métodos de diseño Humedal flujo vertical") y errores de tipeo ("Humedad Construido").
- Tablas con líneas verticales y figuras sin "Fuente:" (la normativa UCM y el profesor piden solo líneas horizontales).
- Citar valores de diseño sin la fuente original en la tabla.

## Diferencias de formato con la normativa UCM

- Es de 2019 y de otra carrera (Ingeniería Constructor): estructura parecida, pero no sigue la normativa ICV-611 actual (portada, índices con "Pág.", leyendas "Figura N.N:").
