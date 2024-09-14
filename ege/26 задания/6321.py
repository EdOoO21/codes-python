banki = 2
kl = 5
f = open('26 (2).txt')
s = [[0, 0] for _ in range(kl)]

for i in s:
    i[0], i[1] = map(int, f.readline().split())
s = sorted(s, key=lambda i: i[0])
print(s)

bank = [0] * banki
ans = []
ochered = []


for i in s:
    f = 0
    for n in range(banki):
        if bank[n] <= i[0]:
            if len(ochered) == 0:
                bank[n] = (i[0] + i[1])
                f = 1
                break
            else:
                bank[n] = ochered[0]
                ochered.pop(0)
                ochered.append(i[0] + i[1])
                per = 1
                f = 1
                while per == 1:
                    flag = 0
                    for j in range(banki):
                        if bank[j] <= i[0]:
                            bank[j] = ochered[0]
                            ochered.pop(0)
                            per = 1
                            flag = 1
                            break
                    if flag == 0:
                        per = 0

    if f == 0:
        minv = 99999999999
        ochered.append(i[0] + i[1])
        for p in range(banki):
            minv = min(bank[p] - ochered[0], minv)

        ans.append(minv)

print(max(ans))
