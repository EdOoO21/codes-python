a = [int(x) for x in open('C:/Users/arbag/Desktop/файлы python/2210201 17.txt')]
minv = 9999999999
for i in a:
    if (minv > i) and (abs(i) % 10 == 5):
        minv = i

s = []
counter = 0
for i in range(len(a)-1):
    if (abs(min(a[i],a[i+1])) % 10 == 5) and ((a[i])**2 + (a[i+1])**2 < (minv)**2):
        counter += 1
        s.append((a[i])**2 + (a[i+1])**2)
print(counter,max(s))