n = int(input())
dictt = {}
string = str(input())

for x in string:
    try:
        dictt[x]
    except KeyError:
        dictt[x] = 1
    else:
        dictt[x] += 1


dictt = dict(sorted(dictt.items(), key=lambda x: x[0]))

chet = []
net = []
ans_len = 0
for i in dictt:
    if dictt[i] % 2 == 0:
        chet.append(i)
        ans_len += dictt[i]
    else:
        net.append(i)
if len(chet) == 0:

    dictt = sorted(dictt.items(), key=lambda x: (-x[1], x[0]))
    print(dictt[0][0] * dictt[0][1])
else:
    dict1 = sorted(dictt.items(), key=lambda x: (-x[1], x[0]))
    el = dict1[0]
    for i in net:
        if (dictt[i] > 1) and el != i:
            dictt[i] -= 1
        elif el == i:
            net.remove(i)
    if net:
        ans_len += 1
    i = 0
    index = 0
    answer = ''
    while i < ans_len:
        if ans_len % 2 == 0:
            if (ans_len / 2) > i:
                answer += chet[index] * (dictt[chet[index]] // 2)
                i += dictt[chet[index]] // 2
                if index < len(chet) - 1:
                    index += 1
            else:
                print(answer + answer[::-1])
                break
        else:
            if (ans_len // 2) > i:
                answer += chet[index] * (dictt[chet[index]] // 2)
                i += dictt[chet[index]] // 2
                if index < len(chet) - 1:
                    index += 1
            else:
                print(answer + (net[0]*dictt[el]) + answer[::-1])
                break
