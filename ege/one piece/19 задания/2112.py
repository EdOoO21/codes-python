def f(x, p):
    if p == 2 and x >= 82:
        return 1
    if (p == 2 and x < 82) or (p != 2 and x >= 82):
        return 0
    if p % 2 == 1:
        return any([f(x + 10, p + 1), f(x * 2, p + 1)])
    else:
        return all([f(x + 10, p + 1), f(x * 2, p + 1)])

for i in range(1,82):
    if f(i,1):
        print(i)
