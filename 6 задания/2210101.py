from turtle import *

up()
goto(-20, 0)
down()
goto(20, 0)
up()
goto(0, -20)
down()
goto(0, 20)
goto(0, 0)
for i in range(11):
    fd(360)
    right(72)

exitonclick()
