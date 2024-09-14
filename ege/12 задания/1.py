l = '22' + (2023 * '1') + '22'

while ('211' in l) or ('112' in l):
    l = l.replace('11','1',1)
    if '21' in l:
        l = l.replace('21','12',1)
    else:
        l = l.replace('12','1',1)
print(l)