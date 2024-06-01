def f(x, p):
    if (p == 3 or p == 5) and x >= 100:
        return 1
    if (p == 5 and x < 100) or (p != 3 and p != 5 and x >= 100):
        return 0
    if p % 2 == 0:
        return any([f(x + 7, p + 1), f(x * 2, p + 1)])
    if p % 2 == 1:
        return all([f(x + 7, p + 1), f(x * 2, p + 1)])


for i in range(1, 100):
    if f(i, 1) :
        print(i)