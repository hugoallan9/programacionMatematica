# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 06:32:29 2016

@author: hugo
"""

import threading

def worker(count):
    for x in range(count):
        print "Programación matemática %s \n " % x
    return
    
threads = list()
t = threading.Thread(target=worker, args=(10,))
threads.append(t)
t.start()
    
print 'Hola mundo'