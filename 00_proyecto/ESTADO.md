# ESTADO — En qué va la tesis

> El "handoff". Lo primero que lee una IA nueva para saber qué hacer.
> Actualizar al final de **cada** sesión de trabajo.

**Última actualización:** 2026-11-19

## Estado general

- ✅ Estructura del repositorio y herramientas listas.
- ✅ Normativa ICV-611 (UCM) cargada, extraída (`01_normativa/REGLAS_FORMATO.md`, `RUBRICA.md`, `PROCESO_TITULACION.md`) y **aplicada** a la plantilla LaTeX.
- ⬜ Material previo del estudiante: aún no subido a `02_material_bruto/`.
- ⬜ `00_proyecto/CONTEXTO.md` sin completar (tema, objetivos, etapa).

## Estado por capítulo

Leyenda: ⬜ no iniciado · 🟨 material bruto (sin triaje) · 🟧 borrador en LaTeX · 🟦 en revisión · ✅ terminado

| Sección | Archivo | Peso rúbrica | Estado | Notas |
|---|---|---|---|---|
| Portada y hoja de firmas | `tesis/portada/` | (Formato 5 %) | 🟧 | Formato listo; faltan datos reales en `config/comandos.tex` |
| Agradecimientos | `tesis/preliminares/agradecimientos.tex` | — | ⬜ | Opcional |
| Resumen / Abstract | `tesis/preliminares/` | 5 % | ⬜ | Se escribe al final |
| Glosario | `tesis/preliminares/glosario.tex` | — | ⬜ | Si corresponde |
| 1. Introducción y Planteamiento del Problema | `capitulos/01_introduccion.tex` | 10 % | ⬜ | |
| 2. Marco Teórico / Estado del Arte | `capitulos/02_marco_teorico.tex` | 15 % | ⬜ | |
| 3. Metodología | `capitulos/03_metodologia.tex` | 20 % | ⬜ | |
| 4. Presentación de Resultados | `capitulos/04_resultados.tex` | 15 % | ⬜ | |
| 5. Discusión de Resultados | `capitulos/05_discusion.tex` | 15 % | ⬜ | |
| 6. Conclusiones | `capitulos/06_conclusiones.tex` | 5 % | ⬜ | |
| Bibliografía | `tesis/bib/referencias.bib` | 5 % | ⬜ | Solo ejemplos oficiales; meta ≥ 15 refs |
| Anexos | `tesis/anexos/` | — | ⬜ | Borrar `anexo_guia_plantilla.tex` antes de entregar |

## Próximos pasos (en orden)

1. [ ] Subir todo el material previo a `02_material_bruto/` (borradores, papers, datos, anteproyecto si existe).
2. [ ] Completar `00_proyecto/CONTEXTO.md` (tipo de proyecto, etapa actual, tema, objetivos).
3. [ ] Completar datos de portada en `tesis/config/comandos.tex` (nombre completo, profesor guía, comisión).
4. [ ] Triaje del material bruto (receta `02_triaje_material.md`).
5. [ ] Pasar lo rescatable a LaTeX, capítulo por capítulo (receta `04_borrador_a_latex.md`), priorizando Metodología (20 %).
6. [ ] Autoevaluar con la rúbrica (receta `10_autoevaluar_rubrica.md`) antes de cada entrega.

## Bloqueos / preguntas abiertas (para el profesor guía)

- **Orden de preliminares:** los Lineamientos ponen *Agradecimientos* antes del *Resumen*; el template Word los pone después del *Abstract*. Se usó el orden de los Lineamientos. ¿Cuál prefiere?
- **Nombres de capítulos 2, 3 y 5:** dependen del tipo de proyecto ("Estado del Arte" vs. "Marco Teórico"; "Materiales y Métodos" vs. "Metodología"; "Discusión" vs. "Análisis de Resultados"). Provisorio: Marco Teórico / Metodología / Discusión de Resultados.
- **Etapa:** si todavía falta entregar el **anteproyecto** (máx. 15 págs., con carta Gantt, encabezado por sección, 2 niveles), se puede generar una versión `main_anteproyecto.tex` a partir de la misma estructura.
- **Logo:** se usa el logo incluido en el template (139 px, baja resolución). Conviene pedir el logo oficial en alta resolución o vectorial.
