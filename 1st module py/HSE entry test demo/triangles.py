a,b,c = int(input()),int(input()),int(input())
if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    arr = [a,b,c]
    arr.sort()
    if arr[2] ** 2 > ((arr[1] ** 2) + (arr[0] ** 2)):print('obtuse')
    elif arr[2] ** 2 < ((arr[1] ** 2) + (arr[0] ** 2)):print('acute')
    else:print('right')
else:print('impossible')

