from turtle import *
k = 30
for i in range(7):
    fd(10*k)
    rt(120)

for x in range(-4,12):
    for y in range(-12,5):
        up()
        goto(x*k,y*k)
        down()
        dot(3)
print('dssssssssdsdsd')
exitonclick()