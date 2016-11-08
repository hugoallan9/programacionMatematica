def fibonachi(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonachi(n-1) + fibonachi(n-2)

n = 0
m = 0
while fibonachi(n) < 4000000:
	if fibonachi(n) % 2 == 0:
		m = m + fibonachi(n)
		n = n + 1 
	else:
		n = n + 1 
		
print m