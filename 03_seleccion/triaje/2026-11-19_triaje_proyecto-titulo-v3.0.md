# Triaje: Proyecto de Título v3.0 (versión enviada al profesor guía)

- **Archivo original:** `02_material_bruto/borradores_previos/2026-11-19_yo_proyecto-titulo-v3.0-enviada-profesor.tex`
  (+ v1.0 y v2.0, que solo difieren en formato y en citas; + `2026-11-19_yo_memoria-calculo-volumenes-humedales.tex`)
- **Origen:** Marco (con apoyo de IA en partes del texto y figuras)
- **Fecha de triaje:** 2026-11-19
- **Contexto:** el profesor guía pidió mejorar el documento (sin observaciones escritas disponibles aún).
- **Veredicto general:** 🔧 **Base técnica valiosa, pero con inconsistencias numéricas, resultados faltantes y referencias con errores.**
  El diseño (caudales, balance de oxígeno, planos, plataforma) es trabajo real y rescatable;
  el problema está en la presentación de resultados, la coherencia interna y la bibliografía.
- **Destino:** migrado a `tesis/` (capítulos 1–6, anexos I–V) con las correcciones evidentes
  aplicadas y marcas `\revisar{}` / `\pendiente{}` donde se requiere decisión o dato del autor.

---

## 1. Problemas críticos (los que más bajan la nota)

| # | Problema | Dónde (v3.0) | Veredicto | Acción |
|---|---|---|---|---|
| C1 | **Resultados que no se presentan**: la Discusión y las Conclusiones citan valores (razón de trabajo 7,2 %, interacción 18,8 %, deflexión 3,81 mm, presión 27,76 kPa vs. 150 kPa) que **no aparecen en el capítulo de Resultados**. Resultados tiene dos secciones vacías (ADT/bombas; Mu, Vu). | Cap. 4 §4.1.3, §4.2.1; Cap. 5; Cap. 6 | ❌ | Presentar en Resultados las tablas de verificación (memoria de cálculo) antes de discutirlas. Rúbrica: Resultados 15 % + Discusión 15 %. |
| C2 | **Perfiles estructurales contradictorios**: Resultados dice vigas 150×150×6 y secundarias 150×100×3; Discusión dice columnas y vigas 250×250×6 y costaneras 150×50×3. | §4.2.1 vs §5.2 | ❓ | Definir cuál es el diseño final (revisar planos 3.1 y 3.2). |
| C3 | **Zona sísmica contradictoria**: Metodología dice Zona 2; Discusión dice Zona 3. | §3.2.2 vs §5.2 | ❓ | Confirmar la zona de Linares en la NCh433 (Tabla 4.1) / NCh2369 vigente y usar una sola. |
| C4 | **NTK irrealmente bajo**: 1,5 mg/L (casa) y 1 mg/L (oficina), "se asume el amonio como NTK". Agua servida doméstica cruda tiene NTK del orden de decenas de mg/L (rango típico en Tchobanoglous et al., 2014). Con esto la demanda por nitrificación queda en 4,7 g O₂/d (despreciable) y el balance de oxígeno sale sobredimensionado. | Anexo A §1; §4.1.2 | ❓ | Verificar los datos de monitoreo. Si son reales, explicarlos; si no, rehacer el balance con NTK representativo. |
| C5 | **Carga amoniacal incoherente**: la memoria de cálculo (`Tablas.tex`, tabla de fases) indica ~3 g NH₄⁺/m²·d (= ~18 g/d en 6 m²), pero el cálculo usa 1,1 g NTK/d. | memoria de cálculo vs §4.1.2 | ❓ | Unificar. Va de la mano con C4. |
| C6 | **Solo se diseña la línea doméstica**: estero Batuco y agroquímicos no tienen caracterización ni dimensionamiento (la Tabla 3.1 dice "Variable / Alta / Baja"). La memoria dice que se replica el área de 6 m² ajustando caudales, pero no se muestra. | §3.1.1 (Tabla), Cap. 4 | 🔧 | Presentar datos y cálculo (aunque sea de replicación) para las 3 líneas, coherente con el título "tres fuentes". |
| C7 | **Bibliografía con errores verificables** (ver §3). Incluye una cita incompleta a un trabajo del propio profesor guía (Vera et al., 2016). | Bibliografía | ❌ | Corregido en `tesis/bib/referencias.bib` (solo lo verificable). |
| C8 | **Introducción incompleta según lineamientos**: falta hipótesis y/o preguntas de investigación, contribuciones del proyecto y alcances. | Cap. 1 | 🔧 | Secciones creadas con `\pendiente{}` en `01_introduccion.tex`. |
| C9 | **Figura 2.1 con texto deformado** ("Direcciónau percorran", "Salidde agua tratada"), típico de imagen generada por IA. **Figura 3.1** con "Baseción de apoyo". **Figura 3.4** es captura de Google Maps sin fuente. | Figs. 2.1, 3.1, 3.4 | ❌/🔧 | Fig. 2.1 redibujada en TikZ (vectorial, editable). Fig. 3.1: corregir rótulo en el archivo fuente. Fig. 3.4: se agregó "Fuente: Google Maps". |

