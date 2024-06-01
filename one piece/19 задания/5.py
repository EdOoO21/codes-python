def f(x, p, n, m):
    if (36 <= x <= 85) and p == n:
        return 1
    if ((x < 36 or x > 85) and p == n) or ((36 <= x <= 85) and p != n):
        return 0
    if p % 2 == m:
        return any([f(x + 2, p + 1, n, m), f(x * 3, p + 1, n, m)])
    else:
        return all([f(x + 2, p + 1, n, m), f(x * 3, p + 1, n, m)])


for i in range(2, 37, 2):
    if f(8, 1, i, 1):
        print(i)
