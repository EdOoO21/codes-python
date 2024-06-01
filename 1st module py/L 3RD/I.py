x,y = float(input()),float(input())
def IsPointInSquare(x,y):
    if (-1 <= y <= 1) and (-1 <= x <= 1):
        return 'YES'
    return 'NO'

print(IsPointInSquare(x,y))