# Receta 06 — Verificación de ecuaciones y cálculos

**Entrada:** un capítulo o un script de `04_analisis/`.
**Salida:** informe en `03_seleccion/notas/verificacion_mat_AAAA-MM-DD.md`.

## Para cada ecuación
1. **Origen:** ¿de qué fuente sale? ¿coincide con la fuente (signos, exponentes, constantes)?
2. **Dimensiones:** comprobar que ambos lados tienen las mismas unidades (usar Pint o análisis manual).
3. **Variables:** todas definidas tras la ecuación, con unidad, y presentes en `GLOSARIO.md`.
4. **Casos límite:** evaluar comportamiento cuando variables → 0, → ∞ o valores típicos.
5. **Verificación simbólica:** si hay desarrollo algebraico, comprobarlo con SymPy (dejar el script en `04_analisis/scripts/verificacion_*.py`).
6. **Verificación numérica:** recalcular un ejemplo a mano o en Python y comparar con lo reportado.

## Para cada script
- ¿Corre de principio a fin (`make figuras`)?
- ¿Los datos de entrada son los de `04_analisis/datos/`?
- ¿Los resultados en la tesis coinciden con lo que genera el script?

Reportar con tabla: `ecuación | verificación | resultado (✅/❌) | comentario`.
