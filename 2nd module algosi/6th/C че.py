n, r = map(int, input().split())
line = list(map(int, input().split()))
ans = 0
right = 0

for i in range(n - 1):
    while (right <= n - 1) and (line[right] - line[i] <= r):
        right += 1
    ans += n - right

print(ans)
