for a in range(10000):
    ok = True
    for x in range(10000):
        if ((((x | 42) > 64) and ((x | 34) <= 102)) <= (not((x | a) < 70))) == 0:
            ok = False
            break
    if ok:
        print(a)
        break

