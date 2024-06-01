for n1 in range(1, 100000000):
    n = bin(n1)[2:]
    if n1 % 3 == 0:
        n2 = n + n[-3:]
    else:
        k = bin((n1 % 3) * 3)[2:]
        n2 = n + k
    if int(n2, 2) > 76:
        print(n1, n, int(n2, 2))
        break
