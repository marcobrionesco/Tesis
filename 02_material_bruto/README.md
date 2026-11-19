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
