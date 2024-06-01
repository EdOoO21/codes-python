n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

arr2 = [[0 for _ in range(m)] for _ in range(n)]

arr2[0][0] = arr[0][0]
for i in range(1, m):
    arr2[0][i] = arr[0][i]
    arr[0][i] += arr[0][i - 1]
for i in range(1, n):
    arr2[i][0] = arr[i][0]
    arr[i][0] += arr[i - 1][0]


for i in range(1, n):
    for j in range(1, m):
        arr2[i][j] = arr[i][j]
        arr[i][j] += min(arr[i - 1][j], arr[i][j - 1])




from collections import deque
ans = deque([[n,m]])
i,j = n-1,m-1
while i + j != 0:
    if arr[i][j] - arr2[i][j] == arr[i-1][j]:
        ans.appendleft([i,j+1])
        i -= 1
    else:
        ans.appendleft([i+1, j])
        j -= 1

print(arr[-1][-1])
print(len(ans))
for i in ans:
    print(*i)