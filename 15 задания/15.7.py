for A in range(1, 10000):
    ok = True
    for x in range(-1000, 1000):
        if ((x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0))) == 0:
            ok = False
            break
    if ok:
        print(A)
        break
