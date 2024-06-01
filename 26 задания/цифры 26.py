a = [int(x) for x in open('C:/Users/arbag/Desktop/файлы python/26 цифры.txt')]
b = []
c = 5000
for i in a:
    if i % 2 == 0:
        b.append(i)

m = 0
counter = 0
for i in range(len(b)-1):
    for n in range(i+1,len(b)):
        if ((b[i] + b[n]) // 2 ) in a:
            counter += 1
            m = max(m,((b[i] + b[n]) // 2 ))
            print(i,n)
        if i == n:
            print('=============================')

print(counter,m)
