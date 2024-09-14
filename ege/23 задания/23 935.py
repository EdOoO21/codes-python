def check(a, b):
    for i in range(2, (a // 2) + 2):
        if a % i == 0 and b % i == 0:
            return 0
    return 1


def f(x, y):
    if x == y:
        return 1
    if x > y or (check(x, x + 1) == 0 and check(x, x + 3) == 0 and check(x, x + 7) == 0):
        return 0
    if x < y:
        if check(x, x + 1) == 0 and check(x, x + 3) == 0 and check(x, x + 7) == 1:
            return f(x + 7, y)
        elif check(x, x + 1) == 0 and check(x, x + 3) == 1 and check(x, x + 7) == 0:
            return f(x + 3, y)
        elif check(x, x + 1) == 1 and check(x, x + 3) == 0 and check(x, x + 7) == 0:
            return f(x + 1, y)
        elif check(x, x + 1) == 1 and check(x, x + 3) == 1 and check(x, x + 7) == 0:
            return f(x + 3, y) + f(x + 1, y)
        elif check(x, x + 1) == 0 and check(x, x + 3) == 1 and check(x, x + 7) == 1:
            return f(x + 3, y) + f(x + 7, y)
        elif check(x, x + 1) == 1 and check(x, x + 3) == 0 and check(x, x + 7) == 1:
            return f(x + 7, y) + f(x + 1, y)
        elif check(x, x + 1) == 1 and check(x, x + 3) == 1 and check(x, x + 7) == 1:
            return f(x + 3, y) + f(x + 7, y) + f(x + 1, y)


print(f(13, 31))
