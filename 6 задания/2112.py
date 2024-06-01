from turtle import *

k = 10
for x in range(13):
    fd(10*k)
    rt(90)
    fd(4*k)
    for i in range(3):
        rt(90)
        fd(3*k)

rt(180)
fd(130*k)
rt(90)
fd(13*k)
exitonclick()