def f(x, y):
    n = str(x)
    if x > y or ('3' in n):
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y)


print(f(1, 40))
