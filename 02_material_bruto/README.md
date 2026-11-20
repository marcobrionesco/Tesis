# 02_material_bruto — La "ingesta" (rushes)

Aquí va **todo** lo que ya tienes, tal cual: lo bueno, lo malo y lo dudoso.
Igual que el material de cámara en edición: **no se edita, no se borra**.
Lo que sirva se reescribe en `03_seleccion/` o `tesis/`.

| Subcarpeta | Qué va |
|---|---|
| `borradores_previos/` | Textos que ya escribiste o generaste con IA (Word, LaTeX, Markdown, Google Docs exportado, chats copiados) |
| `papers/` | PDFs de artículos, libros, normas técnicas |
| `datos_crudos/` | Planillas, mediciones, resultados de software (ETABS, SAP, HEC-RAS...), fotos de terreno |
| `planos/` | Láminas CAD exportadas (PDF/JPG) |
| `figuras/` | Figuras originales usadas en borradores |
| `otros/` | Lo que no calce en lo anterior (presentaciones, apuntes escaneados, itemizado...) |

## Convención de nombres

`AAAA-MM-DD_origen_descripcion.ext`

- `origen`: `yo`, `chatgpt`, `claude`, `gemini`, `profesor`, `paper`, etc.
- Ej.: `2026-05-02_chatgpt_marco-teorico-v2.docx`

Si un archivo está en Word o PDF, conviene **además** generar una copia en
texto para que cualquier IA lo lea fácil:

```bash
make convertir ARCHIVO=02_material_bruto/borradores_previos/mi-borrador.docx
```

(crea `mi-borrador.md` al lado; el original no se toca)

## Ojo con el tamaño

GitHub rechaza archivos de más de 100 MB. PDFs y planillas normales no
tienen problema. Para videos o modelos muy pesados, deja solo un enlace
en un `.md`.

## Inventario

| Fecha | Archivo(s) | Origen | Triaje |
|---|---|---|---|
| 2026-11-19 | `borradores_previos/*proyecto-titulo-v1.0/2.0/3.0*`, `*memoria-calculo*` | yo (v3.0 = enviada al profesor guía) | `03_seleccion/triaje/2026-11-19_triaje_proyecto-titulo-v3.0.md` |
| 2026-11-19 | `planos/EE-ATE250033_*` (láminas 1, 2.1–2.4, 3.1–3.2) | yo (CAD) | ✅ usadas en anexos III–V |
| 2026-11-19 | `figuras/*`, `otros/EE-ATE250033_itemizado*` | yo | ✅/🔧 ver triaje (fig. 2.1 ❌) |
| 2026-11-19 | `datos_crudos/2026-11-19_yo_caracterizacion-afluentes-resumen.pdf` | yo (fase de caracterización, 6 campañas, 5 puntos) | ✅ procesado en `04_analisis/` (QA sin errores) |
| 2026-11-19 | `planos/EE-ATE250033_3.1/3.2_detalle-estructural-plataforma.pdf` | yo (CAD, PDF vectorial) | ✅ reemplazan a los JPG en el anexo V |
| 2026-11-19 | `otros/EE-ATE250033_itemizado-rev1.pdf` | yo | ✅ tabla en anexo II (ver observaciones) |
| 2026-11-19 | `borradores_previos/2026-11-19_yo_EETT-estacion-experimental.docx` | yo (agosto 2026) | ✅ anexo VI (ver observaciones) |
| 2026-11-20 | `datos_crudos/2026-11-19_proyecto_bd-macroparametros-nbs-waterry.pdf` | proyecto ANID (BD con fechas) | ✅ `04_validar_bd.py` (10 diferencias con el resumen) |
| 2026-11-20 | `datos_crudos/2026-11-19_yo_curva-nivel.xlsx` | yo (52 puntos UTM) | ✅ `05_topografia.py` |
| 2026-11-20 | `calculos_originales/2026_yo_*` (Colab: estructura, bombas, excavación; resultados .docx) | yo | ✅ reproducidos y actualizados en `04_analisis/scripts/10_`–`12_` |

