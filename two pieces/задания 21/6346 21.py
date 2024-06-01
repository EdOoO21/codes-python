def f(x, y, p):
    if (x + y >= 60) and (p == 5 or p == 3):
        return 1
    if ((x + y >= 60) and p != 5 and p != 3) or ((x + y < 60) and p == 5):
        return 0

    if p % 2 == 0:
        if x > y:
            return any([f(x + 1, y, p + 1), f(x + 2, y, p + 1), f(x + 3, y, p + 1), f(x, y * 2, p + 1)])
        if x < y:
            return any([f(x, y + 1, p + 1), f(x, y + 2, p + 1), f(x, y + 3, p + 1), f(x * 2, y, p + 1)])
        if x == y:
            return any(
                [f(x, y + 1, p + 1), f(x, y + 2, p + 1), f(x, y + 3, p + 1), f(x + 1, y, p + 1), f(x + 2, y, p + 1),
                 f(x + 3, y, p + 1)])
    if p % 2 == 1:
        if x > y:
            return all([f(x + 1, y, p + 1), f(x + 2, y, p + 1), f(x + 3, y, p + 1), f(x, y * 2, p + 1)])
        if x < y:
            return all([f(x, y + 1, p + 1), f(x, y + 2, p + 1), f(x, y + 3, p + 1), f(x * 2, y, p + 1)])
        if x == y:
            return all(
                [f(x, y + 1, p + 1), f(x, y + 2, p + 1), f(x, y + 3, p + 1), f(x + 1, y, p + 1), f(x + 2, y, p + 1),
                 f(x + 3, y, p + 1)])


minv = 99999999
for x in range(1, 35):
    if f(x, 25, 1):
        print(x)
        break



