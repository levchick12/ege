# r = f'{1097:b}'
# r1 = int("100010010", 2)
# print(r, r1)

# from turtle import *
# screensize(10000,10000)
# tracer(0)
# left(90)
# k = 10
#
# for i in range(6):
#     fd(33*k)
#     rt(90)
#     fd(20*k)
#     rt(90)
# up()
# fd(3*k)
# rt(90)
# fd(9*k)
# lt(90)
# down()
# for i in range(6):
#     fd(24*k)
#     rt(90)
#     fd(25*k)
#     rt(90)
#
# for x in range(9,21):
#     for y in range(3,28):
#         teleport(x*k, y*k)
#         dot(3,'red')
# print((10)*(23))
# update()
# done()


ans = []
for n in range(1,10000):
    r = f'{n:b}'
    if n % 2 == 0:
        r = '10' + r[2:] + '0'
    else:
        r = '11' + r[2:] + '1'
    r = int(r,2)
    if r >= 16:
        ans.append(n)
print(min(ans))