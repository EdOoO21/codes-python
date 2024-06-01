for a in range(1,10000):
    ok = True
    for x in range(1,1000):
        for y in range(1, 1000):
            if ((48 != y + 2*x) or (a < x) or (a < y)) == 0:
                ok = False
                break

    if ok:
        print(a)
