import turtle
from turtle import *

# for i in range(30):  # for 문 사용하기
#     tim.pendown()  # 그릴 준비를 한다.
#     tim.forward(5)  # 움직이며 그린다.
#     tim.penup()  # 움직일 때 그리지 않는다.
#     tim.forward(5)  # 움직이며 그리지 않는다.

# current_step = 0
# steps = 30
#
# while current_step < steps:
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     current_step += 1

# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
# def tim_forward(tim_color, num, angle):
#     tim.color(tim_color)
#     for i in range(num):
#         tim.forward(100)
#         tim.left(angle)
#     # tim.forward(100)
#
# # 삼각형
# tim_forward('red', 3, 120)
#
# # 사각형
# tim_forward('orange', 4, 90)
#
# #오각형
# tim_forward('yellow', 5, 72)
#
# #육각형
# tim_forward('green', 6, 60)
#
# #팔각형
# tim_forward('blue', 8, 45)
#
# #구각형
# tim_forward('navy', 9, 40)
#
# #십각형
# tim_forward('purple', 10, 36)

import random

tim = Turtle()
tim.shape("turtle")
tim.color('red')

screen = Screen()

# colors = ['red', 'orange', 'yellow', 'blue', 'navy', 'purple', 'green', 'turquoise', 'gold']
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
"wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]

tim.width(5)
for i in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(direction)) #setheading(각도)는 터틀을 각도만큼 회전시키게 함


# tim.width(4)  # 두께 수정
# num = 0  # 변수 0으로 설정
#
# while num < 30:  # 30이 될 때까지 while문 반복
#     tim_color = random.randint(0, len(colors))  # 색 랜덤 지정
#     tim.color(colors[tim_color - 1])  # 색 바꿔주기
#     coin = random.randint(0, 1)  # 랜덤 이동지정
#     if coin == 0:  # 0일때
#         tim.right(90)  # 오른쪽으로 90도 돌고
#     elif coin == 1:  # 1일때
#         tim.left(90)  # 왼쪽으로 90도 돌고
#
#     tim.forward(50)  # 앞으로 50 전진
#     num += 1  # num에 1 더해주기



screen.exitonclick()
