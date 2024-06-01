k, line = int(input()), str(input())
amount = 0
ans = 0
for i in range(len(line) - k):
    if line[i] != line[i + k]:
        amount = 0
    else:
        amount += 1
    ans += amount

print(ans)
