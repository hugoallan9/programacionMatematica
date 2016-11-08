def primo(L):
    fi = list(range(L+1))
    for n in range(2, L+1):
        if fi[n] == n:
            for k in range(n, L+1, n):
                fi[k] = fi[k]-fi[k] // n
    return sum(fi) - 1

print (primo(1000000))
