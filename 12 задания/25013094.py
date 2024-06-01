for i in range(101,10000):
    l = '5' * i
    while ('555' in l) or ('888' in l):
        l = l.replace('555','8',1)
        l = l.replace('888','55',1)
    if '8' not in l:
        print(i)
        break
