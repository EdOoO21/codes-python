for i in range(151,161):
    s = i * '1'
    while '111' in s:
        s = s.replace('111','22',1)
        s = s.replace('222','11',1)
    print(i,' === ', s.count('1'),' ==== ',s)