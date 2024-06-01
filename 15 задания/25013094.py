for A in range(-100,10000):
    ok = True
    for x in range(1000):
        for y in range(1000):
            if ((7*y + x < A) or (2*x + 3*y > 98)) == 0:
                ok = False
                break
        if not ok:
            break
    if ok:
        print(A)
        break