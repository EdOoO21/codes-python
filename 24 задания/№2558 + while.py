f = open('C:/Users/arbag/Desktop/файлы python/2558.txt')

s = f.readlines()
k = 0
for i in s:
    for n in range(len(i)-2):
        if i[n] == 'A' and i[n+2] == 'R':
            k+=1
            break
print(k)


'''n = 0
while True:
    input.txt = f.readline()
    if not input.txt:
        break
f.close()

print(n)
'''