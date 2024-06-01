f = open('C:/Users/arbag/Desktop/файлы python/3352.txt')

s = f.readline()

maxv = ''
l = s[0]
for i in range(len(s) - 1):
    if ord(s[i]) > ord(s[i + 1]):
        l += s[i + 1]
        if len(l) > len(maxv):
            maxv = l
    else:
        l = s[i + 1]

print(len(maxv), maxv, s)

print(s.index('xEA541') + 1)
