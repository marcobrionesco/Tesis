# Respuestas a PREGUNTAS_REUNION.md (borrador acordado con el autor)

> Documento de trabajo **fuera del repositorio**. Para que Claude Code lo integre más adelante
> (PREGUNTAS_REUNION.md, DECISIONES.md, capítulos 2–5 y OBSERVACIONES_PROFESOR.md).
> Las respuestas rotuladas **APROBADA** fueron aprobadas por el autor; las rotuladas **PROPUESTA** (8 y 12) esperan su visto bueno. Son decisiones/propuestas del autor para la tesis y para llevar a la reunión; no son respuestas del profesor.

---

## Pregunta 1 — Sismo y zapatas (NCh2369) — APROBADA por el autor (2026-11-20), todas las sub-preguntas

### Respuesta

| Sub-pregunta | Respuesta | Estado |
|---|---|---|
| (a) ¿NCh2369:2003 o 2025? | **NCh2369:2025.** Con la 2003 el resultado es equivalente; la 2003 solo como antecedente. | Aprobada |
| (b) ¿Categoría I (I = 0,8) o II (I = 1,0)? | **Categoría I** (I = 0,8): estructura y equipo menor o provisional, cuya falla no detiene la operación ni pone en peligro otras estructuras. | Aprobada |
| (c) ¿Sistema resistente? | Marco a momento de acero sin anclajes dúctiles, **R = 3** (ξ = 0,02, todo soldado, uniones firmes). No es péndulo invertido (6 pilares). | Aprobada |
| (d) ¿Tipo de suelo? | **No clasificado** por falta de mecánica de suelos. Se **supone suelo C** (el más desfavorable de los plausibles) y q_adm = 150 kPa (φ′ ≈ 32°, arena suelta, Terzaghi/Das 2015). Recomendar mecánica de suelos antes de construir. | Aprobada (supuesto declarado) |
| (e) ¿Diafragma que reparte el sismo entre los 6 pilares? | **Sí: tablero y vigas funcionan como diafragma y los 6 pilares reparten el corte; con eso la zapata cumple** (área apoyada 91 % con I = 0,8 y suelo C). Sin diafragma vuelca. Nota para la tesis: justificar el diafragma en la metodología (un tablero fenólico con fijaciones suele considerarse flexible; conviene describir la conexión). | Aprobada |

### Resultado de la comparación 2003 vs 2025 (zapata 1,0 × 1,0 × 0,5 m, zona 2, A₀ = 0,30 g, R = 3)

Criterio: al menos 80 % del área apoyada (NCh2369:2025, 10.1, combinaciones ASD, e ≤ 0,233·B).

| Caso | Pilares que toman el sismo | C | V (kN) | e (m) | Área apoyada |
|---|---|---|---|---|---|
| 2003 (C = 2,7·A₀/R, como el cálculo original) | 2 | 0,270 | 11,5 | 0,65 | vuelca |
| 2003 | 6 | 0,270 | 11,5 | 0,22 | 85 % ✔ |
| 2025, I = 0,8, suelo B o D | 2 | 0,333 | 14,2 | 0,56 | vuelca |
| 2025, I = 0,8, suelo B o D | 6 | 0,333 | 14,2 | 0,19 | 94 % ✔ |
| 2025, I = 0,8, suelo C | 6 | 0,350 | 14,9 | 0,20 | 91 % ✔ |
| 2025, I = 1,0, suelo B o D | 6 | 0,417 | 17,7 | 0,24 | 80 % ✔ (justo) |
| 2025, I = 1,0, suelo C | 6 | 0,437 | 18,6 | 0,25 | 76 % ✘ |

Conclusiones:
1. La versión de la norma no cambia el veredicto.
2. Lo que decide es el reparto del corte (diafragma) y la categoría de ocupación.
3. Los pilares cumplen siempre (interacción flexocompresión 0,14–0,51).
4. Caso adoptado (I = 0,8, suelo C, 6 pilares): **91 % ✔**. Con Categoría II y suelo C (no adoptado), haría falta agrandar la zapata a ≈ 1,2 m o conectar las zapatas con vigas de fundación (no calculado).

### Supuestos de la comparación (declarar en la tesis si se usa)
- Fórmula 2003 simplificada del cálculo original (C = 2,7·A₀/R); no se verificó la expresión completa de la norma 2003.
- Período estimado con los pilares como voladizos empotrados: T ≈ 0,21 s (6 pilares) y 0,36 s (2 pilares); la norma pide el período de la estructura real.
- Solo suelos B, C y D; R = 3, ξ = 0,02; no se probó R = 1,5 ni apernado.
- Fuerza horizontal combinada con el peso en servicio sin separar la carga de operación de los estanques (SO).
- Combinación ASD con 0,70·E para la zapata (2025); pilar con E sin factor 1,4 (2025) y 1,4·E (2003, como el original).
- Origen del cálculo: `04_analisis/scripts/10_estructura.py` (variables W_sísmico = 42,6 kN, P_serv = 24,2 kN) más un script auxiliar no guardado en el repositorio.

### Glosario para el texto de la tesis
- **Tipo de suelo (Tabla 4 NCh2369:2025):** clasificación sísmica por Vs30 y período predominante: A roca; B roca blanda o suelo muy denso; C suelo denso o firme; D compacidad o consistencia mediana; E más blando; F sitios singulares. Un suelo más blando amplifica el sismo. Las estructuras de Categoría I están exceptuadas del sondaje de 30 m; las de Categoría II pueden exceptuarse amplificando la demanda en 30 % (verificar texto exacto en el PDF antes de citar).
- **Categoría de ocupación (Tabla 1):** I = 0,8 (menores o provisionales), II = 1,0 (normales), III y IV = 1,2. Con II el sismo es 25 % mayor que con I.
- **Diafragma:** elemento horizontal rígido (tablero + vigas) que hace que la plataforma se mueva de una pieza y reparta el corte entre los pilares.

### Fuentes en el repositorio
- `03_seleccion/fichas_lectura/inn2025nch2369.md` (Tablas 1–7, 4.5 combinaciones, 10.1 fundaciones).
- `02_material_bruto/normas/nch2369-2025_ocr.md` (Tabla 4, líneas ≈ 3908–3990).
- `03_seleccion/notas/2026-11-20_verificacion_dossier-gemini.md` (oficialización 9-03-2026; transición de 18 meses, dato de búsqueda web aún no respaldado por documento).
- `04_analisis/resultados/estructura_verificacion.csv`, `capacidad_soporte_sensibilidad.csv`.

### Acciones para Claude Code (cuando se integre)
- Borrar `inn2003nch2369` de `referencias.bib` si no se cita (la rúbrica penaliza referencias no citadas), o citarla como antecedente.
- Completar `02_marco_teorico.tex` línea ≈ 324–336: reemplazar el `\revisar` por la decisión (usar 2025; 2003 solo como antecedente) y mencionar la transición solo si se verifica con el decreto.
- Guardar el script de comparación en `04_analisis/scripts/` (p. ej. `14_sismo_2003_vs_2025.py`) y recalcular `10_estructura.py` con el espectro 2025.
- Actualizar `04_resultados.tex` (≈ línea 273) y `05_discusion.tex` (≈ líneas 61–62) con los valores de la tabla anterior.

---

## Pregunta 2 — Tablero y límite de deformación — APROBADA por el autor (2026-11-20)

### Qué se verifica
Solo la **deformación del tablero** de 15 mm entre vigas secundarias (luz 0,40 m). Las vigas se verifican aparte y cumplen
(secundaria 0,56 mm frente a 5,67 mm; principal 0,24 mm frente a 7,60 mm, ambas con L/300).
**Restricciones fijas del proyecto (no cambian):** vigas secundarias cada 0,40 m y tablero de 15 mm.

