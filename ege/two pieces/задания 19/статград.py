def f(x, y, p):
    if (x >= 48 or y >= 48) and p == 2:
        return 1
    if ((x >= 48 or y >= 48) and p != 2) or (x < 48 and y < 48 and p == 2):
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
            return any([f(x + 1, y, p + 1), f(x + 2, y, p + 1), f(x + 3, y, p + 1), f(x, y * 2, p + 1)])
        if x < y:
            return any([f(x, y + 1, p + 1), f(x, y + 2, p + 1), f(x, y + 3, p + 1), f(x * 2, y, p + 1)])
        if x == y:
            return any(
                [f(x, y + 1, p + 1), f(x, y + 2, p + 1), f(x, y + 3, p + 1), f(x + 1, y, p + 1), f(x + 2, y, p + 1),
                 f(x + 3, y, p + 1)])


minv = 99999999
for x in range(1, 100):
    for y in range(1, 100):
        if f(x, y, 1):
            minv = min(minv,x+y)
print(minv)

