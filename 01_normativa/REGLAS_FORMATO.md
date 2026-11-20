# REGLAS DE FORMATO — Proyecto de Título ICV-611 (UCM)

> Resumen operativo de la normativa. Los originales están en `01_normativa/originales/`
> (no se modifican) y sus copias en texto en `01_normativa/texto/`.
>
> **Abreviaturas de fuente:**
> - **LIN** = `2026-11-19_icv611_lineamientos-proyecto-titulo.docx` (Lineamientos generales, §6 = informe final)
> - **TPL** = `2026-11-19_icv611_template-proyecto-titulo.docx` (template Word oficial)
> - **RUB** = `2026-11-19_icv611_rubrica-evaluacion.xlsx` (ver `RUBRICA.md`)
>
> Universidad Católica del Maule · Facultad de Ciencias de la Ingeniería · Escuela de Ingeniería Civil · Talca.
>
> Estado: ✅ **extraído y aplicado** en la plantilla LaTeX (2026-11-19).
> Las reglas de esta página corresponden al **informe final del Proyecto de Título**.
> El anteproyecto tiene reglas distintas (ver al final).

## 1. Página y tipografía

| Regla | Valor exigido | Fuente | Dónde se aplica | ¿Aplicada? |
|---|---|---|---|---|
| Papel | Carta | LIN §6 | `main.tex` (`letterpaper`) | ✅ |
| Fuente | Times New Roman | LIN §6 | `config/paquetes.tex` (newtx; si no está, mathptmx) | ✅ |
| Tamaño de fuente | 12 pt | LIN §6 | `main.tex` (`12pt`) | ✅ |
| Interlineado | 1,5 | LIN §6 | `config/formato.tex` (`\onehalfspacing`) | ✅ |
| Alineación del texto | Justificado | TPL (estilo Normal) | por defecto en LaTeX | ✅ |
| Sangría de primera línea | 1,25 cm, sin espacio extra entre párrafos | TPL (estilo Normal) | `formato.tex` | ✅ |
| Margen superior | 2,5 cm | LIN §6 | `formato.tex` (geometry) | ✅ |
| Margen inferior | 2,5 cm | LIN §6 | `formato.tex` | ✅ |
| Margen izquierdo | 3 cm | LIN §6 | `formato.tex` | ✅ |
| Margen derecho | 3 cm | LIN §6 | `formato.tex` | ✅ |
| Idioma | Español (excepto Abstract) | LIN §6 | `paquetes.tex` (babel) | ✅ |
| Persona gramatical | **Tercera persona** | LIN §6 | redacción (ver `AGENTS.md`) | ✅ regla |
| Extensión | **Máx. 80 páginas** de cuerpo principal (todo excepto anexos) | LIN §6 | `make revisar` lo mide | ✅ control |
| Entrega final | Un solo archivo **PDF** (a la comisión también se puede enviar Word o LaTeX) | LIN §6 | `make pdf` | ✅ |

## 2. Numeración de páginas, encabezado y pie

| Regla | Valor exigido | Fuente | Dónde se aplica | ¿Aplicada? |
|---|---|---|---|---|
| Posición del número | Extremo **inferior derecho**, solo el número (no "Pág. 32") | LIN §6 | `formato.tex` (fancyhdr) | ✅ |
| Preliminares | Números **romanos** (en TPL: mayúsculas I, II, III…; la portada y la hoja de firmas no se numeran) | LIN §6, TPL | `main.tex` (`\pagenumbering{Roman}`) | ✅ |
| Cuerpo | Números arábigos desde el capítulo de **Introducción** (página 1) | LIN §6 | `main.tex` | ✅ |
| Encabezado | Extremo **superior derecho**: número y nombre del capítulo, ej. "Capítulo 1. Introducción y Planteamiento del Problema"; en anexos: "Anexos" | LIN §6, TPL | `formato.tex` | ✅ |
| Encabezado en primera página de capítulo | Sin encabezado (TPL) | TPL | `formato.tex` (estilo plain) | ✅ |
| Líneas o leyendas extra | **Prohibido** agregar leyendas o subrayados en encabezado o pie | LIN §6 | `formato.tex` (sin líneas) | ✅ |
| Notas al pie | Dentro de los márgenes | LIN §6 | por defecto en LaTeX | ✅ |

## 3. Estructura obligatoria (en este orden)

