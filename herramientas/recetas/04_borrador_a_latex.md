# Receta 04 — Pasar material seleccionado a LaTeX

**Entrada:** fragmentos ✅/🔧 de `03_seleccion/triaje/` y fichas de lectura.
**Salida:** texto en `tesis/capitulos/NN_*.tex`.

## Pasos

1. Leer `REGLAS_FORMATO.md`, `GLOSARIO.md` y el capítulo destino completo (para no repetir ni contradecir).
2. Reescribir (no copiar) cada fragmento con registro académico, en español, **una oración por línea**.
3. Convenciones obligatorias:
   - Unidades con `siunitx` (`\qty{}{}`, `\unit{}`, `\num{}`).
   - Ecuaciones numeradas con `\label{ec:...}` y referidas con `\cref{}`; definir cada variable después de la ecuación.
   - Símbolos iguales a `GLOSARIO.md`.
   - Citas solo con claves existentes en `referencias.bib`. Si falta la fuente: `\pendiente{falta fuente: ...}`.
   - Figuras en `tesis/figuras/` (PDF) con `\caption` y `\label{fig:...}`; mencionarlas en el texto antes de que aparezcan.
4. Compilar (`make pdf`) y revisar (`make revisar`).
5. Marcar en el archivo de triaje qué fragmentos ya se pasaron.
6. Actualizar estado del capítulo en `ESTADO.md` (🟨 → 🟧).

Para convertir de golpe un Word a LaTeX como punto de partida:
`pandoc archivo.docx -t latex -o borrador.tex` (luego limpiar a mano según las convenciones).
