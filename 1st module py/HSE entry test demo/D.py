# counter,l1,l2 = 0,str(input()),str(input())
# a,b = [],[]
#
# for i in range(len(l1) - 1):
#     a += [(l1[i] + l1[i+1])]
# for i in range(len(l2) - 1):
#     b += [(l2[i] + l2[i+1])]
# set(a)
# set(b)
#
# for i in a:
#     if i in b:
#         counter += 1
# print(counter,a,b)


# counter,l1,l2 = 0,str(input()),str(input())
# a,b = [],[]
# a += [(l1[i] + l1[i+1]) for i in range(len(l1) - 1)]
# b += [(l2[i] + l2[i+1]) for i in range(len(l2) - 1)]
# set(a)
# set(b)
#
# counter = [1 for i in a if i in b ]
# print(len(counter))


counter,l1,l2 = 0,str(input()),str(input())
d = {}
for i in range(len(l2) - 1):
    d[l2[i] + l2[i+1]] = 0

for i in range(len(l1) - 1):
    if (l1[i] + l1[i+1]) in d.keys():
        d[l1[i] + l1[i+1]] += 1

print(sum(d.values()))