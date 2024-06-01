def merge(a, b):
    c = []
    max_ind_a = len(a)
    max_ind_b = len(b)
    i = 0
    j = 0
    while (i < max_ind_a) and (j < max_ind_b):
        if a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    return c + a[i:] + b[j:]


def sorting_split(a):
    n = len(a)//2
    first = a[n:]
    second = a[:n]
    if len(first) > 1:
        first = sorting_split(first)
    if len(second) > 1:
        second = sorting_split(second)

    return merge(first, second)


n = int(input())
a = list(map(int, input().split()))
print(*sorting_split(a))
