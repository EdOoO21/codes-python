n, a = int(input()), list((map(int, str(input()).split())))
m, b = int(input()), list((map(int, str(input()).split())))
for i in range(n):
    for k in range(m):
        if a[i] == b[k]:
            b[k] = ''
            print(a[i],end=' ')
            break
