def p(n):
    d = 2
    while d * d < n:
        if n % d == 0:
            return 0
        d += 1
    return 1



for n in range(99, 10000):
    a = '0' + n * '2' + n * '1' + '0'
    while '00' not in a:
        a = a.replace('02', '101', 1)
        a = a.replace('11', '2', 1)
        a = a.replace('12', '21', 1)
        a = a.replace('010', '00', 1)

    if p(sum(list(map(int,a)))) and str(sum(list(map(int,a)))) == str(sum(list(map(int,a))))[::-1]:
        print(n)
        break


