n, m = map(int, str(input()).split())
dict = {}
for i in range(n):
    string = str(input())
    for x in string:
        try:
            dict[x]
        except KeyError:
            dict[x] = 1
        else:
            dict[x] += 1

for i in range(m):
    string = str(input())
    for x in string:
        dict[x] -= 1
        if dict[x] == 0:
            del dict[x]

for i in dict:
    print(i * dict[i], end='')

