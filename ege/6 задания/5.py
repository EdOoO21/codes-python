from turtle import *
x,y = 0,0
for i in range(2):
    x += 60
    y += 20
    goto(x, y)
    y -= 20
    goto(x, y)

for i in range(3):
    x += 20
    y -= 10
    goto(x, y)
    x -= 20
    y -= 10
    goto(x, y)

for i in range(6):
    x -= 20
    y += 10
    goto(x,y)

exitonclick()

