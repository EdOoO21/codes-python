s = '>' + 11 * '1' + 2 * '2' + '3' * 11
while '>1' in s or '>2' in s or '>3' in s:
    s = s.replace('>1', '222>', 1)

    s = s.replace('>2', '3>', 1)

    s = s.replace('>3', '1>', 1)

print(s)
print(s[:-1])
k = 0
x = int(s[:-1])
print(x)
while x > 0:
    k += (x % 10)

    x = x // 10
print(k)
