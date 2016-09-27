# -*- coding: utf-8 -*-
class Pila:
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
        return self.items[len(self.items)-1]

def menu():
    print '='*20
    print '(1) Problema 1'
    print '(2) Problema 2'
    print '(3) Problema 3'
    print '(4) Salir'
    print '='*20,'\n'

def problem2():
    pila = Pila()

    archivo = open('C:\Users\Yovanni\Desktop\Practica1\ArchivoP2.txt','r')
    lineas = archivo.readlines()
    archivo.close()
    lin1 = []
    lin2 = []

    for word in lineas:
        lin1.append(word.replace("\n","")) #eliminamos saltos de linea
    lineas = []

    for word in lin1:
        lin2.append(word.replace(" ","")) #eliminamos espacios vacios
    lin1 = []

    for word in lin2: #recorremos la lista palabra por palabra
        str = word
        for x in range(0,len(str)): #recorremos letra por letra de cada palabra
            if (str[x] == '(' or str[x] == '['):
                pila.push(str[x])
            elif str[x] == ')':
                if pila.isEmpty() == True:
                    print 'Incorrecta'
                    break
                if pila.peek() == '(':
                    pila.pop()
                elif pila.peek() == '[':
                    print 'Incorrecta'
                    break
            elif str[x] == ']':
                if pila.isEmpty() == True:
                    print 'Incorrecta'
                    break
                if pila.peek() == '[':
                    pila.pop()
                elif pila.peek() == '(':
                    print 'Incorrecta'
                    break
            if x == len(str)-1:
                if pila.isEmpty() == True:
                    print 'Correcta'
        if pila.isEmpty() == False:
            while pila.isEmpty() != True:
                pila.pop()


def problem3():
    archivo = open('C:\Users\Yovanni\Desktop\Practica1\ArchivoP3.txt','r')
    lineas = archivo.readlines()
    archivo.close()

    numeros = []

    for numero in lineas:
        numeros.append(float(numero.replace("\n","")))
    numeros.sort()

    lista = []

    for x in numeros:
        lista.append(numeros.count(x))

    print 'El número más pequeño que más veces se repite es: ', numeros[lista.index(max(lista))]




op = ''
while op != '4':
    menu()
    op = raw_input('Ingrese el número del problema a realizar: ')
    print '\n'
    if op == '2':
        problem2()
    elif op == '3':
        problem3()
