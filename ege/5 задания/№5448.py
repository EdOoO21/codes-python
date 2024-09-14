for i in range(1, 400):
    n = format(i, 'b')
    for k in range(2):
        if n.count('1') % 2 == 0:
            n = n.replace('1', '', 1)
            while n[0] == '0':
                n = n.replace('0', '', 1)
        else:
            n = '1' + n + '00'
    res = 0
    s = list(n)
    s.reverse()
    for l in range(len(s)):
        res += (int(s[l]))*2**l
    if res > 100:
        print(i,res)
        break



