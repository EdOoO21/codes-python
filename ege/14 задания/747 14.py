for p in range(5, 100):
    for q in range(6, 100):
        a = 4 + 3 * p + 2 * (p ** 2)
        b = 5 + 4 * q + 3 * (q ** 2)
        if a == b:
            print(a)