### Respuesta
> El tablero de 15 mm con vigas secundarias cada 0,40 m **cumple L/300 si se modela como continuo sobre al menos tres apoyos**,
> que es su condición real: el estanque de 1,0 m de diámetro cubre unos 2,5 vanos y el tablero es una lámina que cruza varias vigas.
> El cálculo original (`10_estructura.py`, sección 3) lo trataba como un solo vano simplemente apoyado (2,91 mm) y sobreestimaba la deflexión.
> Con el modelo continuo la deflexión es **0,8–1,2 mm frente a 1,33 mm admisibles (L/300)**. No cumple L/500 (0,80 mm), que queda solo como referencia
> (NCh427/1, L.3: L/500 a L/1000 para vigas que soportan equipos), por la horizontalidad de los sifones.

### Carga (se mantiene)
13,5 kN/m² es la presión bajo la base del estanque: (1000 L + 40 kg)·g / (π·0,5²) = 13,0 kPa, más 0,5 kPa de tablero y fijaciones.
No se divide por paño: es presión por m², y la franja de 1 m de ancho recibe esa presión. El cálculo del tablero **no incluye sobrecarga de uso adicional**
(solo un estanque lleno y el peso del tablero). Si se quisiera agregarla, habría que recalcular.

### Resultados (modelo de viga continua, elementos finitos de Euler-Bernoulli, 20 elementos por vano; 15 mm, E = 11 GPa, factor de fluencia 2, franja de 1 m)

| Modelo | Deflexión | ¿L/300 (1,33 mm)? | ¿L/500 (0,80 mm)? |
|---|---|---|---|
| Un vano simplemente apoyado (original) | 2,91 mm | No | No |
| Continuo, 3 apoyos (2 vanos cargados) | 1,21 mm (razón 0,91) | Sí | No |
| Continuo, 3 vanos, carga de 1,0 m | 1,19 mm | Sí | No |
| Continuo, 5 vanos, carga de 1,0 m centrada | 0,86 mm (razón 0,65) | Sí | No (apenas) |
| Continuo, 8 vanos, carga de 1,0 m | 0,82 mm (razón 0,62) | Sí | No (apenas) |

**Valor de diseño propuesto:** 1,21 mm (3 apoyos, el más desfavorable), razón 0,91.

### Supuestos aprobados
- **Material:** se supone **pino radiata**, E = 11 GPa (supuesto del cálculo original). El tablero real es fenólico; confirmar E con la ficha técnica del fabricante antes de construir.
- **Factor de fluencia (k_def) = 2,0.** Justificación para la tesis: el Eurocódigo 5 (EN 1995-1-1, tabla 3.2) da factores de deformación diferida de
  0,6, 0,8 y 2,0 para madera aserrada en las clases de servicio 1, 2 y 3 (Master Series, 2026, resumen de EN 1995-1-1, 2.2.3(3));
  la clase de servicio 3 corresponde a madera expuesta a la intemperie, con humedad media superior a 20 % (Swedish Wood, 2022).
  La plataforma está a la intemperie en Linares, por lo que se adopta k_def = 2,0. El valor se aplica a la deflexión instantánea para obtener la deflexión final.
- **Tablero continuo:** se supone que cada paño es continuo sobre al menos tres apoyos, sin juntas bajo los estanques. Los tableros comerciales
  son láminas de unos 1,22 × 2,44 m (verificar en catálogo); sus bordes deben coincidir con una viga secundaria.
- **Margen estrecho (9 %) con 3 apoyos:** se declara como limitación; depende de E y de k_def.

### Aviso sobre la justificación
- El factor 2,0 sale de una norma europea para **madera aserrada**, no para contrachapado ni para la NCh1198. No encontré en el repositorio ni en la búsqueda
  el factor equivalente de la NCh1198 (norma chilena de cálculo de madera); conviene buscarlo. Para contrachapado, el Eurocódigo 5 da un factor mayor
  en clase de servicio 3 (no verificado en esta sesión).
- Fuentes web usadas (no están en el repositorio): https://help.masterseries.com/knowledge/article/2149 (k_def de 0,6, 0,8 y 2 para madera aserrada en clases de servicio 1, 2 y 3);
  https://www.universityofgalway.ie/media/timberengineeringresearchgroup/Design-of-timber-structures_Volume2_Rules-and-formulas-according-to-Eurocode-5.pdf (definición de clases de servicio).
  Lo ideal es citar la norma EN 1995-1-1:2004 directamente.

### Fuentes en el repositorio
- `04_analisis/scripts/10_estructura.py` (sección 3, tablero; parámetros `E_madera`, `K_def_madera`, `sep_sec`, `t_tablero`).
- `04_analisis/resultados/estructura_verificacion.csv` (fila "Tablero 15 mm").
- `03_seleccion/fichas_lectura/inn2016nch427.md` (L.3: límite L/500 a L/1000 para equipos; no fija L/300).
- `tesis/capitulos/03_metodologia.tex` líneas ≈ 111–116, `05_discusion.tex` línea ≈ 55, `06_conclusiones.tex` línea ≈ 27.

### Acciones para Claude Code
- `10_estructura.py`: reemplazar el modelo de un vano del tablero por viga continua (3 apoyos como valor de diseño; mostrar sensibilidad con 5 y 8 vanos); guardar el script del modelo continuo en `04_analisis/scripts/`.
- `estructura_verificacion.csv` y tabla 4.8: la fila del tablero pasa a 1,21 mm frente a 1,33 mm (razón 0,91, cumple).
- `03_metodologia.tex` (≈ 114–116): reemplazar el `\revisar` de L/300 por la justificación (L/300 como límite de servicio; L/500 como referencia para los sifones, NCh427/1 L.3); describir el modelo continuo y el k_def = 2 con su fuente.
- `05_discusion.tex` (≈ 55) y `06_conclusiones.tex` (≈ 27): quitar la afirmación de que el tablero "debe aumentarse a 21 mm"; dejar la recomendación de tablero continuo sin juntas bajo estanques y de confirmar E con el fabricante.
- Agregar la referencia EN 1995-1-1:2004 al `.bib` (y citar la clase de servicio), o la NCh1198 si se encuentra el factor equivalente.
- Pasar a `DECISIONES.md`: el tablero se modela continuo; vigas cada 0,40 m y tablero de 15 mm son fijos.

---

## Preguntas 3 y 4 — Línea de impulsión del estero y selección de bombas — APROBADAS por el autor (2026-11-20)

(Se responden juntas porque la selección de la bomba depende del desnivel y del criterio de llenado.)

### Criterio de llenado (corrige el supuesto del script original)
El script `11_bombas.py` y el cálculo original suponían **1000 L en 30 min**. El autor aclara que eso es solo lo deseable (para que quien active la bomba vuelva pronto a apagarla).
**Criterio adoptado: llenar 1000 L en un máximo de 60 min (≥ 16,7 L/min); 30 min es un valor deseable, no un requisito.**

### Cotas (se usa UNA cota de llegada para todo el documento)
- **Cota de llegada (estanques de la plataforma): 125,27 m s.n.m., para las tres líneas.** El plano del estero rotula 125,27 m y el de agroquímicos
  rotula 124,27 m en los mismos estanques; el autor decide usar 125,27 m en todo el documento y corregir el plano.
- Estero: captación a 111,45 m s.n.m. → desnivel **13,82 m** (plano 2.1, vista lateral del sistema de impulsión del estero).
- Agroquímicos: tapa de la fosa a ≈ 120,85 m (NT +0,05 sobre el terreno de 120,8 m).
- Aguas servidas: tapa de la fosa a ≈ 118,7 m (fosa séptica Bioplastic de 3250 L).
- **Supuesto:** el nivel del agua en las fosas está ≈ 2 m bajo la tapa (no es una cota del plano). Con la bomba periférica, esa distancia es la altura de succión.
- Desniveles resultantes: estero 13,82 m; agroquímicos 125,27 − (120,85 − 2) = **≈ 6,4 m**; aguas servidas 125,27 − (118,7 − 2) = **≈ 8,6 m**.

