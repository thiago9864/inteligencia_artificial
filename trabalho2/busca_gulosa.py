# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:34:23 2019

@author: Thiago
"""

from grafo import Grafo
from Arvore import Arvore
#%%
def ordena(lista_abertos):
#    new = []
#    no_heu = [float(lista_abertos[i].getHeu()) for i in range(len(lista_abertos))]
##    print('heu:'+str(no_heu))
#    no_heu  = sorted(no_heu)
##    print(str(no_heu))
#    for i in range(len(lista_abertos)):
##        print('i:'+str(i))
#        for no in lista_abertos:
#            if float(no.getHeu())== no_heu[i]:
#                new.append(no)
#    print('NEW:'+str([(new[i].label_str) for i in range(len(new))]))
    lista_abertos.sort(key=lambda x: x.getHeu())
#    print("printa")
#    print(lista_abertos)
#    print('NEW:'+str([(lista_abertos[i].label_str) for i in range(len(lista_abertos))]))
#    return new
    
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
lista_fechados = [grafo.getNo(inicial)]
noAtual = grafo.getNo(inicial)
grafo.getNo(inicial).setMarca()


while int(noAtual.id)!= final:
    print(noAtual.label_str)
    #inserindo na lista de abertos
    for aresta_noAtual in noAtual.arestas :
#        if noAtual.label_str=='Sibiu':
#            print('marca:'+str(noAtual.marca))
#            print('sibiu:'+str( [grafo.getNo(noAtual.arestas[i].destino).label_str for i in range(len(noAtual.arestas))]))
        if grafo.getNo(aresta_noAtual.destino) not in lista_fechados :#not in lista_fechados
             print('no entrando:'+grafo.getNo(aresta_noAtual.destino).label_str)
             arvore.gerarFilho(arvore.getNoByLabelInt(noAtual.id).id,grafo.getNo(aresta_noAtual.destino).label_str, 
                      grafo.getNo(aresta_noAtual.destino).id, grafo.getAresta( noAtual.id,grafo.getNo(aresta_noAtual.destino).id).getPeso(), 
                       grafo.getNo(aresta_noAtual.destino).getHeu())
             lista_abertos.append(grafo.getNo(aresta_noAtual.destino))
            #criar uma condição para a lista de fechados
#            print('sem ordenar:'+str( [float(lista_abertos[i].getHeu()) for i in range(len(lista_abertos))]))
#            print(grafo.getNo(aresta_noAtual.destino).label_str)    
#    lista_abertos = ordena(lista_abertos)
    ordena(lista_abertos)
            
    print(str( [(lista_abertos[i].label_str) for i in range(len(lista_abertos))]))
    #print(str(noAtual.id))
    
    velho = noAtual
     
    lista_vizinhos = []
    for aresta in velho.arestas:
        lista_vizinhos.append(grafo.getNo(aresta.destino))
        
    for no in lista_abertos: 
        if no.marca==False:
#            if no in lista_vizinhos:
            noAtual = no
#                print('quem eu marquei do noATual:'+noAtual.label_str)
            break
    
    
#    print('ruim')
#    print(velho.label_str, noAtual.label_str)
    noAtual.setMarca()
       
       
    #se o no final já estiver na lista de abertos,
    if grafo.getNo(final) in lista_abertos:
        break
    else :
#        print('colocando nos fechados:'+grafo.getNo(velho.id).label_str)
        lista_fechados.append(grafo.getNo(velho.id))
        
            

arvore.salvarArquivoGraphViz('arvore.gv')            


