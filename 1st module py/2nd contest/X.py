d = {}
f = open('input.txt')
n = ''
s = []
while True:
    n = f.readline()
    if n == '':
        break
    s = n.split()
    if len(s) == 3:
        x, y, z = s[0], s[1], int(s[2])
        if (x == 'DEPOSIT') and (d.get(y) is not None):
            d[y] += z
        elif (x == 'DEPOSIT') and (d.get(y) is None):
            d[y] = z
        elif (x == 'WITHDRAW') and (d.get(y) is not None):
            d[y] -= z
        elif (x == 'WITHDRAW') and (d.get(y) is None):
            d[y] = -z


    elif len(s) == 2:
        x, y = s[0], s[1]
        if (x == 'BALANCE') and (d.get(y) is None):
            print('ERROR')
        elif (x == 'BALANCE') and (d.get(y) is not None):
            print(d[y])
        elif x == 'INCOME':
            for k in list(d.keys()):
                if (d.get(k) is not None) and d[k] > 0:
                    d[k] += int(d[k] * (int(y) / 100))

    else:
        x, y, w, z = s[0], s[1], s[2], int(s[3])
        if d.get(y) is None:
            d[y] = 0
        if d.get(w) is None:
            d[w] = 0
        d[y] -= z
        d[w] += z
