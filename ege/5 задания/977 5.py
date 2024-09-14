for n in range(1, 1000000):
    i = bin(n)[2:]
    if n % 11 == 0:
        i1 = i + i.count('0') * '0'
    else:
        i1 = i.count('1') * '1' + i
    if int(i1, 2) % 227 == 0:
        print(n)
        break
