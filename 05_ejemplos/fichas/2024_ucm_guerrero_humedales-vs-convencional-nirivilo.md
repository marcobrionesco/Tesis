# Ejemplo: Guerrero (2024) — Lodos activados vs. humedal vertical, Nirivilo

- **Archivo:** `05_ejemplos/tesis/2024_ucm_guerrero_humedales-vs-convencional-nirivilo.pdf` (129 págs.; texto en `.md` al lado)
- **Tipo:** Proyecto de Título, Ingeniería Civil UCM, junio 2024 (aprobado)
- **Autora / guía:** Jera A. Guerrero Méndez / **Dr. Ismael L. Vera Puerto** (mismo guía que esta tesis). Comisión: Vera, Quiroz, Valenzuela.
- **Tema:** diseño y comparación de costos de una planta de lodos activados (aireación extendida) y un humedal construido vertical para 432 habitantes rurales.
- **Relación con mi tesis:** **ALTA** — mismo guía, misma tecnología (humedal vertical), mismo método (balance de oxígeno de Platzer), bombas de impulsión, normativa chilena.
- **¿Es fuente citable?** Es una tesis de pregrado: se puede usar como antecedente, pero los **datos y criterios deben citarse desde su fuente original** (Dotro et al., Vera et al., DWA, ÖNORM).

> Nota: las páginas indicadas son las del PDF unido (= número de página impreso + 14 aprox.).

## ⚠️ Hallazgos que afectan directamente mi diseño

| # | Hallazgo | Dónde (pág. PDF) | Impacto en mi tesis |
|---|---|---|---|
| H1 | **NTK de diseño = 50 mg/L**, tomado de Vera et al. (2016), que reporta para aguas servidas en Chile NT de 20–120 mg/L y amonio (NH₄⁺) de 12–100 mg/L. | Tabla 2.1 (p. 22), Tabla 3.2 (p. 39) | Confirma el problema **C4** del triaje: mi NTK de 1–1,5 mg/L está fuera de rango por 1 a 2 órdenes de magnitud. La fuente (Vera et al., 2016) **ya está en mi bibliografía** y es del profesor guía. |
| H2 | **Parámetros de diseño de humedales verticales** (Dotro et al., 2021, ed. en español de *Treatment Wetlands*): carga orgánica **máxima 20 g DQO/m²·d (Alemania, Austria) y 27 (Dinamarca)**; área específica 3–4 m²/hab-eq; arena 0,06–4 mm, profundidad ≥ 50–100 cm. | Tabla 3.6 (p. 55) | Mi diseño usa **30 g DQO/m²·d**, **sobre** el máximo de las tres guías, y la discusión lo llama "conservador". |
| H3 | Carga hidráulica superficial **máx. 80–120 L/m²·d** según DWA (2017); intervalos de alimentación ≥ 6 h (DWA) o 3–6 h (ÖNORM); 8–12 pulsos/día (guía danesa). | p. 54–55 | Mi diseño usa **125 mm/d = 125 L/m²·d** (sobre el rango) y 6 cargas/día. |
| H4 | Usa **eficiencias y recuperación por desnitrificación** explícitas: 0,7 g O₂/g DQO; 4,3 g O₂/g NTK; **2,9 g O₂/g N desnitrificado**; eliminación DQO 85 %, NTK 90 %, desnitrificación 10 %. | Tabla 4.7 (p. 76) | Modelo para presentar mis supuestos en una tabla; yo desprecié la desnitrificación sin cuantificarla. |

### Cálculo ilustrativo de sensibilidad (NO es un resultado de la tesis)

Con mi mismo método y supuestos, cambiando solo el NTK a 50 mg/L (valor usado por Guerrero con Vera et al., 2016):

| | NTK 1–1,5 mg/L (v3.0) | NTK 50 mg/L (ilustrativo) |
|---|---|---|
| Carga NTK | 1,1 g/d | 0,75 m³/d × 50 g/m³ = **37,5 g/d** |
| OD nitrificación (4,3 g O₂/g NTK) | 4,7 g/d | **161,3 g/d** |
| OD total (+107,1 por DQO) | 111,8 g/d | **268,4 g/d** |
| OI con 6 m² y 6 cargas | 315 g/d | 315 g/d |
| OI/OD | 2,8 | **1,17** |

→ El balance de oxígeno probablemente **sigue cumpliendo**, pero el "amplio margen" desaparece.
Y por carga orgánica (H2), con 180 g DQO/d el área sería **9 m² a 20 g/m²·d** o **6,7 m² a 27 g/m²·d** (hoy: 6 m²).
**Decisión del autor con el profesor guía:** usar datos reales de monitoreo; verificar los límites en la fuente original
(Dotro et al., 2017; DWA-A 262; ÖNORM B 2505) y, si se confirman, redimensionar o justificar la excepción.

