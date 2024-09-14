def d(a, b):
    return a % b == 0


k = 0
for a in range(1, 10000):
    ok = True
    for x in range(-1000, 1000):
        if (d(a, 5) and ((not (d(2020, a))) <= (d(x, 1718) <= d(2023, a)))) == 0:
            ok = False
            break
    if ok:
        print(a)
        k += 1
print(k)
