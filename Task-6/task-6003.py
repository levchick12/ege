from turtle import *

screensize(10_000, 10_000)
tracer(0)
k = 5

left(90)

for i  in range(2):
    fd(10*k)
    right(90)
    fd(20*k)
    right(90)

up()
fd(3*k)
right(90)
fd(7*k)
left(90)
down()

for i in range(2):
    fd(70*k)
    right(90)
    fd(90*k)
    right(90)

for x in range(7,21):
    for y in range(3,11):
        teleport(x * k, y * k)
        dot(4,'red')
print(14*8)

update()
done()