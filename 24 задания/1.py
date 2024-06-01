f1 = open('C:/Users/arbag/Desktop/файлы python/1.txt')
f = f1.readline()
f = f.split('A')
k = 0
print(f)
for i in range(len(f) - 2):
    s = len(f[i]) + len(f[i + 1]) + len(f[i + 2])
    k = max(s, k)
print(k + 3)
