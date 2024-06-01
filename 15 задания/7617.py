for a in range(129, 100000):
    ok = True
    for x in range(0, 10000):
        for y in range(0, 10000):
            if ((x >= 9) or (2 * x < y) or (x * y < a)) == 0:
                ok = False
                break
        if not ok:
            break
    if ok:
        print(a)
        break