### Respuesta
> Se adopta un tiempo de llenado de 1000 L no superior a 60 min, con 30 min como valor deseable. La línea del estero se mantiene en PVC hidráulico de 25 mm
> (plano 2.1 e itemizado 1.2.5), con un desnivel de 13,82 m (111,45 a 125,27 m s.n.m.), y es la más exigente; en agroquímicos y aguas servidas el desnivel total es de ≈ 6,4 y ≈ 8,6 m.
> Se supone una bomba periférica Pedrollo JSWm 1A de 0,75 HP, la misma en las tres líneas, en reemplazo de las sumergibles del cálculo original.
> Llena 1000 L en ≈ 36 min (estero), ≈ 25 min (agroquímicos) y ≤ 17 min (aguas servidas), dentro del límite de 60 min.
> Al ser la misma bomba en todas las líneas, ante una falla se puede intercambiar o priorizar una línea sobre otra; se mantienen repuestos.

### Resultados (Hazen-Williams C = 140, longitudes del itemizado/EETT, pérdidas singulares con ΣK = 7,3: 6 codos, 1 retención, 2 tees)

| Línea | Tubería | Largo | Desnivel | ADT a 33,3 L/min | Caudal de operación (JSWm 1A) | Llenado de 1000 L |
|---|---|---|---|---|---|---|
| Estero | PVC 25 mm (Di 22,0 mm) | 140 m | 13,82 m | 32,1 m | 28,0 L/min (H ≈ 27 m) | **36 min** |
| Agroquímicos | PVC 25 mm | 80 m | ≈ 6,4 m | — | ≈ 40 L/min (H ≈ 22 m) | **≈ 25 min** |
| Aguas servidas | PVC 50 mm (Di 45,2 mm) | 95 m | ≈ 8,6 m | — | ≥ 60 L/min (borde de la curva) | **≤ 17 min** |

Otras bombas de la serie (estero, 25 mm): JSWm 1C 0,5 HP → 20,7 L/min (48 min); JSWm 1B 0,65 HP → 24,7 L/min (40 min). Todas cumplen el límite de 60 min.
Alternativas de diámetro del estero (para 33,3 L/min): 32 mm → ADT 19,2 m; 40 mm → 15,5 m (no se adoptan; el plano indica 25 mm).

### Selección de la bomba (pregunta 4)
- La bomba no está en el itemizado. El autor eligió originalmente una Pedrollo Jet de 0,5 HP; no había stock, y se compró una de **0,75 HP**
  (también se evaluó una Hydrojet de 0,6 HP, tampoco disponible). **Se da por supuesta una Pedrollo JSWm 1A (0,55 kW, 0,75 HP)**; si después se corrige el modelo, se recalcula.
- Datos del fabricante (catálogo Pedrollo JSW1–JSW2, 50 Hz, curvas con aspiración 0 m): JSWm 1C 0,37 kW (0,50 HP), 1B 0,48 kW (0,65 HP), 1A 0,55 kW (0,75 HP);
  altura de aspiración manométrica hasta 9 m. Curva de la 1A (Q en L/min → H en m): 0→48, 5→43, 10→39, 20→31,5, 25→28,5, 30→26, 40→22, 45→20,5, 50→19, 60→17.
  Fuente: https://www.pedrollo.com/public/allegati/JSW1%20-%20JSW2_ES_50Hz.pdf
- El diseño original suponía bombas sumergibles en agroquímicos y aguas servidas; se traspasa a **periféricas** (bomba junto a la fosa, con succión).
- Línea de riego (160 L/h): queda fuera de esta respuesta (otro tipo de bomba).

### Supuestos y avisos
- Modelo y marca de la bomba: supuestos del autor.
- Nivel del agua ≈ 2 m bajo la tapa de las fosas: supuesto.
- Las curvas del catálogo son para aspiración 0 m; la succión de las periféricas se evaluó con la altura estática incluida en el desnivel total. El margen entre el tiempo calculado y el límite (≥ 24 min) cubre la incertidumbre.
- El caudal de aguas servidas queda en el borde de la curva del catálogo (60 L/min); el tiempo real es ≤ 17 min.
- El tiempo de llenado en secuencia de las tres líneas no se informa: las bombas se usan una a la vez (trasladándola) o todas a la vez.

### Fuentes en el repositorio
- `02_material_bruto/planos/EE-ATE250033_2.1_recoleccion-impulsion-vistas-laterales.pdf` (estero: 111,45 y 125,27 m; aguas servidas: tapa a 118,7 m).
- `02_material_bruto/planos/EE-ATE250033_2.4_recoleccion-agroquimicos.pdf` (agroquímicos: 124,27 m en el plano, tapa a ≈ 120,85 m).
- `04_analisis/scripts/11_bombas.py`, `04_analisis/resultados/bombas_adt.csv`, `02_material_bruto/calculos_originales/2026_yo_calculo-partidas-resultados.md`.

### Acciones para Claude Code
- `11_bombas.py`: cambiar a criterio de llenado ≤ 60 min; agregar la curva Pedrollo JSWm 1A (y 1B/1C) al `CATALOGO`; usar desniveles 13,82 / 6,4 / 8,6 m (cota de llegada 125,27 m en todas);
  calcular el punto de operación (intersección de curvas) y el tiempo de llenado por línea; regenerar `bombas_adt.csv` y `tesis/tablas/bombas_adt.tex` (tabla 4.7).
- Unificar en toda la tesis la cota 125,27 m; **corregir el plano 2.4** (124,27 → 125,27 m).
- `04_resultados.tex`: reemplazar el resultado "línea del estero inviable"; `05_discusion.tex` y `06_conclusiones.tex`: quitar la afirmación de que el estero no tiene bomba posible.
- `PREGUNTAS_REUNION.md`: marcar 3 y 4 como resueltas. Registrar en `DECISIONES.md` el criterio de 60 min, la bomba única supuesta y la cota 125,27 m.
- Revisar si los criterios de llenado de 30 min aparecen en otros textos (metodología, anexos).

---

## Pregunta 5 — Caudal del estero y de agroquímicos — APROBADA por el autor (2026-11-20)

### Decisión
El enfoque de la tesis es **sanitario**, por lo que **la carga hidráulica es igual en las tres líneas: 750 L/d por línea (0,75 m³/d en 6 m² = 125 mm/d)**, igual que la línea doméstica.
- **Cada línea es una sola fuente:** doméstica = casa (600 L/d) + oficinas (150 L/d) = 750 L/d; agroquímicos = AGR1 (bodega) + AGR2 (sala de bombas), que se juntan; estero = 750 L/d.
- **Compensación con el estero:** si falta agua en la línea doméstica o en la de agroquímicos, el déficit se completa con agua del estero, de modo que cada humedal reciba siempre 750 L/d.
- Se abandona el criterio de "igual carga orgánica" de la propuesta ANID para estero y agroquímicos (daría 28 421 L/d en el estero, inviable).

### Cargas resultantes con 750 L/d (media medida de DQO)

| Línea | DQO media (mg/L) | Carga orgánica (g DQO/m²·d) |
|---|---|---|
| Estero | 6,3 | 0,8 |
| Agroquímicos, solo AGR2 | 75,7 | 9,5 |
| Agroquímicos, solo AGR1 | 392,7 | 49,1 (sobre los 30 de la fase 1) |
| Agroquímicos, mezcla 50 % AGR1 + 50 % AGR2 | ≈ 234 | ≈ 29 |
| Doméstica (casa + oficinas, diseño del proyecto, con 25 % de remoción en fosa) | 300/400 | 30 |

**Umbral útil:** a 750 L/d, la carga orgánica es ≤ 30 g DQO/m²·d si la DQO media del afluente de la línea es ≤ **240 mg/L** (240 mg/L × 0,75 m³/d / 6 m² = 30).
AGR1 por sí sola (393 mg/L) lo supera; la mezcla con AGR2 o con agua del estero lo baja. Esa es la regla práctica de la compensación con el estero.

### Respuesta
> Las tres líneas operan con la misma carga hidráulica de 750 L/d (125 mm/d en 6 m²), igual que la doméstica. La línea doméstica agrupa casa y oficinas;
> la de agroquímicos, la bodega y la sala de bombas; y la del estero se alimenta del canal. Si una de las dos primeras no aporta el volumen,
> el déficit se completa con agua del estero. Con esta carga, la carga orgánica del estero es 0,8 g DQO/m²·d, y la de agroquímicos se mantiene bajo los 30 g DQO/m²·d de la
> fase 1 siempre que la DQO de la mezcla sea ≤ 240 mg/L.

