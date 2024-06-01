for A in range(1, 10000):
    ok = True
    for x in range(-1000, 1000):
        if ((x & 51 == 0) or ((x & 41 == 0) <= (x & A != 0))) == 0:
            ok = False
            break
    if ok:
        print(A)
        break
