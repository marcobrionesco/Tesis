# CONTEXTO — De qué trata la tesis

> Este es el "resumen maestro". Cualquier IA debe poder entender la tesis
> leyendo solo esta página. Mantenerlo corto (1–2 páginas) y actualizado.
> Lo que está entre `[corchetes]` está por completar.

## Datos generales

- **Autor:** Marco Antonio Isaac Briones Escobar
- **Carrera:** Ingeniería Civil
- **Universidad:** Universidad Católica del Maule (UCM), Talca, Chile
- **Facultad / Escuela:** Facultad de Ciencias de la Ingeniería / Escuela de Ingeniería Civil
- **Curso:** ICV-611 Módulo Integrador Profesional (Proyecto de Título)
- **Tipo de proyecto:** trabajo aplicado de ingeniería (diseño), enmarcado en un proyecto de investigación del profesor guía. [Confirmar si se inscribió como tipo 2 o 3, LIN §1]
- **Profesor guía:** Dr. Ismael Leonardo Vera Puerto (UCM) · **Co-guía:** Luis Rojas Cáceres
- **Comisión:** guía + [2 integrantes por definir]
- **Título:** *Propuesta de diseño para una estación experimental basada en humedales construidos para el tratamiento y reutilización en riego de tres fuentes de aguas residuales, en Frutícola SABA SpA, comuna de Linares*
- **Proyecto marco:** ANID/Anillos/ATE250033 "Nature-based solution strategies for developing new sustainable water sources in sweet cherry production under a scarcity context (NbS-Waterry)"
- **Etapa actual:** informe final en revisión — la v3.0 se envió al profesor guía (sept. 2026) y pidió mejorarla.
- **Fecha de entrega objetivo:** [AAAA-MM-DD]

## El problema

La Región del Maule tiene una vulnerabilidad hídrica creciente que amenaza la producción de cerezo dulce
(*Prunus avium* L.). El reúso de aguas residuales tratadas es una alternativa, pero los sistemas
convencionales son inviables en zonas rurales descentralizadas. Se requiere una tecnología de
tratamiento basada en la naturaleza, adaptada a un predio agrícola real, que trate tres afluentes
distintos y entregue agua apta para riego.

## Pregunta de investigación

[Por formular — ver `\pendiente` en `tesis/capitulos/01_introduccion.tex` §1.3.]

## Objetivos

- **General:** Diseñar la infraestructura hidráulica y estructural de una estación experimental basada en Humedales Construidos de Flujo Subsuperficial Vertical (HCFV), orientada al tratamiento y posterior reutilización agrícola de tres afluentes residuales independientes en Frutícola SABA SpA, comuna de Linares.
- **Específicos:**
  1. Dimensionar el sistema de depuración y las redes de conducción a presión y gravedad (balance de oxígeno de los humedales, equipos de impulsión, especificaciones para las distintas fuentes).
  2. Desarrollar la modelación y el cálculo estructural de la plataforma de acero y sus fundaciones bajo solicitaciones estáticas y sísmicas, integrando la planimetría y los detalles constructivos.
  (Se sugirió evaluar separarlos en más objetivos — ver `ESTADO.md`.)

## Alcance

- **Incluye:** caracterización de caudales y cargas; dimensionamiento de HCFV en módulos IBC (6 m² activos por línea); redes por gravedad e impulsión (PVC 50 y 25 mm), bombas y bypass para microrriego (160 L/h); plataforma de acero A270ES para 3 estanques de 1000 L y 3 dosificadores de 200 L; zapatas 1,0 × 1,0 × 0,5 m; planos EE-ATE250033 (láminas 1, 2.1–2.4, 3.1–3.2); itemizado.
- **No incluye:** operación y monitoreo de la planta, fisiología del cerezo, inocuidad, ACV (son del proyecto marco).

## Metodología (resumen)

Caudales (registro de medidor de la casa + aforos en oficinas) → cargas de DQO/NTK → balance de oxígeno de Platzer (1999) para el área de HCFV → discretización en módulos IBC → redes (Hazen-Williams, pérdidas singulares, ADT, curvas de bombas) → plataforma LRFD (NCh427/1, AISC 360) + sismo NCh2369 (estático equivalente) → zapatas (presión de contacto vs. admisible; DS 60) → planos CAD e itemizado.

## Resultados principales (v3.0, en revisión)

- Caudal doméstico de diseño 0,75 m³/d (casa 0,60 + oficina 0,15).
- DQO 180 g/d al humedal; OD = 111,8 g O₂/d < OI = 315 g O₂/d con 6 m² y 6 cargas diarias (carga hidráulica 125 mm/d; orgánica 30 g DQO/m²·d).
- Estructura: razón de flexión 7,2 %, interacción 18,8 %, deflexión 3,81 mm; presión de contacto 27,76 kPa vs. 150 kPa admisible. **Estos valores aún no tienen respaldo en el capítulo de Resultados y hay inconsistencias** (ver triaje).

## Normas y referencias clave

NCh1333 (calidad de agua para riego), DS 90, NCh2369, NCh427/1, NCh1537, DS 60, AISC 360-16, ACI 318-19;
Platzer (1999), Dotro et al. (2017), Kadlec & Wallace (2008), Brix & Arias (2005), Vera et al. (2016).

## Software y herramientas

CAD (planos), [software de cálculo estructural: completar], LaTeX.

## Palabras clave

Humedales Construidos, Soluciones Basadas en la Naturaleza, Diseño Hidráulico, Cálculo Estructural.
(*Constructed wetlands, Nature-based Solutions, Hydraulic design, Structural calculation.*)
