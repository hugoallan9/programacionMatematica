# -*- coding: cp1252 -*-

import os

N=[]
N2= []
i=0
print 'Para salir del programa presione Enter!'
print ''
N.append(raw_input('Ingrese un numero: '))
while N[i] != '':
	N.append(raw_input('Ingrese un numero: '))
	N2.append(float(N[i]))
	i=i+1

print "El menor de los numeros es: " + str(min(N2))