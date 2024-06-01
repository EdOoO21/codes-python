a = [int(x) for x in open('17 (10).txt')]

maxv = 0

for i in a:
    if len(str(i)) == 3:
        maxv = max(i, maxv)
ans = []
for i in range(len(a) - 1):
    if (((len(str(a[i])) == 3) + (len(str(a[i + 1])) == 3)) == 1) and (((a[i] * a[i + 1]) % maxv) == 0):
        ans.append(a[i] * a[i + 1])

print(len(ans), min(ans))
