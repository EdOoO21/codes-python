n = int(input())
line = []
for _ in range(n):
    k = list(map(int, input().split()))
    line += [[k[0],1]] + [[k[0] + k[1],-1]]

line = sorted(line, key=lambda x: x[1])
line = sorted(line, key=lambda x: x[0])

maxv = 0
counter = 0
for i in line:
    if i[1] == 1:
        counter += 1
        maxv = max(counter,maxv)
    else:
        counter -= 1


print(maxv)