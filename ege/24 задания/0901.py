l = open('C:/Users/arbag/Desktop/файлы python/0901 24.txt')
l = l.readline()
l = l.replace('DAD', '*')
counter = 0
s = []
for i in range(len(l)):
    if l[i] == '*':
        counter += 1
    else:
        s.append(counter)
        counter = 0

print(max(s))
print(32*'DAD')