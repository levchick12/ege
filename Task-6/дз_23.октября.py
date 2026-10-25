# from turtle import *
# screensize(10_000, 10_000)
# tracer(0)
# left(90)
# k = 10
# for i in range(2):
#     fd(10*k)
#     left(270)
#     fd(12*k)
#     right(90)
# up()
# fd(9*k)
# right(90)
# fd(7*k)
# left(90)
# down()
# for i in range(2):
#     fd(13*k)
#     right(90)
#     fd(6*k)
#     right(90)
# for x in range(7, 13):
#     for y in range(9, 21):
#         teleport(x * k, y * k)
#         dot(3, 'red')
# print(6*12)
# update()
# done()

# from turtle import *
# screensize(10000,10000)
# tracer(0)
# k = 10
# left(90)
# for i in range(3):
#     fd(3*k)
#     right(90)
#     fd(4*k)
#     left(90)
# rt(180)
# fd(9*k)
# rt(90)
# fd(12*k)
# up()
# back(2*k)
# left(90)
# down()
# for i in range(3):
#     fd(2*k)
#     left(90)
#     fd(3*k)
#     right(90)
# left(180)
# fd(8*k)
# left(90)
# fd(9*k)
# left(90)
# fd(2*k)
# for x in range(-2,14):
#     for y in range(-6,10):
#         teleport(x*k, y*k)
#         dot(3,'red')
# update()
# done()

from turtle import *
screensize(10_000,10_000)
tracer(0)
left(90)
k = 10
for i in range(9):
    fd(17*k)
    lt(90)
    fd(8*k)
    lt(90)
    fd(17*k)
up()
lt(90)
fd(3*k)
rt(90)
fd(5*k)
lt(90)
down()
for i in range(4):
    fd(97*k)
    rt(90)
    fd(132*k)
    rt(90)

for x in range(-5,1):
    for y in range(-17,-4):
        teleport(x*k,y*k)
        dot(3,'red')
print(6*13)
update()
done()

