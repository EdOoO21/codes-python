for a in range(-100,10000):
    ok = True
    for x in range(1,1000):
        for y in range(1,1000):
            f = (((144 % x == 0) <= (x % y != 0)) or (x + y > 100) or (a - x > y))
            if not f:
                ok = False
                break
        if not ok:
            break
    if ok:
        print(a)