## Qué hace bien (imitar la forma, no el texto)

| Aspecto | Dónde | Cómo aplicarlo en mi tesis | Archivo destino |
|---|---|---|---|
| Tabla de **concentraciones típicas en Chile** con fuente | Tabla 2.1 (p. 22) | Tabla de caracterización de los afluentes con rango de literatura vs. valor de diseño | `02_marco_teorico.tex` / `04_resultados.tex` (tabla 4.3) |
| Tabla de **consideraciones de diseño** (supuestos) separada de la tabla de **resultados de diseño** | Tablas 4.7 y 4.8 (p. 76–77) | Separar "supuestos del balance de O₂" (coeficientes, eficiencias, cargas máximas) de "resultados del balance" | `04_resultados.tex` (tabla 4.5) |
| **Comparar con criterios internacionales** en una tabla (DK / DE / AT) | Tabla 3.6 (p. 55) | Tabla en el marco teórico con criterios de diseño de HCFV, y en la discusión comparar mis valores contra ella | `02_marco_teorico.tex`, `05_discusion.tex` |
| Cada sección de metodología y de resultados **etiquetada por objetivo específico** | Índice (p. 8–10) | Ya lo hago; mantenerlo | — |
| **Planos simplificados propios** (planta y elevación) dentro de Resultados, y planos completos en anexos | Figs. 4.1–4.18 | Agregar a Resultados 1–2 figuras simplificadas del humedal y la plataforma, con referencia a las láminas del anexo | `04_resultados.tex` |
| **Cálculo de impulsión** en anexo (pérdidas, ADT, curva de bomba) con resumen en el texto | Anexo, Figs. 5.2–5.6 (p. 103–115) | Modelo para mi resultado faltante de ADT y bombas (C1) | `04_resultados.tex`, anexo nuevo |
| Introducción con dato duro reciente: **cobertura rural del 10 %** (Vera-Puerto et al., 2022) | p. 15 | Citar Vera-Puerto et al. (2022) — ver referencias útiles | `01_introduccion.tex` |

## Referencias útiles que cita (verificar y citar desde el original)

| Referencia | Para qué me sirve | Estado |
|---|---|---|
| **Vera-Puerto, I., Valdés, H., Bueno, M., Correa, C., Olave, J., Carrasco-Benavides, M., Schiappacasse, F., & Arias, C. A. (2022).** Reclamation of treated wastewater for irrigation in Chile: Perspectives of the current state and challenges. *Water, 14*(4), 627. https://doi.org/10.3390/w14040627 | **Clave para mi introducción y marco teórico**: estado del reúso para riego en Chile (reúso directo < 1 % del caudal tratado; brechas regulatorias). Es del profesor guía y reciente. | ✅ verificado (MDPI) |
| Dotro et al. (2021). *Humedales para tratamiento* (ed. en español de *Treatment Wetlands*, IWA) | Tabla de criterios de diseño de humedales verticales (H2) | Usar la ed. que se consulte; ya cito la de 2017 |
| Arias & Brix (2003). *Humedales artificiales para el tratamiento de aguas residuales* | Antecedente en español | ❓ verificar datos de publicación |
| von Sperling (2007). *Basic principles of wastewater treatment* (IWA) | Caracterización de aguas residuales | ❓ verificar |

## Qué NO imitar

- **Su bibliografía tiene los mismos errores que había en mi v3.0** (Cohen-Shacham "2019", "NCh1333: Agua – vocabulario (2002)", referencias no citadas como Arceivala, Batterman, Giles, Hutton, Prat, SISS, Striebig, Torres). **Mi bibliografía de la v3.0 venía en gran parte de aquí**: no volver a copiar referencias de otra tesis sin verificarlas en la fuente.
- Solo ~9 de ~35 referencias son de los últimos 10 años: la rúbrica actual exige ≥ 10 recientes.
- Resumen de **2 páginas** (la normativa actual exige máx. 1).
- Une "Análisis y Resultados" y no tiene capítulo de Discusión: los lineamientos actuales piden **Resultados** y **Discusión** por separado.
- Incluye en el resumen frases generales sin datos ("El agua residual... presenta una composición variada y compleja").

## Diferencias de formato con la normativa UCM actual

- Índice General sin "Glosario"; mi plantilla sigue los lineamientos 2026.
- Leyendas "elaboración propia" al final con coma; la normativa usa "Figura N.N: Título" (y yo uso "Fuente: elaboración propia.").
