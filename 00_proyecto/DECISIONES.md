# DECISIONES — Registro de decisiones

> Cada decisión importante queda aquí, con fecha y motivo, para que ninguna
> IA (ni tú mismo en 3 meses) la reabra sin razón.
> Formato: la más reciente arriba.

---

## 2026-11-19 — Objetivos y alcance = inscripción

- **Decisión:** los objetivos de la tesis son los **textuales de la inscripción** visada por el profesor guía; la tesis es **solo de diseño** (etapa inicial del proyecto ANID). El dimensionamiento de proceso del humedal se presenta como dato de entrada del proyecto.
- **Motivo:** instrucción del profesor guía ("limitarse exclusivamente a esos objetivos"); la implementación es otra tesis.
- **Consecuencias:** se retiró la sugerencia de dividir los objetivos. Los hallazgos C4, C10 y C11 del triaje se reinterpretan (ver triaje §7). Faltan entregables inscritos: datos de caracterización, tiempos de retención, pérdidas/ADT/bombas, zanjas, especificaciones.

---

## 2026-11-19 — Migración de la v3.0: criterio de edición

- **Decisión:** al migrar la v3.0 se conserva el texto del autor y solo se corrigen errores objetivos (ortografía, persona gramatical, signo de la ecuación de demanda, unidades, decimales, citas verificables). Todo lo que requiere criterio técnico o datos del autor queda marcado con `\revisar{}` o `\pendiente{}`, sin inventar valores.
- **Motivo:** el contenido técnico es responsabilidad del autor; la IA no debe introducir resultados ni datos.
- **Consecuencias:** el PDF actual muestra marcas de color; desaparecen con `\mostrarmarcasfalse` cuando se resuelvan.

## 2026-11-19 — Bibliografía de la v3.0

- **Decisión:** se eliminaron 12 referencias no citadas; se corrigieron Vera et al. (2016) (entrada truncada), Cohen-Shacham et al. (2016, no 2019) y NCh1333 (Of.1978 Mod. 1987, título correcto). Autores solo con las iniciales del original (no se agregaron nombres de pila no verificados).
- **Motivo:** la rúbrica penaliza referencias no citadas y errores APA; el profesor guía es autor de Vera et al. (2016).

## 2026-11-19 — Nombres de capítulos y figuras

- **Decisión:** se mantienen los nombres de la v3.0 ("Marco Teórico", "Metodología", "Discusión y Análisis de Resultados") y se usa "Presentación de Resultados" (template). La figura 2.1 se redibujó en TikZ; la tabla 3.1 sin datos se reemplazó por la tabla 4.3 (caudales y concentraciones por fuente); la demanda de riego de la memoria de cálculo pasó a Resultados (respalda los 160 L/h del bypass).

---

## 2026-11-19 — Aplicación de la normativa ICV-611 (UCM)

- **Decisión:** la plantilla LaTeX replica los Lineamientos y el template Word oficial: carta, Times 12 (newtx/mathptmx), interlineado 1,5 de Word (`\setstretch{1.43}`), márgenes 2,5/2,5/3/3, número abajo a la derecha (romano en preliminares), encabezado "Capítulo N. Nombre" arriba a la derecha, títulos 18/14/12 pt, leyendas 11 pt con rótulo en negrita y dos puntos, tablas con título arriba y figuras abajo, anexos "Anexo I:", APA 7 con "&".
- **Motivo:** el criterio "Formato" de la rúbrica descuenta desde la primera falta.
- **Interpretaciones tomadas:**
  - Interlineado: se igualó el "1,5 líneas" de Word (20,7 pt) y no el `\onehalfspacing` de LaTeX (18 pt), para que el conteo de páginas (máx. 80) sea comparable con Word.
  - Orden de preliminares: el de los Lineamientos (Agradecimientos → Resumen → Abstract), no el del template. **Pendiente confirmar.**
  - Las 80 páginas se miden desde la Introducción hasta el final de la Bibliografía (criterio conservador).
  - Contenido de tablas también en 11 pt (la regla de 11 pt es ambigua entre leyenda y contenido; se aplicó a ambos).
  - Título profesional en la portada: "Ingeniero/a Civil", tal como el template oficial.
- **Alternativas descartadas:** escribir en Word con el template (se pierde control de versiones y trabajo con IA).

## 2026-11-19 — Bibliografía de ejemplo

- **Decisión:** se reemplazaron los libros de ejemplo iniciales por los 4 ejemplos oficiales de los Lineamientos (libro, artículo, norma, sitio web).
- **Motivo:** sirven como modelo exacto de APA 7 según la universidad.

---

## 2026-11-19 — Estructura del repositorio tipo "sala de edición"

- **Decisión:** separar normativa, material bruto, selección, análisis y tesis final en carpetas numeradas.
- **Motivo:** poder retomar el trabajo desde cualquier IA con todo el contexto, y no mezclar material bueno con malo.
- **Alternativas descartadas:** todo en Overleaf (pierde el contexto para IAs y el historial de decisiones).

## 2026-11-19 — Plantilla LaTeX base

- **Decisión:** clase `report`, pdfLaTeX, `biblatex` + `biber`, estilo APA provisorio, `siunitx` para unidades.
- **Motivo:** compatible con Overleaf y con la compilación automática de GitHub; APA es común en ingeniería civil en español.
- **Actualización:** reemplazada por la decisión "Aplicación de la normativa ICV-611" (arriba).

---

<!-- Plantilla para nuevas decisiones:

## AAAA-MM-DD — Título corto

- **Decisión:**
- **Motivo:**
- **Alternativas descartadas:**
- **Consecuencias / pendiente:**

-->

## 2026-11-20 — Objetivos aprobados VF-V2 y entrega en Word

- **Decisión:** se adoptan los objetivos de la inscripción VF-V2 (aprobados por la Escuela a inicios de octubre de 2026): OG + 3 OE
  (caracterización → diseño depurativo e hidráulico → diseño estructural). La versión "visto-ILVP" queda obsoleta.
- **Consecuencia:** caracterización y diseño depurativo del humedal pasan a ser parte del alcance; caps. 3 y 4 se ordenan por los 3 OE.
- **Decisión:** el LaTeX sigue siendo el master; al profesor se le envía Word generado con `make word`.
  Sus ediciones/comentarios en Word se traspasan a mano al LaTeX y se registran en `03_seleccion/triaje/`.
- **Motivo:** correo del profesor guía del 16-11-2026.

## 2026-11-20 — ETABS no se menciona; NCh427/1 remite a NCh3171/NCh2369

- **Decisión (autor):** ETABS no se usó y **no se menciona en la tesis**; su manual (UCM, 2024) solo sirve como apoyo de método.
- **Consecuencia normativa:** la NCh427/1:2016 (B.2) remite cargas y combinaciones a NCh3171, NCh433 y NCh2369, y en sismo
  prevalecen las normas sísmicas. La tesis citará NCh427/1 (numeración chilena, equivalente a AISC 360-10) para la resistencia
  y la NCh3171 para las combinaciones (pendiente conseguirla).
