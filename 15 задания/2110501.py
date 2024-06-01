
for A in range(0,10000):
    ok = True
    for x in range(0,1000):
        for y in range(0, 1000):
            if ((x**2 + y**2 < A) or (x > 3) or (y >= 5)) == 0:
                ok = False
                break
        if not ok:
            break
    if ok:
        print(A)
        break
