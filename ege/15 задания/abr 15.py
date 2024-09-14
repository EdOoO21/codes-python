for a in range(51,10000):
    ok = True
    for x in range(0,10000):
        for y in range(0,1000):
            if ((x < a) or (y < a) or (x + 2*y > 150)) ==0:
                ok = False
                break
        if not ok:
            break
    if ok:
        print(a)
        break