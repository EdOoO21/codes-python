def f(x, y, p):
    if p == 3 and x + y > 62:
        return True
    elif (p != 3 and x + y > 62) or (p == 3 and x + y <= 62):
        return False

    return any([f(x + 1, y, p + 1), f(x * 2, y, p + 1), f(x, y + 1, p + 1), f(x, y * 2, p + 1)])


for x in range(1, 58):
    if f(x, 5, 1):
        print(x)
