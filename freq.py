import heapq
import matplotlib.pyplot as plot
import random
import numpy.random as rnd
from matplotlib.patches import Ellipse


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
        plota_circulo(ponto=r, subplot=121)
        plota_circulo(ponto=r, subplot=122)
        x.append(r[0])
        y.append(r[1])
    
    #circle = plot.Circle(referencia[0], 2)

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
    
    #limites = [xmin, xmax, ymin, ymax] #Limite nao proporcional
    limites = get_limites(x,y)  #Limite porporcional
    
    plot.subplot(121)
    #plot.subplots_adjust(hspace=.45)
    plot.plot(x, y, 'ro')
    plot.title('Pontos de Referencia')
    plot.grid(True)
    plot.gca().set_aspect('equal', adjustable='box')
    plot.axis(limites)
    
    plot.subplot(122)
    #plot.subplots_adjust(hspace=.45)
    plot.plot(x, y, 'k')
    plot.title('Trajetoria de Referencia')
    plot.grid(True)
    plot.gca().set_aspect('equal', adjustable='box')
    plot.axis(limites)
    
    plot.tight_layout(rect=[0, 0.03, 1, 0.95])
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

def get_limites(x_list, y_list):
    print(x_list)
    print(y_list)
    menor_valor = min(x_list+y_list)
    maior_valor = max(x_list+y_list)
    return [menor_valor-1, maior_valor+1, menor_valor-1, maior_valor+1]

def limpa_traj(heap, minimo):
    possiveis = []
    for h in heap:
        if h[0] > minimo:
            possiveis.append(h[1])
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
                    resultado.append(p)

    return resultado

def plota_circulo(ponto, raio=0.65, figure=1, subplot=122):
    fig = plot.figure(figure) 
    ax = fig.add_subplot(subplot)
    
    ell = Ellipse((ponto), raio*2, raio*2)
    ax.add_artist(ell)
    ax.scatter(ponto[0], ponto[1])
    ell.set_clip_box(ax.bbox)
    ell.set_alpha(0.3)
    ell.set_facecolor("blue")
    
plot.figure(1)

t = [[(0.1, 1.5), (1, 2)], [(1, 4), (1, 2)], [(0, 1), (0, 5)], [(1, 4), (1, 2)], [(0.1, 1.5), (0, 2)],
     [(0.1, 1.5), (0, 2)]]

plot.subplot(121)
for cada in t:
    x = []
    y = []
    for c in cada:
        x.append(c[0])
        y.append(c[1])
    plot.plot(x, y, 'r--')
#plot.title('Trajetorias')
#plot.show()
heap, pontos = calcula_frequencia(t)
traj = pontos_referencia(heap, pontos)
#print(traj)
ptos = plota_pontos(traj)
