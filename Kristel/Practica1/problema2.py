# -*- coding: utf-8 -*-
class Pila:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def isEmpty(self):
        return self.items == []
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]

pila = Pila()

archivo = open('prueba2.txt','r')
lineas = archivo.readlines()
lin1 = []
lin2 = []
print (lineas)
for word in lineas:
    lin1.append(word.replace( '\n' ,' '))
    lineas = []
print (lin1)
for word in lin1:
    lin2.append(word.replace(' ',' '))
lin1 = []
print (lin2)
for word in lin2: 
    str = word
    for x in range(0,len(str)): 
        if (str[x] == '(' or str[x] == '['):
            pila.push(str[x])
        elif str[x] == ')':
            if pila.isEmpty() == True:
                print ('Error')
                break
            if pila.peek() == '(':
                pila.pop()
            elif pila.peek() == '[':
                print ('Error')
                break
        elif str[x] == ']':
            if pila.isEmpty() == True:
                print ('Error')
                break
            if pila.peek() == '[':
                pila.pop()
            elif pila.peek() == '(':
                print ('Error')
                break
        if x == len(str)-1:
            if pila.isEmpty() == True:
                print ('Parentizado adecuadamente')
    if pila.isEmpty() == False:
        while pila.isEmpty() != True:
            pila.pop()
