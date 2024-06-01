n, start, stop = map(int, input().split())

if (abs(stop - start) - 1) < (n - max(start, stop) + min(start, stop) - 1):
    print(abs(stop - start) - 1)
else:
    print(n - max(start, stop) + min(start, stop) - 1)
