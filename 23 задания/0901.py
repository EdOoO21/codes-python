def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 3, y) + f(x // 7, y)


print(f(50, 1))
