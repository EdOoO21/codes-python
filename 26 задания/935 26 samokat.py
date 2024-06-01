f = open('26 (5).txt')
m, n = map(int, f.readline().split())
sp = f.readlines()
for i in range(n):
    sp[i] = list(map(int, sp[i].split()))
park = [[] for _ in range(m + 1)]
sp = sorted(sp, key=lambda i: i[0])
samokat = 0
maxv = 0
time = []
for i in sp:
    time.append(i[0])
    time.append(i[0] + i[1])
time.sort()
s = 0
ans = 0
for d in range(time[-1]):
    ans1 = 0
    ss = []
    if s < n:
        while sp[s][0] == d:
            ss += [sp[s]]
            s += 1
            if s == n - 1:
                break
        if len(ss) >= 1:
            for i in ss:
                f = 0
                minv = 10 ** 15
                for k in range(len(park[i[2]])):
                    if type(park[i[2]][k]) == int:
                        if park[i[2]][k] < i[0] and park[i[2]][k] != 0:
                            park[i[2]][k] = 0
                            park[i[3]] += [[i[0], i[0] + i[1]]]
                            f = 1
                            break
                    if type(park[i[2]][k]) == list:
                        if park[i[2]][k][1] < i[0]:
                            park[i[2]][k] = 0
                            park[i[3]] += [[i[0], i[0] + i[1]]]
                            f = 1
                            break
                if f == 0:
                    samokat += 1
                    park[i[3]] += [[i[0], i[0] + i[1]]]
    for h1 in park:
        for h in h1:
            if type(h) == list:
                if h[1] > d:
                    ans1 += 1
    ans = max(ans1, ans)

print(samokat, ans)
