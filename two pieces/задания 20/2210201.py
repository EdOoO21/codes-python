def f(x, y, p):
    if p == 4 and (x + y) > 80:
        return 1
    if (p != 4 and (x + y) > 80) or (p == 4 and (x + y) <= 80):
        return 0

    if p % 2 == 1:
        if x > y:
            return any([f(x, y + 1, p + 1), f(x, y + 2, p + 1), f(x, y * 2, p + 1)])
        elif x < y:
            return any([f(x + 1, y, p + 1), f(x + 2, y, p + 1), f(x * 2, y, p + 1)])
    else:
        if x > y:
            return all([f(x, y + 1, p + 1), f(x, y + 2, p + 1), f(x, y * 2, p + 1)])
        elif x < y:
            return all([f(x + 1, y, p + 1), f(x + 2, y, p + 1), f(x * 2, y, p + 1)])

for i in range(1,69):
    if f(12,i,1):
        print(i)