# BITÁCORA — Registro de sesiones de trabajo

> Una entrada por sesión (humana o con IA). La más reciente arriba.
> Sirve para que la próxima IA sepa qué pasó sin leer todo el historial de Git.

---

## 2026-11-20 (noche, 24) — Ejemplo: anexos de la tesis de Bocaz (humedal de lodos)

- Archivado en `05_ejemplos/tesis/` con ficha (solo anexos: planos, manual de O&M, ficha PTAS, presupuesto/APU, costos de operación).
- Ideas de forma: tabla resumen de "parámetros de diseño y operación" por línea para el cap. 4; cuadro de cantidades en los planos.
- No imitar: anexos con números arábigos; manual de O&M y presupuesto (fuera del alcance inscrito). Sin cambios en `tesis/`.

## 2026-11-20 (noche, 23) — Das (2015) completo: capacidad de carga y cierre de la bibliografía

- Partes 6–7 recibidas (cap. 16–18). Cap. 2: q_adm = q_u/FS (FS ≥ 3) y ecuación de Terzaghi para zapata cuadrada; asentamientos.
  Cap. 3: q_máx con e > B/6 y equivalencia 80 % ⇔ e ≤ 0,233B. Cap. 4: sensibilidad de q_adm a φ′ (nuevo script
  `04_analisis/scripts/13_capacidad_soporte.py`): 150 kPa ⇔ φ′ ≈ 32°. Conclusiones: cita a Das (2015) en español; se eliminó
  `das2015principles` (sin verificar).
- El autor indica que **terminó la recopilación bibliográfica**. Sigue: respuestas del profesor (preguntas 1–18) y recálculo.

## 2026-11-20 (noche, 22) — Das (2015), Fundamentos de ingeniería geotécnica

- Nueva `das2015fundamentos` (4.ª ed. en español; PDF recibido hasta la p. 474, sin los cap. 16–17). Reemplaza a `das2015principles`
  en el cap. 2; esta última sigue solo en conclusiones (sin verificar).
- Cap. 2: filas d₁₀ y U en la tabla de parámetros HCFV (Dotro et al., Tabla 4.1) y su definición (Das, 2.15).
- Cap. 3: ecuación de presiones de contacto con excentricidad (e ≤ B/6) y verificación al deslizamiento (FS 1,5; φ′ reducido), con NCh2369.
- Pendiente: cap. 16–17 de Das (capacidad de carga y asentamiento) para respaldar los 150 kPa supuestos.

## 2026-11-20 (noche, 21) — Riesgo y brecha hídrica (Radiografía del Agua y ARClim)

- Citados: Escenarios Hídricos 2030 (2018, Fundación Chile) (Maule = mayor huella hídrica azul del país, 50 de 212 m³/s; agricultura
  88 % del consumo nacional) y Urquiza et al. (2020, ARClim Asentamientos Humanos) (riesgo futuro de inseguridad hídrica doméstica
  rural se extiende al Maule). Cap. 1: dos oraciones tras el párrafo de la megasequía. Ficha `riesgo-hidrico_2026-11-20.md`.
- Sin cambios en diseño ni cálculos. Siguen pendientes Garreaud et al. (2017) y el catastro de cerezos.

## 2026-11-20 (noche, 20) — Megasequía

- Citados: CR2 (2015) (déficit ~30 % desde 2010; ≥ 25 % atribuible al cambio climático) y Yaksic et al. (2024, SISSA) (zona central:
  314 000 ha de frutales, 84,1 % del país). Cap. 1: primer párrafo con datos cuantitativos (cierra la marca `\revisar`).
- Archivados sin citar: CR2 FONDAP 2023, Sologuren 2024 (memoria), MINAGRI 2020. Pendiente: Garreaud et al. (2017) y catastro de cerezos.

## 2026-11-20 (noche, 19) — Humedales en Chile: Vera et al. (2016) verificado y Vidal y Gómez (2023)

