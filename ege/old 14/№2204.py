k  = 0
l = []
s = (7 * (6561**46)) + (8 * (729**15)) - (6 * 5832)
while s > 0 :
    l.append(s%9)
    if s % 9 ==7:
        k += 1
        s //= 9
    else:
        s//=9
print(k)

k1 = 0
for i in l:
    if i == 7:
        k1 +=1
print(l)
print(k1)