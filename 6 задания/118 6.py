from turtle import *
tracer(0)
k = 60
lt(90)
for i in range(12):
    for n in range(3):
        fd(6*k)
        lt(120)
    rt(120)

for x in range(-15,15):
    for y in range(-15,15):
        up()
        goto(x*k,y*k)
        dot(3)

exitonclick()