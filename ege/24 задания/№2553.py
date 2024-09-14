f  = open('C:/Users/arbag/Desktop/файлы python/2553.txt')

s = f.readlines()
k=0
for i in s:
    if i.count('J') > i.count('E'):
        k+=1
print(k)