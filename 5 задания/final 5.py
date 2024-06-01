for n in range(1,100000):
    i = bin(n)[2:]
    if i.count('0') % 2 == 0:
        i1 = i + i[-2:]
    else:
        i1 = '1' + i + i[-1:]
    i1 += bin(n % 2)[2:]
    if int(i1,2) == 480:
        print(int(i1,2),i1,n)
