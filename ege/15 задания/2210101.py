def d(a,b):
    return a % b == 0
for A in range(-100,10000):
    ok = True
    for x in range(1,1000):
        if ((d(72, x) <= (not(d(120, x)))) or (A - x > 100)) == 0:
            ok = False
            break
    if ok:
        print(A)
        break
