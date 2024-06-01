from itertools import *

k = 1
d = 0
for x in product('0123456789', repeat=7):
    s = ''.join(x)
    if ((s[1] + s[2] == str(int(s[0]) ** 2)) or (s[0] == '1' and s[1] + s[2] == '01') or (
            s[0] == '2' and s[1] + s[2] == '04') or (s[0] == '3' and s[1] + s[2] == '09')) \
            and (s[0] != '0'):

        if 5 <= int(s[6]) <= 9:
            if int(s[3] + s[4] + s[5]) == int(s[6]) ** 3:
                d += 1

        if 3 <= int(s[6]) <= 4:
            if int(s[4] + s[5]) == int(s[6]) ** 3:
                d += 1

        if 0 <= int(s[6]) <= 2:
            if int(s[5]) == int(s[6]) ** 3:
                d += 1
print(d)
