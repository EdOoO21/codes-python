def de(a, b):
    return a % b == 0


def f(x, A):
    return ((not (de(x, A))) <= (not (de(x, 24)) and not (de(x, 36)))) == 1


for A in range(1, 10000):
    ok = True
    for x in range(1, 1000):
        if not (f(x, A)):
            ok = False
            break
    if ok:
        print(A)
