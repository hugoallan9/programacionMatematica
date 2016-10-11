# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:07:22 2016

@author: hugo
"""

try: 
    import cPickle as pickle
except ImportError:
    import pickle
    
class Persona():
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def caminar(self, metros):
        print 'Camino', metros, 'metros'
        

enrique = Persona('Enrique', 23)
fichero = file('enrique.dat', 'w')
pickle.dump(enrique, fichero,2)
fichero.close()

fichero2 = file('enrique.dat', 'r')
enrique2 = pickle.load(fichero2)
enrique2.caminar('10')


        

    
