def f(x, p):
    if x == 1 and p == 3:
        return True
    elif (x != 1 and p == 3) or (x == 1 and p != 3):
        return False
    if p % 2 == 0:
        if x % 2 == 0:
            return f(x // 2, p + 1) or f(x - 3, p + 1)

        elif x % 3 == 0:
            return f(x - 2, p + 1) or f(x // 3, p + 1)

        else:
            return f(x - 2, p + 1) or f(x - 3, p + 1)
    else:
        if x % 2 == 0:
            return f(x // 2, p + 1) or f(x - 3, p + 1)

        elif x % 3 == 0:
            return f(x - 2, p + 1) or f(x // 3, p + 1)

        else:
            return f(x - 2, p + 1) or f(x - 3, p + 1)


for i in range(1, 38):
    if f(i, 1):
        print(i)
