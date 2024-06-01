a = list(map(int, str(input()).split()))
n = int(input())
for i in range(len(a)):
    if a[i] < n:
        print(i + 1)
        break
else:print(len(a)+1)
