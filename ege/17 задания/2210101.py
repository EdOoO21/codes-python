a = [int(x) for x in open('C:/Users/arbag/Desktop/файлы python/17.txt')]


minValue = 111111111111
for i in a:
    if i < minValue and abs(i) % 10 == 7:
        minValue = i


counter = 0

for n in range(5000 - 1):
    if ((abs(a[n]) % 10) == 7 and (abs(a[n + 1]) % 10) != 7) \
            or ((abs(a[n]) % 10) != 7 and (abs(a[n + 1]) % 10) == 7):

        if (a[n] ** 2 + a[n + 1] ** 2) < minValue ** 2:
            counter += 1

print(counter)
