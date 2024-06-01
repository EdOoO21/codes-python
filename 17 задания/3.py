a = [int(x) for x in open('C:/Users/arbag/Desktop/файлы для пробника/17/17var03.txt')]

counter = 0
s = []
for i in range(len(a) - 2):
    if (a[i] % 10 == 0 and a[i+1] % 10 != 0 and a[i+2] % 10 != 0)\
        or (a[i] % 10 != 0 and a[i+1] % 10 != 0 and a[i+2] % 10 == 0)\
        or (a[i] % 10 != 0 and a[i+1] % 10 == 0 and a[i+2] % 10 != 0):
        if a[i] + a[i+1] + a[i+2] < max(a):
            counter += 1
            s.append(a[i] + a[i+1] + a[i+2])

print(counter,max(s))
