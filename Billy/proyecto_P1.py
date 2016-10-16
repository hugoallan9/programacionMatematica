#*-* coding: utf-8 -*-
import os

def IngresarNumero(dato):
	try:							
		int(dato)
		retorno = True
	except ValueError:
		retorno = False
	return(retorno)	

def TorreHanoi(discos, inicio = 1, fin = 3):
	if discos == 1:
		print "Mueve el disco en la columna %d a la columna %d" % (inicio,fin)
	else:
		TorreHanoi(discos - 1, inicio, 6 - inicio - fin)
		print "Mueve el disco en la columna %d a la columna %d" % (inicio, fin)
		TorreHanoi(discos - 1, 6 - inicio - fin, fin)
		
Numero = raw_input("Ingresa el numero de discos que deseas ver la solucion: ")
while True:
	if IngresarNumero(Numero) == True:
		Numero = int(Numero)
		if Numero <= 1:
			os.system("cls")
			Numero = raw_input("Ingresa un numero de discos valido: ")
		else:
			os.system("cls")
			TorreHanoi(Numero)
			n = 2 ** Numero - 1
			print "El numero de movimientos fue: %d" % (n)
			break
	else:
		os.system('cls')
		Numero = raw_input("Ingresa un numero de discos valido: ")

raw_input("Pulse cualquier tecla seguido de Enter para finalizar: ")
