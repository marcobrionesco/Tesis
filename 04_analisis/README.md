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
| `04_validar_bd.py` | BD de macroparámetros (PDF) + CSV de caracterización | `datos/bd_macroparametros.csv`, `resultados/qa_bd_vs_resumen.csv` |
| `05_topografia.py` | Curva de nivel (xlsx) | `datos/curva_nivel.csv`, `resultados/topografia_puntos.png` |
| `10_estructura.py` | Parámetros en el script (dimensiones finales) | `tesis/tablas/verificacion_estructural.tex`, `resultados/estructura_verificacion.csv` |
| `11_bombas.py` | Parámetros en el script (tuberías finales + catálogos) | `tesis/tablas/bombas_adt.tex`, `resultados/bombas_adt.csv`, `resultados/bombas_catalogo_vs_requerido.pdf` |
| `12_excavacion.py` | Datos de las corridas del autor | `resultados/excavacion_*.csv`, `resultados/excavacion_perfiles.pdf` |

### Cálculos originales del autor

Están intactos en `02_material_bruto/calculos_originales/` (Colab). Los scripts `10_`–`12_` los
**reproducen** (los resultados originales coinciden: ADT 14,07 / 7,90 / 10,71 m) y luego los
**actualizan** con las dimensiones finales (planos, EETT, itemizado Rev. 1). Cada dato marcado
`SUPUESTO` en el código debe confirmarse. Las medidas finales son las de los planos, las EETT y el
itemizado Rev. 1 (el documento "CO" es la carta oferta para el contratista y no trae medidas).

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
