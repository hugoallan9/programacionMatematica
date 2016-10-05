#-*- coding: utf-8 -*-
import os

# Cabecera del Menu 1
def Formato():
	formato = '%-*s%*s'
	print "#" * 25
	print "#" * 25
	print formato % (22 , "## 1. Triangulo" , 3 , "##")
	print formato % (22 , "## 2. Rectangulo" , 3 , "##")
	print formato % (22 , "## 3. Cuadrado" , 3 , "##")
	print formato % (22 , "## (Enter) Salir" , 3, "##")
	print "#" * 25
	print "#" * 25

# Cabecera del Menu 2_i
def Formato1():
	formato2 = '%-*s%*s'
	print "#" * 25
	print "#" * 25
	print formato2 % (22 , "## 1. Rellena", 3 , "##")
	print formato2 % (22 , "## 2. Vacia" , 3 , "##")
	print formato2 % (22, "## (Enter) Regresar" , 3 , "##")
	print "#" * 25
	print "#" * 25
	
# Control de error en las opciones de los menus 1 y 2_i
def IngresarOpcion(dato):
	try:							
		float(dato)
		retorno = True
	except ValueError:
		retorno = False
	return(retorno)	
	
# Control de error al ingresar datos en los triangulos, rectangulos o cuadrados
def IngresarDato(dato):
	try:							
		int(dato)
		retorno = True
	except ValueError:
		retorno = False
	return(retorno)	

# Menu principal del programa
def Menu1():
	os.system("cls")
	Formato()
	elec1 = raw_input("Cual figura desea obtener: ")
	while True:
		while IngresarOpcion(elec1) == True:
			aux = float(elec1)
			if aux == 1:
				Menu2_1()
				os.system("cls")
				Formato()
				elec1 = raw_input("Cual figura desea obener: ")
			elif aux == 2:
				Menu2_2()
				os.system("cls")
				Formato()
				elec1 = raw_input("Cual figura desea obener: ")
			elif aux == 3:
				Menu2_3()
				os.system("cls")
				Formato()
				elec1 = raw_input("Cual figura desea obener: ")
			else:
				break
		if elec1 == "":
			break
		else:
			os.system("cls")
			print "No existe esa opcion"
			Formato()
			elec1 = raw_input("Cual figura desea obener: ")
	
# Submenu del menu principal	
def Menu2_1():
	os.system("cls")
	Formato1()
	elec2 = raw_input("Como desea su figura: ")
	while True:
		if IngresarOpcion(elec2) == True:
			aux2 = float(elec2)
			if aux2 == 1:
				os.system("cls")
				TrianguloR()
				break
			elif aux2 == 2:
				os.system("cls")
				TrianguloH()
				break
			else:
				os.system("cls")
				print "No existe esa opcion"
				Formato1()
				elec2 = raw_input("Como desea su figura: ")
		elif elec2 == "":
			break
		else:
			os.system("cls")
			print "No existe esa opcion"
			Formato1()
			elec2 = raw_input("Como desea su figura: ")

# Submenu del menu principal			
def Menu2_2():
	os.system("cls")
	Formato1()
	elec2 = raw_input("Como desea su figura: ")
	while True:
		if IngresarOpcion(elec2) == True:
			aux2 = float(elec2)
			if aux2 == 1:
				os.system("cls")
				RectanguloR()
				break
			elif aux2 == 2:
				os.system("cls")
				RectanguloH()
				break
			else:
				os.system("cls")
				print "No existe esa opcion"
				Formato1()
				elec2 = raw_input("Como desea su figura: ")
		elif elec2 == "":
			break
		else:
			os.system("cls")
			print "No existe esa opcion"
			Formato1()
			elec2 = raw_input("Como desea su figura: ")

# Submenu del menu principal			
def Menu2_3():
	os.system("cls")
	Formato1()
	elec2 = raw_input("Como desea su figura: ")
	while True:
		if IngresarOpcion(elec2) == True:
			aux2 = float(elec2)
			if aux2 == 1:
				os.system("cls")
				CuadradoR()
				break
			elif aux2 == 2:
				os.system("cls")
				CuadradoH()
				break
			else:
				os.system("cls")
				print "No existe esa opcion"
				Formato1()
				elec2 = raw_input("Como desea su figura: ")
		elif elec2 == "":
			break
		else:
			os.system("cls")
			print "No existe esa opcion"
			Formato1()
			elec2 = raw_input("Como desea su figura: ")

# Algoritmo para crear el triangulo relleno
def TrianguloR():
	base = raw_input("Ingrese la longitud de la base del triangulo (Enteros): ")
	while True:
		if IngresarDato(base) == True:
			base = int(base)
			aux = base + 1
			for i in range(1,aux):
				formato2 = '%*s'
				salto = base + i
				print formato2 % (salto , "+ " * i)
				i = i + 1 
			raw_input("Pulse enter o cualquier tecla seguido de enter para seguir: ")
			break
		else:
			os.system("cls")
			base = raw_input("Dato ingresado incorrecto, ingrese la longitud de la base del triangulo (Enteros): ")

