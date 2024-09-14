def f(n, end):
    if n > end or n == 17:
        return 0
    if n == end:
        return 1
    return f(n + 1, end) + f(n * 2, end)


print(f(1, 10) * f(10, 35))
