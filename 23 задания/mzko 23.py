def f(x, y):
    if x > y or x == 24:
        return 0
    if x == y:
        return 1
    if x < y:
        return ((f(x + 1, y)) + (f(3 * x, y)))


print((f(2, 12)) * (f(12, 72)))