- `vera2016humedales` verificado con el PDF (cobertura rural ≤ 20 %; HC < 2 %). Nueva `vidal2023desarrollo` (cap. 3 del libro UNSA 2023).
- Cap. 1: antecedentes de Chile (cobertura y brecha piloto → escala real). Cap. 2: pilotos chilenos FH y FV.
- Cap. 4: factor de restitución respaldado (60–85 %); marca para el 0,9 de oficinas. Höllmann et al. (2018) archivado sin citar.

## 2026-11-20 (noche, 18) — Experiencias con humedales verticales (Sudamérica y Chile)

- `platzer2016long` verificada y corregida (actas IWA Gdańsk; páginas no verificables eliminadas). Nuevas: `altafin2020innovaciones`
  (BID), `vera2025atrapaniebla` y `vera2025nichos` (memorias CEAZA del profesor guía, también en `05_ejemplos/` con ficha).
- Cap. 2: límites de Platzer (< 200 mm/d; ≤ 32 g DBO₅/m²·d), brecha en Chile (Altafin) y diseños CEAZA (COS < 35 g DQO/m²·d).
- Cap. 5: las cargas de la Fase 1 quedan dentro de esos límites. Pregunta 13 actualizada (NCh3456, Cat. D).
- Louage et al. (2026): preprint, archivado sin citar.

## 2026-11-20 (noche, 17) — Cross et al. (2021), Nature-Based Solutions for Wastewater Treatment

- Libro recibido: entrada `cross2021nature` corregida (eran editores, no autores; + DOI). Nueva `langergraber2021vertical` (ficha HCFV).
- Cap. 2: por qué crecen las SbN; eficiencias del HCFV (incl. 2–4 log de coliformes) y ventajas. Cap. 4: efluente del estero
  estimado en clase 1 o excepción por coliformes (marca `\revisar`: estimación teórica).

## 2026-11-20 (noche, 16) — SbN y humedales en Latinoamérica

- Citados: Rodriguez-Dominguez et al. (2020) (revisión de 520 experiencias en LAC; FV 9 %, limitado por falta de conocimiento y
  distribución presurizada) y Reuter et al. (2022, compendio BORDA/Eawag: ficha de HFV, 4–10 dosis/día, sobre el suelo).
- Cap. 2: pertinencia rural de las SbN, párrafo de revisión de literatura en LAC (primer análisis crítico) y dosificación.
- Presentación de Homsi (AIDIS) archivada sin citar.

## 2026-11-20 (noche, 15) — DGA (2004), volumen 1 con anexos

- Archivado; nueva referencia `dga2004volumen1`. Cap. 2: tabla de límites de clases de calidad (instructivo CONAMA, anexo A1).
- Cap. 4: clasificación orientativa del estero: coliformes fecales en clase 4 → la desinfección es el objetivo principal de esa línea.

## 2026-11-20 (noche, 14) — DGA (2004), cuenca del río Maule

- Archivado (2 partes) con ficha; nueva referencia `dga2004maule`. Tabla 2.1, columna del estero completada (pH, DBO₅, SST,
  NH₄⁺, coliformes fecales). Cap. 2: calidad de la cuenca (Putagán y Loncomilla). Cap. 4: comparación con EST (CE igual a la del
  Putagán; OD menor; coliformes altos).
- Caudales del Putagán (5–92 m³/s): no aplicables al estero Batuco. "Research_Report" = texto de IA, archivado.

## 2026-11-20 (noche, 13) — Tesis de Sommer (2016)

- Archivada sin citar: trata de árboles de bosque; la preferencia por nitrato es específica de cada especie. No aporta sobre nitrificación en humedales (ya respaldada con Dotro et al., 2021).

## 2026-11-20 (noche, 12) — Bibliografía sobre nitrato en frutales

