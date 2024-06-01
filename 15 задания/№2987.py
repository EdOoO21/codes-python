for A in range(1001,10000):
    ok = True
    for x in range(-100,10000):
        if (((x % A != 0) or (x % 36 == 0) and (x % 126 == 0)) and (A > 1000)) == 0:
            ok = False
            break
    if ok:
        print(A)
        break
