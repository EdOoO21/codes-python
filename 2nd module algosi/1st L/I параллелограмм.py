def p(p1, p2):
    return (((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)) ** 0.5


amount_p = int(input())
for i in range(amount_p):
    a = tuple(map(int, input().split()))
    a = [(a[0], a[1]), (a[2], a[3]), (a[4], a[5]), (a[6], a[7])]
    a = sorted(a, key=lambda i: (i[0], i[1]))
    try:
        k = (a[3][1] - a[2][1])/(a[3][0] - a[2][0])
        b = a[2][1] - (k*a[2][0])
        f = 0
        for i in range(4):
            if a[i][1] == (k*a[i][0]) + b:
                f += 1
    except ZeroDivisionError:
        if len(set(a)) == len(a):
            if ((p(a[0], a[1]) == p(a[2], a[3])) and (p(a[0], a[3]) == p(a[2], a[1]))) or (
                    (p(a[0], a[1]) == p(a[2], a[3])) and (p(a[0], a[2]) == p(a[1], a[3]))):
                print('YES')
            elif ((p(a[0], a[2]) == p(a[1], a[3])) and (p(a[0], a[3]) == p(a[2], a[1]))) or (
                    (p(a[0], a[2]) == p(a[1], a[3])) and (p(a[0], a[1]) == p(a[2], a[3]))):
                print('YES')
            elif ((p(a[0], a[3]) == p(a[1], a[2])) and (p(a[0], a[1]) == p(a[2], a[3]))) or (
                    (p(a[0], a[3]) == p(a[1], a[2])) and (p(a[0], a[2]) == p(a[1], a[3]))):
                print('YES')
            else:
                print('NO')
        else:
            print('NO')

    else:
        if len(set(a)) == len(a) and f != 4:
            if ((p(a[0], a[1]) == p(a[2], a[3])) and (p(a[0], a[3]) == p(a[2], a[1]))) or (
                    (p(a[0], a[1]) == p(a[2], a[3])) and (p(a[0], a[2]) == p(a[1], a[3]))):
                print('YES')
            elif ((p(a[0], a[2]) == p(a[1], a[3])) and (p(a[0], a[3]) == p(a[2], a[1]))) or (
                    (p(a[0], a[2]) == p(a[1], a[3])) and (p(a[0], a[1]) == p(a[2], a[3]))):
                print('YES')
            elif ((p(a[0], a[3]) == p(a[1], a[2])) and (p(a[0], a[1]) == p(a[2], a[3]))) or (
                    (p(a[0], a[3]) == p(a[1], a[2])) and (p(a[0], a[2]) == p(a[1], a[3]))):
                print('YES')
            else:
                print('NO')
        else:
            print('NO')


