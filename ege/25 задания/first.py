''' 190201; 190280 '''

for i in range(190201, 190280):
    s = []
    for n in range(1, i+1):
        if i % n == 0:
            s.append(n)
    if len(s) == 4:
        s.sort(reverse=True)
        print(*s)

