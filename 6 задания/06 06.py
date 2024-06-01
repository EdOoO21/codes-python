from turtle import *
tracer(0)
k = 30
rt(315)
for i in range(7):
    fd(16*k)
    rt(45)
    fd(8*k)
    rt(135)
for x in range(0,21):
    for y in range(0,21):
        up()
        goto(x*k,y*k)
        dot(3)
exitonclick()