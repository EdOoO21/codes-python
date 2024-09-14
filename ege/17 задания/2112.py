a = [int(x) for x in open('C:/Users/arbag/Desktop/файлы python/2112 17.txt')]
k = (max(a) + min(a)) / 2
s = []

for x in range(0,(len(a)//2)):
    if (min(a[x],a[8343-x]) < k) and (max(a[x],a[8343-x]) > k):
        s.append(a[x]+a[8343-x])

print(len(s),max(s))