| # | Sección | Obligatoria | Detalle | Archivo |
|---|---|---|---|---|
| 1 | Portada | Sí | Según Anexo 3 de LIN / TPL p. 1 | `portada/portada.tex` |
| 2 | Hoja de firmas Comisión Examinadora | Sí | Según Anexo 4 de LIN / TPL p. 2 | `portada/hoja_firmas.tex` |
| 3 | Agradecimientos | Opcional | Máx. **1 página** | `preliminares/agradecimientos.tex` |
| 4 | Resumen | Sí | Objetivos, métodos, resultados y conclusiones; máx. **1 página**; **3 a 5** palabras clave al final | `preliminares/resumen.tex` |
| 5 | Abstract | Sí | Traducción al inglés del resumen + *keywords* | `preliminares/abstract.tex` |
| 6 | Índice General | Sí | Capítulos y subcapítulos con página | `main.tex` |
| 7 | Índice de Figuras | Sí | | `main.tex` |
| 8 | Índice de Tablas | Sí | | `main.tex` |
| 9 | Glosario | Si corresponde | Términos técnicos y siglas con su significado | `preliminares/glosario.tex` |
| 10 | Cuerpo principal | Sí | Ver §4 | `capitulos/` |
| 11 | Bibliografía | Sí | APA 7 | `bib/referencias.bib` |
| 12 | Anexos | Opcional | Desarrollos teóricos auxiliares, encuestas, diseños extensos, planos | `anexos/` |

⚠️ **Discrepancia:** LIN §6 pone *Agradecimientos* antes del *Resumen*; TPL lo pone después
> **Decisión del autor (20-11-2026, pregunta 16):** se mantiene el orden de los Lineamientos (Agradecimientos → Resumen → Abstract); pendiente confirmar con el profesor. La Discusión sigue como capítulo aparte (la rúbrica la puntúa por separado).
del *Abstract*. Se adoptó el orden de LIN (documento normativo). Confirmar con profesor guía
(anotado en `00_proyecto/ESTADO.md` → Bloqueos).

## 4. Cuerpo principal (capítulos)

Nombres según TPL (el que va antes o después de "/" depende del tipo de proyecto):

| Cap. | Título | Contenido exigido (LIN §6) | Archivo |
|---|---|---|---|
| 1 | Introducción y Planteamiento del Problema | Contexto, antecedentes generales y técnicos, hipótesis y/o preguntas de investigación, objetivo general y específicos, contribuciones del proyecto | `01_introduccion.tex` |
| 2 | Estado del Arte (investigación) / Marco Teórico (trabajo aplicado) | Revisión de literatura | `02_marco_teorico.tex` |
| 3 | Materiales y Métodos / Metodología | Metodología para resolver la problemática | `03_metodologia.tex` |
| 4 | Presentación de Resultados | Resultados mediante tablas, gráficos y/o figuras | `04_resultados.tex` |
| 5 | Discusión / Análisis de Resultados | Discusión de los resultados | `05_discusion.tex` |
| 6 | Conclusiones | | `06_conclusiones.tex` |

## 5. Títulos y numeración

| Regla | Valor exigido | Fuente | ¿Aplicada? |
|---|---|---|---|
| Niveles numerados | Hasta **3 niveles** (1.1.1) | LIN §6 | ✅ `secnumdepth=2` |
| Capítulo | "1. Introducción y Planteamiento del Problema": 18 pt, negrita, alineado a la izquierda, sin la palabra "Capítulo" | TPL (estilo Título 1) | ✅ |
| Títulos preliminares sin número (Resumen, Índice General, Glosario, Bibliografía…) | 18 pt, negrita, izquierda | TPL (estilo Título 2) | ✅ |
| Sección | "1.1. Título": 14 pt, negrita | TPL (estilo Título 3) | ✅ |
| Subsección | "1.1.1. Título": 12 pt, negrita | TPL (estilo Título 5) | ✅ |
| Índice General | Título "Índice General", rótulo "Pág." a la derecha, con puntos guía | TPL | ✅ |
| Anexos | "Anexo I: Título", secciones "I.1. …"; numeración romana | TPL | ✅ |

## 6. Figuras, tablas y ecuaciones

| Regla | Valor exigido | Fuente | ¿Aplicada? |
|---|---|---|---|
| Numeración | Por capítulo: "Figura 4.3" = 3.ª figura del cap. 4; figuras y tablas con numeración independiente | LIN §6 | ✅ |
| Formato del título | "**Figura 2.2:** Modelo Conceptual del Sistema": rótulo en negrita, dos puntos, título normal | LIN §6 | ✅ |
| Fuente de leyendas (y de tablas) | Times New Roman **11 pt**; **negrita solo en el rótulo** | LIN §6 | ✅ (`\small` = 11 pt) |
| Posición del título de **tablas** | **Arriba** | LIN §6 | ✅ |
| Posición del título de **figuras** | **Abajo** | LIN §6 | ✅ |
| Referencia en el texto | Antes de que aparezca la figura/tabla, y lo más cerca posible | LIN §6 | ✅ regla de redacción (`[htbp]`) |
| Fuente de la imagen | Si no es propia: "Fuente: …" al final del título (ej. TPL Figura 1.1) | TPL | ✅ regla |
| Ecuaciones | Numeradas "(1.1)" a la derecha, por capítulo | TPL | ✅ |

