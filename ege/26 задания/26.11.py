a = [int(x) for x in open('C:/Users/arbag/Desktop/файлы python/26.11.txt')]
'''''
counter = 0
m = 0

for i in range(0,len(a)-1):
    for n in range(i+1,len(a)):
        if ((a[i] % 2) + (a[n] % 2)) == 1 and ((a[i] + a[i+1]) in a):
            m = max(m,(a[i] + a[i+1]))
            counter += 1
            print(i,n)

    if i == n:
        print('================')
        break
print(counter,m)
'''

counter = 0
m = 0
c = []
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
    else:
        c.append(i)
bb = set(b)
cc = set(c)
for i in b:
    for n in c:
        if i != n:
            if ((i % 2) + (n % 2)) == 1 and ((n + i) in a):
                counter += 1
                m = max(m, (n + i))
                print(i, n)

print(counter, m)
