f = open('C:/Users/arbag/Desktop/файлы python/5 24.txt')
f = f.readline()

s = []
counter = 0

for i in range(0,len(f) - 1, 2):

    if (f[i] == f[i + 1]) and f[i] != 'B':
        counter += 1
    else:
        s.append(counter)
        counter = 0

print(max(s))
counter = 0

for i in range(1, len(f) - 1, 2):
    if (f[i] == f[i + 1]) and f[i] != 'B':
        counter += 1
    else:
        s.append(counter)
        counter = 0

print(max(s))
