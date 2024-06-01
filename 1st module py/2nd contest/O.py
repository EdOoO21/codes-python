a = list(map(int, str(input()).split()))
n = a[0]
a.pop(0)
i = 0
counter = 0
while True:
    if i > len(a) - 3:
        break
    else:
        if (a[i] == a[i + 1]) and (a[i] == a[i + 2]) and (a[i + 1] == a[i + 2]):
            b = i + 2
            for k in range(i + 2, len(a) - 1):
                if a[k] == a[k + 1]:
                    b = k + 1
                else:
                    break
            a = a[:i] + a[b + 1:]
            counter += (b - i + 1)
            i = 0
        else:
            i += 1
print(counter)