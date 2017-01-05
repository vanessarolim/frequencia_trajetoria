from trajetorias import trajetorias_iniciais, d, saida
from latlg_to_utm import *
from auxiliar import *
import time
import csv

inicio = time.time()
trajs = []
for t in trajetorias_iniciais:
    ti = clean_coords(t)
    trajetoria = lat_to_utm(ti)
    trajs.append(trajetoria)

total_pontos = 0
total_trajs = 0
for traj in trajs:
    total_trajs += 1
    for pto in traj:
        total_pontos += 1

print('quantidade total de trajs:' + str(total_trajs))
print('quantidade total de pontos:' + str(total_pontos))

candidatos = anota(d, trajs)

print('pontos candidatos em primeira passada: ' + str(len(candidatos)))

for c in candidatos:
    if len(c.vizinhos) == 0:
        print('puta q pariu')
        candidatos.remove(c)
    print('ponto: ' + str(c.pto_candidato.x) + ',' + str(c.pto_candidato.y) + ' c.vizinhos: ' + str(len(c.vizinhos)))

print('-------------')
candidatos = confere(trajs, candidatos, d)

print('pontos candidatos apos conferencia de melhores pontos: ' + str(len(candidatos)))

for c in candidatos:
    print('ponto: ' + str(c.pto_candidato.x) + ',' + str(c.pto_candidato.y) + ' c.vizinhos: ' + str(len(c.vizinhos)))

fim = time.time()

intervalo = fim - inicio
print('calculou em: ' + str(intervalo) + ' s')

with open(saida, 'w') as saida:
    latlon = []
    for c in candidatos:
        c_latlon = utm_to_lat(c.pto_candidato)
        for v in c.vizinhos:
            latlon.append(utm_to_lat(v))

        fieldnames = ['candidato', 'vizinhos']
        writer = csv.DictWriter(saida, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'candidato': c_latlon, 'vizinhos': latlon})
