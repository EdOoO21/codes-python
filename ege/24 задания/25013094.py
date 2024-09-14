f1 = open('C:/Users/arbag/Desktop/файлы python/25013094 24.txt')
f = f1.readline()

f = f.replace('ZZX', '*')
f = f.replace('XY', '*')

for i in range(1, 10000):
    if '*' * i in f:
        print(i)

print(f.index('*' * 9))

