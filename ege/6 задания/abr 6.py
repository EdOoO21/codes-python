from turtle import *
k = 30
for i in range(2):
    rt(120)
    fd(7*k)
rt(300)
for i in range(2):
    rt(120)
    fd(7*k)




for x in range(-7,7):
    for y in range(-7,7):
        up()
        goto(x*k,y*k)
        dot(3)
exitonclick()