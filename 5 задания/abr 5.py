
for i in range(1,10000):
    n1 = bin(i)[2:]
    if n1.count('1') % 2 == 0:
        n = '1' + n1[2:] + '0'
    else:
        n = '11' + n1[2:] + '1'
    rez = int(n,2)
    if rez == 50:
        print(i,n1,n,rez)
        break