- 3 artículos archivados con ficha. Ninguno respalda que las plantas prefieran nitrato; Schwitzky et al. (2026) muestran
  más amonio que nitrato en suelos de cerezo. Frase del cap. 2 reescrita con `schwitzky2026contrasting` y
  `sanmartino2010isotopically` (eficiencia de absorción 65,7 % primavera / 37,4 % poscosecha) + marca `\revisar`.
- Nueva pregunta 18 al profesor.

## 2026-11-20 (noche, 11) — DGA (2003), clasificación de cursos de agua (vol. 1, metodología)

- Archivado (4 partes) con ficha; nueva referencia `dga2003diagnostico`: clases de calidad (riego irrestricto/restringido) en cap. 2.
- Para datos de cauces cercanos a Linares hace falta el **volumen 8 (Mataquito y Maule)** del mismo estudio.

## 2026-11-20 (noche, 10) — Calidad de aguas superficiales

- 4 documentos archivados con ficha. Citado: Sigoña et al. (2025) (`sigona2025pesticide`): diurón y fosetil-Al en la cuenca
  Putagán-Loncomilla → cap. 2 y nueva fila de plaguicidas en la tabla 2.1. Sin citar: Girardi et al. (2018), DGA (2012, Elqui),
  Osorno (2026, río Damas). Ninguno da caudales para el estero Batuco.
- Pendiente: parámetros convencionales de esteros agrícolas (tabla 2.1, columna del estero).

## 2026-11-20 (noche, 9) — Biolechos: manual AAFC (2018) y folleto FAO/JTI (2016)

- Archivados con ficha. Nueva referencia `braul2018robust` (cap. 2: volumen típico de enjuague 5000–7000 L/año, dimensionamiento y
  eficiencia de biolechos). Cap. 4 y pregunta 5: el agua de lavado disponible podría no alcanzar para la línea de agroquímicos.

## 2026-11-20 (noche, 8) — Bibliografía de aguas con agroquímicos

- 5 documentos archivados (uno escaneado, OCR) con ficha conjunta. Nuevas referencias: `saleh2020removal`,
  `ignatowicz2023treatment`, `mussali2023biobeds`.
- Cap. 2: origen y composición de las aguas con plaguicidas; tabla 2.1 con pH, DQO y DBO (cotas de efluentes de producción);
  párrafo sobre humedales verticales para aguas con plaguicidas y biolechos.
- Pendiente: columna del estero de la tabla 2.1; usar Ignatowicz et al. en la discusión de la línea de agroquímicos.

## 2026-11-20 (noche, 7) — NCh2369:2025

- Norma archivada (3 partes, escaneada, OCR); fórmulas y Tablas 2, 3, 6 y 7 leídas en imagen. Nueva referencia `inn2025nch2369`.
- Cap. 2: sección sísmica reescrita con la norma 2025 (categorías e I, espectro de diseño, cortes mínimo y máximo,
  combinaciones sísmicas LRFD/ASD con SO y SA). Cap. 3: zona 2 para Linares, método y criterio de 80 % de área apoyada.
  Cap. 5: zona corregida (era 3). Conclusiones: cita actualizada.
- Pregunta 1 reescrita (zona resuelta; quedan versión, categoría, R, suelo y diafragma).
- Pendiente: recalcular C, plataforma y zapatas con la norma que se adopte (script `10_estructura.py`).

## 2026-11-20 (noche, 6) — Bibliografía de aguas servidas domésticas

- Archivados: libro *Las aguas servidas y su depuración en zonas rurales* (UdeC, 2014), resumen ejecutivo U. de Chile/SAG (2005)
  y manual ACHIPIA/INDAP de aguas grises (2025), con fichas.
- Nueva referencia `araya2014aguas`. Cap. 2: definición de agua servida (reemplaza la que estaba por verificar), caracterización
  y tabla 2.1 con rangos rurales chilenos (pH, DQO, DBO₅, SST, NT, NH₄⁺, NO₃⁻, PT, coliformes); referencia de Dotro como texto.
