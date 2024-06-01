a = str(input())
counter = 0
c = a.count("h")
for i in range(len(a)):
    if (a[i] == 'h'):
        counter += 1
    if (counter != 1) and (counter != c) and (a[i] == 'h'):
        a = a[:i] + 'H' + a[i + 1:]
print(a)