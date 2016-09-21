# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:26:45 2016

@author: hugo
"""
import random
import sys
import fileinput
import nltk

class Generador():
    
    def __init__(self, x = 'ausente'):
        self.matriz = []
        self.n = 3
        filaBase = []
        filaBase.append(random.uniform(0,10))


        for x in range(self.n):
            fila = []
            for y in range(self.n):
                temp1 = 0
                temp2 = 0
                try:
                    temp1 = self.matriz[x-1][y]
                except IndexError:
                    pass
                try:
                    temp2 = fila[y-1]
                except IndexError:
                    pass
                entrada =random.uniform(max(temp1,temp2)+1, 1000000)
                fila.append(entrada)
            self.matriz.append(fila)
        self.x = 0
        if x == 'presente':
            self.x = random.choice( random.choice(self.matriz) )
        else:
            self.x = random.random()*random.randint(1,10000)
        self.jugar()
        
    def is_number(self,numero):
            try:
                float(numero)
                return(True)
            except ValueError:
                return False
        
    def parser(self, instruccion):
            longitud = 0            
            tokens = nltk.word_tokenize(instruccion)
            if (tokens[0] != "=" and tokens[0] != "?"):
                return "Inc"
            if ( self.is_number( tokens[1] ) == False ):
                return "Inc"
            longitud = longitud + len(tokens[1])
            if ( self.is_number( tokens[2]) == False):
                return "Inc"
            longitud = longitud + len( tokens[2] )
            
            if( longitud + 1 + 2 != len(instruccion) ):
                return "Cor"
            return ""
            
    def jugar(self):
        print self.n, self.n, self.x
        for x in range(250):
            instruccion = raw_input()
            tokens = nltk.word_tokenize(instruccion)
            if self.parser(instruccion) == '':
                if tokens[0] == '?':
                    try:
                        print self.matriz[int(tokens[1])][int(tokens[2])]
                    except IndexError:
                        print 'Te saliste de los indices'
                else:
                    if int (tokens[1]) >= 0 & int (tokens[2] ) >=0:
                        if self.matriz[ int(tokens[1]) ][ int(tokens[2]) ]  == self.x :
                            return 'Encontrado'
                        else:
                            return 'Inc'
            else:
                pass

                
def getline(stream, delimiter="\n"):
  def _gen():
    while 1:
      line = stream.readline()
      if delimiter in line:
        yield line[0:line.index(delimiter)]
        break
      else:
        yield line
  return "".join(_gen())