def f(x, y, A):
    return (4*y + 3*x != 65) or (x > A) or (3*y > A)
for A in range(1, 10000):
    ok = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(f(x, y, A)):
                ok = False
    if ok:
        print(A)