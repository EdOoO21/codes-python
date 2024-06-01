def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        h = 0
        for i in str(x):
            h += int(i)
        return f(x // 2, y) + f(x - 1, y) + f(x - h, y)


print(f(40, 25) * f(25, 10))
