def f(x, y, p):
    if ((x + y) >= 117) and p == 3:
        return 1
    if ((x + y >= 117) and p != 3) or (((x + y) < 117) and p == 3):
        return 0
    if p % 2 == 0:
        return any([f(x + 1, y, p + 1), f(x * 2, y, p + 1), f(x, y + 1, p + 1), f(x, y * 2, p + 1)])
    else:
        return any([f(x + 1, y, p + 1), f(x * 2, y, p + 1), f(x, y + 1, p + 1), f(x, y * 2, p + 1)])

for i in range(1,104):
    if f(13,i,1):
        print(i)

