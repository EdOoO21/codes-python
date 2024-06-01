n, t = map(int,str(input()).split())
arr = [list(map(int,str(input()).split())) for _ in range(n)]

arr1 = [[0]*n for _ in range(n)]
for p in range(t):
    for i in range(n):
        if i == 0:
            for k in range(n):
                counter = 0
                if k == 0:
                    counter = arr[i+1][k] + arr[i][k + 1]
                elif k == n - 1:
                    counter = arr[i + 1][k] + arr[i][k - 1]
                else:
                    counter = arr[i + 1][k] + arr[i][k - 1] + arr[i][k + 1]
                if counter < 2 or counter > 3:
                    arr1[i][k] = 0
                if counter == 3:
                    arr1[i][k] = 1
                if counter == 2:
                    arr1[i][k] = arr[i][k]

        elif i == n - 1:
            for k in range(n):
                counter = 0
                if k == 0:
                    counter = arr[i-1][k] + arr[i][k + 1]
                elif k == n - 1:
                    counter = arr[i - 1][k] + arr[i][k - 1]
                else:
                    counter = arr[i - 1][k] + arr[i][k - 1] + arr[i][k + 1]

                if counter < 2 or counter > 3:
                    arr1[i][k] = 0
                if counter == 3:
                    arr1[i][k] = 1
                if counter == 2:
                    arr1[i][k] = arr[i][k]
        else:
            for k in range(n):
                counter = 0
                if k == 0:
                    counter = arr[i-1][k] + arr[i][k + 1] + arr[i+1][k]
                elif k == n - 1:
                    counter = arr[i - 1][k] + arr[i][k - 1] + arr[i-1][k]
                else:
                    counter = arr[i - 1][k] + arr[i][k - 1] + arr[i][k + 1] + arr[i+1][k]

                if counter < 2 or counter > 3:
                    arr1[i][k] = 0
                if counter == 3:
                    arr1[i][k] = 1
                if counter == 2:
                    arr1[i][k] = arr[i][k]

    for x in range(n):
        for y in range(n):
            arr[x][y] = arr1[x][y]


for x in range(n):
    for y in range(n):
        print(arr[x][y],end=' ')
    print()
