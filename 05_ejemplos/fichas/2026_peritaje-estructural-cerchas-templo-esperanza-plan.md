# Ejemplo: Memoria de cálculo — Peritaje estructural de cerchas, templo Esperanza Plan (2026)

- **Archivo:** `05_ejemplos/memorias_calculo/2026_peritaje-estructural-cerchas-templo-esperanza-plan.pdf` (52 págs.; texto en `.md` al lado)
- **Tipo:** memoria de cálculo profesional / peritaje (Anexo 2 de un informe; código "MC-Esperanza Plan", 20-10-2026)
- **Tema:** verificación de cerchas de madera con modelo en ETABS, cargas según normas chilenas, verificación según NCh1198:2024 y diagnóstico de falla.
- **Relación con mi tesis:** **ALTA para el objetivo específico 2** (estructuras): es el modelo de cómo presentar un cálculo estructural completo, que es justo lo que falta en mi capítulo de resultados (C1 del triaje).
- **¿Es fuente citable?** No para mi tesis (es un informe técnico sin revisión editorial y de otro tema). Úsala como modelo; cita las normas originales.

## Qué hace bien (imitar la forma, no el texto)

| Aspecto | Dónde (pág. PDF) | Cómo aplicarlo en mi tesis | Archivo destino |
|---|---|---|---|
| **Secuencia completa del cálculo**: geometría → materiales → cargas → combinaciones → modelo → resultados → verificación → discusión → conclusiones | Índice (p. 2–3) | Ordenar mi §3.2 (metodología) y §4.2 (resultados) con esta misma secuencia para la plataforma | `03_metodologia.tex`, `04_resultados.tex` |
| **Combinaciones de carga citadas desde la NCh3171**, listadas y con cada símbolo definido | §7.1 (p. 21) | Confirma la observación T3: citar NCh3171 para las combinaciones y definir D, L, E | `02_marco_teorico.tex` (tabla 2.2) |
| **Cuantificación de cargas permanentes** componente por componente, con la fuente de cada peso (proveedor, norma) | §7.1–7.2 (p. 22–24) | Tabla de carga muerta de la plataforma (perfiles A270ES, tableros fenólicos, estanques vacíos) con fuente de cada valor | `04_resultados.tex` |
| **Tabla de esfuerzos por elemento** extraída del software (P, V, M), destacando los más solicitados | Tabla 9-1 (p. 33–34) | La tabla que falta: $P_u$, $V_u$, $M_u$ por elemento de la plataforma (vigas, costaneras, columnas) | `04_resultados.tex` |
| **Figura del modelo con nombres de elementos** y tabla que traduce el nombre del software a la función | Fig. 16, Tabla 8-1 (p. 31–32) | Figura del modelo de la plataforma con etiquetas (V1, C1, …) y tabla de elementos | `04_resultados.tex` |
| **Verificación por tipo de esfuerzo**, cada una con criterio, fórmula, valores y "cumple / no cumple" | §10.1–10.5 (p. 37–48) | Verificación LRFD por elemento: flexión, corte, compresión y flexocompresión (H1-1 de AISC 360) con razón de demanda/capacidad | `04_resultados.tex` |
| **Discusión que interpreta la causa física** de los resultados (por qué fallan, dónde se concentran los esfuerzos) | §11 (p. 48) | Discutir por qué la plataforma trabaja con razones bajas (rigidez, sifones, *sloshing*) con los valores ya presentados | `05_discusion.tex` |
| **Conclusiones numeradas y concretas** | §12 (p. 49) | Una conclusión numerada por objetivo/verificación | `06_conclusiones.tex` |

## Qué NO imitar

- Mezcla de unidades técnicas (kgf, kgf·cm): en la tesis usar **SI** con `siunitx` (kN, kN·m, MPa).
- Numeración de secciones repetida (dos "7.1", dos "4.1"): en LaTeX la numeración es automática.
- Formato de informe de empresa (encabezado "MC-…", "Página I | 52"): la tesis sigue el template UCM.

## Diferencias con mi caso

- Es ASD en madera (NCh1198); mi plataforma es **LRFD en acero** (NCh427/1, AISC 360) con sismo (NCh2369). La estructura del documento sí es transferible.
- No considera sismo; en mi caso es una carga determinante (corte basal, momento volcante).
