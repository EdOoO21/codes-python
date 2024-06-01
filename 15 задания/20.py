for a in range(1,10000):
    ok = True
    for x in range(1,1001):
        if ((90%a==0) and ((x % a != 0) <= ((x % 15 == 0) <= (x % 20 != 0)))) == 0:
            ok = False
            break
    if ok:
        print(a)
        