n = int(input())
stamina = list(map(int,input().split()))
k = int(input())
line = list(map(int,input().split()))

for i in range(k):
    stamina[line[i] - 1] -= 1
for i in range(n):
    if stamina[i] >= 0:
        print('no')
    else:
        print('yes')
