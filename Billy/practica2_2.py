Numerador = 0 
Denominador = 1

for i in range(2,1000001):
	j = i * 3 // 7
	if i % 7 == 0:
		j = j - 1
	if j * Denominador > i * Numerador:
		Numerador = j
		Denominador = i

print Numerador