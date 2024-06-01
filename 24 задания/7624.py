s = open('24_7624.txt').readline()
s = s.replace('X', '*')
s = s.replace('Y', '*')
s = s.replace('Z', '*')
s = s.split('**')
m = 0
for i in s:
    m = max(len(i), m)
print(m + 2)
