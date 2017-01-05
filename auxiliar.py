from primeira_verificacao import *
from errors import *


def confere(trajs, candidatos, d):
    maior = 0
    for traj in trajs:
        for pto in traj:
            if len(pto.pertence) > 1:
                nova_area = []
                for area in pto.pertence:
                    for c in candidatos:
                        if c.pto_candidato == area.pto_candidato:
                            for vizinho in c.vizinhos:
                                dist = distancia(pto, vizinho)
                                if dist['x'] < d and dist['y'] < d:
                                    nova_area.append(vizinho)

                if len(nova_area) > len(c.vizinhos):
                    if len(nova_area) > maior:
                        maior = len(nova_area)
                        area = list(set(nova_area))
                        ponto = pto
                        c = Candidato(ponto, area)
                        for p in ponto.pertence:
                            if p in candidatos:
                                candidatos.remove(p)
                            c.vizinhos.append(p.pto_candidato)
                            p.pto_candidato.pertence.append(c)
                        for pto in area:
                            pto.pertence = [c]
                        ponto.pertence = []
                        candidatos.append(c)

    for c in candidatos:
        c.vizinhos = list(set(c.vizinhos))
        for v in c.vizinhos:
            dist = distancia(v, c.pto_candidato)
            if dist['x'] < d and dist['y'] < d:
                pass
            else:
                raise Fora_Area

    maior = 0
    for c in candidatos:
        if len(c.vizinhos) > maior:
            maior = len(c.vizinhos)

    i = 0
    remove = []
    for c in candidatos:
        if len(c.vizinhos) < (minimo * maior) or len(c.vizinhos) == 0:
            remove.append(candidatos.index(c))
        i += 1

    for r in reversed(remove):
        del candidatos[r]


    return candidatos
