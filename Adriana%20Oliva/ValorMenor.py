# -*- coding: utf-8 -*-
print("Ingrese un número")
var = int(raw_input())
 
for i in range (9):
	print("Ingrese un número")
	var2 = int(raw_input())
	if var2 < var :
		var = var2
print"El valor menor es", var