for i in range(10000):
    n = bin(i)[2:]

    n1 = ''
    if n.count('1') % 2 == 0:
        n1 += '10' + n[2:] + '0'
    else:
        n1 += '11' + n[2:] + '1'

    if int(n1,2) > 40:
        print(i,n,n1,int(n1,2))
        
