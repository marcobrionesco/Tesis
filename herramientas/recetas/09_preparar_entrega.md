# Receta 09 — Preparar una entrega (profesor guía o versión final)

## Lista de control
- [ ] `make limpiar && make pdf` compila sin errores ni advertencias de referencias indefinidas.
- [ ] `make revisar`: chktex limpio y **cero** citas fuera del `.bib`.
- [ ] Revisar la lista de `\pendiente{}` / `\revisar{}` que entrega `make revisar`.
- [ ] Cada regla de `REGLAS_FORMATO.md` marcada ✅ (Formato: 1 sola falta ya baja el puntaje).
- [ ] `make revisar` → extensión: cuerpo ≤ 80 páginas, resumen ≤ 1 página, 3–5 palabras clave.
- [ ] ≥ 15 referencias, ≥ 10 de los últimos 10 años; solo fuentes válidas según lineamientos.
- [ ] Datos de portada y hoja de firmas completos en `tesis/config/comandos.tex` (nombre completo, guía, comisión, fecha).
- [ ] Autoevaluación con la rúbrica (receta 10) sin criterios bajo 3.
- [ ] Resumen (máx. 1 página, con datos cuantitativos) y Abstract actualizados.
- [ ] Simbología sincronizada con `GLOSARIO.md`.
- [ ] Todas las figuras vectoriales o con resolución ≥ 300 dpi.
- [ ] `make figuras` regenera exactamente las figuras de la tesis.

## Solo para la versión final
- [ ] Ocultar marcas: `\mostrarmarcasfalse` en `tesis/config/comandos.tex`.
- [ ] Verificar que no queden marcas `\pendiente{}` ni `\revisar{}` (`make revisar`) y que todas las referencias marcadas "VERIFICAR" en `referencias.bib` estén confirmadas.
- [ ] Revisar portada letra por letra contra la normativa.

## Versionar la entrega
```bash
git tag -a v0.1-entrega-guia -m "Primera entrega al profesor guía"
git push origin v0.1-entrega-guia
```
Al subir una etiqueta, GitHub crea una *Release* con el PDF adjunto.
Para mostrar los cambios respecto a la entrega anterior: `make diff DESDE=v0.1-entrega-guia`.
