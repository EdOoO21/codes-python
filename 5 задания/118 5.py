minv = 99999999999
for n in range(1, 100000000):
    i = bin(n)[2:]
    if n % 5 == 0:
        r = i[:3] + i
    else:
        m = (n % 3) * 5
        r = i + bin(m)[2:]

    if int(r, 2) > 39000:
        minv = min(minv, int(r, 2))


print(minv)
