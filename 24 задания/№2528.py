letters = []
f = open('C:/Users/arbag/Desktop/файлы python/2528.txt')
s = f.readline()

for i in range(26):
    b = str(input())
    letters.append(b)
maxv = 0
l = ''
for i in range(len(s) - 1):
    if s[i] not in letters:
        if int(s[i]) % 2 == 0:
            l += s[i]
            if int(l) > maxv:
                maxv = int(l)
    elif s[i] in letters or int(s[i]) % 2 == 1\
            or ((s.index(l)+1 not in letters) and (s.index(l)-1 not in letters)) :
        l = ''
print(maxv, s.index(str(maxv)))
print(s.index('4444'))
