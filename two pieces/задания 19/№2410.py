def f(x, y, z):
    if x + y >= 79 and z == 3:
        return True
    elif (x + y >= 79 and z != 3) or (x + y < 79 and z == 3):
        return False

    return f(x + 2, y, z + 1) or f(x, y + 2, z + 1) or f(x + x, y, z + 1) or f(x, y + y, z + 1)


for i in range(1, 70):
    if f(9, i, 1):
        print(i)
