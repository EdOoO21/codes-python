def merge(a, b, c):
    d = []
    max_ind_a = len(a)
    max_ind_b = len(b)
    max_ind_c = len(c)
    i = 0
    j = 0
    k = 0
    while (i < max_ind_a) and (j < max_ind_b) and (k < max_ind_c):
        if (a[i] >= b[j]) and (c[k] >= b[j]):
            d.append(b[j])
            j += 1
        elif (a[i] >= c[k]) and (b[j] >= c[k]):
            d.append(c[k])
            k += 1
        elif (c[k] >= a[i]) and (b[j] >= a[i]):
            d.append(a[i])
            i += 1

    if i == max_ind_a:
        while (k < max_ind_c) and (j < max_ind_b):
            if c[k] > b[j]:
                d.append(b[j])
                j += 1
            else:
                d.append(c[k])
                k += 1
        d = d + c[k:] + b[j:]

    elif j == max_ind_b:
        while (k < max_ind_c) and (i < max_ind_a):
            if c[k] > a[i]:
                d.append(a[i])
                i += 1
            else:
                d.append(c[k])
                k += 1
        d = d + c[k:] + a[i:]

    elif k == max_ind_c:
        while (i < max_ind_a) and (j < max_ind_b):
            if a[i] > b[j]:
                d.append(b[j])
                j += 1
            else:
                d.append(a[i])
                i += 1
        d = d + b[j:] + a[i:]

    return d


n = list(map(int, input().split()))
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
print(*merge(a1, a2, a3))