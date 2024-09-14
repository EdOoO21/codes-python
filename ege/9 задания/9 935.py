f = open('9 (4).txt')
counter = 0
for i in f:
    s = list(map(int,i.split()))
    s1 = sorted(s)
    if s1[0] != s[0] and s1[0] != s[3] and s1[3] != s[0] and s1[3] != s[3]:
        if (s1[2] - s1[1]) != 0 and ((s1[3] - s1[0]) % (s1[2] - s1[1]) == 0):
            counter += 1
            print(s,s1)

print(counter)