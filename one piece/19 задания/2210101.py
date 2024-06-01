def f(x, p):
    if x >= 103 and p == 3:
        return 1
    if (x >= 103 and p != 3) or (x < 103 and p == 3):
        return 0
    if p % 2 == 0:
        if (x + 1) % 3 == 0:
            return any([f(x + 2, p + 1), f(x * 2, p + 1)])
        elif (x + 2) % 3 == 0:
            return any([f(x + 1, p + 1), f(x * 2, p + 1)])
        elif (x + 2) % 3 != 0 and (x + 1) % 3 != 0:
            return any([f(x + 1, p + 1), f(x + 2, p + 1), f(x * 2, p + 1)])

    else:
        if (x + 1) % 3 == 0:
            return all([f(x + 2, p + 1), f(x * 2, p + 1)])
        elif (x + 2) % 3 == 0:
            return all([f(x + 1, p + 1), f(x * 2, p + 1)])
        elif (x + 2) % 3 != 0 and (x + 1) % 3 != 0:
            return all([f(x + 1, p + 1), f(x + 2, p + 1), f(x * 2, p + 1)])


for i in range(1, 102):
    if f(i, 1) and (i % 3 != 0):
        print(i)