## 2. Problemas importantes (técnicos y de redacción)

| # | Problema | Dónde | Veredicto | Acción aplicada |
|---|---|---|---|---|
| T1 | Ecuación de demanda con signo equivocado: OD = OD_DQO + OD_Nitr + OD_Desnitr, pero el texto dice que la desnitrificación se **deduce**. | Ec. 2.1, Anexo A | 🔧 | Corregido a OD = OD_DQO + OD_N − OD_DN. |
| T2 | Hazen-Williams sin unidades (J en m/m, Q en m³/s, D en m). Coeficientes C y K sin fuente. | §2.1.3, Tabla 2.1 | 🔧 | Unidades agregadas; `\revisar` para la fuente de C y K. |
| T3 | Combinaciones LRFD (1,4D; 1,2D+1,6L; 1,2D+1,0L+1,4E) citadas a NCh427/1; en Chile las combinaciones vienen de **NCh3171** y la NCh2369 tiene sus propias. | Tabla 2.2 | ❓ | `\revisar`: citar la norma de combinaciones correcta. |
| T4 | El agua de los estanques se trata como carga viva; en NCh2369 el contenido de estanques suele tratarse como carga de operación. | §3.2.1 | ❓ | `\revisar` (consultar con co-guía estructural). |
| T5 | Capacidad admisible de 150 kPa sin fuente (¿mecánica de suelos? ¿supuesto?). | §6 | ❓ | `\pendiente`: indicar de dónde sale. |
| T6 | Normas sísmicas posiblemente desactualizadas: NCh2369 tiene versión **2023**; NCh433 se actualizó en **2026**. | §2.2.2 | ❓ | `\revisar`: justificar la versión usada. |
| T7 | Norma de reúso: v2.0 citaba "NCh3456 (2022)" y v3.0 la cambió a "NCh1333 (2002) Agua – Vocabulario". La NCh1333 real es **Of.1978 Mod. 1987, "Requisitos de calidad del agua para diferentes usos"**. No se encontró evidencia pública de una "NCh3456". | §2.1.1 | 🔧 | Referencia NCh1333 corregida. `\revisar` para confirmar si existe otra norma de reúso aplicable (hay proyecto de ley de reúso en trámite, 2026). |
| T8 | Error de redacción y persona gramatical: "la necesidad de **esta** desarrollo", "**la structure**" (inglés), "**Si recordamos**" (1.ª persona), *Typha* spp. sin cursiva. | §1.2, §6, Anexo A, §3.1.2 | ✅ corregido | — |
| T9 | Decimales con punto en texto en español (1.4 D, 1.00 × 1.00 × 0.50 m) mezclados con coma. | Tabla 2.2, §4.2.2 | ✅ corregido | Unidades y números con `siunitx` (coma decimal). |
| T10 | Glosario: "OD" significa dos cosas (demanda de oxígeno y oxígeno disuelto). Símbolo "C" usado para Hazen-Williams y para coeficiente sísmico. | Glosario, §2 | 🔧 | `\revisar`: usar símbolos distintos. |
| T11 | Variable con dos nombres en el Anexo A: $V_{cargado}$ y $V_{descargadas}$. | Anexo A §2 | ✅ corregido | Unificado como $V_d$. |
| T12 | Desactivación total de la división de palabras (`\hyphenpenalty=10000`, `\lefthyphenmin=62`) produce espacios irregulares en el justificado. | Preámbulo | ✅ | La plantilla nueva usa división normal en español. |
| T13 | Planos insertados con `width=1.1\textwidth` (se salen del margen → falta de formato). | Anexos | ✅ corregido | Planos rotados y escalados dentro del margen. |
| T14 | Resumen sin datos cuantitativos (la rúbrica los exige para el nivel 4). | Resumen | 🔧 | `\pendiente` hasta consolidar resultados (C1–C5). |
| T15 | Conclusiones con citas a literatura para afirmar resultados propios (p. ej. García et al., 2010 para "datos fidedignos") y frases absolutas ("elimina por completo", "absoluto aislamiento"). | Cap. 6 | 🔧 | `\revisar`: las conclusiones deben apoyarse en los resultados propios. |

