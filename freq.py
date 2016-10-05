import heapq

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
            if item in lista: #O(n)
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
    for cada in freq: # O(n)
        heapq.heappush(resultado, (-1 * cada[0], cada[1], cada[2]))
    return resultado,lista


t = [[(0.1, 1.5), (0, 2)], [(0, 4), (1, 5)], [(0, 1), (0, 5)]]
heap, pontos = calcula_frequencia(t)
print(heap)
print(pontos)
