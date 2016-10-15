# -*- coding: utf-8 -*-
print 'Si desea un triángulo presione   1 \nSi desea un cuadrado presione    2 \nSi desea un rectángulo presione  3'
a = 0
while a < 3:
	a = a + 1

	figura = input()

	ancho = int(input('Ingrese el ancho: \n '))

	if figura == 1:
		for x in range(1, ancho):
			print x * '♠' 

	elif figura == 2:
		for x in range(ancho):
			print '┼┼┼' * ancho

	elif figura == 3:
		for x in range(ancho):
			print '████' * ancho