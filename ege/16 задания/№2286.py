def f(n):
    if n >= 13:
        return n ** 3 + n ** 2 + 1
    if n > 13 and n % 3 == 0:
        return f(n - 1) + 2 * (n ** 2) - 3
    if n > 13 and n % 3 != 0:
        return f(n - 2) + 3 * n + 6


k = 0
for i in range(1, 1001):
    if f(i) % 2 == 1:
        k += 1
print(k)


# http://egekp.unoforum.pro/?1-25-15-00000103-000-0-0-1640775626
#сайт с решением