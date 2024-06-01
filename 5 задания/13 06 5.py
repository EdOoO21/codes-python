for n in range(1,10000):
    i = bin(n)[2:]
    if n % 2 == 0:
        i1 = ''
        for k in range(0, len(i)):
            i1 += i[k] * 2
    else:
        i2,i1 = '',''
        for k in range(0, len(i)):
            if i[k] == '0':
                i2 += '1'
            else:
                i2 += '0'
        for k in range(0, len(i)):
            i1 += i2[k] * 2
    if int(i1,2) > 60:
        print(i1,n)
        break




