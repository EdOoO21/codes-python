f = open('C:/Users/arbag/Desktop/файлы python/abr 24.txt')
f = f.readline()
s = []
l = len(f) - 1
i = 0
counter = 0

while i < l:
    if f[i] == 'E' and f[i+1] == 'F':
        i += 2
        counter += 1
    else:
        i += 1
        s.append(counter)
        counter = 0
print(max(s))
i = 0
counter = 0
while i < l:
    if f[i] == 'F' and f[i+1] == 'E':
        i += 2
        counter += 1
    else:
        i += 1
        s.append(counter)
        counter = 0
print(max(s))
print(5*'EF',5*'FE')


