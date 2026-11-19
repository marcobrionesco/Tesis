# 02_material_bruto — La "ingesta" (rushes)

Aquí va **todo** lo que ya tienes, tal cual: lo bueno, lo malo y lo dudoso.
Igual que el material de cámara en edición: **no se edita, no se borra**.
Lo que sirva se reescribe en `03_seleccion/` o `tesis/`.

| Subcarpeta | Qué va |
|---|---|
| `borradores_previos/` | Textos que ya escribiste o generaste con IA (Word, LaTeX, Markdown, Google Docs exportado, chats copiados) |
| `papers/` | PDFs de artículos, libros, normas técnicas |
| `datos_crudos/` | Planillas, mediciones, resultados de software (ETABS, SAP, HEC-RAS...), fotos de terreno |
| `otros/` | Lo que no calce en lo anterior (presentaciones, apuntes escaneados...) |

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
