a, b = float(input()), float(input())


def IsPointInArea(x, y):
    return ((y >= -x) and (y >= (2 * x) + 2) and (4 >= ((x + 1) ** 2) + ((y - 1) ** 2))) \
        or ((y <= -x) and (y <= (2 * x) + 2) and (4 <= ((x + 1) ** 2) + ((y - 1) ** 2)))


a = IsPointInArea(a, b)
if a:
    print('YES')
else:
    print('NO')
