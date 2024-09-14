for A in range(29,30):
    ok = True
    for x in range(1,1001):
        for y in range(1,1001):
            for z in range(1,1001):
                if ((150 != y + 2*x + 2*z) or (A < x) or (A < y) or (A < z)) == 0:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            break
    if ok:
        print(A)