### Avisos
- Se confirma en 750 L/d (el autor mencionó "150 L/d" en un momento, que se interpreta como un lapsus; 150 L/d es el caudal de las oficinas). **Confirmar con el autor.**
- 125 mm/d supera el máximo de 80 L/m²·d del DWA (Dotro et al., 2021) y entra en el rango de climas cálidos (hasta 200 mm/d), valor que usa el diseño del proyecto; declararlo como carga hidráulica del proyecto.
- Producción real de agua de lavado de agroquímicos: desconocida (Braul et al., 2018: 5000–7000 L/año, ≈ 50–70 L/d en la temporada). Por eso el déficit se completa con el estero. La presentación a la empresa
  menciona transportar IBC de 1 m³ en tractor (¿2 veces por semana?): no es un dato confirmado.
- La concentración de la mezcla agroquímicos + estero depende de las proporciones; la tesis debe indicar la DQO esperada de la mezcla y verificar el umbral de 240 mg/L.
- Carga de amonio en agroquímicos (AGR1 12,8 mg/L, AGR2 2,41 mg/L): con 750 L/d, entre ≈ 0,3 y 1,6 g NH₄⁺/m²·d, bajo los ≈ 3 g/m²·d de la fase 1.

### Fuentes en el repositorio
- `01_normativa/proyecto/texto/2025_anid-ate250033_research-proposal.md` (carga de fases, "mismas características de carga", líneas ≈ 682–694).
- `01_normativa/proyecto/texto/2026_anid-ate250033_diseno-humedal.md` (0,75 m³/d, 6 m², 125 mm/d, 30 g DQO/m²·d).
- `01_normativa/proyecto/texto/2026_anid-ate250033_explicacion-diseno-empresa.md` (capacidad 500–1000 L/d, IBC en tractor).
- `04_analisis/resultados/caudal_equivalente_carga.csv`, `caracterizacion_resumen.csv`.

### Acciones para Claude Code
- `04_resultados.tex` (≈ líneas 117–133 tabla 4.3 y ≈ 217–220): caudales de diseño de las tres líneas = 750 L/d; eliminar el `\revisar` de la distribución de caudales; agregar la compensación con el estero y el umbral de 240 mg/L; ajustar la nota de pie c.
- `03_metodologia.tex`: describir el criterio (igual carga hidráulica, fuentes agrupadas, compensación con el estero).
- Actualizar el cálculo de cargas y `caudal_equivalente_carga.csv` con el nuevo criterio (cargas orgánicas de la tabla anterior).
- Revisar que los criterios de bombas e impulsión (preguntas 3 y 4) sigan consistentes con 750 L/d por línea (tiempos de llenado de 1000 L).
- `PREGUNTAS_REUNION.md` y `DECISIONES.md`: registrar la decisión.

---

## Pregunta 9 — Hormigón de zapatas — APROBADA por el autor (2026-11-20)

### Respuesta
> **Hormigón G25** en las zapatas, como indica la lámina del sector 2 (detalle estructural 3.2) y como se usó en el cálculo (`fc = 25 MPa`).
> Las EETT y el itemizado, que dicen G30, se corrigen a G25.

### Notas
- El autor verificó que la lámina dice G25. Las EETT (sección de fundaciones: "calidad G30 (f′c ≥ 30 MPa)") y el itemizado 2.1.2 ("Hormigón armado en zapatas (G30)", 5 m³) deben corregirse.
- Ningún resultado de `10_estructura.py` depende de `fc`: el parámetro se define pero no interviene en las verificaciones.
- **Verificar:** en Chile el grado G de la NCh170 se asocia a resistencia cúbica; no asumir que G25 equivale a f′c = 25 MPa de probeta cilíndrica. Al corregir las EETT, escribir el grado G25 sin la equivalencia "f′c ≥ …" salvo que se confirme con la norma.

### Acciones para Claude Code
- `04_resultados.tex` (≈ línea 278): cambiar G30 a G25 y borrar el `\revisar`.
- `tesis/anexos/anexo_planimetria_estructural.tex` (≈ línea 21), `anexo_eett.tex` (≈ línea 11), `anexos/generados/eett_cuerpo.tex` (≈ línea 64) y `tablas/itemizado.tex` / `04_analisis/datos/itemizado_rev1.csv` (2.1.2): unificar a G25 y quitar los avisos de inconsistencia.
- Revisar la definición del grado en la NCh170 antes de citarla.

---

## Pregunta 10 — Capas filtrantes — APROBADA por el autor (2026-11-20)

### Respuesta
> Se adopta la lámina 2.2 (el autor la verificó en el plano): **grava de 19 mm, 0,15 m (inferior, drenaje); arena gruesa, 0,60 m (intermedia, filtración); gravilla de 12 mm, 0,15 m (superior, distribución)**, en 18 contenedores IBC de 1 m².
> Se corrigen las EETT (tamaños y orden invertidos) y las cantidades del itemizado.

### Volúmenes (18 IBC × 1,0 m² de superficie)
| Capa | Espesor | Volumen |
|---|---|---|
| Grava 19 mm (drenaje, inferior) | 0,15 m | 2,7 m³ |
| Arena gruesa (filtración) | 0,60 m | 10,8 m³ |
| Gravilla 12 mm (distribución, superior) | 0,15 m | 2,7 m³ |
| Total | 0,90 m | 16,2 m³ |

### Discrepancias a corregir
- **EETT** ("Estratos filtrantes"): dice grava de 12 mm abajo, arena como "transición" y gravilla de 19 mm arriba; corregir a grava 19 mm / arena gruesa / gravilla 12 mm.
- **Itemizado** (2.3.5 a 2.3.7): grava 19 mm 3 m³, gravilla 12 mm 18 m³, arena gruesa 3 m³. Los volúmenes parecen intercambiados: arena ≈ 10,8 m³ (con merma, ≈ 12 m³), gravas ≈ 2,7 m³ (≈ 3 m³ cada una). Los 18 m³ no calzan con ningún cálculo: **confirmar con quien armó el itemizado**.
- Plantas: 72 (4 por IBC).

### Diferencia con la literatura (declarar en la tesis)
Dotro et al. (2021) recomienda una capa de transición de ≈ 10 cm (grava de 4 a 8 mm) y limita la grava superior a 5–10 cm porque reduce la difusión de oxígeno. El diseño usa 15 cm de gravilla arriba y no tiene capa de transición.

### Fuentes en el repositorio
- Lámina 2.2 (`02_material_bruto/planos/EE-ATE250033_2.2_humedales-vista-lateral.pdf`); itemizado `04_analisis/datos/itemizado_rev1.csv`; `tesis/anexos/generados/eett_cuerpo.tex`; ficha de Dotro et al. (2021) en `03_seleccion/fichas_lectura/`.

### Acciones para Claude Code
- `02_marco_teorico.tex` (≈ línea 129): reemplazar el `\revisar` de capas por la decisión y la diferencia con Dotro et al.
- `anexo_eett.tex` / `eett_cuerpo.tex`: corregir estratos filtrantes; `anexo_itemizado.tex` y `tablas/itemizado.tex`: corregir cantidades (arena 10,8 m³; gravas 2,7 m³).
- `03_metodologia.tex` (≈ línea 208): mantener la secuencia y agregar los espesores y los volúmenes.

---

## Pregunta 11 — Zanja de la casa — APROBADA por el autor (2026-11-20)

### Decisión
Los trayectos de las zanjas **se modificaron en terreno** durante la ejecución del proyecto; los datos de cotas, tapada y diámetro del cálculo original (zanja 3: tapada mínima 0,11 m frente a 0,50 m exigidos) ya no representan lo construido.
**Por eso la tesis no presenta resultados de excavación** (volúmenes, tapadas, perfiles) y declara la razón. Si el profesor pide el detalle, el autor busca los datos de terreno y se incorporan.

