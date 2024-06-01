n, m = int(input()), int(input())


def ReduceFraction(n, m):
    s = 0
    for i in range(2, (min(n, m) + 1)):
        if (n % i == 0) and (m % i == 0):
            s = i

    if s != 0:
        return (n // s, m // s)

    return (n, m)


print(*ReduceFraction(n, m))
