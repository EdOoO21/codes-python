n = 114091
f = open('C:/Users/arbag/Desktop/файлы python/08 26.txt')
a = [[0] * 10001 for j in range(10001)]
for i in range(n):
    x, y = map(int, f.readline().split(' '))
    a[x][y] += 1

maxv = 0
for x in range(1, 10001):
    counter = 0
    y = 0
    while y < 10000:
        if a[x][y] >= 1 and a[x][y + 1] >= 1:
            y += 2
            counter += 2
        else:
            maxv = max(counter, maxv)
            counter = 0
            y += 1
    if maxv == 10:
        print(x)


print(maxv)

'''
    for y in range(2,10001,2):
        if a[x][y] >= 1:
            counter +=1

    maxv = max(maxv,counter)
    
    
    для этого задания по факту
'''
