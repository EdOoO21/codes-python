from turtle import *
tracer(0)
k = 40
for i in range(4):
    fd(3*k)
    lt(270)
    fd(5*k)
    rt(90)

lt(270)

for i in range(3):
    fd(5*k)
    rt(90)
    fd(3*k)
    lt(270)

for x in range(-15,15):
    for y in range(-15,15):
        up()
        goto(x*k,y*k)
        dot(3)
exitonclick()