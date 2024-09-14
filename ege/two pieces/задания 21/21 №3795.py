def f(x, y, z):
    if x + y >= 62 and (z == 5 or z == 3):
        return True
    elif (x + y < 62 and z == 5) or (x + y >= 62 and z != 5):   # исключение комбинаций, при которых дальнейший подбор не имеет смысла
        return False

    if z % 2 == 0:                 # если ищем числа %2==1, то тут стоит 0 !!!!!!!!!!!!!!!!!!!!!!!!!!
        return f(x + 1, y, z + 1) or f(x, y + 1, z + 1) or f(x + y, y, z + 1) or f(x, y + x, z + 1)
    else:
        return f(x + 1, y, z + 1) and f(x, y + 1, z + 1) and f(x + y, y, z + 1) and f(x, y + x, z + 1)


for i in range(1, 54):
    if f(8, i, 1):
        print(i)
 # можно удалить во 2-ой строке р==5 и код выведет лишние значения!!!!!!