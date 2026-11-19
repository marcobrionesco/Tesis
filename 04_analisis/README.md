# 04_analisis — Cálculos, código y figuras ("VFX y color")

Todo cálculo o figura que vaya a la tesis debe poder **regenerarse** desde
aquí. Así, si cambia un dato, se vuelve a correr y la tesis se actualiza.

| Subcarpeta | Qué va |
|---|---|
| `datos/` | Datos **limpios** listos para usar (los crudos quedan en `02_material_bruto/datos_crudos/`) |
| `scripts/` | Código Python (`.py`) que procesa datos y genera figuras/tablas |
| `notebooks/` | Jupyter notebooks para explorar (`.ipynb`) |
| `resultados/` | Salidas intermedias (CSV, tablas) |

## Regla de oro

Las figuras se guardan directamente en `tesis/figuras/` en **PDF** (vectorial)
y las tablas en `tesis/tablas/` como `.tex`, desde el script. Nunca copiar y
pegar números a mano en la tesis.

```bash
make figuras    # corre todos los scripts de 04_analisis/scripts/
```

## Ejemplo incluido

`scripts/ejemplo_figura.py` muestra el patrón: lee datos, calcula,
guarda la figura con el estilo de la tesis (`estilo_tesis.mplstyle`) y
exporta una tabla LaTeX. Usa SymPy para escribir ecuaciones en LaTeX
automáticamente.

Instalar dependencias:

```bash
pip install -r 04_analisis/requirements.txt
```
