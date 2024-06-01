s = str(input())
m = 0
if s.count('f') == 1:
    print(-1)
elif s.count('f') == 0:
    print(-2)
else:
    for i in range(len(s)):
        if m == 1 and s[i] == 'f':
            print(i)
            break
        elif s[i] == 'f':
            m += 1