f = open('C:/Users/arbag/Desktop/файлы python/readlines vs read vs readline.txt')

readlines1 = f.readlines()

readline1 = f.readline()

read1 = f.read()

print('readlines1 = ', readlines1)

print('readline1 = ', readline1)

print('read1 = ', read1)

readlines1[0] += '12'

print('readlines1 = ', readlines1)

while True:

    s = f.readline()
    if not s:
        break
    print(s)
