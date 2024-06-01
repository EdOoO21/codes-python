for a in range(1, 10000):
    ok = True
    for x in range(1, 1000):
        if (((x & 28 != 0) or (x & 45 != 0)) <= ((x & 48 == 0) <= (x & a != 0))) == 0:
            ok = False
            break
    if ok:
        print(a)
        break