- Cap. 4: comparación de DQO y nitrógeno medidos con esos rangos; marca sobre nitrato > NT. Pregunta 8 ampliada.
- Pendiente: columnas de agroquímicos y estero de la tabla 2.1; revisar cap. 6 del libro para SbN en zonas rurales.

## 2026-11-20 (noche, 5) — NCh3171:2017 y dossier de Gemini

- NCh3171:2017 archivada (OCR) con ficha; nueva referencia `inn2017nch3171`. Cap. 2: tabla de combinaciones LRFD de la
  norma (1–7), regla de F (líquidos) con factor de D, carga muerta mínima para volcamiento, prevalencia de normas sísmicas.
- Dossier Gemini archivado en `02_material_bruto/ia_generado/` y verificado parcialmente (nota en `03_seleccion/notas/`).
  Búsqueda web: NCh2369:2025 oficializada (D.O. 9-03-2026); artículo "Mikkelsen et al. 2022" no encontrado.
- Pregunta 1 actualizada (NCh2369 2003 o 2025). Pendiente: volcamiento con 0,9(D+F)+1,4E y estanques vacíos; verificar pistas.

## 2026-11-20 (noche, 4) — NCh427/1:2016 y manual ETABS

- Archivados: NCh427/1 (4 partes, escaneada; OCR con tesseract) y manual ETABS v9.7.4 de la UCM; fichas de lectura de ambos.
- Tesis: cap. 2 (la NCh427/1 remite cargas y combinaciones a NCh3171/NCh433/NCh2369; marca para reemplazar la tabla de
  combinaciones e incluir 0,9D + 1,4E); cap. 3 (L/300 sin respaldo en NCh427/1, que sugiere L/500–L/1000 para equipos).
- Decisión: ETABS no se menciona en la tesis. Pregunta 2 ampliada (límite de deformación).
- Pendiente: NCh3171:2017 y NCh2369; rehacer volcamiento de zapatas con 0,9D + 1,4E.

## 2026-11-20 (noche, 3) — Libro Humedales para tratamiento (Dotro et al., 2021)

- Archivado en `02_material_bruto/papers/` (2 partes + texto) con ficha de lectura; año 2021 verificado (British Library).
- Nueva referencia `dotro2021humedales`; todas las citas a Dotro pasan a la edición en castellano.
- Cap. 2: tipos de humedales; selección del vertical (nitrificación; NT eliminado solo 20–30 %); capas; tabla de
  parámetros de diseño (Dinamarca/Alemania/Austria); balance de O₂ contrastado (coincide); operación, plantas y mantención;
  tabla 2.1 con DQO 800, DBO₅ 400 y NTK 73 mg/L para aguas servidas crudas.
- Cap. 3: procedimiento de tiempos de retención (TRH nominal ε·h·A/Q) con advertencia para lechos no saturados.
- Cap. 5: cargas de la Fase 1 (30 g DQO/m²·d; 125 mm/d) comparadas con las guías (20–27; 80, hasta 200 en clima cálido).
- Pendiente: fuente agronómica del nitrato; tabla 2.1 para agroquímicos y estero; intervalo entre pulsos y red de distribución.

## 2026-11-20 (noche, 2) — Tesis de Diego y fichas de registro de oficinas

- Archivados: tesis de Yévenes (2019, 2 partes) en `05_ejemplos/tesis/` + ficha; ficha de registro de uso de oficinas y
  documento de cálculo de producción de aguas servidas en `01_normativa/proyecto/` (originales + texto).
- Cap. 2: balance de O₂ con todos los términos explicados (η_DQO = 0,85 eficiencia de eliminación, 0,7 g O₂/g DQO,
  4,3 g O₂/g NTK, desnitrificación 0,10 × 2,9 g O₂/g N, 0,3 g O₂/L = O₂ del aire), según el anexo 9 de Yévenes.
