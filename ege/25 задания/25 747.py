# for x in range(10):
#     a = (1234*10) + x
#     if (a % 137 == 0) and (x % (x**3) == 0):
#         print(a)
#
# for x in range(10):
#     for y in range(10):
#         a = (1234*100) + (y * 10) + x
#         if (a % 137 == 0) and ((y*10 + x) % ((x + y)**3) == 0):
#             print(a)
#
# for x in range(10):
#     for y in range(10):
#         for w in range(10):
#             a = (1234*1000) + (w * 100) + (y * 10) + x
#             if (a % 137 == 0) and ((w * 100 + y * 10 + x) % ((x + y + w)**3) == 0):
#                 print(a)
#
# for x in range(10):
#     for y in range(10):
#         for w in range(10):
#             for z in range(10):
#                 a = (1234*10000) + (z*1000) + (w * 100) + (y * 10) + x
#                 if (a % 137 == 0) and ((z*1000 + w * 100 + y * 10 + x) % ((x + y + w + z)**3) == 0):
#                     print(a)
#
# for x in range(10):
#     for y in range(10):
#         for w in range(10):
#             for z in range(10):
#                 for p in range(10):
#                     a = (1234*100000) + (p * 10000) + (z*1000) + (w * 100) + (y * 10) + x
#                     if (a % 137 == 0) and ((p * 10000 + z*1000 + w * 100 + y * 10 + x) % ((p + x + y + w + z)**3) == 0):
#                         print(a)

from fnmatch import *

for i in range(137, (10 ** 10) + 1, 137):
    if fnmatch(str(i), '1234*'):
        n = int(str(i)[4:])
        s = sum(list(map(int, str(n)))) ** 3
        if n % s == 0:
            print(i)
