n, m, k = map(int, str(input()).split())
a = [[0] * m for _ in range(n)]
for i in range(k):
    c = list(map(int, str(input()).split()))
    a[c[0] - 1][c[1] - 1] = '*'

    if c[0] < n and (a[c[0]][c[1] - 1] != '*'):
        a[c[0]][c[1] - 1] += 1
    if c[0] - 2 >= 0 and (a[c[0] - 2][c[1] - 1] != '*'):
        a[c[0] - 2][c[1] - 1] += 1
    if c[1] <= m - 1 and (a[c[0] - 1][c[1]] != '*'):
        a[c[0] - 1][c[1]] += 1
    if c[1] - 2 >= 0 and (a[c[0] - 1][c[1] - 2] != '*'):
        a[c[0] - 1][c[1] - 2] += 1

    if c[0] < n and c[1] - 2 >= 0 and (a[c[0]][c[1] - 2] != '*'):
        a[c[0]][c[1] - 2] += 1
    if c[0] < n and c[1] < m and (a[c[0]][c[1]] != '*'):
        a[c[0]][c[1]] += 1
    if c[0] - 2 >= 0 and c[1] - 2 >= 0 and (a[c[0] - 2][c[1] - 2] != '*'):
        a[c[0] - 2][c[1] - 2] += 1
    if c[0] - 2 >= 0 and c[1] < m and (a[c[0] - 2][c[1]]!='*'):
        a[c[0] - 2][c[1]] += 1

for i in a:
    print(*i)
