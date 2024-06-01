from collections import deque
deque = deque()
n = int(input())
i = 0
while i < n:
    string = str(input())
    if string == '-':
        print(deque.popleft)

    elif string[0] == '+':
        string = string.split()
        deque.append(string[-1])
    else:
        k = len(deque)
        string = string.split()
        if k % 2 == 0:
            deque = deque[:(k // 2)] + [string[-1]] + deque[(k // 2):]
        else:
            deque = deque[:(k // 2) + 1] + [string[-1]] + deque[(k // 2) + 1:]
    i += 1

