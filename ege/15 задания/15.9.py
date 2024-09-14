for a in range(1,10000):
    ok = True

    for x in range(1,1000):
        for y in range(1,1000):
            if (((x <= 9) <= (x*x <= a)) and ((y*y <= a) <= (y <= 9))) == 0:
                ok = False
                break
    if ok:
        print(a)
