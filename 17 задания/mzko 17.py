a = [0] * 5000
a1 = []
for i in range(5000):
    a[i] = int(input())
k = 0
for i in range(4999):
    if (a[i] % 4 == 0) and (a[i + 1] % 4 == 0):
        k += 1
        a1.append(a[i] + a[i + 1])

print(k, max(a1), sep='')
