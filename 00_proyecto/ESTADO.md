# ESTADO — En qué va la tesis

> El "handoff". Lo primero que lee una IA nueva para saber qué hacer.
> Actualizar al final de **cada** sesión de trabajo.

**Última actualización:** 2026-11-19

## Estado general

- ✅ Estructura del repositorio, herramientas y normativa ICV-611 aplicada a la plantilla.
- ✅ Versión 3.0 de la tesis (la que se envió al profesor guía) **ingresada**, **triada** y **migrada** a la plantilla.
  - Triaje: `03_seleccion/triaje/2026-11-19_triaje_proyecto-titulo-v3.0.md`
  - Autoevaluación con rúbrica: `03_seleccion/notas/autoevaluacion_2026-11-19_v3.0.md` (≈ 50 %, veredicto probable "revisiones mayores")
- ✅ Correcciones objetivas aplicadas en la migración (bibliografía, signo de ecuación, unidades, redacción, figura 2.1 redibujada, planos dentro del margen).
- 🟧 El PDF compila sin errores; contiene **marcas `\revisar{}` (naranja) y `\pendiente{}` (rojo)** con todo lo que falta. Verlas con `make revisar`.
- ✅ 4 ejemplos analizados en `05_ejemplos/` (3 tesis UCM + 1 memoria de cálculo), con fichas. **Hallazgos clave** (ficha de Guerrero, 2024):
  - NTK típico en Chile: 20–120 mg/L (Vera et al., 2016); el diseño usa 1–1,5 mg/L → con 50 mg/L, OI/OD baja de 2,8 a ≈ 1,17.
  - Carga orgánica máxima en humedales verticales: 20–27 g DQO/m²·d (Dotro et al.); el diseño usa 30. Carga hidráulica máx. 80–120 L/m²·d (DWA); el diseño usa 125.
  - Fuente nueva verificada para la introducción: Vera-Puerto et al. (2022), *Water* 14(4), 627.
  - La memoria de cálculo de ejemplo es el modelo para completar los resultados estructurales (OE2).
- ⬜ Faltan las **observaciones escritas del profesor guía** (pedírselas o transcribirlas a `03_seleccion/notas/`).

## ⚠️ Documentos oficiales recibidos (2026-11-19)

Inscripción visada, propuesta ANID, correo del guía y documentos de diseño del proyecto → `01_normativa/proyecto/`.
**El alcance oficial está en `01_normativa/proyecto/ALCANCE.md`.** Consecuencias:
- Objetivos reemplazados por los inscritos (instrucción del guía).
- Tesis **solo de diseño**; el diseño de proceso del humedal (balance de O₂, 6 m², 30 g DQO/m²·d = Fase 1) es **insumo del proyecto**, no un error del autor.
- Caudal de oficinas (150 L/d): **resuelto** por correo del guía.
- Norma de reúso: la propuesta ANID cita **NCh3456 (INN, 2022)**; pedir título exacto.
- Preguntas para la próxima reunión: `00_proyecto/OBSERVACIONES_PROFESOR.md`.

## ✅ Recibidos y procesados (2026-11-19, tarde)

- **Datos de caracterización** (6 campañas, 5 puntos, 18 parámetros) → `04_analisis/` → tabla 4.1 y figura 4.1. QA: los promedios del original son correctos.
- **Láminas 3.1–3.2 en PDF**, **itemizado** (tabla, anexo II) y **EETT** (anexo VI).
- Perfiles de la plataforma confirmados (C2 resuelto). Nuevas inconsistencias C12–C15 (ver triaje §8 y OBSERVACIONES_PROFESOR, preguntas 8–11).

## ✅ Cálculos del autor recibidos y verificados (2026-11-20)

- Scripts originales (estructura, bombas, excavación) + documento de resultados → `02_material_bruto/calculos_originales/`.
- Versiones actualizadas y reproducibles en `04_analisis/scripts/10_`–`12_`, con las dimensiones finales.
  Tablas preliminares en Resultados: ADT por línea (tabla 4.7) y verificación estructural (tabla 4.8).
- **Hallazgos**: tablero 15 mm no cumple; zapata con sismo depende del reparto del corte; placa base al límite;
  línea del estero inviable con PVC 25 mm; zanja 3 con tapada insuficiente; 10 diferencias entre la BD y el resumen.
- Discusión y Conclusiones citan valores del cálculo antiguo (perfil 250×250): marcados para actualizar.
- Documento "CO" recibido: es la carta oferta para el contratista (sin medidas). Medidas finales = planos + EETT + itemizado Rev. 1.
- Bombas: no están en el itemizado (las provee el proyecto, según EETT); la selección debe proponerse en la tesis.

