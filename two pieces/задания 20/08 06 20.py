def f(x, y, p):
    if p == 4 and (x * y) >= 455:
        return 1
    if (p != 4 and (x * y) >= 455) or (p == 4 and (x * y) < 455):
        return 0
    if p % 2 == 1:
        return any([f(x + 1, y, p + 1), f(x * 2, y, p + 1), f(x, y + 1, p + 1), f(x, y * 2, p + 1)])
    if p % 2 == 0:
        return all([f(x + 1, y, p + 1), f(x * 2, y, p + 1), f(x, y + 1, p + 1), f(x, y * 2, p + 1)])


for i in range(1, 91):
    if f(i, 5, 1):
        print(i)
