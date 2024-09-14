a = open('C:/Users/arbag/Desktop/файлы python/2210101 24.txt').readline()
s = a.split('F')
s.remove('\n')
print(s)

maxlength = 0
for i in s:
    if i.count('A') <= 2 and len(i) > maxlength:
        maxlength = len(i)

print(maxlength)
