for n in range(1,100000):
    i = bin(n)[2:]
    if n % 2 == 0:
        i1 = '1' + i + str(i.count('1') % 2)
    else:
        i1 = i + '0' + str(i.count('1') % 2)

    if int(i1,2) == 101:
        print(n)