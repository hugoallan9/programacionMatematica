#*-* coding: utf-8 -*-
import os

NUMEROS=[]

def IngresarNumero(dato):
	try:							
		float(dato)
		retorno = True
	except ValueError:
		retorno = False
	return(retorno)	

os.system('cls')
Num=raw_input("Introduzca un numero o presione enter para salir: ")
while True:
	if IngresarNumero(Num) == True:
		NUMEROS.append(Num)
		Num = raw_input("Introduzca un nuevo numero o presione enter si desea continuar: ")
	elif Num == "":
		os.system('cls')
		break
	else:
		print "Ingrese solo numeros"
		Num = raw_input("Introduzca un nuevo numero o presione enter si desea continuar: ")

if (len(NUMEROS) == 0):
	print "Usted no ha ingresado numeros"
else:
	menor = min(NUMEROS)
	print "El menor numero ingresado es: ", menor
	
raw_input("Pulse cualquier tecla seguido de Enter para finalizar: ")
