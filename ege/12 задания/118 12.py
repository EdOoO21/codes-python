for n in range(6, 10000):
    s = '1' + '5' * n + '2' + '5' * n
    while '15' in s or '255' in s or '555' in s:
        s = s.replace('15', '2', 1)
        s = s.replace('255', '1', 1)
        s = s.replace('555', '12', 1)

    h = sum(list(map(int, s)))
    if h < 1000:
        print(n)
