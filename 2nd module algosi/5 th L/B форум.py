dict = {}
n = int(input())
index = 0
i = 1

while i <= n:
    string = str(input())
    if index == 2:
        dict[string] = [i]
        index -= 1
    elif index == 1:
        index -= 1
        i += 1

    else:
        if string == '0':
            index = 2

        else:
            try:
                int(string)
            except ValueError:
                i += 1
                continue
            else:
                string = int(string)

                for p in list(dict.keys()):
                    if string in dict[p]:
                        dict[p].append(i)
                        break

maxv = -1
name = ''
for i in dict:
    if len(dict[i]) > maxv:
        maxv = len(dict[i])
        name = i
print(name)
