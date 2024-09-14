a=[]
for i in range(300,1000):
    s = i*'5'
    while '555' in s or '888' in s:
        if '555' in s:
            s = s.replace('555','8',1)
        else:
            s = s.replace('888','55',1)
    if s == '58' or s == '85':
        a.append(i)
print(a)