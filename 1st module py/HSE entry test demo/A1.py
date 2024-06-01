a = list(map(int,str(input()).split()))
cc = (a[1]*a[0]) + (a[2]*a[3])
f = 0
for i in range(cc,100000):
    for n in range(1,i + 1):
        if i % n == 0:
            b = (i // n)
            if ((n - a[0] <= a[2]) and (b - a[1] <= a[3]))\
                or ((b - a[0] <= a[2]) and (n - a[1] <= a[3]))

