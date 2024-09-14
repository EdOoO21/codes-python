for a in range(1,10000):
    ok = True
    for x in range(1,1000):
        for y in range(1,1000):
            if ((2*y + 3*x != 135) or (y > a) or (x > a)) == 0:
                ok = False
                break
    if ok:
        print(a)