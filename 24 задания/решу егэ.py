f = open('C:/Users/arbag/Desktop/файлы python/24 решу егэ.txt')
f = f.readline()
f = f.replace('A','*')
f = f.replace('O','*')
length = len(f)-1
i = 0
counter = 0
maxl = 0
while i < length:
    if f[i] != '*' and f[i+1] == '*':
        i += 2
        counter += 1
    else:
        i += 1
        maxl = max(counter,maxl)
        counter = 0

print(maxl)

