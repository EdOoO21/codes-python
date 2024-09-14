for n in range(10, 100):
    l = '3' + n * '7'
    while '27' in l or '377' in l or '777' in l:
        if '27' in l:
            l = l.replace('27', '32', 1)
        if '377' in l:
            l = l.replace('377', '27', 1)
        if '777' in l:
            l = l.replace('777', '3', 1)
    h = 0
    for i in l:
        h += int(i)
    if h % 22 == 0:
        print(n)
