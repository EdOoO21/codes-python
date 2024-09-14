def f(x, y):
    if x == y:
        return 1
    if x < y or x == 50:
        return 0
    if x > y:
        if x % 2 == 0:
            return f(x - 5, y) + f(x - 4, y) + f(x / 2, y)
        else:
            return f(x - 5, y) + f(x - 4, y)


print(f(100, 73) * f(73, 22) * f(22, 2))
