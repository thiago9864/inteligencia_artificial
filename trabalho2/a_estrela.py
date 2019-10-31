from grafo import Grafo
from Arvore import  Arvore


def g(arvore,destino):
    return arvore.getCaminho(destino)

def f(h, g):
    return h + g

def a_estrela(inicio, fim):
    instancia_path = 'arad-bucarest.txt'

    grafo = Grafo(instancia_path)
    arvore = Arvore()

    abertos_heu = heuristica_()
    abertos_ord = busca_ordenada_grafo_local(grafo,grafo.getNo(inicio),grafo.getNo(fim))

    print("Abertos Heuristica\n")
    for i in range (len(abertos_heu)):
        print(str(abertos_heu[i].getHeu())+" - ")

    print("\nAbertos Ordenados\n")
    print(abertos_ord)


    abertos = []
    fechados = []

    atual = grafo.getNo(inicio)
    abertos.append(atual)
'''
    lista_f = []

# enquanto abertos nao estiver vazio
while int(atual.id) != fim:
    for i in range(len(abertos)):
        if (len(abertos) == 1):
            func = f(abertos[i].getHeu(), g(arvore, 0))
        else:
            func = f(abertos[i].getHeu(), g(arvore, abertos[i + 1]))
'''

a_estrela(3,13)






