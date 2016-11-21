#Suma
def sum_digitos(x):
  res = 0
  while x > 0:
    res += x % 10
    x /= 10
  return res

cache = {}

def nb(digitos, alfa, beta):
  k = (digitos, alfa, beta)
  if k in cache: return cache[k]
  if digitos == 1:
    res = 0
    for x in range(0, 10):
      res += 1 if sum_digitos(137*x + alfa) == sum_digitos(x) + beta else 0
  else:
    res = 0
    for x in range(0, 10):
      alfa_b = (137 * x + alfa) / 10
      beta_b = beta + x - (137 * x + alfa) % 10
      res += nb(digitos - 1, alfa_b, beta_b)
  cache[k] = res
  return res
print (nb(18, 0, 0))
