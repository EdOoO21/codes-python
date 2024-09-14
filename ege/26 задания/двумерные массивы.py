f=open('C:/Users/arbag/Desktop/файлы python/лесопилка.txt')
n=int(f.readline())
a=[set() for _ in range(n)]
for _ in range(n):
    x, y = map(int, f.readline().split())
    a[x].add(y)

mx=0
my=0
for i in range(n):
    t=sorted(a[i])
    for n in range(len(t)-1):
        if t[n+1] - t[n] == 12:
            my = max(my,i)
            mx = t[n] + 1
            break
print(mx, my)
#===========================================================================
f = open('C:/Users/arbag/Desktop/файлы python/26 сетка.txt')

a = [set() for _ in range(10001)]

for i in range(114091):
    x, y = map(int, f.readline().split(' '))
    a[x].add(y)

mx = 0
my = 0
for i in range(len(a)):
    t = sorted(a[i])
    l = 1
    for n in range(len(t)-1):
        if t[n+1] - t[n] == 1:
            l += 1
        else:
            if mx < l:
                my = i
                mx = l

print(my,mx)

#========================================================================
f = open('C:/Users/arbag/Desktop/файлы python/26 сетка.txt')

a = [set() for _ in range(10001)]

for i in range(114091):
    x, y = map(int, f.readline().split(' '))
    a[x].add(y)
mx = 0
my = 0
for i in range(len(a)):
    t = sorted(a[i])
    l = 0
    for n in range(len(t)):
        if t[n] % 2 == 1:
            l += 1

    if l > mx:
        my = i
        mx = l

print(mx,my)
'''
a = [['',0]]*10001

f = open('C:/Users/arbag/Desktop/файлы python/26 сетка.txt')
stroka = []
stolbez = []
for i in range(114091):
    input.txt = f.readline()
    input.txt = input.txt.split(' ')
    stroka.append(int(input.txt[0]))
    stolbez.append(int(input.txt[1]))

print(stroka)


for i in range(114091):
    input.txt = f.readline()
    input.txt = input.txt.split(' ')
    m = int(input.txt[0])
    k = int(input.txt[1])
    if k % 2 == 1 and str(k) not in a[m][0]:
        a[m][1] += 1
        a[m][0] += str(k) + ' '


maxi = 0

for i in range(10001):
    maxi =  max(a[i][1],maxi)
print(maxi,a,len(a[1][0]),len(a[2][0]),len(a[55][0]))
'''
