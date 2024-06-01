def f(x, p, c):
    if p == 4 and x >= 59:
        return 1
    if (p != 4 and x >= 59) or (p == 4 and x < 59):
        return 0
    if p % 3 == 0:
        if c == 0:
            return any([f(x * 2, p + 1, 1)])
        if c == 1:
            return any([f(x + 4, p + 1, 0)])
        else:
            return any([f(x + 4, p + 1, 0), f(x * 2, p + 1, 1)])
    else:
        if c == 0:
            return all([f(x * 2, p + 1, 1)])
        if c == 1:
            return all([f(x + 4, p + 1, 0)])
        else:
            return all([f(x + 4, p + 1, 0), f(x * 2, p + 1, 1)])


for i in range(1, 54):
    if f(i, 1, ''):
        print(i)
