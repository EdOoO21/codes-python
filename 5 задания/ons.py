for i in range(1,100):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n = n + '0'
        n1 = '10' + n[2:]
    else:
        n += '1'
        n1 = '11' + n[2:]

    if int(n1,2) >= 16:
        print(i,int(n1,2),n1)
        break