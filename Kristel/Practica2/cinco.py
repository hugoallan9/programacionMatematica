#Problema250


def calcular():
	MOD = 10**16
	sub = [0] * 250  
	sub[0] = 1
	
	for i in range(1, 250250 + 1):
		nsubs = list(sub)
		temp = pow(i, i, 250)
		for j in range(len(sub)):
			k = (j + temp) % 250
			nsubs[k] = (sub[j] + sub[k]) % MOD
		sub = nsubs
	
	sol = (sub[0] - 1) % MOD
	return str(sol)


if __name__ == "__main__":
    print(calcular())



