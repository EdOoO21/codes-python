for A in range(1,10000):
    ok = True
    for x in range(1,10000):
        if (((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 80)) == 0:
            ok = False
            break
    if ok:
        print(A)
        break