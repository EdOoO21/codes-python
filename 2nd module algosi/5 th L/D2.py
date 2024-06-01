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


if len(net) == 0:
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
elif len(net) == 1:
    i = 0
    index = 0
    answer = ''
    ans_len += 1
    while i < ans_len:
        if (ans_len // 2) > i:
            answer += chet[index] * (dictt[chet[index]] // 2)
            i += dictt[chet[index]] // 2
            if index < len(chet) - 1:
                index += 1
        else:
            print(answer + (net[0] * dictt[net[0]]) + answer[::-1])
            break
else:
    if len(chet) != 0:
        d = {}
        for i in dictt:
            if dictt[i] % 2 == 1:
                d[i] = dictt[i]
        d = sorted(d.items(), key=lambda x: (-x[1],x[0]))
        el = d[-1][0]
        elc = dictt[el]
        d.pop(-1)
        for i in d:
            if dictt[i[0]] > 1:
                chet.append(i[0])
                dictt[i[0]] -= 1
        chet = sorted(chet)
        i = 0
        index = 0
        answer = ''
        ans_len += 1
        while i < ans_len:
            if (ans_len // 2) > i:
                answer += chet[index] * (dictt[chet[index]] // 2)
                i += dictt[chet[index]] // 2
                if index < len(chet) - 1:
                    index += 1
            else:
                print(answer + (el * elc) + answer[::-1])
                break
    else:
        d = {}
        for i in dictt:
            if dictt[i] % 2 == 1:
                d[i] = dictt[i]
        d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
        el = d[-1][0]
        elc = dictt[el]
        d.pop(-1)
        for i in d:
            if dictt[i[0]] > 1:
                chet.append(i[0])
                dictt[i[0]] -= 1
        chet = sorted(chet)
        print(chet,el,dictt[chet[0]])
        i = 0
        index = 0
        answer = ''
        ans_len = len(string) - (len(list(dictt.keys())) - 1)
        while i < ans_len:
            if (ans_len // 2) >= i:
                answer += chet[index] * (dictt[chet[index]] // 2)
                i += dictt[chet[index]] // 2
                if index < len(chet) - 1:
                    index += 1
            else:
                print(answer + (el * elc) + answer[::-1])
                break


