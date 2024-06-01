for a in range(1, 10000):
    ok = True
    for m in range(1, 1000):
        for n in range(1, 1000):
            if ((3 * m + 4 * n > 66) or (m <= a) or (n < a)) == 0:
                ok = False
                break
    if ok:
        print(a)
        break

