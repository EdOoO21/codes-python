def f(x, y, p):
    if x + y >= 30 and (p == 5 or p == 3):
        return 1
    if (x + y < 30 and p == 5) or (x + y >= 30 and p != 5 and p != 3):
        return 0
    if p % 2 == 0:
        return any([f(x + 1, y, p + 1), f(x, y + 1, p + 1), f(x * 2, y, p + 1), f(x, y * 3, p + 1)])
    else:
        return all([f(x + 1, y, p + 1), f(x, y + 1, p + 1), f(x * 2, y, p + 1), f(x, y * 3, p + 1)])


for s in range(1, 29):
    if f(1, s, 1) and 7 + s <= 29:
        print(s)