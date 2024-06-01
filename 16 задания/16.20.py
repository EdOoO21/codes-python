def f(n):
    if n > 30:
        return n * n + 5 * n + 4
    if n <= 30 and n % 2 == 0:
        return f(n + 1) + 3 * f(n + 4)
    if n <= 30 and n % 2 == 1:
        return 2 * f(n + 2) + f(n + 5)


k = 0
for i in range(1, 1001):
    s = 0
    f1 = f(i)
    while f1 > 0:
        s += f1 % 10
        f1 //= 10
    if s == 27:
        k += 1
print(k)