## Estado por capítulo

Leyenda: ⬜ no iniciado · 🟨 material bruto · 🟧 borrador en LaTeX · 🟦 en revisión · ✅ terminado

| Sección | Archivo | Peso | Estado | Lo que falta (ver triaje) |
|---|---|---|---|---|
| Portada y firmas | `tesis/portada/` | Formato 5 % | ✅ | Nombres de los 2 integrantes de la comisión |
| Agradecimientos | `preliminares/agradecimientos.tex` | — | ✅ | — |
| Resumen / Abstract | `preliminares/` | 5 % | 🟧 | Datos cuantitativos (al final) |
| Glosario | `preliminares/glosario.tex` | — | 🟧 | Sigla OD duplicada |
| 1. Introducción | `capitulos/01_introduccion.tex` | 10 % | 🟧 | Preguntas de investigación, contribuciones, alcances, datos cuantitativos |
| 2. Marco Teórico | `capitulos/02_marco_teorico.tex` | 15 % | 🟧 | **Estado del arte crítico con literatura 2016–2026**; fuentes de C y K; norma de combinaciones |
| 3. Metodología | `capitulos/03_metodologia.tex` | 20 % | 🟧 | Diagrama + entregables; datos de monitoreo; zona sísmica; fuentes (2 %, L/300) |
| 4. Resultados | `capitulos/04_resultados.tex` | 15 % | 🟧 | **ADT/bombas; verificación LRFD; presiones de contacto; líneas estero y agroquímicos; NTK** |
| 5. Discusión | `capitulos/05_discusion.tex` | 15 % | 🟧 | Unificar perfiles y zona; comparar con literatura |
| 6. Conclusiones | `capitulos/06_conclusiones.tex` | 5 % | 🟧 | Limitaciones y trabajo futuro; apoyar en resultados propios |
| Bibliografía | `bib/referencias.bib` | 5 % | 🟧 | 27 refs; 4 por verificar; sumar artículos recientes |
| Anexos I–V | `tesis/anexos/` | — | 🟧 | Láminas 3.1–3.2 en PDF vectorial; itemizado como tabla |

## Próximos pasos (en orden de impacto)

1. [ ] **Pedir/transcribir las observaciones del profesor guía** y cruzarlas con el triaje.
2. [ ] **Resolver inconsistencias**: zona sísmica (C3), columnas de la tabla de riego, hormigón G25/G30 (C12), capas filtrantes y cantidades (C13), criterio de caudal del estero y agroquímicos; cómo presentar el diseño de proceso del humedal.
3. [ ] **Completar Resultados con los entregables inscritos** (`ALCANCE.md`): datos de caracterización de las 3 fuentes, tiempos de retención, zanjas, especificaciones; y (C1, C6): ADT y bombas, verificación LRFD, corte basal, presiones de contacto, líneas estero/agroquímicos. Modelos: anexo de impulsión de Guerrero (2024) y memoria de cálculo de `05_ejemplos/memorias_calculo/`.
4. [ ] **Reforzar Marco Teórico** con literatura reciente (receta 07 + fichas con receta 03).
5. [ ] **Completar Introducción** (preguntas, contribuciones, alcances) y **Conclusiones** (limitaciones, trabajo futuro).
6. [ ] Verificar las 4 referencias marcadas "VERIFICAR" en `referencias.bib`.
7. [ ] Al final: Resumen con cifras (máx. 1 página), autoevaluación (receta 10), entrega (receta 09).

## Bloqueos / preguntas abiertas (para el profesor guía o el co-guía)

- ¿Cuáles fueron sus observaciones concretas a la v3.0?
- **Perfiles definitivos** de la plataforma: ¿150×150×6 / 150×100×3 o 250×250×6 / 150×50×3?
- **Zona sísmica** de Linares y **versión de NCh2369** a usar (2003 vs. 2023).
- ¿Contenido de estanques como carga viva o de operación? ¿Combinaciones de NCh3171 o de NCh2369?
- **NTK** de las aguas servidas: ¿los 1–1,5 mg/L son datos de monitoreo reales?
- **Norma de reúso**: ¿existe otra además de la NCh1333 (la v2.0 citaba "NCh3456")?
- Origen de la **capacidad admisible de 150 kPa**.
- Orden de preliminares (Agradecimientos antes del Resumen, según Lineamientos) — sigue pendiente.
