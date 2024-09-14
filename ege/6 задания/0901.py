from turtle import *

k = 10

for i in range(7):
    fd(20*k)
    rt(90)
    fd(30*k)
    rt(90)

up()
rt(720)
fd(5*k)
rt(90)
fd(10*k)
rt(90)

down()

for i in range(3):
    fd(25*k)
    rt(90)
    fd(15*k)
    rt(90)

exitonclick()