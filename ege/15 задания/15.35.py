def d(a,b):
    return a % b == 0
for a in range(1,10000):
    ok = True
    for x in range(1,1000):
        if ((d(a, 40)) and ((d(780, x)) <= ((not(d(a, x))) <= (not(d(180, x))))))==0:
            ok = False
            break
    if ok:
        print(a)
        break