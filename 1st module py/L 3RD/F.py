a,b,c,d = float(input()),float(input()),float(input()),float(input())

def distance(x1, y1, x2, y2):
    return (((x2 - x1) ** 2) + ((y2 - y1)**2))**0.5

print(distance(a,b,c,d))