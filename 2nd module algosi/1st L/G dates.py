date_1, date_2, year = map(int, input().split())
if (date_1 > 12) or (date_2 > 12) or (date_1 == date_2):
    print(1)
else:
    print(0)