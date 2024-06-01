a = [int(x) for x in open('C:/Users/arbag/Desktop/файлы python/5 17.txt')]
s = []
for x in range(len(a) - 1):
    for y in range(x+1, len(a)):
        if ((a[x] - a[y]) % 36 == 0) and (a[x] % 13 == 0 or a[y] % 13 == 0):
            s.append(a[x] - a[y])


print(len(s), max(s))
