a = [11,13,17,19]
s = []
for i in range(11000,22001):
    c = (i % 11 == 0) + (i % 13 == 0) + (i % 17 == 0) + (i % 19 == 0)
    if c == 2:
        s.append(i)

print(len(s),min(s))
