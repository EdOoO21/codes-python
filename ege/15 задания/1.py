def d(a,b):
    return a % b == 0

for a in range(1,10000):
    ok = True
    for x in range(1,1000):
        if ((d(x,13) <= (not(d(x,21)))) or (x + a >= 500)) == 0:
            ok = False
            break

    if ok:
        print(a)
        break