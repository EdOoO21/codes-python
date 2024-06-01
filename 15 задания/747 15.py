for a in range(0,10000):
    ok = True
    for x in range(1000):
        for y in range(1000):
            if ((11 <= y) or (7*y < x) or (a > x*y)) == 0:
                ok = False
                break
        if not ok:
            break
    if ok:
        print(a)
        break