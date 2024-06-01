def quicksort(line, oporn):
    firstarr = []
    secondarr = []
    for i in range(n):
        if oporn > line[i]:
            firstarr.append(line[i])
        else:
            secondarr.append(line[i])
    return len(firstarr)



n = int(input())
line1 = list(map(int, input().split()))
oporn1 = int(input())
ans = quicksort(line1, oporn1)
print(ans)
print(n - ans)
