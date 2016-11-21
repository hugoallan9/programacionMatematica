#problema 87
import eulerlib, math

primos = eulerlib.primes(math.sqrt(50000000)) #Lista de numeros primos menores que la raiz cuadrada de 50000000
numeros = {0}

for i in range(2,5): #Recorre los posibles exponentes para los primos [2,3,4]
	numerosaux = set()
	for p in primos: 
		q = p ** i #Prueba las posibles combinaciones entre exponentes y primos
		if q > 50000000:
			break
		for x in numeros:
			if x + q <= 50000000:
				numerosaux.add(x + q)
	numeros = numerosaux

m = len(numeros)
print m
