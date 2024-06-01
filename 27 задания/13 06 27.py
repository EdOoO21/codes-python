f = open('5.txt')
n = int(f.readline())
ans = []
sp = [[]for _ in range(23)]
dl = [0] * 23

for i in f:
    i1 = int(i)

    sp[i1 % 23].append(i1)

for i in range(23):
    if len(sp[i]) != 0:
        dl[i] = i


for i in range(23)[::-1]:
    if len(sp[i]) != 0 and sum(dl[:i]) + i < 23:
        continue


