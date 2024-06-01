def d(a,b):
    return a % b == 0
for a in range(1,10000):
    ok = True
    for x in range(-1000,1000):
        if ((not(d(x,a)))<=(d(x,6)<=(not(d(x,9))))) == 0:
            ok = False
            break
    if ok:
        print(a)