## 3. Referencias

### 3.1 Errores verificados (corregidos en `referencias.bib`)

| Cita en v3.0 | Problema | Corrección |
|---|---|---|
| Vera et al. (2016) | Entrada **truncada** ("Humedales construidos" y nada más). Es del profesor guía. | Vera, I., Jorquera, C., López, D., & Vidal, G. (2016). Humedales construidos para tratamiento y reúso de aguas servidas en Chile: reflexiones. *Tecnología y Ciencias del Agua, 7*(3), 19–35. (verificado en Redalyc / ANID) |
| Cohen-Shacham et al. (2019) | El documento IUCN con DOI 10.2305/IUCN.CH.2016.13.en es de **2016** (y los autores figuran como editores). | Año corregido a 2016, editores. |
| INN (2002) NCh1333 "Agua – Vocabulario" | Título y año incorrectos. | NCh1333.Of1978 Mod. 1987, *Requisitos de calidad del agua para diferentes usos*. |
| DWA (2017) | Falta el código de la hoja técnica. | DWA-A 262 (2017). `\revisar` título exacto. |

### 3.2 Por verificar (no se pudo confirmar en línea)

- **Platzer, Hoffmann & Miglio (2016)**, "Long term experiences…", IWA Gdańsk: no se encontró en búsqueda pública. Pedir el PDF al profesor guía o reemplazar.
- **Uribe Meneses et al. (2012)**, Atlas bioclimático de Chile: confirmar lista exacta de autores.
- **Tietz et al. (2007)**: el artículo trata la biocenosis microbiana; se usa para justificar la transferencia de oxígeno por convección/difusión. Verificar que lo respalde.
- **Das (2015)**: la 8.ª ed. figura como 2015 o 2016 según el catálogo; usar la que diga la portada del libro consultado.

### 3.3 En la bibliografía pero **nunca citadas** en el texto (eliminadas)

Arceivala (1981), Batterman et al. (2009), Giles & Moneva (1970), Hutton & Haller (2004), Jackson et al. (1981),
Lavrnić et al. (2017), Morales et al. (2013), Prat (1998), Rouse et al. (1974), Striebig et al. (2022), SISS (2010),
Torres et al. (2009). Varias (NDVI, temperatura de canopia, bioindicadores) parecen venir del proyecto ANID marco,
no de esta tesis. La rúbrica penaliza referencias no citadas. **Morales et al. (2013)** y **Lavrnić et al. (2017)**
sí son pertinentes: conviene citarlas donde corresponda en el marco teórico.

### 3.4 Brecha frente a la rúbrica

