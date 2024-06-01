import sys


def mod_powers(a, n):
    yield 1
    for i in range(1, n):
        yield (a ** i) % n
        if (a ** i) % n == 1:
            return


exec(sys.stdin.read())

print(*mod_powers(17, 256))
