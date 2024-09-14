from math import *


def f(x, p, k):
    if floor(x * 1.25) - k > 215 and p == 4:
        return 1
    if (floor(x * 1.25) - k > 215 and p != 4) or (floor(x * 1.25) - k <= 215 and p == 4):
        return 0
    if p % 2 == 1:
        if floor(x * 1.5) - k > 215:
            return any([f(floor(x * 1.25), p + 1, k)])
        elif floor(x * 1.75) - k > 215:
            return any([f(floor(x * 1.25), p + 1, k), f(floor(x * 1.5), p + 1, k)])
        elif floor(x * 2.1) - k > 215:
            return any([f(floor(x * 1.25), p + 1, k), f(floor(x * 1.5), p + 1, k), f(floor(x * 1.75), p + 1, k)])
        else:
            return any([f(floor(x * 1.25), p + 1, k), f(floor(x * 1.5), p + 1, k), f(floor(x * 1.75), p + 1, k),
                        f(floor(x * 2.1), p + 1, k)])
    else:
        if floor(x * 1.5) - k > 215:
            return all([f(floor(x * 1.25), p + 1, k)])
        elif floor(x * 1.75) - k > 215:
            return all([f(floor(x * 1.25), p + 1, k), f(floor(x * 1.5), p + 1, k)])
        elif floor(x * 2.1) - k > 215:
            return all([f(floor(x * 1.25), p + 1, k), f(floor(x * 1.5), p + 1, k), f(floor(x * 1.75), p + 1, k)])
        else:
            return all([f(floor(x * 1.25), p + 1, k), f(floor(x * 1.5), p + 1, k), f(floor(x * 1.75), p + 1, k),
                        f(floor(x * 2.1), p + 1, k)])


for s in range(4, 173):
    if f(s, 1, s):
        print(s)


# def f(s0, input.txt, c, m):
#     if (int(input.txt * 1.25 + 0.5) > s0) and (int(input.txt * 1.5 + 0.5) > s0) and (int(input.txt * 1.75 + 0.5) > s0) and (
#             int(input.txt * 2.1 + 0.5) > s0):
#         return c % 2 == m % 2
#     if c == m:
#         return False
#     h = [f(s0, int(input.txt * 1.25), c + 1, m), f(s0, int(input.txt * 1.5), c + 1, m), f(s0, int(input.txt * 1.75), c + 1, m),
#          f(s0, int(input.txt * 2.1), c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for input.txt in range(4, 173):
#     for m in range(5):
#         if f(input.txt + 215, input.txt, 0, m):
#             print(input.txt, m)
#             break
