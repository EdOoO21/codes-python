from collections import deque

n, k = map(int, input().split())
line = list(map(int, input().split()))

deque = deque()

for i in range(n):
    if i <= k - 1:
        if len(deque) > 0:
            while (len(deque) > 0) and (deque[-1][0] >= line[i]):
                deque.pop()
            deque.append((line[i], i))

        else:
            deque.append((line[i], i))
        if i == k - 1:
            print(deque[0][0])
    elif i > k - 1:
        if deque[0][1] <= i - k:
            deque.popleft()
        while (len(deque) > 0) and (deque[-1][0] >= line[i]):
            deque.pop()
        deque.append((line[i], i))
        print(deque[0][0])

