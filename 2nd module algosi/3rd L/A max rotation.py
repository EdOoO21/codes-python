def maxindex(start, end):
    max_element = a[0]
    maxel_index = 0
    for i in range(start+1, end):
        if a[i] > max_element:
            max_element = a[i]
            maxel_index = i
    return maxel_index


n = int(input())


if n > 0:
    a = list(map(int, input().split()))
    for k in range(2, n + 1)[::-1]:
        result = maxindex(0, k)
        a[k - 1], a[result] = a[result], a[k - 1]
    print(*a)