### Redacción propuesta (sin datos de excavación)
> El movimiento de tierras y el trazado de las zanjas se definieron en terreno durante la ejecución del proyecto, ajustando los trayectos de las redes a las condiciones del sitio (obstáculos, cotas y accesos). Por esta razón, esta tesis no incluye el cálculo de excavaciones y se limita a especificar los criterios de diseño de las zanjas: tapada mínima de 0,50 m sobre el tubo [según el criterio de las EETT], tuberías de PVC sanitario de 110 mm en las conexiones de aguas servidas con pendiente mínima de 2,0 % y relleno compactado por capas. Las dimensiones finales corresponden a lo construido.

(Los valores entre corchetes y los criterios de pendiente deben ajustarse a lo que digan las EETT y los planos 2.1; **no introducir cifras que no estén en esos documentos.** Las pendientes de 2,0 % y 2,5 % y el PVC sanitario de 110 mm aparecen en la vista lateral de aguas servidas del plano 2.1; la tapada de 0,50 m es la exigida en el cálculo original y debe confirmarse en las EETT.)

### Avisos
- El entregable inscrito "diseño de zanjas (movimiento de tierras y geometría)" queda cubierto solo con criterios; el profesor puede pedir los datos. Dejar la sección redactada de manera que se pueda reemplazar sin reescribir el capítulo.
- No se deben usar las tablas del script `12_excavacion.py` (cotas originales: zanja 3 con tapada 0,11–0,17 m) como resultados de la tesis.

### Acciones para Claude Code
- Quitar de Resultados la tabla de excavación y cualquier referencia a la tapada insuficiente de la zanja 3; reemplazar por la redacción anterior en la metodología (diseño de zanjas) y en el alcance/limitaciones.
- Mantener `12_excavacion.py` y sus CSV fuera de la tesis (archivarlos como "no usado") para poder reincorporarlos si se piden.
- Marcar en `DECISIONES.md`: "Zanjas: trayectos modificados in situ; sin resultados de excavación; datos disponibles bajo pedido".
- Actualizar `ALCANCE.md` (entregable "zanjas") y las conclusiones/limitaciones.

---

## Pregunta 15 — ¿Redes para la Fase 2 (60 g DQO/m²·d)? — APROBADA por el autor (2026-11-20)

### Respuesta
> El diseño se dimensiona para la **Fase 1** (30 g DQO/m²·d, ≈ 3 g NH₄⁺/m²·d; 6 IBC de 1 m² por línea, 6 m²). Si el proyecto requiriera operar en la **Fase 2** (60 g DQO/m²·d, ≈ 6 g NH₄⁺/m²·d),
> se duplicaría la carga de dos maneras equivalentes: (a) **reducir el área en operación a 3 IBC (3 m²) por línea**, manteniendo 750 L/d; o (b) **duplicar la carga hidráulica a 1500 L/d** en los 6 m².

### Notas
- El autor dijo "3 metros cúbicos, que serían 3 IBC": se interpreta como **3 m² de superficie = 3 IBC** (cada IBC tiene 1 m² de superficie y 1 m³ de volumen).
- La opción (a) es la preferida: no cambia caudales, bombas ni tuberías de alimentación; se logra cerrando las válvulas de salida de 3 IBC por línea (el itemizado incluye 18 válvulas de cierre de 50 mm en la salida de los IBC, ítem 2.4.6).
- La opción (b) lleva la carga hidráulica a 250 mm/d, sobre el máximo de 200 mm/d que cita Dotro et al. (2021) para climas cálidos; implica llenar el estanque de 1000 L 1,5 veces al día y más pulsos por sifón. Declararla como alternativa menos recomendable.
- Con la bomba supuesta (JSWm 1A) el llenado de 1000 L tarda entre 17 y 36 min (preguntas 3 y 4), por lo que 1,5 llenados al día no son un problema para las bombas.
- Para la Fase 2 la carga de amonio sería ≈ 6 g NH₄⁺/m²·d; no se dimensiona en esta tesis.

### Acciones para Claude Code
- Agregar un párrafo en `03_metodologia.tex` (diseño depurativo) o en las limitaciones con la respuesta anterior; en el resumen de parámetros por línea, mostrar la Fase 1 como diseño y la Fase 2 como operación alternativa.
- No recalcular redes ni bombas para la Fase 2.

---

## Pregunta 16 — Orden de preliminares y capítulo de Discusión — APROBADA por el autor (2026-11-20, corregida dos veces)

### Decisión
- **Preliminares: se mantiene el orden actual de la tesis: Agradecimientos → Resumen → Abstract → índices → glosario.** Es el orden de los Lineamientos §6 (documento normativo, que el autor
  conserva como su directriz). La tesis de Bocaz (2026) usó el orden del template (Agradecimientos después del Abstract) porque se presentó con otra directriz.
  El autor está "casi seguro" de que sus reglas piden Agradecimientos primero; **hay que confirmarlo con el profesor** y se cambia si él lo indica.
- **Capítulos: se mantiene la estructura actual**, con **Discusión como capítulo aparte**:
  1 Introducción y Planteamiento del Problema; 2 Marco Teórico; 3 Metodología; 4 Presentación de Resultados; 5 Discusión y Análisis de Resultados; 6 Conclusiones.
  La rúbrica da puntaje separado a "Presentación de resultados" (15 %, cap. 4) y a "Discusión / Análisis de resultados" (15 %, cap. 5). No se fusionan.

### Respuesta
> Los preliminares siguen el orden de los Lineamientos (Agradecimientos, Resumen y Abstract) y el cuerpo mantiene un capítulo de Discusión y Análisis de Resultados separado
> de la Presentación de Resultados, como exigen el template y la rúbrica. Si el profesor guía indica otro orden, se ajusta.

### Del modelo de Bocaz se siguen aplicando (sin tocar el orden ni los capítulos)
Resumen de 4 párrafos; sección "Criterios, supuestos y parámetros de diseño" y diagrama de flujo del diseño (cap. 3); tabla resumen de parámetros por línea (cap. 4);
conclusiones que abren con el cumplimiento del objetivo general, con cifras, más recomendaciones y líneas de investigación futura (cap. 6).

### Acciones para Claude Code
- **No cambiar nada** en el orden de los preliminares ni en los capítulos 1–6. Dejar la discrepancia Lineamientos/template anotada en `REGLAS_FORMATO.md` §3 y en `DECISIONES.md`
  ("se mantiene el orden de los Lineamientos; pendiente confirmar con el profesor").

---

## Pregunta 18 — Nitrato y plantas del humedal — APROBADA por el autor (2026-11-20)

### Decisión
No hay una fuente que respalde que el nitrato sea la forma de nitrógeno **más usada** por las plantas del humedal; **se suaviza la redacción** para no afirmarlo.

### Redacción propuesta
> En un humedal vertical, el amonio se nitrifica y se genera nitrato, que queda disponible para las plantas y los microorganismos del lecho; las macrófitas asimilan nitrógeno, tanto en forma de amonio como de nitrato, en un orden de 0,2 a 0,8 g N/m²·d (Dotro et al., 2021).

(Basta con atribuir a Dotro et al. (2021) el intervalo de asimilación por las plantas, sin afirmar la preferencia por una forma de nitrógeno.)

### Aviso
- La afirmación sobre la preferencia de las plantas por el nitrato **no se cita**; si el profesor la quiere mantener, tendrá que dar la fuente (esa es la pregunta 18 original).

### Acciones para Claude Code
- Buscar en `02_marco_teorico.tex` (sección "por qué humedal vertical") la frase que dice que el nitrato es la forma de nitrógeno que más usan las plantas y reemplazarla por la redacción anterior; quitar el `\revisar` o el `\pendiente` correspondiente.
- Verificar que el intervalo de 0,2 a 0,8 g N/m²·d coincida con la ficha de Dotro et al. (2021).

---

## Pregunta 6 — Fichas y aforos de oficinas, tiempos de retención — APROBADA por el autor (2026-11-20, con supuestos)

