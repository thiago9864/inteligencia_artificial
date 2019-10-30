# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:34:23 2019

@author: Thiago
"""

#classe que representa o vertice
class No:
    def __init__(self, id):
        self.id = id
        self.label = ""
        self.arestas=[]
        self.id_ref=0#essa variavel é um id de referencia
        self.arestas_peso = []
        self.heu = 0
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

    
#classe que representa arestas
class Aresta:
    def __init__(self, origem, destino, peso, heuristica):
        self.origem=origem
        self.destino=destino
        self.peso=peso
        self.heuristica=heuristica
        
    #retorna peso da Aresta
    def getPeso(self):
        return self.peso
        
        
#Classe que representa o grafo
class Grafo:
    grafo = []
    arestas_unicas = []#arestas unicas usadas pra imprimir o grafo
    child_id_autoincrement=0#gera o id unico pra cada vertice criado
    
    #construtor
    def __init__(self, arquivo_instancia=""):
        
        
        self.grafo = []
        self.arestas_unicas = []#arestas unicas usadas pra imprimir o grafo
        self.child_id_autoincrement=0#gera o id unico pra cada vertice criado
    
        if(arquivo_instancia==""):
            return
        
        #faz a leitura do arquivo da instancia
        with open(arquivo_instancia) as instancia:
            for line in instancia.readlines():
                ls = line.rstrip()
                #print(ls)
                if(ls == 'ARESTAS'):
                    funcao_leitura=1
                    
                elif(ls == 'LABELS'):
                    funcao_leitura=2
                    
                elif(ls == 'END'):
                    funcao_leitura=0
                
                elif(funcao_leitura==1):
                    dados = ls.split(' ')
                    self.addAresta(dados[0], dados[1], int(dados[2]),0)
                
                elif(funcao_leitura==2):
                    dados = ls.split(' ')
                    no = self.getNo(dados[0])
                    print('label:'+str(dados[1]))
                    no.label = dados[1]
        print("Grafo criado")
        for n in self.grafo:
            n.heuristica()
        

    ### Vertice ###
    
    
    def getNo(self, id):
        for no in self.grafo:
            if int(no.id) == id:
                return no
        return False
    
    def getNoWithLabel(self, id):
        return self.getNo(id).label
    
    def removeNo(self, id):
        no = self.getNo(id)
        if no != False:
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
        if no != False:
            no.label = label
            
    ### Aresta ###
    
    
    def removeArestaUnica(self, origem, destino):
        for a in self.arestas_unicas:
            if(a.origem==origem and a.destino==destino) or (a.origem==destino and a.destino==origem):
                print('removeu a aresta',origem,destino)
                self.arestas_unicas.remove(a)
                return True
        return False
    
    def addAresta(self, origem, destino, peso, heuristica):
        
        no_origem = self.getNo(origem)
        no_destino = self.getNo(destino)
        
        if(no_origem==False):
            no_origem = No(origem)
            #define o child_id que vai diferenciar os filhos quando gerar a arvore
            no_origem.id_ref = 0
            #adiciona o vertice no grafo
            self.grafo.append(no_origem)
        
        if(no_destino==False):
            no_destino = No(destino)
            #define o child_id que vai diferenciar os filhos quando gerar a arvore
            no_destino.id_ref = 0
            #adiciona o vertice no grafo
            self.grafo.append(no_destino)
            
        #cria arestas
        aresta_1 = Aresta(origem, destino, peso, heuristica)
        aresta_2 = Aresta(destino, origem, peso, heuristica)
        
        #coloca as arestas nos vertices
        no_origem.arestas.append(aresta_1)
        no_destino.arestas.append(aresta_2)
        
        #salva uma delas pra representar a aresta unica
        self.arestas_unicas.append(Aresta(origem, destino, peso, heuristica))
        
        #ajusta variavel de indices com o maior id recebido da leitura de arquivos
        if(int(origem) > int(self.child_id_autoincrement)):
            self.child_id_autoincrement = origem
            
        if(int(destino)>int(self.child_id_autoincrement)):
            self.child_id_autoincrement = origem;
    
    def getAresta(self, origem, destino):
        no = self.getNo(origem)
        if no==False:
            return False
        
        for a in no.arestas:
            if(int(a.destino) == int(destino)):
                return a
        return False
    
    def removeAresta(self, origem, destino):
        a1 = self.getAresta(origem, destino)
        if(a1!=False):
            a2 = self.getAresta(destino, origem)
            self.getNo(origem).arestas.remove(a1)
            self.getNo(destino).arestas.remove(a2)
            return True
        return False
    
    ### criação dos estados e filhos ###
    
    #gera um filho isolado, em geral a raiz
    def gerarRaiz(self, id_ref, label):
        id_no = self.child_id_autoincrement
        no = No(id_no)
        self.child_id_autoincrement+=1
        no.id_ref = id_ref
        no.label = label
        self.grafo.append(no)
        return id_no #retorna o id pra gerar os filhos
    
    
    #gera um filho isolado, em geral a raiz
    def gerarFilho(self, id_pai, id_ref, label, peso=0, heuristica=0):
        
        id_filho = self.child_id_autoincrement
        self.child_id_autoincrement+=1
        
        #gera o nó do filho
        no = No(id_filho)
        no.id_ref = id_ref
        no.label = label
        self.grafo.append(no)
        
        #cria a aresta
        self.addAresta(id_pai, id_filho, peso, heuristica)
        return id_filho #retorna o id pra gerar os filhos
    
    def getNo_heu(self, heuristica):
        for no in self.grafo:
            if float(no.getHeu()) == float(heuristica):
                return no
        return False
        
    
    
 

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
            oc = " (" + str(o.heuristica()) + ")"
            dc = " (" + str(d.heuristica()) + ")"
            if(a.peso!=0):
                f_graphviz.write('   "'+o.label + oc + '"--"' + d.label + dc + '" [label=' + str(a.peso) + ']\n')
            else:
                f_graphviz.write('   "'+o.label + oc + '"--"' + d.label + dc + '"\n')
            
        #escreve fim do arquivo
        f_graphviz.write('}')
        
        #fecha arquivo
        f_graphviz.close()
        print("Arquivo GraphViz gerado.")
        