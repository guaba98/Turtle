import turtle
from turtle import *


import random

tim = Turtle()
turtle.colormode(255) #컬러모드에 255까지 들어갈 수 있게 담아준다.
# tim.shape("turtle")
# tim.color('red')

screen = Screen()

def random_color():
    """r, g, b 색 반환 함수"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


direction = [0, 90, 180, 270]
tim.speed(2)

tim.pensize(15)
for i in range(200):
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction)) #setheading(각도)는 터틀을 각도만큼 회전시키게 함





screen.exitonclick()
