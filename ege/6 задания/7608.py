from turtle import *
tracer(0)
lt(90)
k = 25
rt(45)
for i in range(7):
    fd(6*k)
    rt(45)
    fd(12*k)
    rt(135)

for x in range(-20,20):
    for y in range(-20,20):
        up()
        goto(x*k,y*k)
        dot(3)

exitonclick()