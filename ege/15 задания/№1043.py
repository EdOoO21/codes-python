def f(x, y, A):
    return ((y + 2 * x < A) or (x > 20) or (y > 30)) == 1


for A in range(-100, 100):
    print(A)
    ok = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not (f(x, y, A)):
                ok = False
    if ok:
        print(A, '================')
