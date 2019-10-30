# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:34:23 2019

@author: Thiago, Gabriele
"""

#classe que representa o vertice
class No:
    def __init__(self, id):
        self.id = id
        self.id_pai = -1 #id do pai, pra ser usado na arvore. Usar -1 se for a raiz
        self.label_str = "" #Label string, util pra colocar o nome da cidade
        self.arestas=[]
        self.label_int=0 #Label int, util pra colocar um id de referência pra outro grafo
        self.arestas_peso = []
        self.heu = None #esta None por padrão porque pode pode ter nó com heuristica 0, no caso, o destino
        self.marca = False
    
    def removeAresta(self, destino):
        for a in self.arestas:
            if(a.destino == destino):
                self.arestas.remove(a)
                
    def heuristica(self):
#        print('nó:'+self.id)
        #tenho uma lista de arestas vou ter que organizar por peso
        #vetor com os pesos
#        arestas_peso = []
        self.arestas_peso=[self.arestas[i].getPeso() for i in range (len(self.arestas))]
        menor1 = min(self.arestas_peso)
#        print('menor1:'+str(menor1))
#        print('peso:'+str(self.arestas_peso))
        self.arestas_peso.remove(menor1)
#        print('peso remove1:'+str(self.arestas_peso))
        if len(self.arestas_peso)>0:
            menor2 = min(self.arestas_peso)
#            print('menor2:'+str(menor2))
#            print('peso2:'+str(self.arestas_peso))
            media = (menor1+menor2)/2
        else:
            media = menor1
#        print('quero sair')
        self.heu = media
    
    def getHeu(self):
        return self.heu
    
    def setHeu(self,heuristica):
        self.heu = heuristica
    
    def setMarca(self):
        self.marca = True

     