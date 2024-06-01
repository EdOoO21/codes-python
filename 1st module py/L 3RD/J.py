x, y = float(input()), float(input())


def IsPointInSquare(x, y):
    return (y <= x + 1) and (y <= 1 - x) and (y >= - 1 - x) and (y >= x - 1)

a = (IsPointInSquare(x, y))
if a == True:
    print('YES')
else:
    print('NO')