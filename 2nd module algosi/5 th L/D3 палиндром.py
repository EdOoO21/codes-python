n = int(input())
dict = {}
string = str(input())

for x in string:
    try:
        dict[x]
    except KeyError:
        dict[x] = 1
    else:
        dict[x] += 1

dict = sorted(dict.items(), key=lambda x: x[0])
ans = ''
for i in dict:
    ans += i[0] * (i[1] // 2)
el = ''
for i in dict:
    if i[1] % 2 == 1:
        el = i[0]
        break
print(ans + el + ans[::-1])



# i = 0
# element = 0
#
# while i < len(dict):
#     if (dict[i][1] == 1) and (element == 0):
#         element = dict[i]
#     elif (dict[i][1] == 1) and (element != 0):
#         dict[i] = 0
#         dict.pop(i)
#     else:
#         i += 1
#
# answer = ''
# if not element:
#     for i in range(len(dict)):
#         if (dict[i][1] % 2 == 1) and (i != len(dict) - 1):
#             dict[i] = list(dict[i])
#             dict[i][1] -= 1
#     element = dict[-1]
#     dict.pop(-1)
#     for i in dict:
#         answer += i[0] * (i[1] // 2)
#     print(answer + (element[0] * element[1]) + answer[::-1])
#
# else:
#     for i in range(len(dict)):
#         if dict[i][1] % 2 == 1:
#             dict[i] = list(dict[i])
#             dict[i][1] -= 1
#
#     for i in dict:
#         answer += i[0] * (i[1] // 2)
#     print(answer + (element[0] * element[1]) + answer[::-1])
