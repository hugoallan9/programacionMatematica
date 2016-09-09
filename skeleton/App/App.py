from pila import *

pila = Stack()
print 'La pila esta vacia: ', pila.isEmpty()
pila.push('(')
pila.push('(')
pila.push(')')
print 'La pila esta vacia: ', pila.isEmpty()
print 'La pila tiene ', pila.size(), 'elementos'
print 'El elemento en la cima de la pila es ', pila.peek()
print 'La pila tiene ', pila.size(), 'elementos'
print pila.pop()
print 'La pila tiene ', pila.size(), 'elementos'
