n = int(input())

line = list(map(int, input().split()))
maxv = line[0]
curr_sum = 0
for i in range(len(line)):
    curr_sum += line[i]
    maxv = max(maxv, curr_sum)
    curr_sum = max(0, curr_sum)

print(maxv)
