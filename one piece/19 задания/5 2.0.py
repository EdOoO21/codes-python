def f(x, p):
    if (36 <= x <= 85) and p == 5:
        return 1
    if (x < 36 and p == 5) or (x > 85) or ((36 <= x <= 85) and p != 5):
        return 0
    if p % 2 == 0:
        return any([f(x + 2, p + 1), f(x * 3, p + 1)])
    else:
        return all([f(x + 2, p + 1), f(x * 3, p + 1)])


for i in range(1, 36):
    if f(i, 1):
        print(i)