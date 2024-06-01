def zifr(n):
    s = str(n)
    su = 0
    while len(s) > 1:
        su = 0
        for x in s:
            su += int(x)
        s = str(su)
    return s


def f(x, y):
    zif = zifr(x)
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        if str((x + 2))[-1] == zif and str((x + 1))[-1] == zif:
            return 0
        if str((x + 2))[-1] != zif and str((x + 1))[-1] != zif:
            return f(x + 2, y) + f(x + 1, y)

        if str((x + 1))[-1] == zif:
            return f(x + 2, y)

        if str((x + 2))[-1] == zif:
            return f(x + 1, y)


print(f(12, 37))