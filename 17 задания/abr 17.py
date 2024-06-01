a = [int(x) for x in open('C:/Users/arbag/Desktop/файлы python/abr 17.txt')]
max12 = 0
for i in a:
    if i % 100 == 12:
        max12 = max(i,max12)

max12 = max12**2
s = []
for i in range(len(a) - 1):
    if (((a[i] % 100 == 12) + (a[i+1] % 100 == 12)) == 1) and ((a[i] + a[i+1])**2) < max12:
        s.append(a[i] + a[i+1])
print(len(s),max(s))