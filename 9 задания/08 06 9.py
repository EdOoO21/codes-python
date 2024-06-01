f = open('09.txt')
counter = 0
for i in f:
    s = list(map(int, i.split()))
    s.sort()
    if len(set(s)) == len(s) and ((max(s) + min(s)) * 2) <= ((sum(s) - max(s) - min(s)) * 3) and (s[0] + s[-1]) * 2 <= (s[1] + s[2] + s[3]) * 3:
        counter += 1

print(counter)
