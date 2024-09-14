l = '1110'*5 + '<'
while '0<' in l or '1<' in l:
    if '11<' in l or '10<' in l:
        if '11<' in l:
            l = l.replace('11<', '<3', 1)
        else:
            l = l.replace('10<', '<2', 1)
    else:
        if '00<' in l:
            l = l.replace('00<', '<0', 1)
        if '01<' in l:
            l = l.replace('01<', '<1', 1)

print(l.count('1') + l.count('2') * 2 + l.count('3') * 3)
