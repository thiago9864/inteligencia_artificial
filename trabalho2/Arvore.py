# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:34:23 2019

@author: Thiago
"""

from No import No
from Aresta import Aresta

class Arvore:
    grafo = []
    arestas_unicas = []#arestas unicas usadas pra imprimir o grafo
    ultimo_id=0#gera o id unico pra cada vertice criado
    
    #construtor
    def __init__(self):
        self.grafo = []
        self.arestas_unicas = []#arestas unicas usadas pra imprimir o grafo
        self.ultimo_id=0#gera o id unico pra cada vertice criado

        

    ### Vertice ###
    
    
    def getNo(self, id):
        
        try:
            id_no = int(id)
        except ValueError:
            print("ValueError: O valor do Id tem que ser um número.")
            return None
        
        for no in self.grafo:
            if(no.id == id_no):
                return no
        return None
        
    
    def getNoWithLabel(self, id):
        return self.getNo(id).label
    
    def removeNo(self, id):
        no = self.getNo(id)
        if(no != False):
            #remove as arestas associadas a ele
            for a in no.arestas:
                #remove a origem de todos os nós associados
                self.getNo(a.destino).removeAresta(a.origem)
                                    
                #retira aresta da lista de arestas unicas
                self.removeArestaUnica(a.origem, a.destino)
                    
            #remove vertice do grafo
            self.grafo.remove(no)
        else:
            print("nó "+str(id)+" não encontrado")
            
        
    def setLabelVertice(self, id, label):
        no = self.getNo(id)
        if(no != False):
            no.label = label
            
    ### Aresta ###
    
    
    def removeArestaUnica(self, origem, destino):
        
        try:
            id_origem = int(origem)
        except ValueError:
            print("ValueError: O valor do Id de origem tem que ser um número.")
            return False
        
        try:
            id_destino = int(destino)
        except ValueError:
            print("ValueError: O valor do Id de destino tem que ser um número.")
            return False
        
        for a in self.arestas_unicas:
            if((a.origem==id_origem and a.destino==id_destino) or (a.origem==id_destino and a.destino==id_origem)):
                print('removeu a aresta', id_origem, id_destino)
                self.arestas_unicas.remove(a)
                return True
        return False
    
    
    
    def addAresta(self, origem, destino, peso):
        
        try:
            id_origem = int(origem)
        except ValueError:
            print("ValueError: O valor do Id de origem tem que ser um número.")
            return False
        
        try:
            id_destino = int(destino)
        except ValueError:
            print("ValueError: O valor do Id de destino tem que ser um número.")
            return False
        
        no_origem = self.getNo(id_origem)
        no_destino = self.getNo(id_destino)
        
        if no_origem==False:
            no_origem = No(id_origem)
            #define o child_id que vai diferenciar os filhos quando gerar a arvore
            no_origem.id_ref = 0
            #adiciona o vertice no grafo
            self.grafo.append(no_origem)
        
        if no_destino==False:
            no_destino = No(id_destino)
            #define o child_id que vai diferenciar os filhos quando gerar a arvore
            no_destino.id_ref = 0
            #adiciona o vertice no grafo
            self.grafo.append(no_destino)
            
        #cria arestas
        aresta_1 = Aresta(id_origem, id_destino, peso)
        aresta_2 = Aresta(id_destino, id_origem, peso)
        
        #coloca as arestas nos vertices
        no_origem.arestas.append(aresta_1)
        no_destino.arestas.append(aresta_2)
        
        #salva uma delas pra representar a aresta unica
        self.arestas_unicas.append(Aresta(id_origem, id_destino, peso))
        
        return True
        
    
    def getAresta(self, origem, destino):
        
        try:
            id_origem = int(origem)
        except ValueError:
            print("ValueError: O valor do Id de origem tem que ser um número.")
            return False
        
        try:
            id_destino = int(destino)
        except ValueError:
            print("ValueError: O valor do Id de destino tem que ser um número.")
            return False
        
        no = self.getNo(id_origem)
        if no==False:
            return False
        
        for a in no.arestas:
            if a.destino == id_destino:
                return a
        return None
    
    def removeAresta(self, origem, destino):
        a1 = self.getAresta(origem, destino)
        if a1!=False:
            a2 = self.getAresta(destino, origem)
            self.getNo(origem).arestas.remove(a1)
            self.getNo(destino).arestas.remove(a2)
            return True
        return False
    
    ### criação dos estados e filhos ###
    
    #gera um filho isolado, em geral a raiz
    def gerarRaiz(self, label_str, label_int=0, heuristica=None):
        
        try:
            label_int = int(label_int)
        except ValueError:
            print("ValueError: O valor do de ref_id_grafo tem que ser um número.")
            return None
        
        #incrementa o ultimo id
        self.ultimo_id+=1
        
        #cria um novo nó
        no = No(self.ultimo_id)
        no.label_int = label_int
        no.label_str = label_str
        no.setHeu(heuristica)
        self.grafo.append(no)
        
        return self.ultimo_id #retorna o id pra gerar os filhos
    
    
    #gera um filho isolado, em geral a raiz
    def gerarFilho(self, id_pai, label_str, label_int=0, peso=0, heuristica=None):
        
        try:
            id_pai = int(id_pai)
        except ValueError:
            print("ValueError: O valor do Id do pai tem que ser um número.")
            return None
        
        try:
            label_int = int(label_int)
        except ValueError:
            print("ValueError: O valor do de label_int tem que ser um número.")
            return None
        
        #incrementa o ultimo id
        self.ultimo_id+=1
        
        #gera o nó do filho
        no = No(self.ultimo_id)
        no.label_int = label_int
        no.label_str = label_str
        no.setHeu(heuristica)
        self.grafo.append(no)
        
        #cria a aresta
        self.addAresta(id_pai, self.ultimo_id, peso)
        
        #retorna o id do filho gerado
        return self.ultimo_id 
    
    def getNo_heu(self, heuristica):
        for no in self.grafo:
            if float(no.getHeu()) == float(heuristica):
                return no
        return None
        
    
    
 

    ### Funcoes extra ### 

         
    def salvarArquivoGraphViz(self, nome_arquivo):
        f_graphviz = open(nome_arquivo, 'w+')
        #escreve inicio do arquivo
        f_graphviz.write('graph {\n')
        
        #print(self.arestas_unicas)
        
        #escreve arestas
        for a in self.arestas_unicas:
            o = self.getNo(a.origem)
            d = self.getNo(a.destino)
            #labels que diferenciam um nó do outro
#            oc = "_"+str(o.id) + " (" + str(o.heuristica()) + ")"
#            dc = "_"+str(d.id) + " (" + str(d.heuristica()) + ")"
            if o.getHeu() == None:
                oc = "_"+str(o.id)
            else:
                oc = " (" + str(o.getHeu()) + ")"
            
            if d.getHeu() == None:
                dc = "_"+str(d.id)
            else:
                dc = " (" + str(d.getHeu()) + ")"
                
            if a.peso!=0:
                f_graphviz.write('   "'+o.label_str + oc + '"--"' + d.label_str + dc + '" [label=' + str(a.peso) + ']\n')
            else:
                f_graphviz.write('   "'+o.label_str + oc + '"--"' + d.label_str + dc + '"\n')
            
        #escreve fim do arquivo
        f_graphviz.write('}')
        
        #fecha arquivo
        f_graphviz.close()
        print("Arquivo GraphViz gerado.")
        