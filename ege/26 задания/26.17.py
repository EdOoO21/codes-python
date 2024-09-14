f = open('C:/Users/arbag/Desktop/файлы python/26 17.txt')
a = [int(x) for x in f]
a = sorted(a,reverse = True)
ans = [a[0]]
for i in range(len(a)):
    if ans[-1] - a[i] >= 3:
        ans.append(a[i])
print(len(ans),ans[-1])
