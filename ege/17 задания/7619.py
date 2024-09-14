a = [int(x) for x in open('17_7619.txt')]
m = 0
for i in a:
    if len(str(i)) == 2:
        m = max(m, i)
ans = []
for i in range(len(a) - 1):

    if (((len(str(a[i])) == 2) + (len(str(a[i + 1])) == 2)) == 1) \
            and (((a[i] + a[i + 1]) % m) == 0):
        ans.append(a[i] + a[i + 1])

print(len(ans), max(ans))
