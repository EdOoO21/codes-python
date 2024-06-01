for n in range(10, 100):
    l = '3' + '7' * n
    while '37' in l or '577' in l or '777' in l:
        l = l.replace('37', '7', 1)
        l = l.replace('577', '73', 1)
        l = l.replace('777', '5', 1)
    s = 0
    for h in l:
        s += int(h)
    if len(str(s)) == 2 :
        f = 0
        for i in range(2, min(s, n) + 1):
            if n % i == 0 and s % i == 0:
                f = 1
                break

        if f == 0:
            print(n)
