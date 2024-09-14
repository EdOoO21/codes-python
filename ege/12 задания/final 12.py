for n in range(1, 101):
    l = '3' + n * '2'
    while '222' in l or '31' in l:
        if '222' in l:
            l = l.replace('222', '11', 1)
        if '31' in l:
            l = l.replace('31', '523', 1)
    h = 0
    for i in l:
        h += int(i)
    if h % 15 == 0 and len(l) % 2 == 0:
        print(n)
