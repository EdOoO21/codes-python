f = open('26 дз.txt')
print(f.readline())
print(f.readline())
b = [[[0, 0] for s in range(15)]] + [[[0, 0] for s in range(10)]] + [[[0, 0] for s in range(1)]] + [
    [[0, 0] for s in range(11)]] + [[[0, 0] for s in range(7)]] + [[[0, 0] for s in range(55)]]
a = [list(map(int, s.split())) for s in f]
a.sort(key=lambda i: (i[0], i[1]))
p = []
p1 = []

for i in a:
    fl = 0
    for j in (b[(i[2]):]):

        for k in j:
            if i[0] >= k[0] + 1:
                k[0] = i[0] + i[1]
                k[1] += 1
                fl = 1
                if len(b[b.index(j)]) == 55:
                    p.append(i[0])
                break

        if fl == 1:
            break
a1 = [0]*6
for i in range(6):
    for j in range(len(b[i])):
        a1[i] += b[i][j][1]
print(a1)
m = 0
n = []
for i in b:
    col = 0
    for j in i:
        col += j[1]
    if col > m:
        m = col
        n = i
h = max([s[0] for s in n])
print(m, h)
