f = open('26 урок.txt')
p = list(map(int, f.readline().split()))
t, n, m = p[0], p[1], p[2]

sp = f.readlines()
for h in range(len(sp)):
    sp[h] = list(map(int, sp[h].split()))

    if sp[h][2] >= m:
        sp[h] = 0

while sp.count(0) > 0:
    sp.remove(0)


po = []
sp = sorted(sp, key=lambda j: j[0])

ans = [0, 0]

for i in range(0, 1441, t):

    for p in range(0, len(sp)):
        if sp[p][0] <= i:

            po.append(sp[p] + [0])
            sp[p] = 0
        else:
            break

    while sp.count(0) > 0:
        sp.remove(0)


    for k in range(len(po)):
        if po[k][1] < i or ((po[k][2] + po[k][3]) >= m):
            if (po[k][3]) > ans[1]:
                ans[0] = po[k][1] - po[k][0] + 1
                ans[1] = po[k][3]
            po[k] = 0
    while po.count(0) > 0:
        po.remove(0)

    mintov = 999999999999999
    maxtime = 0

    for l in range(len(po)):
        mintov = min(mintov, po[l][2] + po[l][3])
        maxtime = max(maxtime, po[l][1])

    for n in range(len(po)):
        if po[n][1] == maxtime and (po[n][2] + po[n][3]) == mintov:
            po[n][3] += 1

print(*ans)

