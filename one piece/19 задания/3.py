def f(x, p):
    if p == 3 and x >= 153:
        return 1
    if (p != 3 and x >= 153) or (p == 3 and x < 153):
        return 0
    if p % 2 == 0:
        return any([f(x + 1, p + 1), f(x * 2, p + 1)])
    else:
        return all([f(x + 1, p + 1), f(x * 2, p + 1)])

for i in range(1,153):
    if f(i,1):
        print(i)
