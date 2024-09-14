f = []
for x in range(100,5000):
    s = x * '1'
    while '333' in s or '111' in s:
        if '333' in s:
            s = s.replace('333','11',1)
        if '111' in s:
            s = s.replace('111','3',1)
    f.append(s)
m = max(f)
for i in range(4900):
    if f[i] == m:
        print(i+100,' = ', f[i])