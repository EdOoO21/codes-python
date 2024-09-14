l = '0' + '122122122122122122111111' + '0'
while '00' not in l:
    l = l.replace('011', '20', 1)
    l = l.replace('01', '220', 1)
    l = l.replace('02', '110', 1)
    l = l.replace('022', '10', 1)
if l.count('1') == 40 and l.count('2') > 50:
    print(12)
print(l, l.count('1'), l.count('2'))
