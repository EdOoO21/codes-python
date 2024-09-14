def de(x,L):
    return x % L == 0
def f(x, A):
    return de(45,A) and ((de(x,30) and de(x,12)) <= de(x,A))

for A in range(1,10000):
    ok = True
    for x in range(1,10000):
        if not(f(x, A)):
            ok = False
    if ok:
        print(A)