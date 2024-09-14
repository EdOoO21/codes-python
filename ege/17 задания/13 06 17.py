a = [int(x) for x in open('17 (12).txt')]
maxv = 0
for i in a:
    if len(str(abs(i))) == 2:
        maxv = max(maxv, i)

ans = []

for i in range(len(a) - 1):
    if ((len(str(abs(a[i]))) == 2) + (len(str(abs(a[i + 1]))) == 2)) != 0 \
            and (a[i] + a[i + 1]) <= maxv:
        ans.append(a[i] + a[i + 1])

print(len(ans), max(ans))
