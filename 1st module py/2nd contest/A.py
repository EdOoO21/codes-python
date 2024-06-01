s = str(input())
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
for i in range(0,len(s),2):
    print(s[i],end='')
print()
for i in range(1,len(s),2):
    print(s[i],end='')
print()
print(s[::-1])
m = s[::-1]
for i in range(0,len(m),2):
    print(m[i],end='')
print()
print(len(m))

