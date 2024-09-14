from turtle import *

k = 10
for i in range(4):
    fd(7*k)
    rt(90)
    fd(7 * k)
    lt(90)
    fd(7 * k)
    rt(90)




for x in range(-7*k,15*k):
    for y in range(-22*k):
        goto(x,y)
        dot(4)

exitonclick()