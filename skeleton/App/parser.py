# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 09:39:40 2016

@author: hugo
"""

from collections import namedtuple
from pprint import pprint as pp


OpInfo = namedtuple('OpInfo', 'prec assoc')
L, R = 'Left Right'.split()

ops = {
    '(': OpInfo(prec = 10, assoc = L),
    '^': OpInfo(prec = 4, assoc = R),
    '*': OpInfo(prec = 3 , assoc = L),
    '/': OpInfo(prec = 3, assoc = L),
    '+': OpInfo(prec = 2, assoc = L),
    '-': OpInfo(prec =2, assoc =L),
    ')': OpInfo(prec = 0, assoc = L)
}

NUM, LPAREN, RPAREN = 'NUMBER ( )'.split()


def get_input(infix= None):
    if infix is None:
        infix = raw_input(' \n Escribe la expresión: \n')
    tokens = infix.strip().split()
    tokenvals = []
    for token in tokens:
        if token in ops:
            tokenvals.append( (token, ops[token]) )
        else:
            tokenvals.append( (NUM, token) ) 
    return tokenvals
    
def parse_rpn(tabla):
    outq, stack = [], []
    table =  ['TOKEN', 'ACTION', 'RPN', 'OUTPUT', 'OP STACK', 'NOTES']
    for token, val in tabla:
        note = ''
        action = ''
        if token is NUM:
            action = 'Agregando el número a la salida'
            outq.append(val)
            table.append(val, action, ' '.join(outq), '' , '', note)
        elif token in ops:
            t1, (p1, a1) =  token, val
            v = t1
            note = 'Pop ops de la pila a la cola'
            while stack:
                t2,(p2, a2)=  stack[-1]
                if (a1 == L and p1 <= p2) or (a1 == R and p1 < p2):
                    if t1 != RPAREN:
                        if t2 != LPAREN:
                            stack.pop()
                            action = '(Pop al operador)'
                            outq.append(t2)
                        else:
                            break
                            
                                    
            
                        
            
    


