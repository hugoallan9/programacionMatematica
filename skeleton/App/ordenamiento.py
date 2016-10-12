# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:24:41 2016

@author: hugo
"""

from time import clock

def burbuja1(lista):
    tiempo_inicial = time.clock()
    n = len(lista)
    for x in range(n):
        for y in range(x+1,n):
            if not lista[x] <= lista[y]:
                aux = lista[x]
                lista[x] = lista[y]
                lista[y] = aux
    tiempo_final = time.clock()
    tiempo = tiempo_final - tiempo_inicial
    print lista
    print 'El tiempo de ejecución fue de ', tiempo
    
if __name__ == "__main__":
    l = range(10000)
    burbuja1(l)
    
                