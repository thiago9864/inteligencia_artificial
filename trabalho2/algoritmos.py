def busca_ordenada(grafo, origem, destino):

    # durante a execução cada nó terá o custo do caminho e a lista de nós do caminho
    atual = {'no': origem, 'custo': 0, 'caminho': [origem]}
    abertos = [atual]
    fechados = []

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