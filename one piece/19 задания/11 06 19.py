def f(x,p):
    if x < 32 and p == 3:
        return 1
    if (x < 32 and p != 3) or (x >= 32 and p == 3):
        return 0
    if p % 2 == 0:
        if x % 4 == 0:
            return any([f(x - 3,p + 1),f(x - 2,p + 1),f(x // 4, p + 1)])
        else:
            return any([f(x - 3, p + 1), f(x - 2, p + 1)])
    if p % 2 == 1:
        if x % 4 == 0:
            return all([f(x - 3,p + 1),f(x - 2,p + 1),f(x // 4, p + 1)])
        else:
            return all([f(x - 3, p + 1), f(x - 2, p + 1)])

for i in range(32,10000):
    if f(i,1):
        print(i)