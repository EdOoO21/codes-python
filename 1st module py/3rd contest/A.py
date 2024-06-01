import sys

sys.setrecursionlimit(1000000000)


def ackerman(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackerman(m - 1, 1)
    elif n > 0 and m > 0:
        return ackerman(m - 1, ackerman(m, n - 1))


print(ackerman(1000, 1))
