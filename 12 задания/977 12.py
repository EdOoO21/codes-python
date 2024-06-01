for n in range(1, 10000):
    l = '>' + '0' * 37 + '1' * n + '2' * 37
    while '>0' in l or '>1' in l or '>2' in l:
        if '>1' in l:
            l = l.replace('>1', '22>', 1)
        if '>2' in l:
            l = l.replace('>2', '2>', 1)
        if '>0' in l:
            l = l.replace('>0', '1>', 1)

    s = 0
    for x in l[:-1]:
        s += int(x)
    f = 0
    for i in range(2, int(s ** 0.5) + 1):
        if s % i == 0:
            f = 1
            break
    if f == 0:
        print(n)
        break
