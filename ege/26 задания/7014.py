f = open('26_7014 (1).txt')
n = int(f.readline())

a = [int(x) for x in f]
s = 0
counter = 1
ans = []
for x in range(len(a)):
    f = 0
    for y in range(x + 1, len(a)):
        if a[y] >= a[x]:
            f = 1
            break
    if f == 1:
        counter += 1
        continue
    if f == 0:
        s += counter * a[x]
        ans.append(counter * a[x])
        counter = 1

ans.sort()
print(s,ans[-1])