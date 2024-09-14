for i in range(400000000, 600000001):
    m = 0
    n = 0
    ok = True
    while i > 1:
        if i % 2 == 0:
            i //= 2
            m += 1
        elif i % 3 == 0:
            i //= 3
            n += 1
        else:
            ok = False
    print(i)
    if ok:
        print(i, '=', '2 **', n, ' * ', '3 **', m)
