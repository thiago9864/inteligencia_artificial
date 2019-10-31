# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:34:23 2019

@author: Thiago
"""

from grafo import Grafo
from Arvore import Arvore
from algoritmos import busca_ordenada_grafo_local

#variaveis
instancia_path = '/home/victor/Documentos/UFJF/IA/inteligencia_artificial/trabalho2/arad-bucarest.txt'

#inicia o grafo principal
g = Grafo(instancia_path)  


#verifica os nós
print("\nVerifica os nós\n")
ids = []
for no in g.grafo:
    print(no.id, type(no.id), no.label_str)
    ids.append(no.id)
    
#verifica a função getNo
print("\nTesta getNo()\n")
for id in ids:
    no = g.getNo(id)
    print(no.id, no.label_str, no.getHeu())
    

#verifica a função getAresta
print("\nTesta getAresta()\n")
arestasOk = True
for no in g.grafo:
    for aresta in no.arestas:
        if g.getAresta(no.id, aresta.destino) == False:
            print("Aresta (%d, %d) não encontrada" % no.id, aresta.destino)
            arestasOk=False
        else:
            print("Aresta (%d, %d)" % (no.id, aresta.destino))
if arestasOk:
    print("\nArestas Ok\n")

g.salvarArquivoGraphViz('test-arad.gv')

g.salvarArquivoGraphViz("teste_grafo.gv")

arvore = Arvore()

lista_abertos = []
lista_abertos.append(arvore.gerarRaiz("Arad", 3, 96.5))
lista_abertos.append(arvore.gerarFilho(lista_abertos[0], "Sibiu", 4, 99, 89.5))
lista_abertos.append(arvore.gerarFilho(lista_abertos[0], "Zerind", 2, 140, 73.0))
lista_abertos.append(arvore.gerarFilho(lista_abertos[0], "Barra Mansa", 25, 999))


arvore.salvarArquivoGraphViz("teste_arvore.gv")

(a,_,_) = busca_ordenada_grafo_local(g,3,13)

a.salvarArquivoGraphViz("teste_busca.gv")