from math import ceil

f = open('26 (10).txt')
n = int(f.readline())
k = int(f.readline())
c = int(f.readline())

park = [[0 for _ in range(k)], [0 for _ in range(k)], [0 for _ in range(k)]]

sp = f.readlines()

for i in range(len(sp)):
    sp[i] = list(map(int, sp[i].split()))
sp = sorted(sp, key=lambda i: i[0])
counter = 0
s = 0
for i in sp:
    for m in range(k):
        if park[i[2] - 1][m] == 0:
            park[i[2] - 1][m] = i[1]
            counter += 1
            if i[2] - 1 == 0:
                s += (ceil((i[1] - i[0]) / 3600)) * c
            elif i[2] - 1 == 1:
                s += (ceil((i[1] - i[0]) / 3600)) * 2 * c
            elif i[2] - 1 == 2:
                s += (ceil((i[1] - i[0]) / 3600)) * 4 * c
            break
        elif park[i[2] - 1][m] <= i[0] - 60:
            park[i[2] - 1][m] = i[1]
            counter += 1
            if i[2] - 1 == 0:
                s += (ceil((i[1] - i[0]) / 3600)) * c
            elif i[2] - 1 == 1:
                s += (ceil((i[1] - i[0]) / 3600)) * 2 * c
            elif i[2] - 1 == 2:
                s += (ceil((i[1] - i[0]) / 3600)) * 4 * c
            break

print(s, counter)
