def de(a,b):
    return a % b == 0
def f(x,A):
    return( de(120,A)and((not(de(x,A)))<=(de(x,36)<=(not(de(x,15)))))) == 1
for A in range(1,10000):
    ok = True
    for x in range(1,1000):
        if not(f(x,A)):
            ok = False
            break
    if ok:
        print(A)