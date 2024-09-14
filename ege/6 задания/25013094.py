from turtle import *
k = 20
lt(90)
for i in range(7):
    fd(10*k)
    rt(120)

up()
goto(0,0)
for i in range(11):
    for n in range(11):
        goto(i*k,n*k)
        dot(2)

exitonclick()