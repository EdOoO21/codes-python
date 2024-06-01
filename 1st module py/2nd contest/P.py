a = []
for i in range(8):
    a.append(list(map(int, str(input()).split())))
f = True
for i in range(len(a) - 1):
    if not f:
        break
    for k in range(i + 1, len(a)):
        if ((abs(a[i][0] - a[k][0])) == (abs(a[i][1] - a[k][1]))) \
                or ((a[i][0] - a[k][0]) == 0) or ((a[i][1] - a[k][1]) == 0):
            print('YES')
            f = False
            break

if f:
    print('NO')
