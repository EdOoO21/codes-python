def f(x, p):
    if (p == 3 or p == 5) and x == 1:
        return 1
    if (p != 3 and p != 5 and x == 1) or (p == 5 and x != 1):
        return 0

    if p % 2 == 0:
        if x % 2 == 0:
            return f(x // 2, p + 1) or f(x - 3, p + 1)

        elif x % 3 == 0:
            return f(x - 2, p + 1) or f(x // 3, p + 1)

        else:
            return f(x - 2, p + 1) or f(x - 3, p + 1)
    else:
        if x % 2 == 0:
            return f(x // 2, p + 1) and f(x - 3, p + 1)

        elif x % 3 == 0:
            return f(x - 2, p + 1) and f(x // 3, p + 1)

        else:
            return f(x - 2, p + 1) and f(x - 3, p + 1)


for i in range(1, 38):
    if f(i, 1):
        print(i)
# 5 6 9

# c помощью 19 задания задание 5 и 6 - лишние
