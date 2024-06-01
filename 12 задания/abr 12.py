l = '7' * 116
while '333' in l or '7777' in l:
    if '333' in l:
        l = l.replace('333','77',1)
    else:
        l = l.replace('7777','3',1)
print(l)