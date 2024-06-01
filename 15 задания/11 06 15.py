for a in range(11, 1000):
    ok = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            for z in range(1, 1000):
                if ((2 * x + y != 136) or (z * y < 100) or (a ** 2 >= x + y)) == 0:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            break
        print(x)

    if ok:
        print(a)
        break
