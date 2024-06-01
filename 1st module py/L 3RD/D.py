import sys


def sum_of_digits(n: int):
    s = 0
    n = abs(n)
    while n > 0:
        s += (n % 10)
        n //= 10
    return s


exec(sys.stdin.read())
