# -*- coding: utf-8 -*-
archivo = open('C:\Usuarios\Home\Desktop\numeros.txt','r')

lineas = archivo.readlines()
print lineas
numeros = []

for numero in lineas:
    numeros.append(float(numero.replace("\n","")))
    
print numeros
numeros.sort()
print numeros

contador = 0
lista = []

for x in numeros:
    lista.append(numeros.count(x))

print 'El número que más pequeño que se repite más veces es: ', numeros[lista.index(max(lista))]
archivo.close()