- `papers/2021_dotro-vera-arias_humedales-para-tratamiento_parte1.pdf` y `_parte2.pdf` (+ texto `.md`): Dotro et al. (2021), *Humedales para tratamiento*, edición en castellano editada por Vera-Puerto y Arias (IWA, acceso abierto). Ficha: `03_seleccion/fichas_lectura/dotro2021humedales.md`.
- `normas/nch427-1_parte1–4.pdf` (+ `nch427-1_ocr.md`): NCh427/1:2016, estructuras de acero (escaneada; OCR). Ficha: `03_seleccion/fichas_lectura/inn2016nch427.md`.
- `papers/2024_ucm_manual-etabs-v9.7.4_rev0.pdf` (+ `.md`): manual ETABS de la UCM. **No mencionar ETABS en la tesis**; ficha de método: `03_seleccion/fichas_lectura/2024_ucm_manual-etabs.md`.
- `normas/nch3171-2017.pdf` (+ `nch3171-2017_ocr.md`): NCh3171:2017, combinaciones de cargas (escaneada; OCR). Ficha: `03_seleccion/fichas_lectura/inn2017nch3171.md`.
- `ia_generado/2026-11-20_gemini-deep-research_revision-bibliografica.pdf` (+ `.md`): **dossier generado por IA, no citable**. Verificación: `03_seleccion/notas/2026-11-20_verificacion_dossier-gemini.md`.
- `papers/2014_vidal-araya_aguas-servidas-zonas-rurales_parte1–2.pdf`: libro UdeC (GIBA/EULA). Ficha: `03_seleccion/fichas_lectura/araya2014aguas.md`.
- `papers/2005_uchile-sag_criterios-calidad-agua-riego_resumen-ejecutivo.pdf` y `papers/2025_achipia-indap_manual-reutilizacion-aguas-grises.pdf`. Ficha: `03_seleccion/fichas_lectura/2005-2025_documentos-riego-y-aguas-grises.md`.
- `normas/nch2369-2025_parte1–3.pdf` (+ `nch2369-2025_ocr.md`): NCh2369:2025 (escaneada; copia con licencia personal de terceros, no distribuir). Ficha: `03_seleccion/fichas_lectura/inn2025nch2369.md`.
- `papers/2020_saleh…`, `2023_ignatowicz…`, `2023_mussali-galante…`, `2009_fogg…`, `1986_gonzalez…` (+ `.md`): aguas con agroquímicos y calidad de agua de riego. Ficha: `03_seleccion/fichas_lectura/aguas-agroquimicos_2026-11-20.md`.
- `papers/2025_sigona…`, `2018_girardi…`, `2012_dga…`, `2026_osorno…` (+ `.md`): calidad de aguas superficiales. Ficha: `03_seleccion/fichas_lectura/aguas-superficiales_2026-11-20.md`.
- `papers/2003_dga_diagnostico-clasificacion-cursos-agua_parte1–4.pdf` (+ `.md`): DGA, vol. 1 metodología. Ficha: `03_seleccion/fichas_lectura/aguas-superficiales_2026-11-20.md`.
- `papers/2026_schwitzky…`, `2010_san-martino…`, `2024_ruiz-romero…` (+ `.md`): nitrógeno en frutales. Ficha: `03_seleccion/fichas_lectura/nitrato-frutales_2026-11-20.md`.
- `papers/2016_sommer_tesis-doctoral-ciclo-c-n-bosque_parte1–3.pdf` (+ `.md`): no citado. Ficha: `03_seleccion/fichas_lectura/nitrato-frutales_2026-11-20.md`.
- `papers/2004_dga_diagnostico-clasificacion-cuenca-maule_parte1–2.pdf` (+ `.md`): DGA, cuenca del Maule (calidad y caudales del Putagán y Loncomilla). Ficha: `03_seleccion/fichas_lectura/aguas-superficiales_2026-11-20.md`.
- `ia_generado/2026-11-20_research-report-ia_volumen-maule.pdf`: texto de IA, no citable.
- `papers/2004_dga_diagnostico-clasificacion-vol1-informe-final_parte1–4.pdf` (+ `.md`): DGA vol. 1 con anexos (límites de clases de calidad). Ficha: `03_seleccion/fichas_lectura/aguas-superficiales_2026-11-20.md`.
- `papers/2020_rodriguez-dominguez…`, `2022_reuter_compendio…_parte1–3`, `2017_homsi_aidis…` (+ `.md`): SbN y humedales en Latinoamérica. Ficha: `03_seleccion/fichas_lectura/sbn-humedales-latinoamerica_2026-11-20.md`.
- `papers/2021_cross_nbs-wastewater-treatment_parte1–4.pdf` (+ `.md`): Cross et al. (Eds.), IWA. Ficha: `03_seleccion/fichas_lectura/sbn-humedales-latinoamerica_2026-11-20.md`.
