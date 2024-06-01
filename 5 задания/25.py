counter = 0
for i in range(1000,10000):
    n1 = str(i)
    n = ''
    if int(n1[0]) % 4 == 0:
        n = '9' + n1[1:]
    if int(n1[0]) % 4 != 0 and int(n1[0]) % 2 == 0:
        n = '3' + n1[1:]
    if n != '':
        n2 = oct(int(n))[2:]
        if n[0] == '9' and n2[len(n2) - 1] == '4':
            counter += 1
            print(i,n,n2)
print(counter)