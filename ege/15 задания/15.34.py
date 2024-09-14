for a in range(1,10000):
    ok = True
    for x in range(1,1000):
        if ((x & 85 == 0) <= ((x & 54 != 0) <= (x & a != 0))) == 0:
            ok = False
            break
    if ok:
        print(a)
        break