### A. Aforo de los artefactos
- **Lavaplatos y lavamanos:** método volumétrico; se llenó un recipiente de **0,92 L** y se midió el tiempo con cronómetro, con la llave en tres aperturas (alta, media, baja). Se usó el caudal medio.
  - Lavaplatos: 6,19 / 9,07 / 22,48 s → 8,9 / 6,1 / 2,5 L/min (se usa 6,1).
  - Lavamanos: 5,51 / 7,55 / 24,86 s → 10,0 / 7,3 / 2,2 L/min (se usa 7,3).
  - El PDF muestra una sola medición por apertura; no consta que haya repeticiones.
- **WC:** volumen por descarga de **9,1 L, tomado del manual del fabricante** (no medido).
- **Tiempos de uso por ocasión:** 0,5 min (lavamanos) y 1,5 min (lavaplatos), estimados por el equipo (el PDF no documenta cómo se definieron). El documento del proyecto y el correo del profesor usan además 1 min para el WC.
  El profesor redondeó los caudales a 9, 6 y 6 L/min en su tabla.
- **Fichas:** cada persona anotó por día cuántas veces usó cada artefacto; el equipo multiplicó usos × caudal × tiempo. No se describe en detalle quién respondió ni cuántas personas son.

### B. Semanas del registro y columna "02S1" repetida
Fuente: PDF "Consumo de agua – Casa y oficinas SABA". Las semanas son **01S4, 02S1, 02S2, 02S3 y 02S4** (cuarta semana de enero y las cuatro de febrero de 2026).
En el documento del proyecto las columnas aparecen como 01S3, 01S4, 02S1, 02S1 y 02S3: la "02S1" repetida corresponde a **02S2** y el resto está desplazado. El registro llega hasta 02S4 (con el viernes incompleto), no hasta la tercera semana de febrero.
- **Escenario 1** (personal completo): promedio de 01S4 y 02S1. **Escenario 2:** febrero (por vacaciones y postnatal).

### C. Corrección del resumen del PDF (error de cálculo)
En las tablas de resumen del PDF el "volumen diario" de lavamanos y lavaplatos es en realidad **semanal** (promedio de usos semanales × caudal × tiempo, ya sin dividir por 5); solo el WC está bien. Corregido (÷ 5 días hábiles):

| Escenario | PDF | Corregido |
|---|---|---|
| 01S4 + 02S1 | 476,7 L/d (9534 L/mes) | **158,7 L/d** (≈ 3174 L/mes) |
| Febrero completo | 347,6 L/d (6952 L/mes) | **108,8 L/d** (≈ 2177 L/mes) |

Esto es consistente con la tabla del profesor (165 y 96 L/d) y con el caudal adoptado de **150 L/d** (restitución 0,9, valor confirmado por el director, correo del 23-10-2026). **Si las tablas del PDF van a un anexo, corregirlas.**

### D. Casa
El medidor de agua potable da 743,6 L/d en 13 meses; con restitución **0,85** da 632 L/d, y el proyecto adoptó **600 L/d** (con 0,7 m³/d redondeado). Se usa 0,85 (documento de cálculo del proyecto), no el 0,8 de la v3.0.

### E. Tiempos de retención (entregable de la inscripción VF-V2)
La inscripción compromete "tiempos de retención" en la memoria de cálculo hidráulico, sin decir de qué unidad. **Se refieren al humedal**; para ser completos se calcula el tiempo de permanencia del agua en cada unidad de la cadena de tratamiento.

**Cadena de cada línea (una por fuente):** fuente → estanque de almacenamiento 1000 L (×3) → estanque dosificador de 200 L con sifón (×3) → humedal (6 IBC, 6 m²) → cámara de cloración de 100 L (×3) → fosa de acopio final de 3250 L (×3) → riego.
(Itemizado 2.2.1, 2.2.2, 2.3.4, 2.4.1 y 2.4.3; el autor recordaba un acopio de 2000 a 3000 L, pero el itemizado y las EETT dicen **3250 L**.)

**Pulsos (supuesto):** el diseño del proyecto usa 6 cargas por día (balance de oxígeno con 6 m² y 6 cargas): 750 L/d / 6 = **125 L por pulso** (21 mm sobre 6 m²; un pulso cada 4 h). El estanque dosificador de 200 L tiene capacidad sobre ese volumen.
El autor recordaba pulsos de 165 a 250 L; no hay ese dato en el repositorio. Si el profesor indica otro volumen, se recalcula.

| Unidad | Volumen | Caudal | Tiempo de retención nominal |
|---|---|---|---|
| Estanque de almacenamiento | 1000 L | 750 L/d | ≈ 1,3 d |
| Dosificador (entre pulsos) | 125 L por pulso | 6 pulsos/d | 4 h entre pulsos |
| Lecho del humedal (τ = ε·h·A/Q; 0,60 m de arena, ε ≈ 0,35–0,40, supuesto) | ≈ 1,3–1,4 m³ | 0,75 m³/d | ≈ 1,7–1,9 d (referencial) |
| Cámara de cloración | 100 L | 750 L/d | ≈ 3,2 h |
| Fosa de acopio final | 3250 L | 750 L/d | ≈ 4,3 d |

- El tiempo del lecho es **solo referencial**: en un humedal vertical no saturado, Dotro et al. (2021) advierten que los conceptos de lechos saturados no se aplican directamente; la porosidad es un supuesto (falta fuente).
- La fosa de acopio queda más corta en operación, porque de ahí se riega: ≈ 1280 L por evento de riego cada 2 días (10 plantas × 128 L; = 640 L/d, columna "Demanda" de la tabla 4.x), por sector. Esto resuelve el aviso de la tabla de riego: la "Demanda" es el volumen por evento dividido por 2 días, y la columna "Volumen total (L por semana)" es en realidad por evento. **Confirmar con el autor** que el riego es cada 2 días y por sector de 10 plantas.

### Respuesta
> El caudal de las oficinas se estimó con fichas diarias de uso de los artefactos entre la cuarta semana de enero y la cuarta de febrero de 2026; el caudal de cada artefacto se aforó por el método volumétrico (recipiente de 0,92 L y cronómetro, apertura alta, media y baja; se usó la media) y el del WC se tomó del manual del fabricante (9,1 L por descarga). Los tiempos de uso son estimados del equipo. Con los escenarios de 165 L/d (personal completo) y 96 L/d (vacaciones) y un factor de restitución de 0,9, se adoptó 150 L/d, confirmado por el director del proyecto.
> Los tiempos de retención se calcularon por unidad de la cadena de tratamiento (almacenamiento, humedal, cloración y acopio final); el del lecho es referencial por tratarse de un humedal vertical no saturado.

### Avisos
- Pulsos de 125 L (6 por día): supuesto; confirmar con el profesor.
- Porosidad del lecho: supuesto sin fuente.
- El riego cada 2 días por sector: interpretación; confirmar.
- Volumen de acopio final: 3250 L (itemizado/EETT); los planos pueden decir otro valor, verificar la lámina 2.2/2.3.

### Acciones para Claude Code
- `03_metodologia.tex` (≈ líneas 57–59, 74–81): reemplazar los `\pendiente`/`\revisar` de aforo y de tiempos de retención por el texto de A y E; describir la cadena de unidades y el supuesto de 6 pulsos de 125 L.
- `04_resultados.tex`: agregar la tabla de tiempos de retención (E); corregir las tablas de caudales de oficina con los valores corregidos (C), y corregir la tabla de riego (encabezados: volumen por evento; demanda = evento / 2 días).
- `anexos` (Anexo I): corregir las tablas de resumen del PDF (diarios = semanales ÷ 5) y rotular bien las semanas (01S4, 02S1 a 02S4).
- Verificar el volumen de la fosa de acopio (3250 L) en las láminas 2.2/2.3 y el volumen del estanque dosificador (200 L).

---

## Pregunta 7 — Datos de caracterización: fuente, exclusión y tipo de muestra — APROBADA por el autor (2026-11-20)

