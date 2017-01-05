from candidato import *
from trajetorias import minimo


def anota(d, trajs):
    candidatos = []
    for traj in trajs:
        for pto in traj:
            if len(candidatos) == 0:
                c = Candidato(pto, [])
                candidatos.append(c)
            else:
                vizinho = False
            i = 0
            while i < len(candidatos):
                dist = distancia(pto, candidatos[i].pto_candidato)
                if dist['x'] < d and dist['y'] < d:
                    candidatos[i].vizinhos.append(pto)
                    pto.pertence.append(candidatos[i])
                    vizinho = True
                i += 1

            if not vizinho:
                c = Candidato(pto, [])
                candidatos.append(c)
    maior = 0
    for c in candidatos:
        if len(c.vizinhos)> maior:
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


def x_maior(pto, candidato):
    return pto.x > candidato.x


def y_maior(pto, candidato):
    return pto.y > candidato.y


def distancia(pto, candidato):
    d = {'x': candidato.x - pto.x, 'y': candidato.y - pto.y}

    if x_maior(pto, candidato):
        d['x'] = -1 * d['x']

    if y_maior(pto, candidato):
        d['y'] = -1 * d['y']

    return d
