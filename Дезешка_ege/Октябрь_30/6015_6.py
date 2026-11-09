from turtle import *
screensize(10000,10000)
tracer(0)
left(90)
k = 10

for i in range(6):
    fd(8*k)
    rt(90)
    fd(18*k)
    rt(90)
up()
fd(4*k)
rt(90)
fd(10*k)
lt(90)
down()
for i in range(2):
    fd(17*k)
    rt(90)
    fd(7*k)
    rt(90)

for x in range(10,18):
    for y in range(4,9):
        teleport(x*k,y*k)
        dot(3,'red')
print((8+1)*(18+1)+(17+1)*(7+1)-(18-10)*(9-4))
update()
done()