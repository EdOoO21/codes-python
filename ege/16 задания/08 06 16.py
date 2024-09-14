import sys

sys.setrecursionlimit(10000)


def f(n):
    if n < 3:
        return 2
    if n > 2:
        return 2 * f(n - 2)


print(f(2222) // f(2182))

f = [0] * 2300
for i in range(2300):
    if i < 3:
        f[i] = 2
    if i > 2:
        f[i] = 2 * f[i-2]

print(f[2222]//f[2182])