for n in range(3,1000000):
    s = '3' + '5'*n
    while '25' in s or '355' in s or '555' in s:
        s = s.replace('25','32',1)
        s = s.replace('355', '25', 1)
        s = s.replace('555', '3', 1)

    ans = 0
    for i in s:
        ans += int(i)

    if ans == 17:
        print(n,s)
        break