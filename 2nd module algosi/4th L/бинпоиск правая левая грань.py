def bin_poisk(value, line, place):
    l, r = 0, len(line) - 1
    sred = r // 2
    extra = -1
    while l <= r:
        if line[sred] > value:
            r = sred - 1
        elif line[sred] < value:
            l = sred + 1

        elif place == 1:
            l = sred + 1
            extra = sred
        else:
            r = sred - 1
            extra = sred
        sred = (l + r) // 2
    extra += 1
    return extra


n = int(input())
a1 = list(map(int, input().split()))
k = int(input())
a2 = list(map(int, input().split()))
for i in a2:
    print(bin_poisk(i, a1, -1), bin_poisk(i, a1, 1))
