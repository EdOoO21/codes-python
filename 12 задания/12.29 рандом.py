s = 50 * '1' + 50*'2' + 50*'3'

while '21' in s or '31' in s or '23' in s:
    s = s.replace('21','12',1)
    s = s.replace('31','13',1)
    s = s.replace('23','32',1)


m = s[9] + s[89] + s[129]
print(m)