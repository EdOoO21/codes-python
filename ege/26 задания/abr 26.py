n = 10000
f = open('C:/Users/arbag/Desktop/файлы python/abr 26.txt')
a = [int(x) for x in f]
a1 = a
a = sorted(a)
s = []
leng = 0
minmax = 0
minv = 999999999999


# все комбинации
ok = True
while ok:
    s = []
    for i in range(len(a)):
        if len(s) != 0:
            if a[i] != 0 and (abs(a[i] - s[len(s) - 1]) >= 6):
                s.append(a[i])
                a[i] = 0
        if len(s) == 0 and a[i] != 0:
            s.append(a[i])
            a[i] = 0

    if len(s) == 0:
        break

    leng = max(leng, len(s))
    minmax = max(minmax, s[0])
print(leng, minmax)


# 1 комбинация
a1 = sorted(a1, reverse=True)
s = [max(a1)]

for i in range(len(a)):

    if (abs(a1[i] - s[len(s) - 1]) >= 6):
        s.append(a1[i])
        a[i] = 0

print(len(s), min(s))
