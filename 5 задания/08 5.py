for i in range(1,1000000):
    n1 = bin(i)[2:]
    edin = 0
    null = 0
    for k in range(0,len(n1),2):
        if n1[k] == '0':
            null += 1
    for k in range(1,len(n1),2):
        if n1[k] == '1':
            edin += 1
    if abs(null - edin) == 5:
        print(i,n1)
        break
print((691200*3600)/ (27 * (2**46)))