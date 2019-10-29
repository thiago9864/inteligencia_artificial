# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:34:23 2019

@author: Thiago
"""
    
class Aresta:
    def __init__(self, origem, destino, peso):
        self.origem=origem
        self.destino=destino
        self.peso=peso
        
    #retorna peso da Aresta
    def getPeso(self):
        return self.peso
