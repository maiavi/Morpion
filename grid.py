from turtle import Screen, Turtle
from turtle import *


N = 4  # N by N grid
LENGTH = N * 20  # each grid element will be LENGTH x LENGTH pixels

def grid(turtle, n, length):
    sign = 1
    for _ in range(2):

        for _ in range(n):
            turtle.forward(length * n)
            turtle.left(sign * 90)
            turtle.forward(length)
            turtle.left(sign * 90)
            sign = 0 - sign

        turtle.forward(length * n)
        [turtle.right, turtle.left][n % 2](90)
        sign = 0 - sign

screen = Screen()
yertle = Turtle()

yertle.penup()
yertle.goto(-N * LENGTH/2, -N * LENGTH/2)  # center our grid (optional)
yertle.pendown()

grid(yertle, N, LENGTH)

List = []
for j in range ((N**2) + 1):
    List.append(j)


#Point = [
#    (-LENGTH,LENGTH),(0,LENGTH),(LENGTH,LENGTH),
#    (-LENGTH,0),(0,0),(LENGTH,0),
#    (-LENGTH,-LENGTH),(0,-LENGTH),(LENGTH,-LENGTH)
#]

Point = [
    (-LENGTH - N,LENGTH),(0,1),(0,2),
    (1,0),(1,1),(1,2),
    (1,0),(1,1),(1,2),
    (-LENGTH,-LENGTH),(0,-LENGTH),(LENGTH,-LENGTH)
]

i=0
print(LENGTH)
while i<N**2:
    up()
    goto(Point[i])
    down()
    write(List[i])
    i=i+1
    up()



screen.exitonclick()