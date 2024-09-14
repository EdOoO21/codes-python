a = [int(x) for x in open('C:/Users/arbag/Desktop/файлы python/0901 17.txt')]
s1 = []
for i in a:
    if i % 73 == 0:
        s1.append(i)
maxv = max(s1)

s = []

for i in range(len(a) - 1):
    if a[i] >= maxv and a[i + 1] >= maxv:
        s.append(a[i] + a[i + 1])

print(len(s), max(s))
