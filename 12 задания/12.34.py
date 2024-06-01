for i in range(201,220):
    s = i * '1'
    while '111' in s:
        s = s.replace('111','22',1)
        s = s.replace('222','1',1)
    if s.count('2') == 0:
        print(i,s)
        break