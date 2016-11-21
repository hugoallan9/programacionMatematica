#Funcion Totiente
def f(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result - set([1])

def primo(m,n):

    if f(m) & f(n):
            return False
    else:
          return True


def n_totiente(n):
 
    if n == 2:
        return 2
    if n == 3:
        return 1.5

    tot = 0
    for k in range(1,n):
        if primo(k,n):
            tot += 1
    return float(n)/tot

def respuesta(n):
    maxnum = {"n/fi(n)" : 0, "n" : 0}
    
    for k in  range(2,n):
        if n_totiente(k) > maxnum["n/fi(n)"]:
            maxnum["n/fi(n)"] = n_totiente(k)
            maxnum["n"] = k
    return maxnum

print (respuesta(1000000))

