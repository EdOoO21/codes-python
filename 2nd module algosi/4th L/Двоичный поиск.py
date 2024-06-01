def bin_poisk(value, line):
    l, r = 0, len(line) - 1
    sred = r // 2
    while l <= r:
        if line[sred] > value:
            r = sred - 1
        elif line[sred] < value:
            l = sred + 1
        else:
            return 1
        sred = (l+r) // 2
    return 0




n, k = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

for i in a2:
    if bin_poisk(i,a1):
        print('YES')
    else:
        print('NO')