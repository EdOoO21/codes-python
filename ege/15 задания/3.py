def tre(a, b, c):
    if (a < b + c) and (c < a + b) and (b < a + c):
        return 1
    else:
        return 0


for a in range(1, 10000):
    ok = True
    for x in range(1, 10000):
        if (not ((tre(x, 11, 18) == (not (max(x, 5) > 15))) and (tre(x, a, 5)))) == 0:
            ok = False
            break

    if ok:
        print(a)
