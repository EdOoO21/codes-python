n = int(input())
a = [int(input()) for _ in range(n - 1)]
a.sort()
if n == 1:
    print(1)
elif a[0] != 1:
    print(1)
elif a[-1] != n:
    print(n)
else:
    for i in range(n - 2):
        if a[i] != (a[i + 1] - 1):
            print(a[i] + 1)
            break


