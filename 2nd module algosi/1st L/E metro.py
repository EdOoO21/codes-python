delay1 = int(input())
delay2 = int(input())
amount1 = int(input())
amount2 = int(input())

min_time1 = (delay1 * (amount1 - 1)) + amount1
min_time2 = (delay2 * (amount2 - 1)) + amount2

max_time1 = (delay1 * (amount1 + 1)) + amount1
max_time2 = (delay2 * (amount2 + 1)) + amount2

if min(max_time1, max_time2) >= max(min_time1, min_time2):
    print(max(min_time1, min_time2), min(max_time1, max_time2))
else:
    print(-1)
