s = [0] * 15000
s[10002] = 1
for i in range(12, 10001)[::-2]:
    s[i] = s[i + 2] + (i % 10)
for i in range(1, 15000):
    if i <= 10:
        s[i] = i
    if i >= 10000:
        s[i] = 1
    if 10 < i < 10000 and i % 2 == 0:
        s[i] = (i % 10) + s[i + 2]
    if 10 < i < 10000 and i % 2 == 1:
        s[i] = s[i - 2] - ((i - 1) % 10)

print(s[4500] + s[5515])
'''
from sys import *
from functools import lru_cache
setrecursionlimit(10000)
@lru_cache()



def f(n):
    if n <= 10:
        return n
    if n >= 10000:
        return 1
    if 10 < n < 10000 and n % 2 == 0:
        return (n % 10) + f(n + 2)
    if 10 < n < 10000 and n % 2 == 1:
        return f(n - 2) - ((n - 1) % 10)


print(f(4500) + f(5515))
'''
