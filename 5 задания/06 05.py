for i in range(10, 100000):
    n = bin(i)[2:]
    if i % 3 == 0:
        n1 = n + n[:3]
    else:
        l = 3 * (i % 3)
        n1 = n + bin(l)[2:]
    if int(n1, 2) < 100:
        print(i,' == ',' == ',n,n1)
