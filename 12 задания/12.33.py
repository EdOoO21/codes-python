for i in range(31,1000):
    s = i * '1'
    while '111' in s:
        s = s.replace('111','2',1)
        s = s.replace('222','1',1)
    if s == '211':
        print(i,s)
        break