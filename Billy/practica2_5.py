#problema 52
import itertools

for i in itertools.count(1):
	digitos = sorted(str(i)) # ordena los digitos de i
	if all(sorted(str(i * j)) == digitos for j in range(2,7)): #Compara los digitos ordenados de los productos con los digitos ordenados del inicial
		print i
		break
