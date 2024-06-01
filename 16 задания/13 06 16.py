from sys import *

setrecursionlimit(5000)


def f(n):
    if n > 3000:
        return n
    if n <= 3000:
        return f(n + 2) + 2


print(f(40) - f(43))
