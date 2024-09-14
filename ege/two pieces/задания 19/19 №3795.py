def f(x, y, z):
    if x + y >= 62 or z > 3:
        return z == 3
    return f(x + 1, y, z + 1) or f(x, y + 1, z + 1) or f(x + y, y, z + 1) or f(x, y + x, z + 1)


for i in range(1, 54):
    if f(8, i, 1):
        print(i)
        break