### Decisión
1. **Manda el informe del laboratorio.** Los seis informes del Laboratorio del Agua (Facultad de Ciencias de la Ingeniería, UCM, Talca; analista Erica Alarcon Bustcovich; fechas de recepción = fechas de muestreo) son la fuente primaria. La base de datos y el resumen se corrigen contra ellos (comparación celda a celda de los 462 valores).
2. **Tipo de muestra (dato del autor):** muestras **puntuales**, tomadas por el equipo en cada punto y entregadas al laboratorio sin compositar (el laboratorio informó cada punto por separado).
   - **AS1 = oficinas:** salida de la oficina. **AS2 = casa:** salida de la casa, al llegar al estanque (aguas abajo de la salida).
   - **AS2 solo tiene las semanas 1 y 2:** desde la semana 3 las muestras de la casa no llegaron al laboratorio (dato del autor). Las medias de AS2 tienen n = 2 y no son representativas.
3. **Semana atípica (dato del autor):** una semana no se consideró en el cálculo porque las muestras se tomaron mal. Es la **semana 1**: AS1 con SST 2370 mg/L, turbiedad 1330 NTU y DQO total 2478 mg/L, valores muy distintos del resto de las semanas (SST 53–114 mg/L, turbiedad 48–135 NTU, DQO 266–560 mg/L); AS2 muestra el mismo patrón (SST 3303 mg/L, turbiedad 1855 NTU).
   - La DQO total de AS1 de la semana 1 **sí la reportó el laboratorio** (no es error de digitación); se reincorpora a la base como valor medido, marcada como **atípica por mal muestreo**.
   - Criterio: la semana 1 se excluye de las **medias de diseño**, pero se reportan ambas medias (con y sin ella).
   - **Inconsistencia a corregir:** el resumen actual solo excluyó la DQO total de AS1 de la semana 1; SST, turbiedad, DBO₅ y DQO disuelta de esa semana siguen dentro de las medias. Aplicar el criterio a toda la semana 1 (o decir expresamente cuáles parámetros se excluyen). **Verificar con el autor** qué parámetros dejó fuera cuando hizo el resumen.

| AS1 (oficinas) | Media con semana 1 | Media sin semana 1 |
|---|---|---|
| SST (mg/L) | 463 | 82 |
| Turbiedad (NTU) | 304 | 99 |
| DQO total (mg/L) | 756 | 411 |
| DBO₅ (mg/L) | 270 | 219 |

Los valores de **diseño** no cambian: DQO 300 (casa) y 400 mg/L (oficinas).

### Correcciones a la base de datos (contra el laboratorio)
| Celda | Base de datos | Laboratorio |
|---|---|---|
| ORP AGR1, semana 3 | 4,12 (es el OD) | 114,2 mV |
| SST AGR2, semana 3 | 11,40 | 35,1 mg/L |
| Coliformes AGR2, semana 3 | 5,0 × 10³ | 5,0 × 10⁴ NMP/100 mL |
| ORP AS2, semana 2 | 89 (redondeo) | 88,6 mV |

### Correcciones al resumen (contra el laboratorio)
| Celda | Resumen | Laboratorio |
|---|---|---|
| Nitrato estero, semana 6 | 7,3 | 6,4 mg/L (la media del estero baja de 4,98 a 4,83 mg/L) |
| Nitrógeno total estero, semana 6 | 0,9 | 1,0 mg/L |
| Fósforo total estero | 0,16 | 0,17 mg/L |
| Fósforo total AS1, semana 6 | 0,12 | 0,13 mg/L |
| SST AGR1, semana 3 | 35,4 (redondeo) | 35,43 mg/L |
| DQO total AS1, semana 1 | omitida | 2478 mg/L (atípica) |

### Otras declaraciones que exigen los informes
- **Coliformes: son totales, no fecales.** Los informes dicen "coliformes total". Corregir el nombre en la base, el resumen, las tablas y el texto (E. coli se informa por separado).
- **DBO₅ de la semana 4:** una nota del laboratorio indica que se midió a los **4,7 días**, no a los 5.
- **Informe de la semana 3:** el archivo corresponde a una **repetición** del análisis.
- **Informe del 24-03-2026:** el laboratorio lo rotuló "5º monitoreo", pero es el sexto.
- **Nitrógeno total:** no se midió en la semana 1 en ningún punto.
- **Métodos analíticos:** los informes **no los indican** (tampoco el tipo de muestra). En la tesis se declara "método no informado por el laboratorio"; solicitar la ficha de métodos al laboratorio. No se inventan métodos.
- **DBO₅ de la casa (AS2) = 15,0 y 10,8 mg/L** frente a una DQO total de 546 y 129 mg/L: relación DBO₅/DQO ≈ 0,04 (AS1 ≈ 0,66). Es anormalmente baja; tratarla como poco confiable y no usarla para diseño.

### Respuesta
> Las muestras fueron puntuales y se analizaron en el Laboratorio del Agua de la Facultad de Ciencias de la Ingeniería de la Universidad Católica del Maule; los informes del laboratorio son la fuente de los datos. AS1 se tomó en la salida de las oficinas y AS2 en la salida de la casa, a la llegada al estanque; de AS2 solo se dispone de las dos primeras campañas, porque las muestras posteriores no llegaron al laboratorio. La primera campaña de AS1 y AS2 se consideró atípica por errores de muestreo (SST, turbiedad y DQO muy superiores al resto) y se excluyó de las medias, que se presentan con y sin ella. Los coliformes informados son totales.

### Avisos
- AS2 con n = 2 (semanas 1 y 2): sin la semana 1, queda un solo dato (semana 2: DQO 129 mg/L, NH₄⁺ 1,82 mg/L, SST 406 mg/L). Por eso el diseño usa los valores de diseño y no la media medida.
- Los parámetros que el resumen dejó dentro de la semana 1 de AS1 deben confirmarse con el autor (ver arriba).
- No se conoce el método analítico ni la conservación de las muestras (tiempo entre toma y análisis).

### Fuentes en el repositorio
- `04_analisis/datos/caracterizacion_afluentes.csv`, `bd_macroparametros.csv`; `04_analisis/resultados/caracterizacion_resumen.csv`, `qa_bd_vs_resumen.csv`.
- Informes del laboratorio (seis .docx de enero a marzo de 2026, entregados por el autor; **no están en el repositorio**).
- `tesis/capitulos/03_metodologia.tex` (líneas ≈ 38, 45), `04_resultados.tex` (≈ 35–43), `tesis/tablas/caracterizacion_afluentes.tex`.

### Acciones para Claude Code
- Agregar los seis informes del laboratorio al repositorio (`02_material_bruto/` o `03_seleccion/`) y citarlos como fuente primaria.
- Corregir `caracterizacion_afluentes.csv` y `bd_macroparametros.csv` con las 4 correcciones de la base; reincorporar DQO total de AS1, semana 1 (2478 mg/L) con un indicador de "atípica"; cambiar "Coliformes fecales" por "Coliformes totales" en datos, scripts, `caracterizacion_resumen.csv`, `tesis/tablas/caracterizacion_afluentes.tex` y capítulos 2, 4 y 5.
- Recalcular `caracterizacion_resumen.csv` con las 5 correcciones del resumen y con medias con y sin la semana 1 (AS1 y AS2); actualizar `qa_bd_vs_resumen.csv` (0 diferencias).
- `03_metodologia.tex` (≈ líneas 38 y 45): reemplazar los `\pendiente` por el tipo de muestra (puntual), los puntos de toma, el laboratorio, "métodos no informados por el laboratorio" y el criterio de exclusión de la semana 1.
- `04_resultados.tex` y tabla de caracterización: notas al pie (DBO₅ de la semana 4 a los 4,7 días; semana 3 por repetición; nitrógeno total no medido en la semana 1; AS2 con n = 2; DBO₅ de AS2 poco confiable).
- Registrar en `DECISIONES.md` y marcar la pregunta 7 como resuelta; dejar como pendiente para el laboratorio: métodos y conservación.

---

## Pregunta 8 — Nitrógeno bajo y base de diseño — PROPUESTA (pendiente de visto bueno del autor)

