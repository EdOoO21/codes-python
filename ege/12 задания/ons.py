l = 96*'9'

while '22222' in l or '9999' in l:
    if '22222' in l:
        l = l.replace('22222','99',1)
    else:
        l = l.replace('9999','2',1)

print(l)