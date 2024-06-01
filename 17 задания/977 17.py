a = [int(x) for x in open('17 (8).txt')]

minv = 999999

for x in a:
    x1 = abs(x)
    minv = min(minv, x1)

ans = []

for i in range(len(a) - 1):
    if ((a[i] == abs(a[i])) + (a[i + 1] == abs(a[i + 1]))) == 1 and ((a[i] + a[i + 1]) > 0) and (((a[i] + a[i + 1]) % minv) == 0):
        ans.append((a[i] + a[i + 1]))

print(len(ans),max(ans))
