l = 2022 * '7'
while '777' in l or '333' in l:
    l = l.replace('777','3',1)
    l = l.replace('333', '7', 1)
print(l)