def f(x, y, p):
    if x + y >= 30 and p == 4:
        return 1
    if (x + y < 30 and p == 4) or (x + y >= 30 and p != 4):
        return 0
    if p % 2 == 1:
        return any([f(x + 1, y, p + 1), f(x, y + 1, p + 1), f(x * 2, y, p + 1), f(x, y * 3, p + 1)])
    else:
        return all([f(x + 1, y, p + 1), f(x, y + 1, p + 1), f(x * 2, y, p + 1), f(x, y * 3, p + 1)])


for k in range(1, 23):
    if f(k, 7, 1) and 7 + k <= 29:
        print(k)
