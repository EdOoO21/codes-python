s1 = 5 * (216 ** 155) + 4 * (36 * 156) - 4 * (6**157) - 2023
counter = 0
s = []
while s1 > 0:
    if s1 % 6 == 0:
        counter += 1
    s.append(s1 % 6)
    print(s1 % 6)
    s1 //= 6
print(counter,s.count(0))