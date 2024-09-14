for n in range(1, 10000):
    l = 15 * '3' + 18 * '2' + '1' * n
    while '31' in l or '33' in l or '21' in l:
        l = l.replace('31', '123', 1)
        l = l.replace('33', '211', 1)
        l = l.replace('21', '1', 1)
    summer = 0

    for i in range(len(l)):
        summer += int(l[i])

    if summer > 24:
        print(n)
        break
