f = open('6286')
f = f.readlines()
ans = {}
f[999] += '00'

for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    ans[l] = 0

for i in f:
    sl = {}
    i = i[:-2]

    for p in range(len(i) - 1):
        if i[p] == 'X':
            if i[p + 1] not in sl.keys():
                sl[i[p + 1]] = 1
            else:
                sl[i[p + 1]] += 1

    m = max(sl.values())

    for p in sl.items():
        if p[1] == m:
            ans[p[0]] += 1

print(max(ans.values()), ans)
