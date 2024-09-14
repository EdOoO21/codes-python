y = 8**4024 - 4**1605 + 2**1024 - 126
count = 0
while y > 0:
    if y % 2 == 1:
        count +=1
    y //= 2
print(count)