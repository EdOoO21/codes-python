f = open('26 дз.txt')
d1 = list(map(int, f.readline().split()))
m, n = d1[0], d1[1]
park = [0] * m
ka = list(map(int, f.readline().split()))
for i in range(len(ka)):
    park[i] = [0] * ka[i]

sp = f.readlines()
for k in range(len(sp)):
    sp[k] = list(map(int, sp[k].split()))

sp = sorted(sp, key=lambda g: g[0])
ans = [[0, 0, 0] for _ in range(m)]

for i in sp:
    flag = 0
    for k in range(i[2], m):
        for n in range(len(park[k])):
            if park[k][n] <= i[0]:
                park[k][n] = i[0] + i[1]
                ans[k][0] += 1
                ans[k][2] = max(ans[k][2], i[0] + i[1])

                if ans[k][1] == 0:
                    ans[k][1] = i[0]

                flag = 1
                break
        if flag == 1:
            break

ans = sorted(ans, reverse=True, key=lambda i: i[0])
print(ans[0][2], ans[0][0],ans)


