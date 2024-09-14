def f(x, y, p):
    if x + y > 61 and p == 4:
        return True
    elif (x + y > 61 and p != 4) or (x + y <= 61 and p == 4):
        return False

    if p % 2 == 1:
        return any([(f(x + 3, y, p + 1)), (f(x * 2, y, p + 1)), (f(x, y + 3, p + 1)), (f(x, y * 2, p + 1))])
    else:
        return all([(f(x + 3, y, p + 1)), (f(x * 2, y, p + 1)), (f(x, y + 3, p + 1)), (f(x, y * 2, p + 1))])


for i in range(1, 55):
    if f(7, i, 1):
        print(i)
