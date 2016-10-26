from trajetorias import trajs
from latlg_to_utm import *
from freq import *

ts = []
for t in trajs:
    ti = clean_coords(t)
    a = lat_to_utm(ti)
    b = utm_to_xy(a)
    ts.append(b)

resultado, pontos = calcula_frequencia(ts)
ptos_ref = pontos_referencia(resultado, pontos)
print('ptos_ref:', ptos_ref)

r = raio(ptos_ref, 2)
possiveis = limpa_traj(resultado, 2)
perto = encontra_perto(possiveis, r, ts)
print('possiveis: ', possiveis)

print('perto: ', perto)
