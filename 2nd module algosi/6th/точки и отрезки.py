n, m = map(int, str(input()).split())
line = []
for i in range(n):
    k = list(map(int, input().split()))
    line.append((max(k[0], k[1]), -1))
    line.append((min(k[0], k[1]), 1))
arr = list(map(int, input().split()))
k1 = {}
line += [(i, 0) for i in arr]
line = sorted(line, key=lambda x: (x[0], -x[1]))
counter = 0

for i in line:
    if i[1] == 0:
        k1[i[0]] = counter
    elif i[1] == 1:
        counter += 1
    else:
        counter -= 1

for i in arr:
    print(k1[i], end=' ')
