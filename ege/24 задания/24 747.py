f = open('24_8378 (2).txt').readline()
f = f.replace('TAA','*')
f = f.replace('TGA','*')
f = f.replace('TAG','*')
f = f.split('*')

for i in f:
    if len(i) > 11:
        if i[-3:] == 'ACA' and 'TTT' in i:
            print(i)

#========================================================
f = open('24_8378 (2).txt').readline()
f = f.split('ACATAA')

for i in range(len(f)):
    n = f[i]
    n = n.replace('TAA', '*')
    n = n.replace('TGA', '*')
    n = n.replace('TAG', '*')
    c = 0
    for j in range(0,len(n))[::-1]:
        if n[j] == '*':
            c = j
            break
    if c != 0:
        if 'ATGTTT' not in n[c:] and 'TGTTT' != n[c+1:c+6]:
            f[i] = ''

n = ''
for k in f:
    if k != '':
        n = k
        break

n = n.replace('TAA', '*')
n = n.replace('TGA', '*')
n = n.replace('TAG', '*')
c = 0
for j in range(0,len(n))[::-1]:
    if n[j] == '*':
        c = j
        break
print(n[c:])

#*TGTTTGTCAA
#ATGTTTGTCAAACATAA
