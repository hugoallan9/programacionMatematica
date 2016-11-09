#Primo
def primo(n):
    count = 0
    for i in range(2, n):
        if n%i == 0:
            return False
            break
        else:
            count += 1
    if count == n-2:
        return True

def termino(n):
    x = 0
    count = 0
    while count != n:
        x += 1
        if primo(x) == True:
            count += 1
    print (x)
termino(10001)
