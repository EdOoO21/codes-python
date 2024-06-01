f = open('C:/Users/arbag/Desktop/файлы python/24 пробник.txt')
f = f.readline()
f = 'EFEFDEFEFEFEFEFEFD'
dl = 0
s = []
skip = 0
for i in range(len(f) - 1, 2):
    if f[i] == 'E' and f[i + 1] == 'F':
        dl += 1
        skip = 1
    elif skip == 1:
        skip -= 1
        dl += 1
    else:
        s.append(dl)
        dl = 0

print(max(s))

'''
    if f[i] == 'E':
        dl+=1
        print('9 ==',dl)
        if f[i+1] == 'F':
            dl+=1
            print('12 =',dl)
            km = max(dl,km)
        else:
            km = max(dl,km)

    else:
        km = max(dl,km)
        dl = 0

f = input.txt
f = f.readline()
input.txt = input.txt.readline()
f = f.replace('FE', '*')
f = f.replace('F', 'D')
f = f.replace('E', 'D')
f = f.split('D')

print(f[0:100])
dl = 0
for i in range(len(f) - 1):
    dl = max(dl, len(f[i]))

print(f.index('*****'))
print(input.txt[748986], input.txt[748987], input.txt[748988])
'''
