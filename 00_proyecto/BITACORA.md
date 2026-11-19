# BITÁCORA — Registro de sesiones de trabajo

> Una entrada por sesión (humana o con IA). La más reciente arriba.
> Sirve para que la próxima IA sepa qué pasó sin leer todo el historial de Git.

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
