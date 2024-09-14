def f(x, p):
    if x > 29 and p == 4:
        return 1
    if (x > 29 and p != 4) or (x <= 29 and p == 4):
        return 0
    if p % 2 == 1:
        if x % 2 == 0:
            return any([f(x + 4, p + 1), f(x + 6, p + 1)])
        if x % 2 == 1:
            return any([f(x + (x % 10), p + 1), f(x + 6, p + 1)])
    else:
        if x % 2 == 0:
            return all([f(x + 4, p + 1), f(x + 6, p + 1)])
        if x % 2 == 1:
            return all([f(x + (x % 10), p + 1), f(x + 6, p + 1)])

for i in range(1,27):
    if f(i,1):
        print(i)
