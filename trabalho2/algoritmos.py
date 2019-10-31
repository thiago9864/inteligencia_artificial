from grafo import *
from Arvore import Arvore

def busca_ordenada_networkx(grafo, origem, destino):

    # durante a execução cada nó terá o custo do caminho e a lista de nós do caminho
    atual = {'no': origem, 'custo': 0, 'caminho': [origem]}
    fechados = [atual]
    abertos = []

    # Realizamos as iterações enquanto o caminho não passar por todos os nós e 
    # não encontrar o destino
    while len(atual['caminho']) < grafo.number_of_nodes() and atual['no'] != destino:
        
        # adicionando novos nós a lista de abertos
        for adj in grafo[atual['no']]:
            
            # garante a não visitação de nós repetidos
            if adj not in atual['caminho']:
                    
                novo_custo = grafo[atual['no']][adj]['weight'] + atual['custo']
                novo_caminho = atual['caminho'] + [adj]

                abertos.append({'no': adj, 'custo': novo_custo, 'caminho': novo_caminho})
                
        abertos.sort(key=lambda x: x['custo']) # ordenando lista de abertos pelo custo do caminho
        fechados.append(atual)   # adiciona no já visitado a lista de fechados 
        proximo = abertos.pop(0) # visitando o nó de caminho mais curto
        
        atual = proximo

    return atual, abertos, fechados

def busca_ordenada_grafo_local(grafo, no_origem, no_destino):
    arvore_resultado = Arvore()
    no_atual = grafo.getNo(no_origem)
    no_destino = grafo.getNo(no_destino)

    # ao adicionar um no na árvore ele retorna o id do novo nó na árvore
    atual_id = arvore_resultado.gerarRaiz(no_atual.label_str, label_int=no_atual.id)

    # durante a execução cada nó terá o custo do caminho e a lista de nós do caminho
    atual = {'no': atual_id, 'custo': 0, 'caminho':[ ]}
    destino = no_destino.id
    fechados = [atual]
    abertos = [] 

    # Realizamos as iterações enquanto o caminho não passar por todos os nós e 
    # não encontrar o destino
    while arvore_resultado.getNo(atual['no']).label_int != no_destino.id:

        for adj in no_atual.arestas: # percorrendo arestas do grafo original
            
            # garante a não visitação de nós repetidos
            if adj.destino not in atual['caminho']:

                grafo_id = arvore_resultado.getNo(atual['no']).label_int # id do nó da arvore no grafo

                # custo da aresta no grafo original
                novo_custo = grafo.getAresta(grafo_id, adj.destino).peso + atual['custo']
                
                adj_label = grafo.getNo(adj.destino).label_str # label do nó no grafo
                
                # adicionando aresta na árvore e armazenando o id do novo nó
                novo_id = arvore_resultado.gerarFilho(atual['no'], label_str=adj_label, 
                                            label_int=adj.destino, peso=novo_custo)
                
                novo_caminho = atual['caminho'] + [grafo_id] # novo caminho em relação aos nós do grafo

                abertos.append({'no': novo_id, 'custo': novo_custo, 'caminho': novo_caminho})

        abertos.sort(key=lambda x: x['custo']) # ordenando lista de abertos pelo custo do caminho.
        fechados.append(atual)                 # adiciona no já visitado a lista de fechados 
        proximo = abertos.pop(0)               # visitando o nó de caminho mais curto

        atual = proximo
        grafo_id = arvore_resultado.getNo(atual['no']).label_int # id do nó da arvore no grafo 
        no_atual = grafo.getNo(grafo_id)       # nó do grafo original
 
    return arvore_resultado, abertos, fechados