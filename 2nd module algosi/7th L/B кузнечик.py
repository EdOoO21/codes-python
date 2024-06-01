n, k = map(int, input().split())
arr = [0] * (n + k)
arr[0 + k] = 1
for i in range(0 + k, n + k):
    arr[i] += sum(arr[i - k:i])
print(arr[-1])
