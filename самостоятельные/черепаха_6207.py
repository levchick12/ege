from turtle import *
screensize(10_000,10_000)
tracer(0)
left(90)
k = 10

for i in range(2):
    fd(25*k)
    rt(90)
    fd(10*k)
    rt(90)
fd(3*k)
lt(90)
fd(15*k)
rt(90)
for i in range(2):
    fd(9*k)
    rt(90)
    fd(32*k)
    rt(90)
for x in range(0,11):
    for y in range(0,26):
        teleport(x*k,y*k)
        dot(3,'red')
update()
done()
print((18+15)*(10))
print(26*11)