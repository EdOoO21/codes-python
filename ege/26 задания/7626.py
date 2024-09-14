f = open('26_7626.txt')
n = int(f.readline())
n1 = int(f.readline())


pas =[[0,0] for _ in range(n1)]

for i in pas:
    i[0],i[1] = map(int,f.readline().split())

pas.sort()

ach = [0] * n
counter = 0
for i in pas:

    for n in range(len(ach)):
        if ach[n] < i[0]:
            ach[n] = i[1]
            counter += 1

            print(n + 1)
            break

print(counter)