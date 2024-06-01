def p(p1, p2):
    return (((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)) ** 0.5


def k(p1, p2):
    try:
        (p2[1] - p1[1]) / (p2[0] - p1[0])
    except ZeroDivisionError:
        return 0
    else:
        return (p2[1] - p1[1]) / (p2[0] - p1[0])


amount_p = int(input())
for i in range(amount_p):
    a = tuple(map(int, input().split()))
    a = [(a[0], a[1]), (a[2], a[3]), (a[4], a[5]), (a[6], a[7])]
    a = sorted(a, key=lambda i: (i[0], i[1]))

    if len(set(a)) == len(a):
        if (p(a[0], a[1]) == p(a[2], a[3])) and (k(a[0], a[1]) == k(a[2], a[3])):
            print('YES')
        elif (p(a[0], a[2]) == p(a[1], a[3])) and (k(a[0], a[2]) == k(a[1], a[3])):
            print('YES')
        elif (p(a[0], a[3]) == p(a[1], a[2])) and (k(a[0], a[3]) == k(a[1], a[2])):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
