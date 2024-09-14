from turtle import *
tracer(0)
k = 15
up()
lt(90)
fd(10*k)
rt(90)
down()
rt(30)
for i in range(10):
    fd(25*k)
    rt(90)
up()
for a in range(-50,30):
    for b in range(-50,30):

        goto(a*k,b*k)
        dot(2)
exitonclick()