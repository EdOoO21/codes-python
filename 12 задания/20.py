for i in range(101,10000):
    l = '1'*i
    while '111' in l:
        l = l.replace('111','22',1)
        l = l.replace('222', '11', 1)
    if l.count('1') == 1:
        print(l,i)
        break
