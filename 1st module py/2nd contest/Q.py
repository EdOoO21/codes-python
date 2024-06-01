s, n, f = [], ' ', open('input.txt')
while n != '':
    n = f.readline()
    s += n.split()
d = {}
for i in s:
    if d.get(i) is None:
        print(0, end=' ')
        d[i] = 1
    else:
        print(d[i], end=' ')
        d[i] += 1

# # open('input.txt').readline()
# f = open('input.txt').readlines()
# f = f[:-1]
# print(f, len(f))
# d, n, f = {}, ' ', open('input.txt')
# while n != '':
#     n = f.readline()
#     s = n.split()
#     for i in s:
#         if i not in list(d.keys()):
#             print(0, end=' ')
#             d[i] = 1
#         else:
#             print(d[i], end=' ')
#             d[i] += 1
# f, n, s, k = open('input.txt'), ' ', [], 0
# while n != '':
#     n = f.readline()
#     s += f.readline().split()
#     for i in s[k]:
#         print(i.count(s))

