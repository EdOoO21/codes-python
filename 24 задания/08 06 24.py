f = open('24 (14).txt')
s = f.readline()
for i in range(10):
    if i % 2 == 0:
        s = s.replace(str(i), '* ')
    else:
        s = s.replace(str(i), '+ ')

s = s.split()

maxlen = 0
st = ''
for i in range(len(s) - 1):
    if s[i][-1] != s[i + 1][-1]:
        if maxlen < len(s[i][-1] + s[i + 1]):
            st = s[i][-1] + s[i + 1]
            maxlen = len(s[i][-1] + s[i + 1])
print(st, maxlen)

# for i in range(10):
#     if i % 2 == 0:
#         input.txt = input.txt.replace(str(i), '*')
#     else:
#         input.txt = input.txt.replace(str(i), '+')
# f = 0
# st = ''
# count = 0
# ans = []
# for i in range(len(input.txt)):
#     if f == 0:
#         if input.txt[i] == '*' or input.txt[i] == '+':
#             f = 1
#     elif f == 1 and (input.txt[i] == '+' or input.txt[i] == '*'):
#         ans.append([st, count])
#         st = ''
#         count = 0
#         f = 0
#     else:
#         st += input.txt[i]
#         count += 1
# ans = sorted(ans, reverse=True, key=lambda i: i[1])
#
# print(ans[0], ans[1], ans[2],ans[3])
