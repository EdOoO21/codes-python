s = [0] * 1040
s[1] = 2
for n in range(2, 1040):
    if n % 7 != 0:
        s[n] = s[n - 1] * ((3 ** (n % 5)) / (3 ** (n % 7)))
    else:
        s[n] = 1
print(s[1025]/s[1030])
