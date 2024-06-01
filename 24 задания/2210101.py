f1 = open('C:/Users/arbag/Desktop/файлы python/2210101.txt')
f = f1.readline()
a = ['A', 'O']
c = 0
arr = []
comp = 0
for i in range(len(f) - 2):
    if (f[i] not in a) and (f[i + 1] not in a) and (f[i + 2] in a) and comp == 0:
        c += 1
        comp = 2

    elif comp != 0 and (not ((f[i] not in a) and (f[i + 1] not in a) and (f[i + 2] in a))):
        comp -= 1
    else:
        arr.append(c)
        c = 0

print(max(arr))

b = f
b = b.replace('A','1')
b = b.replace('O','1')
b = b.replace('F','x')
b = b.replace('C','x')
b = b.replace('D','x')
b = b.replace('xx1','*')

km = 0
k = 0
for i in b:
    if i == '*':
        k+=1
        km = max(k,km)
    else:
        k = 0
print(km)

