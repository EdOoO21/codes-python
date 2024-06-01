n = int(input())
line = list(map(int,input().split()))
arr = sorted(line)
i = 0
stack = []
k = 0
while i <= n - 1:
    if len(stack) > 0 and stack[-1] == arr[i]:
        stack.pop(-1)
        i += 1
    elif len(stack) == 0 or stack[-1] != arr[i] and k <= n - 1:
        stack.append(line[k])
        k += 1
    elif len(stack) == 0 or stack[-1] != arr[i] and k >= n:
        stack = [1]
        break




if not stack:
    print('YES')
else:
    print('NO')
