def f(x, p):
    if x >= 165 and p == 3:
        return 1
    if (x < 165 and p == 3) or (x >= 165 and p != 3):
        return 0

    if p % 2 == 0:
        return any([f(x + 1, p + 1), f(x * 2, p + 1)])
    else:
        return all([f(x + 1, p + 1), f(x * 2, p + 1)])


for i in range(1, 165):
    if f(i, 1):
        print(i)
