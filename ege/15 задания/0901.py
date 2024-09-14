for A in range(1,10000):
    ok =  True
    for x in range(1,10000):
        if ((x + A >= 160) or ((x % 7 == 0) <= (x - 17 <= 0))) == 0:
            ok = False
            break
    if ok:
        print(A)
        break