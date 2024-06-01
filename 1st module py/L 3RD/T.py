n = int(input())

global a
global b
global c
a = 0
b = 1


def phib(k):
    global a
    global b
    global c
    if k == 0:
        return a
    c = a + b
    a, b = b, c

    return phib(k - 1)


print(phib(n))
