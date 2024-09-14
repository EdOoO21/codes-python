from math import *


def f(x, p, k):
    if floor(x * 1.25) - k > 215 and p == 5:
        return 1
    if (floor(x * 1.25) - k > 215 and p != 5) or (floor(x * 1.25) - k <= 215 and p == 5):
        return 0
    if p % 2 == 0:
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

