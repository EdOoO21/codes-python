f = open('C:/Users/arbag/Desktop/файлы для пробника/24/24var03.txt')
s1 = f.readline()
s = s1.split('AB')
k = 99999999999999999999999999

for i in range(len(s) - 19):
    a = 0
    for x in range(20):
        a += len(s[i + x])
    k = min(a,k)

print(k + (21*2))
m = 239
while m > 0:
    print(m% 3)
    m//=3
