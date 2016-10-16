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
			Lista.append(arreglo[0])

class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]
		
CargarArchivo("C:\Users\Othmaro\Desktop\practica 1\prueba1.txt")

def Parentizar(lista):
	Aux = ""
	Guardar = Stack()
	if len(lista) % 2 == 1:
		return "esta mal parentizada"
	else:
		if lista[0] == ")" or lista[0] == "]":
			return "esta mal parentizada"
		else:
			for i in lista:
				if i == "(" or i == "[":
					Guardar.push(i)
				else:
					Aux = i
					if Aux == ")" and Guardar.peek() == "(":
						Guardar.pop()
					elif Aux == "]" and Guardar.peek() == "[":
						Guardar.pop()
					else:
						Guardar.push(Aux)
						break
			if Guardar.isEmpty() == True:
				return "esta bien parentizada"
			else:
				return "esta mal parentizada"
			
j = 0		
for i in Lista:
	j = j + 1
	m = str(j)
	Aux1 = []
	for k in i:
		Aux1.append(k)
	mensaje = Parentizar(Aux1)
	print "La palabra " + m + " " + mensaje
	
raw_input("Pulse cualquier tecla seguido de Enter para finalizar: ")
