f = open('6320')
n1 = 50
m = 3500
a = [[0, 0] for _ in range(m)]
for i in a:
    i[0], i[1] = list(map(int, f.readline().split()))
a = sorted(a, key=lambda i: i[0])
print(a)
start = 600
end = 1320
tr = [0] * n1

counter = 0
for i in a:
    for n in range(len(tr)):
        if tr[n] < i[0]:
            tr[n] = i[1]
            counter += 1
            print(n + 1)
            break
print(counter)

