y = 2 * 9**10 - 3**5 + 5
count = 0
while y > 0:
    if y % 3 == 2:
        count += 1
    y //=3
print(count)