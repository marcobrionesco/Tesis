# DECISIONES — Registro de decisiones

> Cada decisión importante queda aquí, con fecha y motivo, para que ninguna
> IA (ni tú mismo en 3 meses) la reabra sin razón.
> Formato: la más reciente arriba.

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
