a = list(map(int, str(input()).split()))
sup = []
counter = 0
for i in range(len(a)):
    if a[i] != '':
        if a.count(a[i]) >= 2:
            counter += ((a.count(a[i])-1)*((a.count(a[i]))/2))
            m = a[i]
            k = i
            while m in a:
                if a[k] == m:
                    a[k] = ''
                k += 1
print(int(counter))