## 7. Referencias bibliográficas

| Regla | Valor exigido | Fuente | ¿Aplicada? |
|---|---|---|---|
| Formato | **APA 7.ª edición** | LIN §6 | ✅ `biblatex` `style=apa` |
| Fuentes válidas | Solo libros editados, revistas especializadas, publicaciones institucionales y reportes técnicos con revisión comprobada | LIN §6 | ✅ regla |
| Cantidad (para nota máxima) | **≥ 15** referencias pertinentes, **≥ 10** de los últimos 10 años | RUB (Bibliografía) | control manual |
| Todas citadas | Toda referencia del listado debe estar citada en el texto y viceversa | RUB | ✅ `make revisar` |
| Título de la sección | "Bibliografía" | LIN §6, TPL | ✅ |

Ejemplos oficiales (LIN §6), ya cargados en `referencias.bib` como modelo:
- Libro: Suarez, L. E. (2014). *Análisis de Estructuras Con Cargas Dinámicas…* Createspace Independent Publishing Platform.
- Artículo: Zhou, Z., Zeng, Y., Zhou, X., He, X., & Ke, K. (2026). Performance-based plastic design… *Journal of Constructional Steel Research, 238*, 110206. https://doi.org/10.1016/j.jcsr.2025.110206
- Norma: Instituto Nacional de Normalización. (2009). NCh433:1996 Mod. 2009, Diseño sísmico de edificios. Santiago, Chile.
- Sitio web: Ministerio de Obras Públicas de Chile. (s.f.). Proyectos. Recuperado el 17 de marzo de 2026, de https://proyectos.mop.gob.cl/

⚠️ Detalle: los ejemplos oficiales usan "&" entre autores aunque el texto esté en español.
La plantilla está configurada con "&" para coincidir con esos ejemplos.

## 8. Portada y hoja de firmas

**Portada** (TPL p. 1, centrada):
logo UCM · UNIVERSIDAD CATÓLICA DEL MAULE / FACULTAD DE CIENCIAS DE LA INGENIERÍA / ESCUELA DE INGENIERÍA CIVIL (12 pt) ·
**TÍTULO** (14 pt, negrita, mayúsculas) · **NOMBRE APELLIDO1 APELLIDO2** (12 pt, negrita) ·
**PROFESOR GUÍA: NOMBRE** (12 pt, negrita) · "Proyecto de Título presentado en conformidad a los requisitos para obtener el título de Ingeniero/a Civil" · TALCA, MES AÑO.

**Hoja de firmas** (TPL p. 2): mismos encabezados + "Proyecto de título presentado en conformidad…" + título + nombre + profesor guía +
tabla **COMISIÓN EXAMINADORA / FIRMA** con 3 filas: "Dr. / Mg. / Sr." + PROFESOR GUÍA / PROFESOR DE COMISIÓN / PROFESOR DE COMISIÓN + línea para firma · TALCA, MES AÑO.

Datos a completar en `tesis/config/comandos.tex`.

## 9. Otras reglas del proceso

Ver `01_normativa/PROCESO_TITULACION.md` (plazos, comisión, veredictos, defensa) y
`01_normativa/RUBRICA.md` (cómo se evalúa el informe).

---

## Anexo: reglas del ANTEPROYECTO (distintas al informe final)

| Regla | Anteproyecto (LIN §5) |
|---|---|
| Contenido | Portada (Anexo 2 de LIN), Índice, Introducción (contexto, antecedentes, hipótesis/preguntas, objetivos, contribuciones), Metodología, Programación (**carta Gantt**), Bibliografía |
| Extensión | Máx. **15 páginas** de cuerpo principal |
| Niveles de numeración | Hasta **2** (1.1) |
| Encabezado | Nombre y número de **sección** |
| Entrega | Un archivo Word o PDF, en el LMS, a más tardar la **semana 12** |
| Resto | Igual al informe final (carta, Times 12, 1,5, márgenes 2,5/2,5/3/3, APA 7, figuras/tablas) |

## Anexo: Informe de PRÁCTICA (no aplica a la tesis)

`formato-informe-practica.docx`: márgenes distintos (sup. 2,5 / inf. 2 / der. 2 / izq. 3,5 cm), máx. 20 páginas,
estructura propia (resumen ejecutivo, organización, área, actividades…). **No usar para el Proyecto de Título.**