- Cap. 3: producción de aguas servidas descrita como en la tesis de Diego (fichas, escenarios, restitución), remite al Anexo I.
- Cap. 4: factor de restitución de la casa corregido a 0,85 (≈ 632 L/d; proyecto adopta 600) y de oficinas 0,9 (165 → 150 L/d).
- Nuevo **Anexo I** (fichas de lavaplatos, lavamanos e inodoro + tabla de usos diarios); los demás anexos se renumeran.
- Pregunta 6 actualizada (aforo, semana "02S1" repetida, 0,85 vs 0,8, traducción de Dotro).
- Pendiente: método del aforo; confirmar 600 frente a 632 L/d; fichas posteriores al 1 de febrero.

## 2026-11-20 (noche) — Revisión del profesor (v3.0 comentada) y objetivos aprobados VF-V2

- Recibidos: PDF de la v3.0 con **47 comentarios** del profesor guía (→ `02_material_bruto/revisiones_profesor/`),
  inscripción **VF-V2 con los objetivos aprobados** y captura del correo del 16-11 (→ `01_normativa/proyecto/`).
- Comentarios extraídos con pymupdf y transcritos en `03_seleccion/triaje/2026-11-16_revision-profesor-v3.0.md`.
- Aplicado: objetivos/título VF-V2 (tesis, ALCANCE, CONTEXTO); cap. 1 (textos que dictó el profesor);
  cap. 2 y 3 reestructurados según sus comentarios; cap. 4 alineado a los 3 OE (IBC y planta general movidos a resultados);
  resumen en 4 párrafos (resultados y conclusiones como `\pendiente`).
- Nuevo `herramientas/latex_a_word.py` + `make word` (Word con APA, numeración y marcas resaltadas).
- Pregunta 6 de la reunión reemplazada (el diseño del humedal ya está en el alcance): ahora pide trabajo de Diego y traducción de Dotro.
- Pendiente: completar tabla 2.1 con fuentes reales; párrafos de resultados/conclusiones del resumen; abstract.

## 2026-11-20 (cont.) — Documento CO, bombas y preguntas para la reunión

- Se recibió el documento **CO**: es la *Carta Oferta Económica-Técnica* en blanco (formulario de licitación, sin medidas).
  Guardado en `02_material_bruto/otros/EE-ATE250033_carta-oferta-economica-tecnica.docx`.
  Las medidas que mandan son: planos + EETT + itemizado Rev. 1 (ya usados en `04_analisis/`).
- Itemizado reenviado: idéntico al ya archivado. **No contiene bombas** (las EETT indican que las provee el proyecto),
  por lo que la tesis debe proponer la selección (compromiso de la inscripción). Nota agregada en `04_resultados.tex`.
- Nuevo `00_proyecto/PREGUNTAS_REUNION.md`: 17 preguntas ordenadas por prioridad (alta/media/baja), sin las ya resueltas.
  `make preguntas` genera `salida/preguntas_reunion.pdf` y `.docx` para imprimir.
- Pendiente: respuestas del profesor; propuesta de selección de bombas por línea.

## 2026-11-20 — Base de datos, topografía y verificación de los cálculos

- **Quién:** Marco + Claude Code
- **Qué se hizo:** se ingresaron la BD de macroparámetros (fechas de las 6 campañas; QA contra el resumen con 10 diferencias), la curva de nivel (52 puntos UTM) y los cálculos originales del autor (Colab: estructura, bombas, excavación + documento de resultados). Se crearon `04_validar_bd.py`, `05_topografia.py` y las versiones actualizadas `10_estructura.py`, `11_bombas.py` y `12_excavacion.py`, que reproducen los resultados originales y los recalculan con las dimensiones finales. Se agregaron a Resultados las tablas de ADT y de verificación estructural (preliminares) y la sección de zanjas.
- **Hallazgos:** ver triaje §9 (C16–C20) y OBSERVACIONES_PROFESOR, preguntas 12–16.
- **Qué quedó pendiente:** documento "CO - Estación-Experimental-ATE250033"; decisiones de diseño (tablero, sismo, estero, zanja 3); actualizar Discusión y Conclusiones con los valores nuevos.
- **Archivos tocados:** `02_material_bruto/*`, `04_analisis/*`, `tesis/capitulos/04–06`, `tesis/tablas/*`, `00_proyecto/*`, triaje.

