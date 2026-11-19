# BITÁCORA — Registro de sesiones de trabajo

> Una entrada por sesión (humana o con IA). La más reciente arriba.
> Sirve para que la próxima IA sepa qué pasó sin leer todo el historial de Git.

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
