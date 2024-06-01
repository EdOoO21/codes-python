def d(a,b):
     return a % b == 0
for a in range(1,10000):
    ok = True
    for x in range(1,1000):
        if (d(x,18) <= ((not(d(x,a))) <= (not(d(x,12))))) ==0:
            ok = False
            break
    if ok:
        print(a)