- Hay **27 referencias citadas**; de los últimos 10 años (≥ 2016) son ~10, la mayoría normas y libros.
- **Faltan artículos científicos recientes** sobre humedales verticales (HCFV), tratamiento de residuos de
  agroquímicos en humedales, reúso en riego en Chile y sistemas modulares en contenedores. El criterio
  "Estado del arte / Marco teórico" (15 %) exige análisis crítico de literatura reciente.
- Sugerencias a evaluar (reales, verificar antes de citar): Garreaud et al. (2017, 2020) sobre la megasequía
  de Chile central; publicaciones del grupo del profesor guía sobre humedales en Chile.

### 3.5 Origen de los errores (hallazgo posterior, al analizar `05_ejemplos/`)

La bibliografía de la v3.0 coincide casi por completo con la de la tesis de Guerrero (2024, mismo profesor guía),
incluidos sus errores (Cohen-Shacham "2019", "NCh1333: Agua – vocabulario (2002)", entradas no citadas).
**Lección:** no copiar referencias de otra tesis; buscar y verificar cada fuente original.

### 3.6 Nuevos hallazgos técnicos (ver `05_ejemplos/fichas/2024_ucm_guerrero_…md`)

| # | Hallazgo | Veredicto |
|---|---|---|
| C10 | Carga orgánica de diseño 30 g DQO/m²·d **supera** el máximo de las guías de diseño de humedales verticales (20–27 g DQO/m²·d, Dotro et al.). La discusión la llama "conservadora". | ❓ verificar en la fuente original y redimensionar o justificar |
| C11 | Carga hidráulica 125 L/m²·d **supera** el rango de DWA (80–120 L/m²·d). | ❓ ídem |

## 4. Qué se rescata tal cual (✅)

- Planteamiento general, antecedentes del proyecto ANID/Anillos/ATE250033 y objetivo general.
- Cálculo de caudales de casa (registro de 13 meses, R = 0,8) y oficina (aforos, 2 escenarios).
- Demanda de riego por escenarios (memoria de cálculo): **incorporada a Resultados**, porque sustenta
  el caudal de 160 L/h que se discute en el bypass.
- Procedimiento del balance de oxígeno (Platzer, 1999) y su desarrollo numérico (salvo C4/C5).
- Planos EE-ATE250033 (1, 2.1–2.4, 3.1–3.2), itemizado y figuras propias (3.2, 3.3, 4.1).
- Discusión sobre rigidez, *sloshing*, sifones y bypass: buen razonamiento ingenieril, falta respaldarlo con resultados.

## 5. Resumen

| Categoría | Cantidad |
|---|---|
| ❌ Descartar / rehacer | 3 (figura 2.1, 12 refs no citadas, tabla 3.1 sin datos) |
| 🔧 Reescribir / completar | ~15 |
| ❓ Verificar con datos o profesor | 8 (C2–C5, T3–T7) |
| ✅ Rescatable | la mayor parte del texto y todos los planos |

**Estimación:** ~70 % del contenido es rescatable; el trabajo pendiente se concentra en
(1) consolidar y presentar resultados, (2) resolver las inconsistencias numéricas y
(3) reforzar el marco teórico con literatura reciente.

---

## 7. Revisión tras recibir los documentos oficiales (2026-11-19)

Documentos: inscripción visada, propuesta ANID, correo del guía (23-10-2026), diseño del humedal y presentación a la empresa
(`01_normativa/proyecto/`). Cambian el diagnóstico así:

