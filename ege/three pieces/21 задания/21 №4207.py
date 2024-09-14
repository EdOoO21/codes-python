def f(x, y, z, p):
    if x + y + z >= 73 and (p ==5 or p == 3):
        return True
    elif (x + y + z < 73 and p == 5) or (x + y + z >= 73 and p != 5 and p != 3):
        return False
    if p % 2 == 0:
        return f(x + 3, y, z, p + 1) or f(x + 13, y, z, p + 1) or f(x + 23, y, z, p + 1) \
               or f(x, y + 3, z, p + 1) or f(x, y + 13, z, p + 1) or f(x, y + 23, z, p + 1) \
               or f(x, y, z + 3, p + 1) or f(x, y, z + 13, p + 1) or f(x, y, z + 23, p + 1)
    else:
        return all([f(x + 3, y, z, p + 1) , f(x + 13, y, z, p + 1) ,f(x + 23, y, z, p + 1)
               , f(x, y + 3, z, p + 1) , f(x, y + 13, z, p + 1), f(x, y + 23, z, p + 1)
               ,f(x, y, z + 3, p + 1) ,f(x, y, z + 13, p + 1) ,f(x, y, z + 23, p + 1) ])


for i in range(1, 24):
    if f(2, i, 2 * i, 1):
        print(i)

# проверка неверных чисел осуществляется через удаление во второй строке р==3, а потом р ==5