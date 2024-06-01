f = open('27a (3).txt')
n = int(f.readline())

k = int(f.readline())
t = int(f.readline())

a = [int(x) for x in f]
m = [0]

for i in range(len(a) - k - t - 1):
    for n in range(i + t + k, len(a) - k + 1):
        if sum(m) < a[i] + a[i + k - 1] + a[n] + a[n + k - 1]:
            m = [a[i], a[i + k - 1], a[n], a[n + k - 1]]

m = [0,0]
for i in range(len(a) - k):
    for n in range(i, len(a) - k):
        if abs(i + k - 1 - n) >= t + 1:
            if sum(m) < sum(a[i: i + k]) + sum(a[n: n + k]):

                a1 = a[i: i + k]
                a2 = a[n: n + k]
                m = a1 + a2

print(sum(m),m)
