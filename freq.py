import heapq
import matplotlib.pyplot as plot


def calcula_frequencia(trajs):
    lista = []
    freq = []
    i = 0

    while i < len(trajs):
        j = 0
        while j < len(trajs[i]):
            t = trajs[i][j]
            x = int(t[0])
            y = int(t[1])
            item = (x, y)
            if item in lista:  # O(n)
                indice = lista.index(item)
                tr = freq[indice][2]
                tr.append(i)
                freq[indice] = (freq[indice][0] + 1, freq[indice][1], tr)
            else:
                lista.append(item)
                indice = lista.index(item)
                freq.append((1, indice, [i]))
            j += 1
        i += 1
    resultado = []
    for cada in freq:  # O(n)
        heapq.heappush(resultado, (cada[0], cada[1], cada[2]))
    heapq._heapify_max(resultado)
    return resultado, lista


def pontos_referencia(heap, pontos):
    ref = []
    for h in heap:
        if h[0] > 1:
            ref.append(pontos[h[1]])
    return ref


def plota_pontos(referencia):
    x = []
    y = []
    for r in referencia:
        x.append(r[0])
        y.append(r[1])

    xmin = referencia[0][0] - 1
    xmax = referencia[-1][0] + 1
    ymin = referencia[0][1] - 1
    ymax = referencia[-1][1] + 1
    plot.subplot(211)
    plot.subplots_adjust(hspace=.45)
    plot.plot(x, y, 'ro')
    plot.title('Pontos de Referência')
    plot.grid(True)
    plot.axis([xmin, xmax, ymin, ymax])

    plot.subplot(212)
    plot.subplots_adjust(hspace=.45)
    plot.plot(x, y, 'k')
    plot.title('Trajetória de Referência')
    plot.grid(True)
    plot.axis([xmin, xmax, ymin, ymax])
    plot.show()


def raio(ref, distancia):
    meia = distancia / 2
    resultado = []
    for ponto in ref:
        x = ponto[0]
        y = ponto[1]
        xi = x - meia
        xf = x + meia
        yi = y - meia
        yf = y + meia
        xs = (xi, xf)
        ys = (yi, yf)
        resultado.append((xs, ys))

    return resultado


def limpa_traj(heap, minimo):
    possiveis = []
    for h in heap:
        if h[0] >= minimo:
            for t in h[2]:
                if t not in possiveis:
                    possiveis.append(t)
    return possiveis


def encontra_perto(possiveis, raios, trajs):
    '''
    possiveis: lista de indices de trajetorias possiveis
    raios: lista de tuplas, com valores de raios calculados sobre pontos de referencia
    trajs: lista de trajetorias inicial
     '''
    resultado = []
    for p in possiveis:
        traj = trajs[p]
        for ponto in traj:
            for pto in raios:
                if (ponto[0] > pto[0][0] or ponto[0] < pto[0][1]) and (ponto[1] > pto[1][0] or ponto[1] < pto[1][1]):
                    resultado.append(ponto)

    return resultado


# plot.figure(1)
#
# t = [[(0.1, 1.5), (1, 2)], [(1, 4), (1, 2)], [(0, 1), (0, 5)], [(1, 4), (1, 2)], [(0.1, 1.5), (0, 2)],
#      [(0.1, 1.5), (0, 2)]]
#
# plot.subplot(221)
# for cada in t:
#     x = []
#     y = []
#     for c in cada:
#         x.append(c[0])
#         y.append(c[1])
#     plot.plot(x, y, 'r--')
# plot.title('Trajetórias')
# plot.show()
#
# heap, pontos = calcula_frequencia(t)
# traj = pontos_referencia(heap, pontos)
# plot.figure(1)
# ptos = plota_pontos(traj)


