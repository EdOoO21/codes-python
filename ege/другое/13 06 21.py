def f(x, y, p):
    if (x ** 2 + y ** 2) ** (0.5) > 14 and (p == 3 or p == 5):
        return 1
    if ((x ** 2 + y ** 2) ** (0.5) > 14 and p != 3 and p != 5) \
            or ((x ** 2 + y ** 2) ** (0.5) <= 14 and p == 5):
        return 0
    if p % 2 == 0:
        return any([f(2 * x, y, p + 1), f(x, y + 3, p + 1), f(x, y + 4, p + 1)])
    if p % 2 == 1:
        return all([f(2 * x, y, p + 1), f(x, y + 3, p + 1), f(x, y + 4, p + 1)])


for i in range(1, 14):
    if f(3, i, 1):
        print(i)
