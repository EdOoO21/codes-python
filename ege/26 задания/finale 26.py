f = open('266')
k = int(f.readline())
n = int(f.readline())
sp = [0] * n
for i in range(n):
    sp[i] = list(map(int, f.readline().split()))

yach = [0] * k
sp = sorted(sp, key=lambda i: (i[0],i[1]))
ans = []
for i in sp:
    for j in range(len(yach)):
        if yach[j] < i[0]:
            yach[j] = i[1]
            ans.append(j + 1)
            break

print(len(ans), ans[-1], ans)

