a = [int(x) for x in open('C:/Users/arbag/Desktop/файлы python/25013094 17.txt')]

s = []
counter = 0
middle = sum(a) / len(a)

for i in range(1, len(a) - 2):
    if a[i] * a[i + 1] > a[i - 1] * a[i + 2]:
        s.append(a[i] + a[i + 1])
        if a[i] > middle or a[i] > middle:
            counter += 1

print(max(s), counter)
