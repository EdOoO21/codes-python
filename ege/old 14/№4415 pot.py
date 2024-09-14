y = 16**44 * 16**30 - (32**5 * (8**40 - 8 **32 ) * (16**17 - 32**4))
s = []
s1 = []
count = 0
count1 = 0
count2 = 0
while y > 0:
    if y % 16 == 15:
        s.append(0)
    else:
        s.append(y % 16)
    y //= 16
    count += 1
print(s)
print(count)
for i in range(count):
    if s[i] == 0:
        count1 +=1
print(count1)
for i in range(count):
    if s[i] != 0:
        s1.append(i)
print(s1)
print(count1 - (count - ((max(s1))+1) + 3) )





'''while y > 0:
    if y % 16 == 15:
        input.txt.append(0)
        count +=1
    else:
        input.txt.append(y % 16)
    y //= 16
    count1 +=1
print(input.txt)
for i in range(count1):
    if input.txt[i] != 0:
        s1.append(i)
print(sorted(s1))
for i in range(s1[0]):
    input.txt.pop(i)
print(input.txt)
for i in range(count1 - s1[0]):
    if input.txt[i] == 0:
        count2 +=1
print(count2)
'''


