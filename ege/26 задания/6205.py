f = open('6205')
l, n = map(int, f.readline().split())

sp = f.readlines()

for i in range(n):
    sp[i] = list(map(int, sp[i].split()))
    sp[i] += [sp[i][1] - sp[i][0]]

sp = sorted(sp, key=lambda i: (i[2], i[0], i[1]))
print(sp)
