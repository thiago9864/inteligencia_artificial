# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:34:23 2019

@author: Thiago
"""

from grafo import Grafo
from Arvore import Arvore
#%%
def ordena(lista_abertos):
    new = []
    no_heu = [float(lista_abertos[i].getHeu()) for i in range(len(lista_abertos))]
    no_heu  = sorted(no_heu)
#    print(str(no_heu))
    for i in range(len(lista_abertos)):
#        print('i:'+str(i))
        for no in lista_abertos:
            if float(no.getHeu())== no_heu[i]:
                new.append(no)
    return new
    
#%%
#variaveis
instancia_path = 'arad-bucarest.txt'

#inicia o grafo principal
grafo = Grafo(instancia_path)
#grafo.removeNo(1)      
#grafo.addAresta(1,3,10,0)
#grafo.setLabelVertice(1, 'Barra Mansa')
grafo.salvarArquivoGraphViz('teste.gv')

lista_abertos = []

arvore = Arvore()
inicial = 3 #Arad
final = 13 #Bucareste
grafo.getNo(final).setHeu(0)
arvore.gerarRaiz( grafo.getNo(inicial).label_str,inicial,grafo.getNo(inicial).getHeu())#colocar as grafo
lista_abertos.append(grafo.getNo(inicial))
lista_fechados = []
noAtual = grafo.getNo(inicial)
grafo.getNo(inicial).setMarca()

while int(noAtual.id)!= final:
    #inserindo na lista de abertos
    for i in range(1,20):
        if grafo.getAresta(int(noAtual.id),i):
            if grafo.getNo(i) not in lista_fechados:
                lista_abertos.append(grafo.getNo(i))
            #criar uma condição para a lista de fechados
#            print('sem ordenar:'+str( [float(lista_abertos[i].getHeu()) for i in range(len(lista_abertos))]))
            lista_abertos = ordena(lista_abertos)
            
#            print(str( [float(lista_abertos[i].getHeu()) for i in range(len(lista_abertos))]))
    #print(str(noAtual.id))
    velho = noAtual
    for no in lista_abertos: 
        if no.marca==False:
            noAtual = no
            break
        
    print(velho.id, noAtual.id)
    
    arvore.gerarFilho(velho.id, 
                      noAtual.label_str, 
                      noAtual.id, 
                      grafo.getAresta(velho.id, noAtual.id).getPeso(), 
                      noAtual.getHeu()
                      )         
    #se o no final já estiver na lista de abertos,
    if grafo.getNo(final) in lista_abertos:
        break
    else :
        lista_fechados.append(grafo.getNo(noAtual.id))
            

arvore.salvarArquivoGraphViz('arvore.gv')            


