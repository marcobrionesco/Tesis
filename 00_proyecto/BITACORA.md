# BITÁCORA — Registro de sesiones de trabajo

> Una entrada por sesión (humana o con IA). La más reciente arriba.
> Sirve para que la próxima IA sepa qué pasó sin leer todo el historial de Git.

---

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
