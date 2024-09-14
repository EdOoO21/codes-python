def f(x, y, z, p):
    if x + y + z >= 73 and p == 3:
        return True
    elif (x + y + z < 73 and p == 3) or (x + y + z >= 73 and p != 3):
        return False

    return any([f(x + 3, y, z, p + 1) , f(x + 13, y, z, p + 1) , f(x + 23, y, z, p + 1)
           , f(x, y + 3, z, p + 1) , f(x, y + 13, z, p + 1) , f(x, y + 23, z, p + 1)
           , f(x, y, z + 3, p + 1) , f(x, y, z + 13, p + 1) , f(x, y, z + 23, p + 1)])


for i in range(1, 24):
    if f(2, i, 2 * i, 1):
        print(i)
