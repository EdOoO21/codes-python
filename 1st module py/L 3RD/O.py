a, n = float(input()), int(input())


def power(a, n):
    if n == 1:
        return a
    if n == 0:
        return 1
    return a * (power(a, n - 1))


print(power(a, n))
