def f(x,y,p):
    if x + y >= 40 and (p == 5 or p == 3):
        return True
    elif (x + y >= 40 and p != 5 and p != 3) or (x + y < 40 and p == 5):
        return False

    if p % 2 == 0:
        return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x * 2, y, p + 1) and f(x, y * 2, p + 1)

k=0
for i in range(1,31):
    if f(9,i,1):
        print(i)
        k+=1

print(k)

# можно удалить во 2-ой строке р==5 и код выведет лишние значения!!!!!!