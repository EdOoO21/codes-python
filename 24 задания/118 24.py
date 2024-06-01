f = open('24_8480 (1).txt').readline()
f = f.replace('A','*')
f = f.replace('B','*')
f = f.replace('C','*')
f = f.split('**')

maxv = 0
for i in f:
    maxv = max(maxv,len(i))

print(maxv + 2)
