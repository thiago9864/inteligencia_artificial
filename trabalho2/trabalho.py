# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:34:23 2019

@author: Thiago
"""

from grafo import Grafo

#variaveis
instancia_path = 'arad-bucarest.txt'

#inicia o grafo principal
grafo = Grafo(instancia_path)
grafo.removeNo(1)      
grafo.addAresta(1,3,10,0)
grafo.setLabelVertice(1, 'Barra Mansa')
grafo.salvarArquivoGraphViz('teste.gv')

lista_abertos = []

arvore = Grafo()
lista_abertos.append(arvore.gerarRaiz(3, grafo.getNo(3).label))#colocar as grafo
lista_abertos.append(arvore.gerarFilho(lista_abertos[0], 2, "F1"))## pai, id referencia, label
lista_abertos.append(arvore.gerarFilho(lista_abertos[0], 9, "F2"))
lista_abertos.append(arvore.gerarFilho(lista_abertos[0], 3, "F3"))

lista_abertos.append(arvore.gerarFilho(lista_abertos[2], 3, "F3"))
lista_abertos.append(arvore.gerarFilho(lista_abertos[2], 2, "F1"))

arvore.salvarArquivoGraphViz('arvore.gv')