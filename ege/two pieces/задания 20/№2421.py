def f(x,y,p):
    if x + y >= 40 and p == 4:
        return True
    elif (x + y >= 40 and p != 4) or (x + y < 40 and p == 4):
        return False

    if p % 2 == 1:
        return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x , y*2, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x * 2, y, p + 1) and f(x, y * 2, p + 1)


for i in range(1,31):
    if f(9,i,1):
        print(i)