n = int(input())
numbers = list(map(int, input().split()))

for i in range(1, n):
    ok = False
    for k in range(i, 0, -1):
        if numbers[k] < numbers[k - 1]:
            numbers[k], numbers[k - 1] = numbers[k - 1], numbers[k]
            ok = True
        else:
            break
    if ok:
        print(*numbers)
