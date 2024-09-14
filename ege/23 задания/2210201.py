s = []


def f(x, y, k1, k2):
    if x > y:
        return 0
    if x == y:
        return 1

    if k1 == 0 and k2 == 2:
        s.append(f(x + 1, y, k1 + 1, k2 - 2))
        return f(x + 1, y, k1 + 1, k2 - 2)
    elif k1 == 2 and k2 == 0:
        s.append(f(x * 2, y, k1 - 2, k2 + 1))
        return f(x * 2, y, k1 - 2, k2 + 1)
    elif k1 == 0 and k2 == 1:
        s.append(f(x + 1, y, k1 + 1, k2 - 1))
        return f(x + 1, y, k1 + 1, k2 - 1)
    elif k1 == 1 and k2 == 0:
        s.append(f(x * 2, y, k1 - 1, k2 + 1))
        return f(x * 2, y, k1 - 1, k2 + 1)
    elif k1 == 0 and k2 == 0:
        s.append(f(x * 2, y, k1, k2 + 1) + f(x + 1, y, k1 + 1, k2))
        return f(x * 2, y, k1, k2 + 1) + f(x + 1, y, k1 + 1, k2)


f(1, 14, 0, 0)
print(sum(s))
