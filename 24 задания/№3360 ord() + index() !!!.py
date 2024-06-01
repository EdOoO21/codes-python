f = open('C:/Users/arbag/Desktop/Текстовый документ.txt')
s= f.read()

maxx = ''

t = s[0]

for i in range(len(s)-1):
    if ord(s[i]) < ord(s[i+1]):
        t += s[i+1]
        if len(t) > len(maxx):
            maxx = t
    else:
        t = s[i+1]

print(maxx,s.index('DLXipu')+1)

