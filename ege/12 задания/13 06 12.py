for n in range(1,10000):
    l = '1' + '7'*n
    while '17' in l or '377' in l or '777' in l:
        if '17' in l:
            l = l.replace('17','1',1)
        if '377' in l:
            l = l.replace('377','73',1)
        if '777' in l:
            l = l.replace('777','3',1)

    if l.count('3') == 2:
        print(n,l)
        break