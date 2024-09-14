f = open('27-A.txt')
n = int(f.readline())

s = [0]
for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    s = [a+b for a in s for b in pair]

    s = {x % 10: x for x in sorted(s)}.values()

print(max(x for x in s if x % 10 != 5))

f = open('27-B.txt')
n = int(f.readline())
s = [0]
for i in range(n):

    pair = [int(x) for x in f.readline().split()]
    s = [a+b for a in s for b in pair]

    s = {x % 10: x for x in sorted(s)}.values()
print(s)
print(max(x for x in s if x % 10 != 5))