| Hallazgo | Antes | Ahora |
|---|---|---|
| C4/C5 (NTK 1–1,5 mg/L) | Error del autor | El valor viene del **documento de diseño del proyecto**. La propuesta ANID plantea ≈ 3 g NH₄⁺/m²·d en la Fase 1. **Preguntar al guía** el valor medido; no redimensionar por cuenta propia. |
| C10/C11 (30 g DQO/m²·d; 125 L/m²·d sobre las guías) | Sobrecarga, redimensionar a ~9 m² | Es la **carga de la Fase 1 experimental**, definida a propósito por el proyecto (Fase 2: 60). **No es un error de diseño**; el error es llamarla "conservadora". El dimensionamiento de proceso está **fuera del alcance** inscrito. |
| Oficinas 150 L/d sin justificar | `\revisar` | **Resuelto**: decisión del director del proyecto (correo 23-10-2026). |
| T7 (norma de reúso) | NCh1333 corregida; NCh3456 no encontrada | La propuesta ANID cita **NCh3456 (INN, 2022)** para reúso en riego: es probablemente la norma correcta; pedir el título exacto. |
| Sugerencia de dividir los objetivos | Recomendada | **Retirada**: el guía pidió limitarse a los objetivos inscritos. |
| Objetivos de la v3.0 | — | **No coincidían** con los inscritos (agregaban balance de O₂ y fundaciones). Reemplazados por los textuales. |
| Entregables inscritos faltantes | — | Datos de caracterización de las 3 fuentes, **tiempos de retención**, pérdidas de carga, ADT y selección de bombas, zanjas, especificaciones. |

## 8. Revisión tras recibir datos, planos PDF, EETT e itemizado (2026-11-19)

| Hallazgo | Resultado |
|---|---|
| C2 (perfiles contradictorios) | ✅ **Resuelto**: láminas 3.1–3.2, EETT e itemizado coinciden en pilares y vigas principales 150×150×6 y secundarias 150×100×3 (A270ES). La discusión de la v3.0 estaba errada; corregida. |
| C4/C5 (NTK) | ✅ **Explicado por los datos**: el nitrógeno medido en AS1/AS2 es realmente bajo (NH₄⁺ 1,28/1,98 mg/L; NT 2,7/2,0 mg/L). Los valores de diseño (1,0/1,5) están algo **por debajo** de las medias medidas. Falta interpretar la causa. |
| C6 (sin datos de estero y agroquímicos) | 🟧 Datos de calidad ya presentes (tabla 4.1). Falta el **criterio de caudal**: igualar la carga orgánica es inviable para el estero (≈ 28 400 L/d). |
| C12 (nuevo) | Hormigón G30 (EETT, itemizado, texto) vs. G25 (lámina 3.2). |
| C13 (nuevo) | Capas filtrantes inconsistentes entre EETT, lámina 2.2 y tesis; cantidades de arena/gravilla del itemizado aparentemente intercambiadas. |
| C14 (nuevo) | El índice de las EETT es de otro proyecto (pintura, cielo, panel LED); se omitió en el anexo VI. |
| C15 (nuevo) | Itemizado con numeración incompleta y placas base medidas en m². |

## 9. Revisión tras recibir los cálculos del autor (2026-11-20)

| Hallazgo | Resultado |
|---|---|
| C1 (resultados que no se presentaban) | 🟧 Ahora hay tablas preliminares de ADT (4.7) y verificación estructural (4.8), generadas por scripts que reproducen y actualizan los cálculos del autor. |
| Origen de 7,2 %, 18,8 %, 3,81 mm y 27,76 kPa | Calculados con una versión anterior (perfil 250×250×6, costanera 150×50×3 de 3 m, zapata 0,8×0,8×0,4, plataforma 5,5×3,0 m). Con el diseño final: 9 %, 44–59 %, 0,56 mm y 24,2 kPa. |
| C16 | El registro del autor muestra que el tablero de 15 mm no cumplía (1,85 > 1,33 mm) pero se concluyó "cumple". Recalculado: 2,91 mm. |
| C17 | Zapata: con el supuesto sísmico del autor (corte en 2 pilares en voladizo) hay volcamiento. Depende del reparto del corte. |
| C18 | Estero: ADT ≈ 31 m con PVC 25 mm; inviable con los catálogos. |
| C19 | Zanja 3: tapada insuficiente; el cálculo usa Ø 52 mm y las EETT, 110 mm. Datos de los scripts ≠ datos de las corridas guardadas (zanjas 1 y 2). |
| C20 | El cálculo estructural mezclaba tensiones admisibles y cargas mayoradas (pilar) y cargaba una sola viga con todos los estanques: corregido en la versión actualizada. |
