def f(x, p):
    if p == 3 and x >= 100:
        return 1
    if (p == 3 and x < 100) or (p != 3 and x >= 100):
        return 0
    if p % 2 == 0:
        return any([f(x + 7, p + 1), f(x * 2, p + 1)])
    if p % 2 == 1:
        return all([f(x + 7, p + 1), f(x * 2, p + 1)])


def f1(x, p):
    if p == 4 and x >= 100:
        return 1
    if (p == 4 and x < 100) or (p != 4 and x >= 100):
        return 0
    if p % 2 == 1:
        return any([f1(x + 7, p + 1), f1(x * 2, p + 1)])
    if p % 2 == 0:
        return all([f1(x + 7, p + 1), f1(x * 2, p + 1)])


for i in range(1, 100):
    if f(i, 1) :
        print(i)
