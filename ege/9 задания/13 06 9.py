f = open('9 (2).txt')
a = [list(map(int,x.split())) for x in f]
counter = 0
# for i in a:
#     if i.count(i[0]) + i.count(i[1]) + i.count(i[2])\
#         + i.count(i[3]) + i.count(i[4]) == 7:
#         i.sort()
#         if (i[0] + i[-1])**2 < i[1]**2 + i[2]**2 + i[3]**2:
#             print(i)
#             counter += 1
# print(counter)

for i in a:
    s = list({s:i.count(s) for s in i}.values())
    print(s)
    input()