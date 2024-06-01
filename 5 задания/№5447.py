result = 0
for i in range(1,1001):
    n = format(i,'b')
    for k in range(2):
        if n.count('1') % 2 == 0:
            n = n.replace('1','',1)
            while n[0] == '0':
                n = n.replace('0', '', 1)
        else:
            n = n.replace('0', '')
            n += '1'
    res = 0
    s = list(n)
    s.reverse()
    for l in range(len(s)):
        res += (int(s[l])) * (2**l)

    if res == 7:
        print(i)
        result += 1
print(result,' !!!')
