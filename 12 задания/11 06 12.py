for n in range(1, 100000):
    l = '13' * n
    while '13' in l or '31' in l or '11' in l:
        if '13' in l:
            l = l.replace('13', '4', 1)
        if '31' in l:
            l = l.replace('31', '1', 1)
        if '11' in l:
            l = l.replace('11', '2', 1)
        if '44' in l:
            l = l.replace('44', '1', 1)
    h = 0
    for k in l:
        h += int(k)
    if h == 99:
        print(n)
        break
