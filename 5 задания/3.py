for i in range(1,1000):
    n = bin(i)[2:]
    print(n)
    if len(n) % 2 == 0:
        n1 = n[:len(n)//2] + '1' + n[len(n)//2:]
    else:
        n1 = n
    if int(n1,2) >= 26:
        print(i)
        break