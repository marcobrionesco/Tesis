# Receta 09 — Preparar una entrega (profesor guía o versión final)

## Lista de control
- [ ] `make limpiar && make pdf` compila sin errores ni advertencias de referencias indefinidas.
- [ ] `make revisar`: chktex limpio y **cero** citas fuera del `.bib`.
- [ ] Revisar la lista de `\pendiente{}` / `\revisar{}` que entrega `make revisar`.
- [ ] Cada regla de `REGLAS_FORMATO.md` marcada ✅.
- [ ] Resumen y abstract actualizados y dentro del límite de palabras (`make contar`).
- [ ] Simbología sincronizada con `GLOSARIO.md`.
- [ ] Todas las figuras vectoriales o con resolución ≥ 300 dpi.
- [ ] `make figuras` regenera exactamente las figuras de la tesis.

## Solo para la versión final
- [ ] Ocultar marcas: `\mostrarmarcasfalse` en `tesis/config/comandos.tex`.
- [ ] Quitar `\include{anexos/anexo_guia_plantilla}` de `main.tex` y borrar las referencias de ejemplo no usadas.
- [ ] Revisar portada letra por letra contra la normativa.

## Versionar la entrega
```bash
git tag -a v0.1-entrega-guia -m "Primera entrega al profesor guía"
git push origin v0.1-entrega-guia
```
Al subir una etiqueta, GitHub crea una *Release* con el PDF adjunto.
Para mostrar los cambios respecto a la entrega anterior: `make diff DESDE=v0.1-entrega-guia`.
