for i in range(2,10000):
    n1 = bin(i)[2:]
    n2 = n1 + n1[len(n1) - 2]
    n = n2 + n2[1]

    if int(n,2) > 150:
        print(i,n1,n,int(n,2))
        break