from turtle import Screen, Turtle
from turtle import *


N = 3  # N by N grid
LENGTH = 200  # each grid element will be LENGTH x LENGTH pixels

def grid(turtle, n, length):
    sign = 1
    for _ in range(2):

        for _ in range(n):
            turtle.speed(8)
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

Point =[ (-
200,200),(0,200),(200,200),(-
200,0),(0,0),(200,0),(-200,-200),(0,-
200),(200,-200)]
while i<N**2:
    up()
    goto(Point[i])
    down()
    write(List[i])
    i=i+1
    up()



screen.exitonclick()
