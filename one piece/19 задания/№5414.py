def f(x,p):
    if p == 3 and x <= 10:
        return 1
    if (p != 3 and x <= 10) or (p == 3 and x > 10):
        return 0
    if p % 2 == 0:
        return any([f(x//3,p+1),f(x-10,p+1)])
    else:
        return all([f(x // 3, p + 1), f(x - 10, p + 1)])

for i in range(11,10000):
    if f(i,1):
        print(i)