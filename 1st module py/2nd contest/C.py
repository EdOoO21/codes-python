s = str(input())
if 'f' in s:
    if s.index('f') == (len(s)) - 1 - (s[::-1].index('f')):
        print(s.index('f'))

    else:
        print(s.index('f'), (len(s)) - 1 - (s[::-1].index('f')))
