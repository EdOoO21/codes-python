f = open('7855.txt')
for s in f:
    print(type(s))
a = [list(map(int, s.split())) for s in f]
k = [0] * 30

print(a)



