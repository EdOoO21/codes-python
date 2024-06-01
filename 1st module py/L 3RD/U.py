n = int(input())
global k
k=1

def phib(a, b, c):
    global k
    if b == n:
        return k
    k += 1
    return phib(b, c, c + b)


print(phib(0, 1, 1))