# Algoritmo para crear el triangulo vacio			
def TrianguloH():
	base = raw_input("Ingrese la longitud de la base del triangulo (Enteros): ")
	while True:
		if IngresarDato(base) == True:
			base = int(base)
			aux = base + 1
			for i in range(1,aux):
				if i == 1 or i == base:
					formato2 = '%*s'
					salto = base + i
					print formato2 % (salto , "+ " * i)
					i = i + 1 
				else:
					formato3 = "%*s%*s"
					salto1 = base - i + 1
					salto2 = 2 * (i - 1)
					print formato3 % (salto1 , "+" , salto2 , "+")
					i = i + 1
			raw_input("Pulse enter o cualquier tecla seguido de enter para seguir: ")		
			break
		else:
			os.system("cls")
			base = raw_input("Dato ingresado incorrecto, ingrese la longitud de la base del triangulo (Enteros): ")

# Algoritmo para crear el rectangulo relleno			
def RectanguloR():
	base = raw_input("Ingrese la longitud de la base del rectangulo (Enteros): ")
	altura = raw_input("Ingrese la longitud de la altura del rectangulo (Enteros): ")
	while True:
		if (IngresarDato(base) == True and IngresarDato(altura) == True):
			base = int(base)
			altura = int(altura)
			aux = altura + 1
			for i in range(1,aux):
				print "+ " * base
				i = i + 1
			raw_input("Pulse enter o cualquier tecla seguido de enter para seguir: ")
			break
		elif (IngresarDato(base) == True and IngresarDato(altura) == False):
			os.system("cls")
			altura = raw_input("Dato ingresado incorrecto, Ingrese la longitud de la altura del rectangulo (Enteros): ")
		elif (IngresarDato(base) == False and IngresarDato(altura) == True):
			os.system("cls")
			base = raw_input("Dato ingresado incorrecto, Ingrese la longitud de la base del rectangulo (Enteros)")
		else:
			os.system("cls")
			print "Datos Incorrectos"
			base = raw_input("Ingese la longitud de la base del rectangulo (Enteros): ")
			altura = raw_input("Ingrese la longitud de la altura del rectangulo (Enteros): ")

# Algoritmo para crear el rectangulo vacio
def RectanguloH():
	base = raw_input("Ingrese la longitud de la base del rectangulo (Enteros): ")
	altura = raw_input("Ingrese la longitud de la altura del rectangulo (Enteros): ")
	while True:
		if (IngresarDato(base) == True and IngresarDato(altura)) == True:
			base = int(base)
			altura = int(altura)
			aux = altura + 1
			for i in range(1,aux):
				if i == 1 or i == altura:
					print "+ " * base
					i = i + 1
				else:
					formato = "%s%*s"
					aux1 = 2 * base - 2
					print formato % ("+" , aux1, "+")
					i = i + 1
			raw_input("Pulse enter o cualquier tecla seguido de enter para seguir: ")
			break
		elif (IngresarDato(base) == True and IngresarDato(altura) == False):
			os.system("cls")
			altura = raw_input("Dato ingresado incorrecto, Ingrese la longitud de la altura del rectangulo (Enteros) : ")
		elif (IngresarDato(base) == False and IngresarDato(altura) == True):
			os.system("cls")
			base = raw_input("Dato ingresado incorrecto, Ingrese la longitud de la base del rectangulo (Enteros): ")
		else:
			os.system("cls")
			print "Datos Incorrectos"
			base = raw_input("Ingrese la longitud de la base del rectangulo (Enteros): ")
			altura = raw_input("Ingrese la longitud de la altura del rectangulo (Enteros): ")

# Algoritmo para crear el cuadrado relleno
def CuadradoR():
	base = raw_input("Ingrese la longitud del lado del cuadrado (Enteros): ")
	while True:
		if IngresarDato(base) == True:
			base = int(base)
			aux = base + 1
			for i in range(1,aux):
				print "+ " * base
				i = i + 1
			raw_input("Pulse enter o cualquier tecla seguido de enter para seguir: ")
			break
		else:
			os.system("cls")
			print "Datos Incorrectos"
			base = raw_input("Ingrese la longitud del lado del cuadrado (Enteros): ")

# Algoritmo para crear el cuadrado relleno
def CuadradoH():
	base = raw_input("Ingrese la longitud del lado del cuadrado (Enteros): ")
	while True:
		if IngresarDato(base) == True:
			base = int(base)
			aux = base + 1
			for i in range(1,aux):
				if i == 1 or i == base:
					print "+ " * base
					i = i + 1
				else:
					formato = "%s%*s"
					aux1 = 2 * base - 2
					print formato % ("+" , aux1, "+")
					i = i + 1
			raw_input("Pulse enter o cualquier tecla seguido de enter para seguir: ")
			break
		else:
			os.system("cls")
			print "Datos Incorrectos"
			base = raw_input("Ingrese la longitud del lado del cuadrado (Enteros): ")

# LLamada al Menu principal para iniciar el programa.
Menu1()