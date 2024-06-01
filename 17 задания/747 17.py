a = [int(x) for x in open('17 (7).txt')]
minv = 999999999

for i in a:
    if i % 2 == 0:
        minv = min(minv,i)

ans = []

for i in range(len(a) - 2):
    if ((a[i] % 2 == 0) + (a[i+2] % 2 == 0)) == 1 and a[i+1] % minv == 0:
        ans.append(a[i] + a[i+2])

print(len(ans),min(ans))