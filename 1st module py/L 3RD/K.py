a, b, c, d, e = float(input()), float(input()), float(input()), float(input()), float(input())


def IsPointInCircle(x, y, xc, yc, r):
    return ((x - xc) ** 2) + ((y - yc) ** 2) <= r ** 2


a = (IsPointInCircle(a, b, c, d, e))
if a:
    print('YES')
else:
    print('NO')
