for a in range(0,10000):
    ok = True
    for x in range(1000):
        for y in range(1000):
            if ((x >= 27) or (2*x < 3*y) or ((2 + x)*(y - 3) < a)) == 0:
                ok = False
                break
        if not ok:
            break
    if ok:
        print(a)
        break