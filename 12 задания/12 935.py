simple = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
for n in simple:
    l = '>' + 11 * '2' + '0' * 21 + n * '1'
    while '>1' in l or '>0' in l or '>2' in l:
        if '>1' in l:
            l = l.replace('>1', '22>', 1)
        if '>2' in l:
            l = l.replace('>2', '2>', 1)
        if '>0' in l:
            l = l.replace('>0', '1>', 1)
    h = 0
    for i in l[:-1]:
        h += int(i)
    if h % n == 0:
        print(n)
        break
