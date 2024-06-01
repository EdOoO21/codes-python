first = str(input())
second = str(input())
arr = [[0, 0] for x in range(10)]

for x in first:
    arr[int(x)][0] += 1

for x in second:
    arr[int(x)][1] += 1

answer = ''
for i in range(len(arr) - 1, -1, -1):
    answer += str(i) * min(arr[i][0], arr[i][1])

if set(answer) == {'0'}:
    print(0)
elif (not answer) or (answer[0] == '0'):
    print(-1)
else:
    print(answer)
