f = open('9_8467.txt')
counter = 0
for i in range(6877):
    a = list(map(int,f.readline().split()))
    a.sort()
    if ((len(set(a)) == len(a)) + ((a[0] + a[4])*2 < (a[1] + a[2] + a[3]))) == 1:
            counter += 1
print(counter)