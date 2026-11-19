"""Extrae la tabla de caracterización de afluentes (PDF de una página) a CSV.

Entrada : 02_material_bruto/datos_crudos/2026-11-19_yo_caracterizacion-afluentes-resumen.pdf
Salida  : 04_analisis/datos/caracterizacion_afluentes.csv
Método  : asigna cada número a su columna (punto de muestreo, semana) según su
          posición x en la página, y verifica que los promedios del original
          coincidan con los recalculados (QA). Ejecutar desde la raíz del repo:
          python 04_analisis/scripts/01_extraer_caracterizacion.py
"""
import csv
import re
import statistics
from collections import Counter
from pathlib import Path

import pymupdf

RAIZ = Path(__file__).resolve().parents[2]
pdf = RAIZ / "02_material_bruto/datos_crudos/2026-11-19_yo_caracterizacion-afluentes-resumen.pdf"
out = RAIZ / "04_analisis/datos/caracterizacion_afluentes.csv"
words=pymupdf.open(pdf)[0].get_text('words')
hdr_y=64
cols=[]  # (xcenter, sitio, semana o 'prom')
sitios=['EST','AS1','AS2','AGR1','AGR2']
row=sorted([w for w in words if abs(round(w[1])-hdr_y)<=2 and (w[0]+w[2])/2>140], key=lambda w:w[0])
k=0
for w in row:
    s=sitios[k//8]; c='prom' if w[4]=='Prom' else int(w[4]); cols.append(((w[0]+w[2])/2,s,c)); k+=1
assert len(cols)==40, len(cols)
cells=[w for w in words if (w[0]+w[2])/2>140 and w[1]>hdr_y+5]
# agrupar filas por y
cells.sort(key=lambda w:(w[1]+w[3])/2)
filas=[]; 
for w in cells:
    yc=(w[1]+w[3])/2
    if filas and abs(yc-filas[-1][0])<4: filas[-1][1].append(w)
    else: filas.append([yc,[w]])
params=[('pH','-'),('Temperatura','°C'),('Conductividad eléctrica','µS/cm'),('Potencial de óxido-reducción','mV'),('Oxígeno disuelto','mg/L'),
 ('Sólidos disueltos totales','mg/L'),('Turbiedad','NTU'),('DQO total','mg/L'),('DQO disuelta','mg/L'),('DBO5','mg/L'),('SST','mg/L'),
 ('Amonio','mg/L'),('Nitrato','mg/L'),('Nitrógeno total','mg/L'),('Fósforo total','mg/L'),('Fosfato','mg/L'),('Coliformes fecales','NMP/100 mL'),('E. coli','NMP/100 mL')]
assert len(filas)==18, [len(f[1]) for f in filas]
def num(t):
    t=t.replace(' ','')
    m=re.fullmatch(r'([<>]?)(-?\d+(?:\.\d+)?)(?:x10(\d+))?',t)
    return (float(m.group(2))*(10**int(m.group(3)) if m.group(3) else 1), m.group(1)) if m else (None,None)
rows=[]; qa=[]
for (yc,ws),(par,unid) in zip(filas,params):
    celda={}
    for w in sorted(ws,key=lambda w:w[0]):
        xc=(w[0]+w[2])/2
        c=min(cols,key=lambda c:abs(c[0]-xc))
        if abs(c[0]-xc)>9: qa.append(f'{par}: palabra {w[4]!r} fuera de columna (x={xc:.0f})'); continue
        celda.setdefault((c[1],c[2]),[]).append(w[4])
    for s in sitios:
        vals=[]
        for sem in range(1,8):
            t=' '.join(celda.get((s,sem),[]))
            v,cen=num(t) if t not in ('','-') else (None,None)
            if t not in ('','-') and v is None: qa.append(f'{par} {s} sem{sem}: no numérico {t!r}')
            if t!='': rows.append(dict(punto=s,parametro=par,unidad=unid,semana=sem,valor='' if v is None else v,censura=cen or '',texto_original=t))
            if v is not None: vals.append(v)
        p=' '.join(celda.get((s,'prom'),[]))
        pv,_=num(p) if p else (None,None)
        if vals and pv is not None and par not in ('Coliformes fecales','E. coli'):
            m=statistics.mean(vals)
            if abs(m-pv)>max(0.011,abs(m)*0.003): qa.append(f'{par} {s}: promedio original {pv} ≠ calculado {m:.3f} (n={len(vals)})')
        elif par in ('Coliformes fecales','E. coli'): pass
with open(out,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(len(rows),'celdas con dato'); print('QA:'); [print(' ',q) for q in qa] or print('  sin observaciones')
# semanas con datos
print('Semanas con datos:',sorted(Counter(r['semana'] for r in rows if r['valor']!='').items()))
