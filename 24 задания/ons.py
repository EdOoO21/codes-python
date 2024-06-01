f = open('C:/Users/arbag/Desktop/файлы python/ons 24.txt')
f = f.readline()

a = ['A','O']
counter = 0
s = []
for i in range(0,len(f)-1,2):
    if f[i] not in a and f[i+1] in a:
        counter += 1
    else:
        s.append(counter)
        counter = 0

print(max(s))
counter = 0

for i in range(1,len(f)-1,2):
    if f[i] not in a and f[i+1] in a:
        counter += 1
    else:
        s.append(counter)
        counter = 0
print(max(s))
counter = 0
skip = 0
for i in range(0,len(f)-1,2):
    if f[i] not in a and f[i+1] in a:
        counter += 1
        skip = 1
    if f[i] in a and f[i-1] not in a:
        skip -= 1
    else:
        s.append(counter)
        counter = 0


print(max(s))