n = int(input())
list1 = [list(map(int, input().split())) for _ in range(n)]
list1 = sorted(list1, key=lambda x: (x[0], -x[1]))
f = set()
height = 0
for i in range(n):
    if list1[i][0] not in f:
        height += list1[i][1]
        f.add(list1[i][0])

print(height)
