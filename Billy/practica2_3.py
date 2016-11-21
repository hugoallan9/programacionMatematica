#problema 112
import itertools

n = 0

for i in itertools.count(1):
	j = str(i)
	k = "".join(sorted(j)) #Teniendo la cadena j lo ordena de menor a mayor
	if j != k and j[::-1] != k: #Evalua que el numero visto como cadena no sea creciente o decreciente
		n = n + 1
	if n * 100 == 99 * i: #Busca el 99 porciento 
		print i
		break
