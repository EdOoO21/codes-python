def palin(x):
    for i in range((len(x) // 2) + 1):
        if x[i] != x[len(x) - i - 1]:
            return 0
    return 1


a = [int(x) for x in open('17 (13).txt')]

counter = 0

for i in a:
    if palin(str(abs(i))):
        counter += 1

ans = []
for i in range(len(a) - 1):
    if ((((len(str(abs(a[i]))) == 3) and (abs(a[i]) % 2 == 0)) + (
            (abs(a[i + 1]) % 2 == 0) and (len(str(abs(a[i + 1]))) == 3))) == 1) \
            and ((a[i] + a[i + 1]) >= counter):
        ans.append([a[i] * a[i + 1],(abs(a[i] * a[i + 1])) % 7])
ans = sorted(ans,key=lambda i:(i[1],i[0]))
print(len(ans))
