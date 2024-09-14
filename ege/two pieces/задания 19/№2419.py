def f(x, y, p):
    if p == 3 and x + y >= 62:
        return 1
    if (p != 3 and x + y >= 62) or (p == 3 and y + x < 62):
        return 0
    if p % 2 == 0:
        return any([f(x + 3, y, p + 1), f(x, y + 3, p + 1), f(x * 2, y, p + 1), f(x, y * 2, p + 1)])
    else:
        return any([f(x + 3, y, p + 1), f(x, y + 3, p + 1), f(x * 2, y, p + 1), f(x, y * 2, p + 1)])

for i in range(1,55):
    if f(7,i,1):
        print(i)

        #14