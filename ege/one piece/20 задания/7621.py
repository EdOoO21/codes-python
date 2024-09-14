def f(x, p):
    if x >= 43 and p == 4:
        return 1
    if (x >= 43 and p != 4) or (x < 43 and p == 4):
        return 0
    if p % 2 == 1:
        return any([f(x + 1, p + 1), f(x + 4, p + 1), f(x * 3, p + 1)])
    if p % 2 == 0:
        return all([f(x + 1, p + 1), f(x + 4, p + 1), f(x * 3, p + 1)])


for i in range(1, 43):
    if f(i, 1):
        print(i)
