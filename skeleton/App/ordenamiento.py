# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:24:41 2016

@author: hugo
"""

from time import clock

def burbuja1(lista):
    tiempo_inicial = clock()
    n = len(lista)
    for x in range(n):
        for y in range(x+1,n):
            if not lista[x] <= lista[y]:
                aux = lista[x]
                lista[x] = lista[y]
                lista[y] = aux
    tiempo_final = clock()
    tiempo = tiempo_final - tiempo_inicial
    #print lista
    print 'El tiempo de ejecución fue de ', tiempo

def merge(izquierda, derecha):
    resultado = []
    while izquierda != [] and derecha != []:
        if izquierda[0] <= derecha[0]:
            resultado.append(izquierda.pop(0))
        else:
            resultado.append(derecha.pop(0))
    if izquierda != []:
        resultado = resultado + izquierda
    if derecha != []:
        resultado = resultado + derecha
    return resultado
            
    
    
   
def mergeSort(lista):
        izquierda, derecha = [], [] 
        if len(lista) == 1:
            return lista
        else:
            n = len(lista)
            for x in range(n/2):
                izquierda.append(lista[x])
            for y in range(n/2,n):
                derecha.append(lista[y])
        izquierda = mergeSort(izquierda)
        derecha = mergeSort(derecha)
        if izquierda[-1] <= derecha[0]:
            return izquierda + derecha
        else:
            resultado = merge(izquierda,derecha)
            return resultado

    
if __name__ == "__main__":
    l = range(10000)
    burbuja1(l)
    tiempo_inicio = clock()
    l1 = mergeSort(l)
    tiempo_fin = clock()
    print 'Con un tiempo', tiempo_fin - tiempo_inicio
    
                