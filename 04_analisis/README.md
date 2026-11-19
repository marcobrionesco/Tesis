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

## Scripts de la tesis (se ejecutan en orden con `make figuras`)

| Script | Entrada | Salida |
|---|---|---|
| `01_extraer_caracterizacion.py` | PDF de caracterización en `02_material_bruto/datos_crudos/` | `datos/caracterizacion_afluentes.csv` (con QA de promedios) |
| `02_caracterizacion.py` | CSV anterior | `tesis/tablas/caracterizacion_afluentes.tex`, `tesis/figuras/caracterizacion_afluentes.pdf`, `resultados/*.csv` |
| `03_itemizado.py` | PDF del itemizado en `02_material_bruto/otros/` | `datos/itemizado_rev1.csv`, `tesis/tablas/itemizado.tex` |

Las especificaciones técnicas (Word) se convierten con `herramientas/docx_a_anexo.py` → `tesis/anexos/generados/eett_cuerpo.tex`.

## Ejemplo incluido

`scripts/ejemplo_figura.py` muestra el patrón: lee datos, calcula,
guarda la figura con el estilo de la tesis (`estilo_tesis.mplstyle`) y
exporta una tabla LaTeX. Usa SymPy para escribir ecuaciones en LaTeX
automáticamente.

Instalar dependencias:

```bash
pip install -r 04_analisis/requirements.txt
```
