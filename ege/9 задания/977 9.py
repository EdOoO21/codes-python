f = open('9 (1).txt')
counter = 0
for i in range(5230):
    a = list(map(int, f.readline().split()))
    if len(set(a)) == len(a) and ((max(a) + min(a)) // 2) in a:
        counter += 1
    else:
        s1 = 0
        s2 = 0
        for x in a:
            if a.count(x) > 1:
                s1 += x ** 2
            else:
                s2 += x ** 2
        if s1 != 0 and s1 < s2:
            counter += 1
print(counter)
