l = 54 * '5' + '7'
while '722' in l or '557' in l:
    if '722' in l:
        l = l.replace('722','57',1)
    else:
        l = l.replace('557','72',1)
print(l)