# import sys
#
# sys.setrecursionlimit(10000)
# def f(n):
#     if n > 3456:
#         return n + 1
#     if n <= 3456 and n % 3 == 0:
#         return f(n + 1) + f(n + 2)
#     if n <= 3456 and n % 3 != 0:
#         return f(n + (n % 3)) + 2
#


f = [0] * 3500
for i in range(3457, 3500):
    f[i] = i + 1

for i in range(0, 3456)[::-1]:
    if i % 3 == 0:
        f[i] = f[i + 1] + f[i + 2]
    else:
        f[i] = f[i + (i % 3)] + 2

print(f[12] - f[17])