---

## 2026-11-19 — Datos de caracterización, planos PDF, EETT e itemizado

- **Quién:** Marco + Claude Code
- **Qué se hizo:** se procesaron los datos de caracterización (scripts `01_`/`02_` en `04_analisis/`, QA de promedios sin errores) y se agregaron a Resultados (sección 4.1.1, tabla y figura) y Metodología. Se reemplazaron las láminas 3.1–3.2 por PDF vectorial, se convirtió el itemizado a tabla (`03_itemizado.py`, anexo II) y las EETT a anexo VI (`herramientas/docx_a_anexo.py`). Se corrigieron los perfiles en Discusión y Resultados según planos/EETT. Las 7 figuras reenviadas ya estaban ingresadas.
- **Hallazgos:** C2 resuelto; el nitrógeno bajo es real (datos); igualar la carga orgánica del estero es inviable (~28 400 L/d); nuevas inconsistencias C12–C15.
- **Qué quedó pendiente:** preguntas 8–11 al guía; interpretar la caracterización; resultados hidráulicos (ADT, bombas, tiempos de retención) y estructurales (verificación LRFD).
- **Archivos tocados:** `02_material_bruto/*`, `04_analisis/*`, `tesis/capitulos/03–05`, `tesis/anexos/*`, `tesis/tablas/*`, `tesis/figuras/*`, `herramientas/docx_a_anexo.py`, `00_proyecto/*`, `01_normativa/proyecto/ALCANCE.md`, triaje.

---

## 2026-11-19 — Documentos oficiales y alcance

- **Quién:** Marco + Claude Code
- **Qué se hizo:** se ingresaron la inscripción visada, la propuesta ANID ATE250033, el correo del guía (23-10-2026), el diseño del humedal y la presentación a la empresa en `01_normativa/proyecto/`. Se creó `ALCANCE.md` (objetivos textuales, qué incluye y qué no, datos de diseño del proyecto) y `00_proyecto/OBSERVACIONES_PROFESOR.md`. Se reemplazaron los objetivos de la tesis por los inscritos y se redactaron Contribuciones y Alcances. Se reinterpretaron hallazgos del triaje (§7): el NTK y la carga de 30 g DQO/m²·d vienen del proyecto (Fase 1), no son errores del autor.
- **Qué quedó pendiente:** preguntas para el guía (OBSERVACIONES_PROFESOR.md); completar los entregables inscritos.
- **Archivos tocados:** `01_normativa/proyecto/*`, `00_proyecto/*`, `AGENTS.md`, `tesis/capitulos/01–05`, `tesis/anexos/anexo_calculos_humedal.tex`, triaje, ficha de Guerrero.

---

## 2026-11-19 — Ejemplos de referencia (05_ejemplos)

- **Quién:** Marco + Claude Code
- **Qué se hizo:** se creó `05_ejemplos/` y se ingresaron 3 tesis UCM (Guerrero 2024, Arancibia 2026, Jove 2026; las que venían en 2 partes se unieron) y 1 memoria de cálculo estructural (peritaje Esperanza Plan, 2026), con texto extraído y una ficha por documento (receta 11).
- **Hallazgos:** la bibliografía de la v3.0 venía en gran parte de la tesis de Guerrero (2024), con sus mismos errores. La misma tesis aporta el NTK típico (Vera et al., 2016) y los criterios de diseño de humedales verticales (Dotro et al.), que el diseño actual supera (30 g DQO/m²·d; 125 L/m²·d). Las notas `\revisar` de los capítulos 1, 2, 4 y 5 se actualizaron con estos datos.
- **Qué quedó pendiente:** decidir con el profesor guía el NTK y el área del humedal; usar la memoria de cálculo como modelo para los resultados estructurales.
- **Archivos tocados:** `05_ejemplos/*`, `tesis/capitulos/01,02,04,05`, `00_proyecto/ESTADO.md`, `03_seleccion/triaje/…v3.0.md`.

