def vv(x, y):
    if x == y:
        return 1
    if x == 85 or x == 15 or x > y:
        return 0
    if x < y:
        return vv(x + 1, y) + vv(x * 2, y)


print(vv(1, 50) * vv(50,100))


def vn(x, y):
    if x == y:
        return 1
    if x == 85 or x == 15 or x < y:
        return 0
    if x > y:
        return vn(x - 1, y) + vn(x // 2, y)


print(vn(100, 50) * vn(50,1))
