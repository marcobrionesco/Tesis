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

## 2026-11-20 — Sin preguntas de investigación

- **Decisión:** se elimina la sección "Preguntas de investigación" del cap. 1. **Motivo:** el profesor guía indicó explícitamente
  que no es necesaria (prevalece sobre la sugerencia de los Lineamientos §6). La discusión y las conclusiones se organizan por los
  tres objetivos específicos aprobados (VF-V2).

## 2026-11-20 — Criterio sísmico de la plataforma (pregunta 1, propuesta aprobada por el autor)

- **Decisión:** NCh2369:2025 (2003 solo como antecedente); categoría de ocupación I (I = 0,8); marco a momento soldado sin anclajes
  dúctiles, R = 3, ξ = 0,02; suelo C supuesto (sin mecánica de suelos) y q_adm = 150 kPa; tablero + vigas como diafragma (6 pilares).
- **Resultado:** zapata 1,0 × 1,0 × 0,5 m con 91 % de área apoyada (mínimo 80 %); sin diafragma vuelca; con categoría II y suelo C, 76 %.
- **Motivo:** la versión de la norma no cambia el veredicto; deciden el diafragma y la categoría. Cálculo: `04_analisis/scripts/14_sismo_2003_vs_2025.py`.
- **Pendiente:** justificar el diafragma (conexión tablero-vigas), recalcular pilares y placa base con el espectro 2025, verificar 0,9D + 1,4E. A confirmar con el profesor.

## 2026-11-20 — Respuestas del autor a las preguntas 2–7, 9–11, 15, 16 y 18 (aprobadas)

Detalle: `03_seleccion/notas/2026-11-20_respuestas-preguntas-autor.md`. Pendientes de visto bueno: 8 (nitrógeno) y 12 (dosificadores).

- **P2 Tablero:** vigas secundarias cada 0,40 m y tablero de 15 mm son fijos. El tablero se modela como lámina continua (3 apoyos = diseño):
  1,21 mm frente a 1,33 mm (L/300, razón 0,91); L/500 solo referencia. E = 11 GPa (pino radiata, supuesto) y k_def = 2,0 (EN 1995-1-1, clase de servicio 3; falta citar la norma).
- **P3/P4 Bombas:** llenado de 1000 L en ≤ 60 min (30 min deseable); cota de llegada única 125,27 m (corregir lámina 2.4); desniveles 13,82 / ≈ 6,4 / ≈ 8,6 m
  (nivel en fosas 2 m bajo la tapa, supuesto); misma bomba periférica supuesta Pedrollo JSWm 1A (0,55 kW) en las tres líneas: 36 / 25 / ≤ 17 min. Estero sigue en PVC 25.
- **P5 Caudales:** 750 L/d en cada línea (125 mm/d); líneas = doméstica (casa + oficinas), agroquímicos (AGR1 + AGR2), estero; déficit completado con agua del estero;
  DQO de la mezcla ≤ 240 mg/L para no superar 30 g DQO/m²·d. Se abandona "igual carga orgánica".
- **P6 Oficinas y TRH:** aforo volumétrico (0,92 L, cronómetro, 3 aperturas, media); WC 9,1 L (fabricante); semanas 01S4 y 02S1–02S4; TRH por unidad de la cadena
  (almacenamiento 1000 L, dosificador 200 L con 6 pulsos de 125 L, lecho, cloración 100 L, acopio 3250 L); porosidad y pulsos supuestos.
- **P7 Caracterización:** mandan los 6 informes del Laboratorio del Agua UCM (`02_material_bruto/laboratorio/`); muestras puntuales; semana 1 de AS1 y AS2 atípica
  (se excluye de las medias, se informa aparte); coliformes TOTALES; métodos no informados. Base reconstruida con `00_laboratorio_a_csv.py`.
- **P9:** hormigón de zapatas G25 (EETT e itemizado corregidos). **P10:** capas de la lámina 2.2 (grava 19 / arena 0,60 / gravilla 12); itemizado: arena 12 m³, gravas 3 m³.
- **P11 Zanjas:** trayectos modificados en terreno; la tesis no presenta excavaciones, solo criterios (`12_excavacion.py` queda fuera de la tesis).
- **P15 Fase 2:** se dimensiona para la Fase 1; Fase 2 = 3 IBC por línea (recomendada) o 1500 L/d. **P16:** orden de los Lineamientos y Discusión aparte.
- **P18:** se elimina la afirmación de que el nitrato es la forma "más usada"; solo asimilación de 0,2–0,8 g N/m²·d (Dotro et al., 2021).
