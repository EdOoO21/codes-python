a = [int(x) for x in open('17 (11).txt')]
minv = 1000000

for i in a:
    if len(str(abs(i))) == 2 and (abs(i) % 10) == 1:
        minv = min(minv,i)

minv = minv ** 2
ans = []
for i in range(len(a) - 1):
    if ((a[i] ** 2 < minv) + (a[i + 1]**2 < minv)) == 1 and (a[i] + a[i + 1]) >= 0:
        ans.append(a[i] + a[i + 1])

print(len(ans),min(ans))