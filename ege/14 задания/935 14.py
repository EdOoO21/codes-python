s = 10 ** 15
for p in range(6, 10000):
    for q in range(6, 1000):
        a = 1 + 5 * p + 3 * (p ** 2) + 4 * (p ** 3) + 2 * (p ** 4)
        b = 5 + 2 * q + 3 * (q ** 2) + 4 * (q ** 3) + 1 * (q ** 4)
        if a == b:
            s = min(s, a)

print(s)
