from functools import reduce

with open('input.txt') as f:
    string = f.readlines()
    string = reduce(lambda x, y: x + y, string)
    string = string.replace('\n', '')
    dict = {}
    for x in string:
        try:
            dict[x]
        except KeyError:
            if x != ' ':
                dict[x] = 1
        else:
            if x != ' ':
                dict[x] += 1
    dict = sorted(dict.items(), key=lambda x: ord(x[0]))
    maxv = max(dict, key=lambda x: x[1])[1]
    now_string = ' ' * len(dict)
    while maxv > 0:
        for i in range(len(dict)):
            if dict[i][1] >= maxv:
                now_string = now_string[:i] + '#' + now_string[i + 1:]
        print(now_string)
        maxv -= 1
    for i in dict:
        print(i[0], end='')
