len_w, len_s = map(int, str(input()).split())
string_w, string_s = str(input()), str(input())
word = {}
keys = []
ans = 0
diff = {x: 0 for x in set(string_s)}
for x in string_w:
    try:
        word[x]
    except KeyError:
        word[x] = 1
        keys.append()
    else:
        word[x] += 1

k = [0,0]
for i in range(0, len_s):
    if i < len_w - 1:
        diff[string_s[i]] += 1

    elif i == len_w - 1:
        diff[string_s[i]] += 1

        for j in list(word):
            if diff[j] != word[j]:
                k = [j, diff[j] - word[j]]
                break
        else:
            ans += 1

    else:
        diff[string_s[i - len_w]] -= 1
        if (string_s[i - len_w] == k[0]) and (k[1] - 1 == 0):
            k = []
        elif string_s[i - len_w] == k[0]:
            k[1] -= 1
        diff[string_s[i]] += 1
        if (string_s[i - len_w] == k[0]) and (k[1] + 1 == 0):
            k = []
        elif string_s[i - len_w] == k[0]:
            k[1] += 1

        if not k:
            for i in word.keys():
                if diff[i] != word[i]:
                    k = [i, diff[i] - word[i]]
                    break
            else:
                ans += 1

print(ans)

