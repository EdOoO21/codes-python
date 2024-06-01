a, n = float(input()), int(input())


def power(a, n):
    s = 1
    for i in range(abs(n)):
        s *= a

    if n < 0:
        return 1 / s
    elif n > 0:
        return  s
    else:
        return 1



print(power(a, n))
