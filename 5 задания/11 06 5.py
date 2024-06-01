m = 10**10
for n in range(1,10000000):
    i = bin(n)[2:]
    if n % 3 == 0:
        i1 = '10' + i[2:] + '1'
    else:
        i1 = bin(((n % 3) * 2))[2:] + i
    if 8000 < int(i1,2) <= 8193:
        m = min(int(i1,2),m)
        break

print(m)