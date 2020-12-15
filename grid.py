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
i=0
while i<N**2:
    yertle.penup()
    yertle.goto(Point[i])
    yertle.pendown()
    yertle.write(List[i])
    i=i+1
    yertle.penup()


def rond(numero):
  Points = [(-200,150),(0,150),(200,150),(-
  200,- 50),(0,-50),(200,-50),(-200,-250),(0,-
  250),(200,-250)]
  yertle.width(5)
  yertle.color('green')
  yertle.goto(Points[numero-1])
  yertle.pendown()
  yertle.circle(50)
  yertle.penup()
  yertle.goto(-350,0)
  yertle.color('black')
  yertle.width(1)


screen.exitonclick()
