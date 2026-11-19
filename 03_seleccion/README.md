# 03_seleccion — "Logging" y selección de tomas

Aquí se decide qué del material bruto sirve. Es el paso que en edición
se hace antes de cortar: ver todo, marcar lo bueno, descartar lo malo.

| Subcarpeta | Qué va | Plantilla |
|---|---|---|
| `triaje/` | Evaluación de cada borrador previo: qué rescatar, qué reescribir, qué descartar | `triaje/_PLANTILLA_triaje.md` |
| `fichas_lectura/` | Una ficha por fuente (paper, libro, norma) — es lo que "lee" la IA como NotebookLM | `fichas_lectura/_PLANTILLA_ficha.md` |
| `notas/` | Ideas sueltas, esquemas, apuntes de reuniones | libre |

## Semáforo del triaje

- ✅ **Usar** — correcto y bien escrito, pasa casi directo a LaTeX.
- 🔧 **Reescribir** — la idea sirve pero hay errores, mala redacción o falta fuente.
- ❌ **Descartar** — incorrecto, irrelevante, repetido o inventado (p. ej. citas que no existen).
- ❓ **Verificar** — no se sabe si es correcto; requiere revisar fuente o preguntar al profesor.

## Fichas de lectura

Nombre: `apellido-año-palabraclave.md`, igual que la clave en `referencias.bib`.
Ej.: `chopra-2017-dinamica.md` ↔ `@book{chopra2017dinamica, ...}`
