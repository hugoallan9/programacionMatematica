#*-* coding:utf8 -*-

ancho = input('Ingrese el ancho: \n ')

ancho_precio = 10
ancho_item = ancho - ancho_precio 

print '=' * ancho 

formato_cabecera = '%-*s%*s'
formato = '%-*s%*.2f'

print '-' * ancho 

print formato_cabecera % (ancho_item, 'Item', ancho_precio, 'Precioj')
