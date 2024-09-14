def f(x, y, p):
    if x > y or p > 5:
        return 0
    if x == y:
        return 1

    return (f(x + 1, y, p + 1)) or (f(x * 2, y, p + 1))


for i in range(2, 100):
    if f(1, i, 0) == False:
        print(i)

