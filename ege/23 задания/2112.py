def f(x, y, a, b, c):
    if (x > y) or (x == y and (a == 0 or b == 0 or c == 0)):
        return 0
    if x == y and a > 0 and b > 0 and c > 0:
        return 1
    if x < y:
        return f(x + 1, y, a + 1, b, c) + f(x + 2, y, a, b + 1, c) + f(x * 2, y, a, b, c + 1)


print(f(3, 25, 0, 0, 0))
