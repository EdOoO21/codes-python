from turtle import *

k = 10
down()
for i in range(4):
    fd(10*k)
    rt(90)

up()

fd(3*k)
lt(90)
fd(5*k)
rt(90)

down()

for i in range(2):
    fd(10*k)
    rt(90)
    fd(12*k)
    rt(90)

exitonclick()