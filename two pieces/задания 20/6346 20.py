def f(x, y, p):
    if (x + y >= 60) and p == 4:
        return 1
    if ((x + y >= 60) and p != 4) or ((x + y < 60) and p == 4):
        return 0

    if p % 2 == 1:
        if x > y:
            return any([f(x + 1, y, p + 1), f(x + 2, y, p + 1), f(x + 3, y, p + 1), f(x, y * 2, p + 1)])
        if x < y:
            return any([f(x, y + 1, p + 1), f(x, y + 2, p + 1), f(x, y + 3, p + 1), f(x * 2, y, p + 1)])
        if x == y:
            return any(
                [f(x, y + 1, p + 1), f(x, y + 2, p + 1), f(x, y + 3, p + 1), f(x + 1, y, p + 1), f(x + 2, y, p + 1),
                 f(x + 3, y, p + 1)])
    if p % 2 == 0:
        if x > y:
            return all([f(x + 1, y, p + 1), f(x + 2, y, p + 1), f(x + 3, y, p + 1), f(x, y * 2, p + 1)])
        if x < y:
            return all([f(x, y + 1, p + 1), f(x, y + 2, p + 1), f(x, y + 3, p + 1), f(x * 2, y, p + 1)])
        if x == y:
            return all(
                [f(x, y + 1, p + 1), f(x, y + 2, p + 1), f(x, y + 3, p + 1), f(x + 1, y, p + 1), f(x + 2, y, p + 1),
                 f(x + 3, y, p + 1)])


minv = 99999999
for x in range(1, 48):
    if f(x, 12, 1):
        print(x)

