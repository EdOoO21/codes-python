av = int(input())
if av >= 48:
    print(av // 48, end=' ')
    av -= (av // 48) * 48
else:
    print(0, end=' ')
if av >= 16:
    print(av // 16, end=' ')
    av -= (av // 16) * 16
else:
    print(0, end=' ')
if av >= 4:
    print(av // 4, end=' ')
    av -= (av // 4) * 4
else:
    print(0, end=' ')

print(av)