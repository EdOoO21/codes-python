def f(x, p):
    if (p == 3 or p == 5) and x >= 50:
        return 1
    if (p == 5 and x < 50) or (p != 3 and p != 5 and x >= 50):
        return 0
    if p % 2 == 0:
        return any([f(x + 2, p + 1), f(x * 3, p + 1)])
    else:
        return all([f(x + 2, p + 1), f(x * 3, p + 1)])


for i in range(1, 50):
    if f(i, 1):
        print(i)

'''
11
12   =>   15
15         16      -лишние с помощью первого кода => ответ 1112
16

'''
