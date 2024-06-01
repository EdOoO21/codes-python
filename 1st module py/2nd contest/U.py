d = {}
f = open('input.txt')
n = ''
while True:
    n = f.readline()
    if n == '':
        break
    x, y, z = n.split()
    z = int(z)
    if d.get(x) is None:
        d[x] = {}
        d[x][y] = z
    else:
        if d[x].get(y) is None:
            d[x][y] = z
        else:
            d[x][y] += z

d = dict(sorted(d.items(), key=lambda i: i[0]))
for i in list(d.keys()):
    d[i] = dict(sorted(d[i].items(), key=lambda i: (i[0], i[1])))
    print(i,':',sep='')
    for k in list(d[i].keys()):
        print(k,d[i][k])


