for i in range(1, 10000):
    n1 = bin(i)[2:]
    n = n1 + n1[-1]

    if n1.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'

    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'

    if int(n, 2) > 105:
        print(int(n, 2))
        break
