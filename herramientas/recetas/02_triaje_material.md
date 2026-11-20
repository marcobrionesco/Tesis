# Receta 02 — Triaje del material bruto

**Entrada:** un archivo de `02_material_bruto/borradores_previos/`.
**Salida:** `03_seleccion/triaje/<mismo-nombre>.md` usando `_PLANTILLA_triaje.md`.

## Pasos

1. Si el archivo es Word/PDF, convertirlo primero: `make convertir ARCHIVO=...`.
2. Leer el archivo completo **sin modificarlo**.
3. Dividirlo en fragmentos (por sección o idea) y clasificar cada uno:
   - ✅ **Usar**: correcto, relevante, con fuente verificable.
   - 🔧 **Reescribir**: la idea sirve, pero tiene errores, redacción pobre, unidades mal, o falta fuente.
   - ❌ **Descartar**: incorrecto, irrelevante, repetido, relleno genérico, o con citas inexistentes.
   - ❓ **Verificar**: no se puede decidir sin revisar la fuente o preguntar al profesor.
4. **Verificar cada cita** del texto: ¿el autor, año y título existen? Buscar el DOI.
   Texto generado por IA suele traer citas inventadas → ❌ hasta probar lo contrario.
5. **Verificar valores numéricos y normas**: ¿de dónde sale cada número? ¿la norma citada es la vigente?
6. Señalar capítulo y sección de destino para cada fragmento ✅ y 🔧.
7. Al final, resumir: % rescatable, principales problemas, y qué falta que el material no cubre.
8. Actualizar `00_proyecto/ESTADO.md` (capítulos pasan de ⬜ a 🟨).

**Criterio de desconfianza:** frases muy generales ("es de vital importancia", "en la actualidad"),
datos sin fuente, y listas sin desarrollo suelen ser relleno de IA → 🔧 o ❌.
