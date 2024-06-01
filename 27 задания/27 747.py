f=open('27A_8381.txt')
n, d, t = map(int, f.readline().split())
a = [int(x) for x in f]
counter = 0

for i in range(len(a) - 1):
    for j in range(i + t, len(a)):
        if a[i] % d != 0 and a[j] % d != 0:
            k = [x for x in a[i + 1:j] if x % d == 0]
            if len(k) == t:
                counter += 1

print(counter)
