n = 0

for i in range (100,1000):
	for j in range(100,1000):
		k = i * j
		r = str(k)
		if r == r[::-1] and k > n:
			n = k

print n