def f(x, y, p):
    if ((x + y) >= 107) and p == 3:
        return 1
    if (((x + y) >= 107) and p != 3) or (((x + y) < 107) and p == 3):
        return 0
    if p % 2 == 0:
        return any([f(x + 2, y, p + 1), f(x * 2, y, p + 1), f(x, y + 2, p + 1), f(x, y * 2, p + 1)])
    else:
        return all([f(x + 2, y, p + 1), f(x * 2, y, p + 1), f(x, y + 2, p + 1), f(x, y * 2, p + 1)])


for i in range(1, 90):
    if f(17, i, 1):
        print(i)
