import sys


def babylonian_sequence(a):
    if a != 1:
        yield 1
        x = 1
        x = 0.5 * (x + (a / x))
        while ((x ** 2) - a) >= 0.0000001:
            yield x
            x = 0.5 * (x + (a / x))
    else:
        yield 1

exec(sys.stdin.read())
for value in babylonian_sequence(1):
    print(value, end=" ")
