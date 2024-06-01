
from turtle import *
tracer(0)
k = 45

for i in range(3):
    fd(4*k)
    lt(270)
    fd(7*k)
    rt(90)

lt(315)

for i in range(4):
    fd(7*k)
    rt(90)
    fd(4*k)
    lt(270)

for x in range(-15,15):
    for y in range(-15,15):
        up()
        goto(x*k,y*k)
        dot(4)
exitonclick()