# AGENTS.md — Instrucciones para cualquier IA que trabaje en esta tesis

> Este archivo es el **punto de entrada**. Si eres una IA (Claude, ChatGPT, Gemini,
> Copilot, NotebookLM, etc.), léelo completo antes de hacer cualquier cosa.
> Los humanos también pueden leerlo: es el "manual de la sala de edición".

## 1. Qué es este repositorio

Tesis de **Ingeniería Civil** de Marco Briones, escrita en **LaTeX**.
El repositorio está organizado como un proyecto de edición de video:
material bruto entra por un lado, se clasifica, se trabaja y sale un
único "master" final (el PDF de la tesis).

## 2. Orden de lectura obligatorio (antes de trabajar)

1. `AGENTS.md` (este archivo) — reglas y mapa.
2. `00_proyecto/CONTEXTO.md` — de qué trata la tesis (tema, pregunta, objetivos).
3. `00_proyecto/ESTADO.md` — en qué va el trabajo y qué toca hacer ahora.
4. `01_normativa/REGLAS_FORMATO.md` — reglas de la universidad (mandan sobre todo).
5. `00_proyecto/DECISIONES.md` — decisiones ya tomadas (no reabrirlas sin motivo).
6. Solo entonces, los archivos específicos de la tarea.

## 3. Mapa del repositorio (flujo tipo edición de video)

| Carpeta | Equivalente en video | Qué contiene | ¿Se edita? |
|---|---|---|---|
| `00_proyecto/` | Preproducción / guion | Contexto, estado, plan, decisiones, glosario, bitácora | Sí |
| `01_normativa/` | Specs de entrega del canal | Instrucciones de formato de la universidad | `originales/` **NUNCA**; `REGLAS_FORMATO.md` sí |
| `02_material_bruto/` | Ingesta / rushes | Todo lo generado antes (bueno y malo), papers, datos crudos | **NUNCA se modifica**, solo se agrega |
| `03_seleccion/` | Logging / selección de tomas | Fichas de lectura, triaje de borradores, notas de investigación | Sí |
| `04_analisis/` | Efectos / VFX / color | Código (Python), cálculos, notebooks, scripts que generan figuras | Sí |
| `tesis/` | **Timeline / master** | SOLO el LaTeX final que va al PDF | Sí, con cuidado |
| `herramientas/` | Plugins / presets / scripts | Scripts y recetas (prompts) reutilizables | Sí |
| `salida/` | Exportaciones / render | PDFs compilados (no se versiona, lo genera la CI) | No |

**Flujo de trabajo** (como en edición: ingesta → selección → corte → afinado → export):

```
02_material_bruto  →  03_seleccion  →  tesis/ (borrador)  →  revisión  →  salida/tesis.pdf
   (ingesta)          (triaje/fichas)   (corte bruto)       (corte fino)    (master)
                           ↑
                     04_analisis (cálculos y figuras alimentan la tesis)
```

## 4. Reglas que NO se rompen

1. **Nunca inventar referencias.** Toda cita `\cite{...}` debe existir en
   `tesis/bib/referencias.bib` y corresponder a una fuente real (idealmente con DOI).
   Si no hay fuente, escribe `\pendiente{falta fuente: ...}` en vez de inventar.
2. **Nunca inventar datos, resultados ni valores de normas.** Si falta un dato,
   marcarlo con `\pendiente{...}`.
3. **No modificar** `01_normativa/originales/` ni `02_material_bruto/`. Son la
   "cinta original". Lo que se rescate de ahí se reescribe en `03_seleccion/` o `tesis/`.
4. **La normativa de la universidad manda** sobre cualquier preferencia de estilo.
5. **Al terminar una sesión**, actualizar `00_proyecto/ESTADO.md` y agregar una
   entrada en `00_proyecto/BITACORA.md` (qué se hizo, qué quedó pendiente).
6. Las decisiones importantes (estructura, norma de citas, enfoque metodológico)
   se registran en `00_proyecto/DECISIONES.md`.
7. Escribir en **español**, registro académico, impersonal o primera persona
   plural según `REGLAS_FORMATO.md`.
8. La tesis debe **compilar** después de cada cambio (`make pdf`). Si no puedes
   compilar, dilo explícitamente.

## 5. Convenciones LaTeX

- Un archivo por capítulo en `tesis/capitulos/NN_nombre.tex`.
- Etiquetas con prefijo: `cap:`, `sec:`, `fig:`, `tab:`, `ec:`, `anx:`.
  Ej.: `\label{fig:perfil-suelo}`. Referenciar con `\cref{...}`.
- Unidades **siempre** con `siunitx`: `\qty{25}{\mega\pascal}`, `\unit{\kilo\newton\per\meter}`.
- Comandos propios en `tesis/config/comandos.tex` (no definir comandos dentro de capítulos).
- Figuras en `tesis/figuras/` (las generadas por código salen de `04_analisis/`).
- Marcas de trabajo: `\pendiente{...}` (falta algo) y `\revisar{...}` (dudoso).
  Se pueden ocultar todas para la versión final cambiando una línea en `comandos.tex`.
- Una oración por línea en el `.tex` (facilita ver diferencias en Git).

## 6. Cómo compilar

```bash
make pdf        # compila tesis/main.tex → salida/tesis.pdf
make vigilar    # recompila automáticamente al guardar
make revisar    # chktex: errores típicos de LaTeX
make contar     # cuenta palabras por capítulo
make contexto   # genera salida/contexto_completo.md para subir a otra IA / NotebookLM
make limpiar    # borra archivos auxiliares
```

En GitHub, cada `push` compila el PDF automáticamente (pestaña *Actions* → artefacto `tesis-pdf`).

## 7. Recetas (prompts reutilizables)

En `herramientas/recetas/` hay instrucciones paso a paso para tareas
recurrentes (triaje de borradores, revisar un capítulo, verificar
ecuaciones, pasar un borrador a LaTeX, buscar bibliografía...). Si el
usuario pide una de esas tareas, **sigue la receta correspondiente**.

## 8. Herramientas y lenguajes

Ver `herramientas/HERRAMIENTAS.md`: catálogo de "lenguajes especiales"
(LaTeX, BibLaTeX, TikZ, SymPy, Pandoc, Mermaid, etc.) y para qué sirve cada uno.
