#*-* coding:utf8 -*-

ancho = input('Ingrese el ancho: \n ')

ancho_precio = 10
ancho_item = ancho - ancho_precio 

print '=' * ancho 

formato_cabecera = '%-*s%*s'
formato = '%-*s%*.2f'

print '-' * ancho 

print formato_cabecera % (ancho_item, 'Item', ancho_precio, 'Precio')
print '-' * ancho 
print formato % (ancho_item, 'Manzanas', ancho_precio, 15.78)
print formato % (ancho_item, 'Cereal', ancho_precio, 22)
print formato % (ancho_item, 'Leche Deslactosada', ancho_precio, 14.50)

print '-' * ancho 

