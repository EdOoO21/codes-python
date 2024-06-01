def f(n):
    k = []
    d = 2
    while d * d < n:
        if n % d == 0:
            k.append(d)
            k.append(n // d)
        d += 1
    if d ** 2 == n:
        k.append(d)
    k.sort()
    return k


# print(f(24))
c = 0
for i in range(850001, 1000000000):
    if len(f(i)) > 0:
        t1 = max(f(i))
        t2 = min(f(i))
        if (t1 - t2) % 13 == 0:
            print(i, t1 - t2)
            c += 1
            if c > 5:
                break
