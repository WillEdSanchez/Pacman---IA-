import heapq
import math

from collections import deque

def no_pared(x,y,pared):
    if(x,y) not in pared:
        return True
    return False

def buscar_v(original, pared):
    vecinos_encontrados = []

    if(no_pared(original[0],original[1] + 24,pared)): #subir
        vecinos_encontrados.append((original[0],original[1] + 24))
    if(no_pared(original[0],original[1] - 24,pared)): #bajar
        vecinos_encontrados.append((original[0], original[1] - 24))
    if(no_pared(original[0] - 24,original[1],pared)): #izquierda
        vecinos_encontrados.append((original[0] - 24, original[1]))
    if(no_pared(original[0] + 24,original[1],pared)): #derecha
        vecinos_encontrados.append((original[0] + 24, original[1]))

    return vecinos_encontrados

def BEST_FIRST_SEARCH(estadoInicial, goalTest, pared):
    frontera = deque() #COLAS
    explorados = []
    vecinos = {}

    frontera.append(estadoInicial)
    vecinos.setdefault((estadoInicial),buscar_v(estadoInicial, pared))

    while frontera:

        print("frontera")
        print(frontera)

        estado = frontera.popleft()
        explorados.append(estado)

        print("explorados")
        print(explorados)

        if goalTest==estado:
            return explorados

        for vec in vecinos[estado]:
            if not vec in frontera:
                if not vec in explorados:
                    frontera.append(vec)
                    vecinos.setdefault((vec), buscar_v(vec, pared))

    return 0

def DEPTH_FIRST_SEARCH(estadoInicial, goalTest, pared):
    frontera = deque() #PILAS
    explorados = []
    vecinos = {}

    frontera.append(estadoInicial)
    vecinos.setdefault((estadoInicial),buscar_v(estadoInicial, pared))

    while frontera:

        print("frontera")
        print(frontera)

        estado = frontera.pop()
        explorados.append(estado)

        print("explorados")
        print(explorados)

        if goalTest==estado:
            return explorados

        for vec in vecinos[estado]:
            if not vec in frontera:
                if not vec in explorados:
                    frontera.append(vec)
                    vecinos.setdefault((vec), buscar_v(vec, pared))

    return 0

def heuristica(lista):
    heapq.heapify(lista)
    minimo = heapq.heappop(lista)
    return (minimo[1],minimo[2])

def GREEDY_BEST_FIRST_SEARCH(estadoInicial, goalTest, pared):
    frontera = [] #COLA PRIORIDAD -> h(n)
    heapq.heappush(frontera, (9999, estadoInicial[0], estadoInicial[1]))
    explorados = []
    vecinos = {}

    vecinos.setdefault((estadoInicial),buscar_v(estadoInicial, pared))

    while frontera:

        print("frontera")
        print(frontera)

        estado = heuristica(frontera)
        explorados.append(estado)

        print("explorados")
        print(explorados)

        if goalTest==estado:
            return explorados

        for vec in vecinos[estado]:
            dist_punto = math.sqrt(math.pow((goalTest[0] - vec[0]),2) + math.pow((goalTest[1] - vec[1]),2))
            if not (dist_punto,vec[0],vec[1]) in frontera:
                if not (vec[0],vec[1]) in explorados:
                    heapq.heappush(frontera, (dist_punto,vec[0],vec[1]))
                    vecinos.setdefault((vec), buscar_v(vec, pared))

    return 0