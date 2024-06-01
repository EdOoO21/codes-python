n = int(input())
i = 4
arr = [''] * (n + 1)

if n == 2 :
    print(1)
    print('1 2')
elif n == 3:
    print(1)
    print('1 3')
elif n == 1:
    print(0)
    print(1)
else:
    arr[1] = ''
    arr[2] = '2'
    arr[3] = '3'
    while i < n + 1:
        a = len(arr[i // 2])
        b = len(arr[i // 3])
        c = len(arr[i - 1])
        if (i % 2 == 0) and (i % 3 == 0):

            if a == min(a, c, b):
                arr[i] = arr[i // 2] + f' {i}'

            elif b == min(a, b, c):
                arr[i] = arr[i // 3] + f' {i}'
            else:
                arr[i] = arr[i - 1] + f' {i}'
        elif i % 2 == 0:
            if a == min(a, c):
                arr[i] = arr[i // 2] + f' {i}'
            else:
                arr[i] = arr[i - 1] + f' {i}'
        elif i % 3 == 0:
            if b == min(b, c):
                arr[i] = arr[i // 3] + f' {i}'
            else:
                arr[i] = arr[i - 1] + f' {i}'
        else:
            arr[i] = arr[i - 1] + f' {i}'
        i += 1
    print(len((arr[n]).split()))
    print('1 ' + arr[n])