---

## 2026-11-19 — Ingreso, triaje y migración de la v3.0

- **Quién:** Marco + Claude Code
- **Qué se hizo:** se ingresó el ZIP con las versiones 1.0, 2.0 y 3.0 de la tesis, la memoria de cálculo, figuras, planos e itemizado a `02_material_bruto/` (nombres normalizados). Se hizo el triaje completo de la v3.0 (`03_seleccion/triaje/`), verificando referencias en línea, y una autoevaluación con la rúbrica (`03_seleccion/notas/`). Se migró todo a la plantilla: capítulos 1–6, preliminares, 5 anexos y 27 referencias en biblatex. Se corrigieron los errores objetivos y se marcaron con `\revisar`/`\pendiente` las decisiones y datos faltantes. La figura 2.1 (texto deformado) se redibujó en TikZ. Se reemplazó el logo por la versión en alta resolución. La guía de ejemplos de la plantilla se movió a `herramientas/ejemplos/`.
- **Hallazgos principales:** resultados que se discuten sin presentarse; perfiles y zona sísmica contradictorios; NTK irrealmente bajo; solo se diseña la línea doméstica; entrada bibliográfica truncada de un trabajo del profesor guía; 12 referencias no citadas.
- **Qué quedó pendiente:** ver "Próximos pasos" y "Bloqueos" en `ESTADO.md`.
- **Archivos tocados:** `02_material_bruto/*`, `03_seleccion/*`, `tesis/*`, `00_proyecto/*`, `Makefile`, `herramientas/ejemplos/`.

---

## 2026-11-19 — Normativa ICV-611 cargada y aplicada

- **Quién:** Marco + Claude Code
- **Qué se hizo:** se subieron los 4 documentos de la universidad (lineamientos, template Word, rúbrica, formato de práctica) a `01_normativa/originales/` con copias en texto en `01_normativa/texto/`. Se extrajeron las reglas (`REGLAS_FORMATO.md`), la rúbrica (`RUBRICA.md`) y el proceso (`PROCESO_TITULACION.md`). Se ajustó toda la plantilla LaTeX (formato, portada, hoja de firmas, índices, glosario, capítulos, anexos, APA 7) y se comparó visualmente con el template Word. Se agregó `herramientas/verificar_extension.py` a `make revisar` y la receta 10 (autoevaluación con rúbrica).
- **Qué quedó pendiente:** ver "Bloqueos" en `ESTADO.md` (orden de preliminares, nombres de capítulos, etapa actual, logo en alta resolución); subir material previo.
- **Archivos tocados:** `01_normativa/*`, `tesis/*`, `herramientas/*`, `AGENTS.md`, `00_proyecto/*`, `Makefile`.

---

## 2026-11-19 — Montaje de la estructura

- **Quién:** Marco + Claude Code
- **Qué se hizo:** se creó la estructura del repositorio, la plantilla LaTeX, los scripts de compilación, la compilación automática en GitHub y las recetas para IA.
- **Qué quedó pendiente:** subir normativa y material previo; completar `CONTEXTO.md`.
- **Archivos tocados:** todo el repositorio (estructura inicial).

---

<!-- Plantilla:

## AAAA-MM-DD — Tema de la sesión

- **Quién:** Marco + [IA usada]
- **Qué se hizo:**
- **Qué quedó pendiente:**
- **Archivos tocados:**

-->
