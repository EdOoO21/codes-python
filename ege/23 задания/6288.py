def f(x, y, s, p):
    if x > y or s > 1 or p > 1:
        return 0
    if x == y:
        return 1
    if x < y:

        if s == 1:
            return f(x * 2, y, 0, 1) + f(x * 3, y, 0, 1)
        if p == 1:
            return f(x + 1, y, 1, 0) + f(x + 3, y, 1, 0)
        if p == 0 and s == 0:
            return f(x + 1, y, 1, 0) + f(x + 3, y, 1, 0) + f(x * 2, y, 0, 1) + f(x * 3, y, 0, 1)


print(f(1, 9999, 0, 0))
