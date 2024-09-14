for i in range(1, 10000000):
    n = bin(i)[2:]
    l = []
    for k in range(len(n)):
        if n[k] == '1':
            l.append('0')
        else:
            l.append('1')

    n1 = ''
    for m in l:
        n1 += m

    n1 = int(n1,2)

    if i - n1 == 999:
        print(i)
        break
