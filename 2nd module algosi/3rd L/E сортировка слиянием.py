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


n1 = int(input())
a1 = list(map(int, input().split()))
n2 = int(input())
a2 = list(map(int, input().split()))
print(*merge(a1, a2))
