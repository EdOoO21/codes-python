f = open('9 (6).txt')
s = f.readlines()
counter = 0
for i in range(len(s)):
    a = 0
    b = 0
    s[i] = list(map(int, s[i].split()))
    if ((abs(s[i][0]) % 10 == 3) + (abs(s[i][1]) % 10 == 3) + (abs(s[i][2]) % 10 == 3) + (abs(s[i][3]) % 10 == 3) + (
            abs(s[i][4]) % 10 == 3)) == 3:
        for k in s[i]:
            if k > 0:
                a += k
            if k < 0:
                b += k
        if a ** 2 < b ** 2:
            counter += 1
            print(s[i])

print(counter)
