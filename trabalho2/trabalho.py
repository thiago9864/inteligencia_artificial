# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:34:23 2019

@author: Thiago
"""

from Grafo import Grafo
from Arvore import Arvore

#variaveis
instancia_path = 'arad-bucarest.txt'

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


g.salvarArquivoGraphViz("teste_grafo.gv")

arvore = Arvore()

#### Teste da estrutura de geração da arvore ####

# a lista de abertos e fechados contem ids referentes aos nós da arvore
lista_abertos = []
lista_fechados = []


#%% Insere a origem na arvore como a raiz

lista_abertos.append(arvore.gerarRaiz("Arad", 3, 96.5))



#%% Teste de uma primeira iteração qualquer


#obtem o id do pai na arvore
id_pai = lista_abertos[0]

#pra buscar no grafo, obtem o id do pai no grafo
id_pai_no_grafo = arvore.getNo(id_pai).label_int

#obtem uma lista de nós do grafo, como candidatos a filhos
candidatos = [(g.getNo(a.destino),a.peso) for a in g.getNo(id_pai_no_grafo).arestas]

for no_grafo, peso_caminho in candidatos:
    
    #se o candidato não estiver no caminho
    # !!! aqui entra as condições da busca !!!
    if arvore.verificaNoCaminhoWithLabelInt(id_pai, no_grafo.id) == False:
        
        #gera um filho pra esse caminho
        filho = arvore.gerarFilho(
                                  id_pai, 
                                  no_grafo.label_str, 
                                  no_grafo.id, 
                                  peso_caminho, 
                                  no_grafo.getHeu()
                                 )
    #coloca na lista de abertos
    lista_abertos.append(filho)

#depois de gerar os filhos, adiciona a lista de fechados    
lista_fechados.append(id_pai)



#%% Teste de uma segunda iteração qualquer


#gerando os filhos (#2)
id_pai = lista_abertos[1]

#pra buscar no grafo, obtem o id do pai no grafo
id_pai_no_grafo = arvore.getNo(id_pai).label_int

#obtem uma lista de nós do grafo, como candidatos a filhos
candidatos = [(g.getNo(a.destino),a.peso) for a in g.getNo(id_pai_no_grafo).arestas]

for no_grafo, peso_caminho in candidatos:
    
    #se o candidato não estiver no caminho
    # !!! aqui entra as condições da busca !!!
    if arvore.verificaNoCaminhoWithLabelInt(id_pai, no_grafo.id) == False:
        
        #gera um filho pra esse caminho
        filho = arvore.gerarFilho(
                                  id_pai, 
                                  no_grafo.label_str, 
                                  no_grafo.id, 
                                  peso_caminho, 
                                  no_grafo.getHeu()
                                 )
    #coloca na lista de abertos
    lista_abertos.append(filho)

#depois de gerar os filhos, adiciona a lista de fechados    
lista_fechados.append(id_pai)



#%% Teste de uma terceira iteração qualquer



#gerando os filhos
id_pai = lista_abertos[3]

#pra buscar no grafo, obtem o id do pai no grafo
id_pai_no_grafo = arvore.getNo(id_pai).label_int

#obtem uma lista de nós do grafo, como candidatos a filhos
candidatos = [(g.getNo(a.destino),a.peso) for a in g.getNo(id_pai_no_grafo).arestas]

for no_grafo, peso_caminho in candidatos:
    
    #se o candidato não estiver no caminho
    # !!! aqui entra as condições da busca !!!
    if arvore.verificaNoCaminhoWithLabelInt(id_pai, no_grafo.id) == False:
        
        #gera um filho pra esse caminho
        filho = arvore.gerarFilho(
                                  id_pai, 
                                  no_grafo.label_str, 
                                  no_grafo.id, 
                                  peso_caminho, 
                                  no_grafo.getHeu()
                                 )
    #coloca na lista de abertos
    lista_abertos.append(filho)

#depois de gerar os filhos, adiciona a lista de fechados    
lista_fechados.append(id_pai)
    


#%% Salva o resultado da arvore

    
arvore.salvarArquivoGraphViz("teste_arvore.gv")
