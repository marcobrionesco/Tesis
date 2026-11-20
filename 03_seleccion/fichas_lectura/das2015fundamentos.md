# Das (2015) — *Fundamentos de ingeniería geotécnica* (4.ª ed. en español) — `das2015fundamentos` ✅ citado

- **Referencia:** Das, B. M. (2015). *Fundamentos de ingeniería geotécnica* (J. León Cárdenas, Trad.; 4.ª ed.). Cengage Learning (México, D.F.). ISBN 978-607-519-373-1. Traducción de *Fundamentals of Geotechnical Engineering*, 4th ed. (Cengage, 2013).
- **PDF:** `02_material_bruto/papers/2015_das_fundamentos-ingenieria-geotecnica_parte1–5.pdf` (texto en `.md`). Libro **completo** (partes 6–7 recibidas después: cap. 16–18 y anexos).
- **Relevancia:** media-alta para el OE3 (zapatas) y media para el medio filtrante.

## Usado en la tesis

| Tema | Lo que dice | Pág. | Dónde |
|---|---|---|---|
| Tamaño efectivo y coef. de uniformidad | D₁₀ = diámetro del 10 % más fino; C_u = D₆₀/D₁₀; C_c = D₃₀²/(D₆₀·D₁₀); bien gradada: C_u > 4 (gravas), > 6 (arenas) | 2.15, p. 40–41 | Cap. 2: definición de d₁₀ y U de la tabla `tab:parametros-hcfv` (filas d₁₀ y U tomadas de Dotro et al., 2021, Tabla 4.1) |
| Presión de contacto con excentricidad | q_máx,mín = ΣV/B·(1 ± 6e/B), e = B/2 − CE; si e > B/6, q_mín < 0 (tracción, indeseable: el suelo casi no resiste tracción) | 15.7, ec. 15.16–15.20, p. 428–429 | Cap. 3: `ec:presion-contacto` (extendida a zapata B × L, A = BL, I = LB³/12) |
| Capacidad de carga | Comparar q_máx con q_u (Meyerhof, ec. 16.23); FS(capacidad de carga) = q_u/q_máx, generalmente 3 | 15.7, ec. 15.21–15.22, p. 429–430 | Cap. 2 (cita junto a Bowles) |
| Deslizamiento | FS = (ΣV·tan(k₁φ′) + B·k₂c′ + P_p)/(P_a cos α); mínimo 1,5; k₁, k₂ = 1/2 a 2/3; P_p a menudo se ignora | 15.6, ec. 15.9–15.13, p. 426–427 | Cap. 3 (junto a NCh2369 10.1.3) |
| Capacidad de carga, Terzaghi | Zapata cuadrada: q_u = 1,3c′N_c + qN_q + 0,4γBN_γ; N según φ′ (Tabla 16.1) | 16.3, ec. 16.4, p. 482–483 | Cap. 2: `ec:terzaghi-cuadrada`; script `04_analisis/scripts/13_capacidad_soporte.py` |
| Factor de seguridad | q_adm = q_u/FS; FS al menos 3 | 16.6, ec. 16.14–16.16, p. 487–488 | Cap. 2 y 4 |
| Excentricidad > B/6 | q_máx = 4Q/[3L(B − 2e)]; separación entre zapata y suelo; método de área efectiva de Meyerhof (B′ = B − 2e) | 16.7, ec. 16.17–16.25, p. 490–492 | Cap. 3 (longitud apoyada 3(B/2 − e) ⇒ 80 % ⇔ e ≤ 0,233B) |
| Asentamiento | Antes de la falla por corte puede haber asentamientos que dañen la estructura (elástico y por consolidación) | 17.1, p. 512 | Cap. 2 y conclusiones (reemplaza a `das2015principles`, eliminada) |
| Compacidad y φ′ | Muy suelto < 30°; suelto 30–35°; compacto 35–40°; denso 40–45° | Tabla 10.1, p. 230 | Cap. 4 (150 kPa ⇔ φ′ ≈ 32°, arena suelta) |
| Volcamiento | FS = ΣM_R/ΣM_O; mínimo deseable 1,5 a 2 | 15.5, ec. 15.3, p. 425–426 | No usado (la NCh2369 manda el criterio del 80 % de área apoyada) |

## Otros datos útiles (no usados aún)

- **Tabla 6.1, p. 122:** conductividad hidráulica típica (cm/s): grava limpia 100–1; arena gruesa 1–0,01; arena fina 0,01–0,001; arcilla limosa 0,001–0,00001; arcilla < 0,000001. Podría servir para justificar la secuencia de capas del filtro (pregunta 10).
- **Tabla 10.1:** ángulo de fricción vs densidad relativa en suelos sin cohesión → base para suponer φ′ en el deslizamiento si no hay mecánica de suelos.
- **Cap. 12:** programa de exploración del subsuelo (sondajes, SPT, informe) → respalda la recomendación de un estudio de mecánica de suelos.

## Resultado de la sensibilidad (supuestos: c′ = 0, γ = 18 kN/m³, D_f = 0,50 m, B = 1,00 m, FS = 3)

| φ′ | 28° | 30° | 32° | 34° | 35° |
|---|---|---|---|---|---|
| q_adm (kPa) | 86 | 113 | 150 | 201 | 233 |

- Los 150 kPa del cálculo original equivalen a φ′ ≈ 32° (arena suelta). La presión estática (24,2 kPa) cumple incluso con 86 kPa.
- Con 6 pilares: e = 0,217 m → longitud apoyada 3(0,5 − 0,217) = 0,85 m = 85 % (coincide con el script 10_estructura).
- Otros: 17.6 (p. 528): las ecuaciones de carga admisible con N₆₀ suponen 25 mm de asentamiento total y unos 19 mm de diferencial.
