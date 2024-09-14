counter = 0
c = 0
for i in range(100,201):
    n = bin(i)[2:]
    if len(n) % 2 == 0:
        n += '10'
    else:
        n += '11'

    n1 = int(n,2)

    if n1 % 2 == 0 :
        counter += 1
    if n[len(n) - 1] == '0':
        c += 1

print(counter, c)