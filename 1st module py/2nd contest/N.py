n, k = map(int,str(input()).split())
a = ['I'] * n
b = []
for i in range(k):
    l, r = list(map(int, input().split()))
    b += [x for x in range(l,r + 1)]
b.sort()
for i in b:
    a[i-1] = '.'

print(*a,sep='')