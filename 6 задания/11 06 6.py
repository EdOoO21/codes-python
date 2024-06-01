from turtle import *
tracer(0)
k = 35
up()
x, y = 0, 0
goto(x + 1.5 * k, y + 0)
x, y = x + 1.5 * k, y + 0
down()
for i in range(12):
    goto(x + 1.5 * k, y + 15 * k)
    x, y = x + 1.5 * k, y + 15 * k
    goto(x + 8 * k,y + 0*k)
    x,y = x + 8 * k,y + 0*k
    goto(x + 1.5 * k, y + (-15) * k)
    x, y = x + 1.5 * k, y + (-15) * k
    goto(x + (-11) * k, y + 0 * k)
    x, y = x + (-11) * k, y + 0 * k

for a in range(-15,15):
    for b in range(-15,30):
        up()
        goto(a*k,b*k)
        dot(3)
print(44 + 90)
exitonclick()
