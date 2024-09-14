f = open('24 (16).txt').readline()
for i in 'ABCD':
    f = f.replace(i,'*')

f = f.split('***')

st = ''
leng = 0
for i in f:
    if len(i) > len(st):
        leng = len(i)
        st = i

print(leng + 4,st)