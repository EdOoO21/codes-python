import sys
from functools import reduce


def f(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


def binomial_coefficients(n):
    yield 1
    for i in range(1, n + 1):
        if n != i:
            yield f(n)//(f(i) * f(n - i))
        else:
            yield 1


exec(sys.stdin.read())
print(list(binomial_coefficients(7)))
