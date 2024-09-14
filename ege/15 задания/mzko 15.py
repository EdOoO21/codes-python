for A in range(1, 10000):
    ok = True
    for x in range(1, 10000):
        if ((not (x % 54 == 0) or not (x % 80 == 0)) <= (not (x % A == 0))) == 0:
            ok = False
            break
    if ok:
        print(A)
