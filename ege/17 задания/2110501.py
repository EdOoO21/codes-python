a = [int(x) for x in open('C:/Users/arbag/Desktop/файлы python/2110501.txt')]
sred = 0
s1 = 0
s = 0
for i in range(len(a))[::2]:
    s1 += a[i]
    s += 1

sred = s1 / s
k = []
counter = 0
for i in range(len(a) - 2):
    if ((abs(a[i]) % 3) != (abs(a[i + 1]) % 3)) and ((abs(a[i + 1]) % 3) != (abs(a[i + 2]) % 3)) and ((abs(a[i]) % 3) != (abs(a[i + 2]) % 3)):
        if (a[i] < sred and a[i + 1] >= sred and a[i + 2] >= sred) \
                or (a[i] >= sred and a[i + 1] < sred and a[i + 2] >= sred) \
                or (a[i] >= sred and a[i + 1] >= sred and a[i + 2] < sred):
            k.append(a[i] + a[i + 1] + a[i + 2])
            counter += 1

print(counter, max(k))
