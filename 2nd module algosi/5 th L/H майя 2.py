len_w, len_s = map(int, str(input()).split())
string_w, string_s = str(input()), str(input())
window = {}
word = {}
ans = 0
diff = {}
string=''
for x in string_w:
    try:
        word[x]
    except KeyError:
        word[x] = 1
        string += x
    else:
        word[x] += 1

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
for i in range(0, len_s):
    if i < len_w - 1:
        try:
            window[string_s[i]]
        except KeyError:
            window[string_s[i]] = 1
        else:
            window[string_s[i]] += 1


    elif i == len_w - 1:
        try:
            window[string_s[i]]
        except KeyError:
            window[string_s[i]] = 1
        else:
            window[string_s[i]] += 1

        for j in word.keys():
            try:
                window[j]
            except KeyError:
                diff[j] = -word[j]
            else:
                if window[j] - word[j] != 0:
                    diff[j] = window[j] - word[j]
        if not diff:
            ans += 1

    else:
        window[string_s[i - len_w]] -= 1

        if window[string_s[i - len_w]] == 0:
            del window[string_s[i - len_w]]


        try:
            diff[string_s[i - len_w]]
        except KeyError:
            if string.find(string_s[i - len_w]) == -1:
                pass
            else:
                diff[string_s[i - len_w]] = -1
        else:
            diff[string_s[i - len_w]] -= 1
            if diff[string_s[i - len_w]] == 0:
                del diff[string_s[i - len_w]]

        try:
            window[string_s[i]]
        except KeyError:
            window[string_s[i]] = 1

        else:
            window[string_s[i]] += 1

        try:
            diff[string_s[i]]
        except KeyError:
            if string.find(string_s[i]) == -1:
                pass
            else:
                diff[string_s[i]] = 1
        else:
            diff[string_s[i]] += 1
            if diff[string_s[i]] == 0:
                del diff[string_s[i]]

        if not diff:
            ans += 1


print(ans)
ч