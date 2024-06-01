l = open('24-colors.txt').readline()
l1 = l
l = l.split('g')
maxlen = 0
str = 0

for i in l:
    if len(set(i)) == 1 and len(i) > maxlen:
        maxlen = len(i)
        str = i

print(maxlen + 2,str)
maxlen = 0
str = 0
i = 0
fl = 0
counter = 0
ans = ['',0]
l = l1
for i in range(len(l1)-1):
    if fl == 1 and l[i] == l[i + 1]:
        counter += 1
        str = l[i]
    if fl == 1 and l[i] != l[i + 1]:
        if counter > ans[1]:
            ans[0] = str * counter
            ans[1] = counter
        counter = 1
        str = ''
    if fl == 0 and l[i] == l[i + 1]:
        fl = 1
    else:
        continue

print(ans)

print(l.index('g' * 898))