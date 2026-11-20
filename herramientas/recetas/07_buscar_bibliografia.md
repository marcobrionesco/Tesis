# Receta 07 — Búsqueda de bibliografía

**Entrada:** un tema o una afirmación que necesita fuente (p. ej. un `\pendiente{falta fuente...}`).
**Salida:** lista de fuentes candidatas en `03_seleccion/notas/busquedas.md`.

## Reglas
- **Solo fuentes que existan y se puedan verificar** (DOI, ISBN o enlace a sitio oficial).
- Si no tienes acceso a internet o no puedes verificar, **dilo** y entrega solo las ecuaciones de búsqueda para que el usuario busque.
- Priorizar: normas oficiales vigentes > libros de referencia > artículos indexados (Scopus/WoS) > tesis > otros.

## Pasos
1. Definir conceptos clave y sinónimos en español e inglés.
2. Construir la ecuación booleana (ver `herramientas/HERRAMIENTAS.md` §1).
3. Registrar en `busquedas.md`: fecha, base de datos, ecuación, nº de resultados, seleccionados.
4. Por cada fuente seleccionada: DOI → `doi2bib.sh` → `referencias.bib`, y crear su ficha (receta 03).
