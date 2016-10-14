# -*- coding: utf8 -*-
import os

lista = []

def LecturaDatos(ruta):
    archivo = open(ruta, 'r')
    while True:
	linea = archivo.readline()
	if not linea:
	    break
	else: 
	    arreglo = linea.split()
	    lista.append(float(arreglo[0]))    

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


while True:
    Entrada=raw_input("Presione Enter")

    if Entrada=="":
        LecturaDatos('C:\Users\MAMA TIVO\Desktop\listado.txt')
        os.system('cls')
        print "La lista de numeros es:"
        print lista
        mergeSort(lista)
	n = len(lista)
        c, aux1, aux2 = 1, 0, 0
	for x in range(0, n-1):
            if lista[x]==lista[x+1]:
                c=c+1
            elif aux1<c:
                aux1=c
                aux2=lista[x]
                c=1
            else:
                c=1
        print "Numero menor que se repite mas veces: " + str(aux2)
        break
    else:
        break




