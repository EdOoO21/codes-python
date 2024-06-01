f = open('26_5988 (1).txt')
n = int(f.readline())
sp = f.readlines()
for i in range(n):
    sp[i] = list(sp[i].split())
    sp[i][0] = int(sp[i][0])

sp = sorted(sp, reverse=True, key=lambda j: j[0])
korobs = []
a = []

for i in range(len(sp)):
    if sp[i] == 0:
        continue
    if len(a) == 0:
        a.append(sp[i])
        sp[i] = 0
        continue
    else:
        for j in range(i + 1, len(sp)):
            if sp[j] != 0:
                if (a[-1][0] - sp[j][0]) >= 7 and a[-1][1] != sp[j][1]:
                    a.append(sp[j])
                    sp[j] = 0
                else:
                    for k in korobs:
                        for b in range(1, len(k) - 1):
                            if ((a[-1][0] - k[b][0]) >= 7 and a[-1][1] != k[b][1]) \
                                    and (
                                    (sp[j][0] - k[b + 1][0]) >= 7 and (k[b - 1][0] - sp[j][0]) >= 7 and k[b - 1][1] !=
                                    sp[j][1] and k[b + 1][1] != sp[j][1]):
                                print(sp[j], k[b], '||||', k[b - 1], k[b + 1], '|||||', a[-1])
                                k[b] = sp[j]

                                a.append(k[b])
                                sp[j] = 0
                                break
                        if sp[j] == 0:
                            break
                        if (abs(a[-1][0] - k[0][0]) >= 7 and a[-1][1] != k[0][1]) \
                                and (abs(sp[j][0] - k[0 + 1][0]) >= 7 and k[0 + 1][1] != sp[j][1]):
                            print(sp[j], k[0], '||||', k[0 + 1], '|||||', a[-1])
                            k[0] = sp[j]

                            a.append(k[0])
                            sp[j] = 0
                            break
                        if (abs(a[-1][0] - k[-1][0]) >= 7 and a[-1][1] != k[-1][1]) \
                                and (abs(sp[j][0] - k[-2][0]) >= 7 and k[-2][1] != sp[j][1]):
                            print(sp[j], k[-1], '||||', k[-2], '|||||', a[-1])
                            k[-1] = sp[j]
                            a.append(k[len(k) - 1])
                            sp[j] = 0
                            break
                        if sp[j] == 0:
                            break

        korobs.append(a)
        a = []

m,minv = 0,10**100
for i in korobs:
    m = max(m, len(i))
    minv= min(minv,i[-1][0])
print(m, minv)

print(korobs)
