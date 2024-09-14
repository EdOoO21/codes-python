for n in range(1, 100000000):
    n1 = hex(n)[2:]
    if n % 2 == 0:
        r = n1 + 'F'
    else:
        r = n1 + '0'
    m = 0
    for k in range(2):
        for a in r:
            m += int(a, 16)
        r += hex(m % 16)[2:]

    maxv = 0
    minv = 20

    for b in r:
        maxv = max(maxv, int(b, 16))
        minv = min(minv, int(b, 16))

    if r.count(hex(maxv)[2:]) / r.count(hex(minv)[2:]) == 5:
        print(n, r, minv, maxv)

