a = [int(x) for x in open('C:/Users/arbag/Desktop/файлы python/17 ons.txt')]
minimal = min(a)
counter = 0
s = []
for i in range(len(a) - 1):
    if (a[i] % 117 == minimal) or (a[i+1] % 117 == minimal):
        s.append(a[i] + a[i+1])
        counter += 1

print(counter,max(s))