def f(x, y, z):
    if x + y >= 79 and (z == 5 or z == 3):
        return True
    elif (x + y < 79 and z == 5) or (x + y >= 79 and z != 5):   # исключение комбинаций, при которых дальнейший подбор не имеет смысла
        return False

    if z % 2 == 0:
        return f(x + 2, y, z + 1) or f(x, y + 2, z + 1) or f(x + x, y, z + 1) or f(x, y + y, z + 1)
    else:
        return f(x + 2, y, z + 1) and f(x, y + 2, z + 1) and f(x + x, y, z + 1) and f(x, y + y, z + 1)

for i in range(1, 70):
    if f(9, i, 1):
        print(i)
 # можно удалить во 2-ой строке р==5 и код выведет лишние значения!!!!!!