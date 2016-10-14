# -*- Coding: utf-8 -*-
import calendar
import os

def IngresarNumero(dato):
	try:							
		int(dato)
		retorno = True
	except ValueError:
		retorno = False
	return(retorno)

def Marzo(year):
	a = year % 19
	b = year % 4
	c = year % 7
	d = (19 * a + 24) % 30
	e = (2 * b + 4 * c + 6 * d + 5) % 7
	f = 22 + d + e
	g = d + e - 9
	h = calendar.monthcalendar(year,3)
	if f <= 0 or f > 31:
		return f
	else:
		for i in h:
			if i[calendar.SUNDAY] == f:
				print "El domingo de Pascua es el %d de marzo" % (f)
				break

def Abril(year):
	a = year % 19
	b = year % 4
	c = year % 7
	d = (19 * a + 24) % 30
	e = (2 * b + 4 * c + 6 * d + 5) % 7
	f = 22 + d + e
	g = d + e - 9
	h = calendar.monthcalendar(year,4)
	if g <= 0 or g > 30:
		return g
	else:
		for i in h:
			if i[calendar.SUNDAY] == g:
				print "El domingo de Pascua es el %d de abril" % (g)
				break	

anio = raw_input("Ingresa un anio entre 1900 y 2099: ")
while True:
	if IngresarNumero(anio) == False:
		os.system("cls")
		anio = raw_input("Ingresa un numero en el rango: ")
	else:
		anio = int(anio)
		if (anio >= 1900 and anio < 2100):
			os.system("cls")
			Marzo(anio)
			Abril(anio)
			break
		else:
			os.system("cls")
			anio = raw_input("Ingresa un numero en el rango: ")