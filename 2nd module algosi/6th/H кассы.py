n = int(input())
time = [0]*1440
extra = 0
for i in range(n):
    curr_t = list(map(int, input().split()))
    start = (curr_t[0]*60) + curr_t[1]
    end = (curr_t[2]*60) + curr_t[3]
    if start == end:
        extra += 1
    elif start < end:
        for k in range(start,end):
            time[k] += 1
    else:
        for k in range(start,1440):
            time[k] += 1
        for k in range(0,end):
            time[k] += 1
ans = 0
for i in time:
    if i + extra == n:
        ans += 1
print(ans)