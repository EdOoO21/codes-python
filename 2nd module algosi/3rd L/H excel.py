from collections import deque
n = int(input())
arr = list(map(int, input().split()))
d = {i: 0 for i in list(set(arr))}
ans = deque()
for i in range(n - 1, -1, -1):
    if d[arr[i]] == 1:
        continue
    else:
        ans.appendleft(arr[i])
        d[arr[i]] = 1

print(len(ans))
print(*ans)