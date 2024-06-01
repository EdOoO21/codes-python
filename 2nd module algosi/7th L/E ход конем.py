n, m = map(int, input().split())

ans = [[0 for n in range(m)]for _ in range(n)]
ans[0][0] = 1
for x in range(n):
    for y in range(m):
        if x - 2 >= 0:
            ans[x][y] += ans[x - 2][y - 1]
        if y - 2 >= 0:
            ans[x][y] += ans[x - 1][y - 2]
print(ans[-1][-1])

