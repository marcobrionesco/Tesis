# Recetas — Prompts reutilizables para cualquier IA

Son como los *presets* de un editor de video: instrucciones probadas para
tareas que se repiten. Para usarlas, dile a la IA:

> "Lee `AGENTS.md` y aplica la receta `herramientas/recetas/05_revisar_capitulo.md` al capítulo 2."

Si la IA no tiene acceso al repositorio (ChatGPT web, Gemini), pega el
contenido de la receta junto con el archivo `salida/contexto_completo.md`
(`make contexto`).

| Receta | Cuándo usarla | Etapa (video) |
|---|---|---|
| `00_inicio_sesion.md` | Al empezar con una IA nueva | Abrir proyecto |
| `01_extraer_normativa.md` | Al subir instrucciones de la universidad | Specs de entrega |
| `02_triaje_material.md` | Para clasificar borradores previos | Logging / selección |
| `03_ficha_lectura.md` | Para cada paper o libro | Logging |
| `04_borrador_a_latex.md` | Para pasar texto rescatado a la tesis | Corte bruto |
| `05_revisar_capitulo.md` | Para revisar un capítulo completo | Corte fino |
| `06_verificar_matematica.md` | Para revisar ecuaciones y cálculos | Corrección de color |
| `07_buscar_bibliografia.md` | Para encontrar fuentes reales | Material de archivo |
| `08_cierre_sesion.md` | Al terminar cada sesión | Guardar proyecto |
| `09_preparar_entrega.md` | Antes de entregar al profesor o la versión final | Export / QC final |
| `10_autoevaluar_rubrica.md` | Para estimar la nota con la rúbrica oficial antes de entregar | Visionado de prueba |
| `11_analizar_ejemplo.md` | Para estudiar una tesis o memoria de cálculo ajena y sacar mejoras | Ver referencias |
