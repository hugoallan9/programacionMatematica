# -*- Coding: utf-8 -*-
import sys

Lista = []

def CargarArchivo(ruta):
	archivo = open(ruta, "r")
	while True:
		linea = archivo.readline()
		if not linea: 
			break
		else:
			arreglo = linea.split()
			Lista.append(float(arreglo[0]))
			
def mergeSort(alist1):
	sys.setrecursionlimit(100000)
	if len(alist1)>1:
		mid1=len(alist1)//2
		lefthalf1 = alist1[:mid1]
		righthalf1 = alist1[mid1:]
		mergeSort(lefthalf1)
		mergeSort(righthalf1)

		i=0
		j=0
		k=0
		while i<len(lefthalf1) and j<len(righthalf1):
			if lefthalf1[i]<righthalf1[j]:
				alist1[k]=lefthalf1[i]
				i=i+1
			else:
				alist1[k]=righthalf1[j]
				j=j+1
			k=k+1

		
		while i<len(lefthalf1):
			alist1[k]=lefthalf1[i]
			i=i+1
			k=k+1

		while j<len(righthalf1):
			alist1[k]=righthalf1[j]
			j=j+1
			k=k+1
			
def ContarVeces(elemento, lista):
	veces = 0
	for i in lista:
		if elemento == i:
			veces = veces + 1
	return veces
	
def EncontrarNumero(lista):
	Aux1 = 0 
	Aux2 = 0 
	for i in lista:
		if ContarVeces(i,lista) > Aux1:
			Aux1 = ContarVeces(i, lista)
			Aux2 = i
		else:
			Aux1 = Aux1
			Aux2 = Aux2
	return Aux2
			
CargarArchivo("C:\Users\Othmaro\Desktop\practica 1\prueba.txt")
mergeSort(Lista)		
EncontrarNumero(Lista)
print EncontrarNumero(Lista)