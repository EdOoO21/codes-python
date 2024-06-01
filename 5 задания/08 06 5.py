for n in range(1,100000):
    i = bin(n)[2:]
    if n % 5 == 0:
        i1 = i + i[-3:]
    else:
        i1 = i + bin((n % 5)*5)[2:]
    if int(i1,2) > 256:
        print(n,i1,int(i1,2))
        break