for i in range(1,1000):
    n = bin(i)[2:]
    if n[len(n) - 1] == '0':
        n += '0'
    else:
        n+='1'
    n1 = ''

    if n.count('1') % 3 == 0:
        n1 += '11' + n[2:]
    else:
        n1 += '10' + n[2:]

    if int(n1,2) >= 26:
        print(i)
        break