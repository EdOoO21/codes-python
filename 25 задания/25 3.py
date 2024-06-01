def pr(n):
    d = 2
    while (d ** 2) <= n:
        if (n % d) == 0:
            return False
        d+=1
    return True


def f(n):
    d = 2
    s = 0
    while (d * d) < n:
        if n % d == 0:
            if pr(d):
                s += d
            if pr(n // d):
                s += (n // d)
        d += 1
    if d ** 2 == n:
        if pr(d):
            s += d
    return s


c = 0
for i in range(550001, 10 ** 10):
    if f(i) % 10 == 1:
        print(i, f(i))
        c += 1
        if c > 4:
            break
