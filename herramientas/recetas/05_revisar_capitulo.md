# Receta 05 — Revisión completa de un capítulo

**Entrada:** un archivo `tesis/capitulos/NN_*.tex`.
**Salida:** informe de revisión en `03_seleccion/notas/revision_capNN_AAAA-MM-DD.md` y, si el usuario aprueba, correcciones aplicadas.

Revisar en **cuatro pasadas separadas** (como en edición: corte, sonido, color, títulos):

## Pasada 1 — Contenido técnico
- ¿Cada afirmación técnica es correcta y tiene fuente?
- ¿Los valores numéricos coinciden con las fuentes y con `04_analisis`?
- ¿Se usa la versión vigente de las normas?
- ¿El capítulo cumple su función dentro de la tesis (ver `CONTEXTO.md`)?

## Pasada 2 — Estructura y argumento
- ¿Hay hilo lógico entre secciones? ¿Cada sección abre y cierra?
- ¿Hay repeticiones con otros capítulos?
- ¿Los objetivos específicos se abordan donde corresponde?

## Pasada 3 — Redacción
- Registro académico, sin muletillas ni relleno ("cabe destacar", "es importante mencionar").
- Párrafos de una idea; oraciones de menos de ~35 palabras.
- **Tercera persona** en todo el texto (exigido por la normativa ICV-611).
- Ortografía y tildes; términos en inglés en cursiva.

## Pasada 4 — Formato LaTeX y normativa
- `make revisar` sin errores; ninguna cita fuera del `.bib`.
- Unidades con `siunitx`, símbolos según `GLOSARIO.md`.
- Toda figura/tabla citada en el texto con `\cref`; leyendas con fuente si no es propia.
- Cumplimiento de `REGLAS_FORMATO.md`.

## Pasada 5 — Rúbrica oficial
- Comparar el capítulo con su criterio en `01_normativa/RUBRICA.md` y estimar el puntaje (0–4).

**Formato del informe:** tabla con `línea | problema | gravedad (alta/media/baja) | corrección propuesta`.
No aplicar cambios grandes sin aprobación del usuario.
