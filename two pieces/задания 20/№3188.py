def f(x, y, p):
    if x + y >= 100 and p == 4:
        return 1
    if (x + y >= 100 and p != 4) or (x + y < 100 and p == 4):
        return 0
    if p % 2 == 1:
        return any([f(x + 1, y, p + 1), f(x * 4, y, p + 1), f(x, y + 1, p + 1), f(x, y * 4, p + 1)])
    else:
        return all([f(x + 1, y, p + 1), f(x * 4, y, p + 1), f(x, y + 1, p + 1), f(x, y * 4, p + 1)])


for i in range(1, 94):
    if f(6, i, 1):
        print(i)      # 3 23
