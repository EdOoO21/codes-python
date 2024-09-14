def f(x, p):
    if p == 4 and x >= 229:
        return 1
    if (p == 4 and x < 229) or (p != 4 and x >= 229):
        return 0
    if p % 2 == 1:
        return any([f(x + 1, p + 1), f(x * 2, p + 1)])
    else:
        return all([f(x + 1, p + 1), f(x * 2, p + 1)])


for i in range(1, 229):
    if f(i, 1):
        print(i)
