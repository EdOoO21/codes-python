f = open('24 (11).txt').readline()
f = f.replace('1', '*')
f = f.replace('3', '*')
f = f.replace('5', '*')
f = f.replace('7', '*')
f = f.replace('9', '*')
f = f.replace('0', '+')
f = f.replace('2', '+')
f = f.replace('4', '+')
f = f.replace('6', '+')
f = f.replace('8', '+')

f1 = f
f = f.replace('+*','=')
f = f.replace('*+','=')
f1 = f1.replace('*+','=')
f1 = f1.replace('+*','=')
f = f.split('=')
f1 = f1.split('=')
print(len(f),len(f1))
maxv = 0
for x in f:
    maxv = max(len(x),maxv)
for x in f:
    if len(x) == maxv:
        print(x)
print(maxv + 2)
maxv = 0
for x in f1:
    maxv = max(len(x),maxv)
for x in f1:
    if len(x) == maxv:
        print(x)

print(maxv + 2)