def f(n):
    if n <= 3:
        return n + 3
    if n > 3 and f(n - 1) % 2 == 0:
        return f(n - 2) + n
    if n > 3 and f(n - 1) % 2 == 1:
        return f(n - 2) + 2 * n



s = 0
for i in range(40, 51):
    s += f(i)
    print(f(i))
print(s)
