s1 = []
for i in range(1,1000):
    s = i*'8'
    while '555' in s or '888' in s:
        s = s.replace('555','88',1)
        s = s.replace('888','55',1)
    if s not in s1:
        s1.append(s)
print(len(s1),s1)