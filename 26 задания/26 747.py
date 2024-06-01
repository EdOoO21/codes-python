f = open('26_8380.txt')
k, n = map(int, f.readline().split())
a = [list(map(int, s.split())) for s in f]
a = sorted(a, key=lambda i: i[0], reverse=False)

doms = [[0] * 10 for _ in range(20)]
for i in a:
    f = 0
    for x in doms:
        for y in range(10):
            if x[y] <= i[0]:
                x[y] = i[1] + 1
                f = 1
                break
        if f == 1:
            break

n = doms.index([0]*10)
print(n,end=' ')
kon = a[-1][0]
counter = 0
for i in doms:
    for x in range(10):
        if i[x] - 1 >= kon + 1:
            counter += 1

print(counter)
