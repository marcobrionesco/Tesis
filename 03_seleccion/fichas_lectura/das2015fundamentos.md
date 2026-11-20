# Das (2015) — *Fundamentos de ingeniería geotécnica* (4.ª ed. en español) — `das2015fundamentos` ✅ citado

- **Referencia:** Das, B. M. (2015). *Fundamentos de ingeniería geotécnica* (J. León Cárdenas, Trad.; 4.ª ed.). Cengage Learning (México, D.F.). ISBN 978-607-519-373-1. Traducción de *Fundamentals of Geotechnical Engineering*, 4th ed. (Cengage, 2013).
- **PDF:** `02_material_bruto/papers/2015_das_fundamentos-ingenieria-geotecnica_parte1–5.pdf` (texto en `.md`). **Solo llega a la p. 474 (cap. 15)**: faltan el cap. 16 (*Cimentaciones poco profundas: capacidad de carga*, p. 478–511, con 16.6 factor de seguridad, 16.7 cimentaciones con carga excéntrica y 16.9 excentricidad en dos direcciones) y el cap. 17 (*Asentamiento*, p. 512–).
- **Relevancia:** media-alta para el OE3 (zapatas) y media para el medio filtrante.

## Usado en la tesis

| Tema | Lo que dice | Pág. | Dónde |
|---|---|---|---|
| Tamaño efectivo y coef. de uniformidad | D₁₀ = diámetro del 10 % más fino; C_u = D₆₀/D₁₀; C_c = D₃₀²/(D₆₀·D₁₀); bien gradada: C_u > 4 (gravas), > 6 (arenas) | 2.15, p. 40–41 | Cap. 2: definición de d₁₀ y U de la tabla `tab:parametros-hcfv` (filas d₁₀ y U tomadas de Dotro et al., 2021, Tabla 4.1) |
| Presión de contacto con excentricidad | q_máx,mín = ΣV/B·(1 ± 6e/B), e = B/2 − CE; si e > B/6, q_mín < 0 (tracción, indeseable: el suelo casi no resiste tracción) | 15.7, ec. 15.16–15.20, p. 428–429 | Cap. 3: `ec:presion-contacto` (extendida a zapata B × L, A = BL, I = LB³/12) |
| Capacidad de carga | Comparar q_máx con q_u (Meyerhof, ec. 16.23); FS(capacidad de carga) = q_u/q_máx, generalmente 3 | 15.7, ec. 15.21–15.22, p. 429–430 | Cap. 2 (cita junto a Bowles) |
| Deslizamiento | FS = (ΣV·tan(k₁φ′) + B·k₂c′ + P_p)/(P_a cos α); mínimo 1,5; k₁, k₂ = 1/2 a 2/3; P_p a menudo se ignora | 15.6, ec. 15.9–15.13, p. 426–427 | Cap. 3 (junto a NCh2369 10.1.3) |
| Volcamiento | FS = ΣM_R/ΣM_O; mínimo deseable 1,5 a 2 | 15.5, ec. 15.3, p. 425–426 | No usado (la NCh2369 manda el criterio del 80 % de área apoyada) |

## Otros datos útiles (no usados aún)

- **Tabla 6.1, p. 122:** conductividad hidráulica típica (cm/s): grava limpia 100–1; arena gruesa 1–0,01; arena fina 0,01–0,001; arcilla limosa 0,001–0,00001; arcilla < 0,000001. Podría servir para justificar la secuencia de capas del filtro (pregunta 10).
- **Tabla 10.1:** ángulo de fricción vs densidad relativa en suelos sin cohesión → base para suponer φ′ en el deslizamiento si no hay mecánica de suelos.
- **Cap. 12:** programa de exploración del subsuelo (sondajes, SPT, informe) → respalda la recomendación de un estudio de mecánica de suelos.

## Pendiente

- Pedir al autor las páginas 478–530 (cap. 16 y 17) para respaldar la capacidad admisible supuesta de 150 kPa (ecuación de capacidad de carga con φ′ supuesto), el contacto parcial con e > B/6 (16.7) y la frase de asentamientos de las conclusiones (hoy citada con `das2015principles`, entrada sin verificar).