### Hallazgos
- **Nitrato:** el informe del laboratorio lo rotula **NO₃⁻** (no N-NO₃⁻). El nitrato medio de AS1 (9,3 mg/L) y AS2 (5,9 mg/L) equivale a ≈ 2,1 y 1,3 mg N/L (÷ 4,43).
- **El nitrógeno total medido es poco confiable:** el informe no indica su base (se supone N). Al convertir (amonio × 0,776 y nitrato ÷ 4,43, ambos a N), el nitrógeno inorgánico supera al nitrógeno total en **4 de 5 semanas de AS1** (semanas 2, 3, 5 y 6; la 4 queda igual), y también en el estero y en AGR2. Eso es imposible físicamente; apunta a un problema de método o de límite de detección del laboratorio, no a una característica del agua.
- **Causa del nitrógeno bajo:** no se conoce una causa. El autor describe muestras puntuales tomadas en la salida de oficinas y de la casa; la dilución (agua de lavado de manos, cocina y WC de baja carga) y las muestras mal tomadas son hipótesis, no un hecho.

### Decisión propuesta
1. **Base de diseño:** valores de diseño del proyecto (DQO 300 casa / 400 oficinas; NH₄⁺ 1,5 / 1,0 mg/L), no las medias medidas. Las medias medidas son **validación** (n = 2 en AS2).
2. **Nitrógeno total:** declararlo como **limitación** de la caracterización (valor no consistente con amonio + nitrato) y no usarlo para el diseño.
3. **Meta de ≈ 3 g NH₄⁺/m²·d de la fase 1:** se mantiene como meta de **diseño**, pero con estas aguas **no se alcanza**: con 750 L/d (125 mm/d) la carga de amonio es muy baja (tabla siguiente). Declarar que la nitrificación se evaluará a carga baja o con dosificación de amonio (a discutir con el profesor).

### Cargas en la línea doméstica (750 L/d en 6 m² = 125 mm/d; casa 600 L/d + oficinas 150 L/d)
| Base | DQO de la mezcla (mg/L) | Carga orgánica (g DQO/m²·d), con 25 % de remoción en fosa | NH₄⁺ de la mezcla (mg/L) | Carga de amonio (g NH₄⁺/m²·d) |
|---|---|---|---|---|
| Diseño (300/400; 1,5/1,0) | 320 | **30,0** | 1,4 | 0,18 |
| Medias medidas (338/411; 1,98/1,28) | 352 | **33,0** | 1,84 | 0,23 |
| Medidas sin semana 1 (AS2 = 129; AS1 = 411) | 185 | 17,4 | — | — |

- La carga orgánica medida (33 g/m²·d) queda cerca de la de diseño (30); la de diseño es razonable y algo conservadora frente al rango 17–33.
- Para llegar a 3 g NH₄⁺/m²·d con 125 mm/d, el afluente necesitaría ≈ 24 mg NH₄⁺/L, unas 13 veces el medido.

### Respuesta
> El nitrato se informó como NO₃⁻. El nitrógeno total medido es inconsistente con el amonio y el nitrato (el nitrógeno inorgánico lo supera en la mayoría de las campañas), por lo que se declara como limitación y no se usa para el diseño. El diseño se basa en los valores del proyecto (DQO 300 y 400 mg/L; NH₄⁺ 1,5 y 1,0 mg/L), y las medias medidas se usan como validación: con ellas, la carga orgánica de la línea doméstica es de ≈ 33 g DQO/m²·d, similar a los 30 g DQO/m²·d de diseño, mientras que la carga de amonio (≈ 0,2 g NH₄⁺/m²·d) es muy inferior a la meta de ≈ 3 g/m²·d.

### Avisos
- Se supone que el nitrógeno total del laboratorio está en mg N/L y el amonio, en mg NH₄⁺/L; los informes no lo indican. Confirmar con el laboratorio.
- La causa del nitrógeno bajo es desconocida; no afirmarla en la tesis.
- La carga de amonio muy por debajo de 3 g/m²·d cambia lo que se puede concluir sobre nitrificación: consultar al profesor si se doseará amonio en la fase 1.
- Coherente con la pregunta 18 (nitrato y plantas).

### Acciones para Claude Code
- `04_resultados.tex` (≈ líneas 35–43) y `05_discusion.tex`: agregar la tabla de cargas, la limitación del nitrógeno total y la comparación diseño/medido; reemplazar el `\revisar` correspondiente.
- `caracterizacion_afluentes.csv`/resumen: rotular el nitrato como NO₃⁻ y agregar una columna de conversión a N si se usa.
- `04_analisis/resultados/caudal_equivalente_carga.csv`: agregar las cargas de amonio y la comparación diseño/medido.
- Marcar la pregunta 8 como "propuesta del autor" hasta su aprobación.

---

## Pregunta 12 — Estructura auxiliar de los dosificadores — PROPUESTA (supuesto; pendiente de visto bueno del autor)

### Hallazgos en el repositorio
- La lámina 3.2 muestra **3 bastidores** (uno por dosificador) de 0,95 m de ancho, con **4 vigas** a 0,24 / 0,20 / 0,20 / 0,24 m, rotulados "Perfil de 15 × 15 × 6 mm". Ese perfil no es posible: un cajón de 15 × 15 mm con 6 mm de espesor no tiene hueco.
- El itemizado (2.1.9) pide "Perfil cajón 15x15x6 mm", **100 ml**, cantidad incoherente con lo que se ve en la lámina (≈ 11 m de perfil en vigas).
- El autor no recuerda el perfil comprado; **se adopta un supuesto** que el profesor puede corregir.

### Supuesto y verificación
Perfil cajón de acero **40 × 40 × 2 mm** (I = 73 365 mm⁴; W = 3668 mm³), en vigas biapoyadas de 0,95 m.
- **Carga:** estanque dosificador de 200 L lleno (200 kg) + 15 kg de tanque vacío supuesto = 215 kg ≈ 2,1 kN.
- **Resistencia (ASD, 0,6 Fy con Fy = 250 MPa):** el momento por viga con 4, 3 o 2 vigas cargadas es 0,13 / 0,17 / 0,25 kN·m, frente a una capacidad de 0,55 kN·m (razón de 0,23 / 0,30 / 0,46).
- **Deformación (centro de la viga):** 0,64 / 0,86 / 1,28 mm (L/1480, L/1110, L/740), que cumple L/500–L/1000 de la NCh427/1 para vigas que soportan equipos y deja los sifones horizontales.
- **Comparación:** un cajón de 30 × 30 × 2 mm resiste (razón 0,43–0,85), pero con solo 2 vigas cargadas deflecta 3,2 mm (L/297) y no cumple L/500; por eso se adopta 40 × 40 × 2 mm.

### Respuesta
> La estructura auxiliar de cada dosificador es un bastidor de perfiles cajón 40 × 40 × 2 mm con cuatro vigas de 0,95 m de luz, dimensionado para el estanque de 200 L lleno (≈ 2,1 kN); las razones de demanda a capacidad son ≤ 0,46 y la deformación máxima es 1,3 mm (L/740), compatible con la horizontalidad que exigen los sifones. El rótulo "15 × 15 × 6 mm" de la lámina 3.2 se declara como error de rotulado.

### Avisos
- El perfil es un **supuesto** (no hay compra confirmada); el peso del tanque vacío (15 kg) y el reparto de la carga en las vigas también.
- No se verificó la fijación del bastidor a la estructura principal ni al suelo, ni el sismo (NCh2369) sobre el equipo; seguir el mismo criterio de la pregunta 1 si el profesor lo pide.
- El itemizado (100 ml) no coincide con la lámina; cubicar de nuevo.

### Acciones para Claude Code
- `04_resultados.tex` (≈ línea 274): reemplazar el `\revisar` de la estructura de los dosificadores por la verificación anterior y la nota sobre el rotulado.
- `04_analisis/scripts/10_estructura.py`: agregar la verificación de las vigas del bastidor y su salida en `estructura_verificacion.csv`.
- `anexo_itemizado.tex` / `itemizado_rev1.csv` (partida 2.1.9): señalar que "15x15x6 mm" es un error y que la cantidad (100 ml) debe cubicarse; corregir la lámina 3.2.
- Registrar el supuesto en `DECISIONES.md`.

---

*(Las preguntas 13, 14 y 17 no se pueden responder con el repositorio y quedan **pendientes del profesor** (texto de la NCh3456, anexo de referencias bibliográficas ANID y observaciones escritas del profesor).)*
