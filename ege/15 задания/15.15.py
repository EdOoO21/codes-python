for a in range(1, 10000):
    ok = True
    for y in range(1, 1000):
        for x in range(1, 1000):
            if ((y + 2*x < a) or (x > 15) or (y > 30) )== 0:
                ok = False
                break
    if ok:
        print(a)
        break

