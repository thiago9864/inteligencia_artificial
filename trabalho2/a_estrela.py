from grafo import Grafo
from Arvore import  Arvore

def busca_a_estrela(grafo, no_origem, no_destino):
    arvore_resultado = Arvore()
    no_atual = grafo.getNo(no_origem)
    no_destino = grafo.getNo(no_destino)

    atual_id = arvore_resultado.gerarRaiz(no_atual.label_str, label_int=no_atual.id)

    atual = {'no': atual_id, 'custo': 0, 'caminho': []}
    destino = no_destino.id
    fechados = [atual]
    abertos = []


    while arvore_resultado.getNo(atual['no']).label_int != no_destino.id:

        for adj in no_atual.arestas:

            if adj.destino not in atual['caminho']:
                grafo_id = arvore_resultado.getNo(atual['no']).label_int

                novo_custo = grafo.getAresta(grafo_id, adj.destino).peso + atual['custo'] + grafo.getNo(
                    grafo_id).getHeu()

                adj_label = grafo.getNo(adj.destino).label_str

                novo_id = arvore_resultado.gerarFilho(atual['no'], label_str=adj_label,
                                                      label_int=adj.destino, peso= grafo.getAresta(grafo_id, adj.destino).peso,
                                                      heuristica=novo_custo)

                novo_caminho = atual['caminho'] + [grafo_id]

                abertos.append({'no': novo_id, 'custo': novo_custo, 'caminho': novo_caminho})

        abertos.sort(key=lambda x: x['custo'])  # ordenando lista de abertos pelo custo do caminho.
        fechados.append(atual)
        proximo = abertos.pop(0)

        atual = proximo
        grafo_id = arvore_resultado.getNo(atual['no']).label_int
        no_atual = grafo.getNo(grafo_id)

    return arvore_resultado, abertos, fechados





