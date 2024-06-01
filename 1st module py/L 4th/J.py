from functools import reduce


def factorial(n):
    if type(n) == int and n >= 0:
        if n != 0:
            return reduce(lambda x, y: x * y, range(1, n + 1))
        return 1
    else:
        return 'FactorialCalculateError'


print(factorial(2))
