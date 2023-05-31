import random

import colorgram
from turtle import *
import turtle as t

# 컬러그램으로 색 추출하기
# colors = colorgram.extract('image.jpg', 30) #색들을 30가지 추출하고
# color_palette = [] #이를 담을 빈 리스트 만들어 놓는다.
#
# for color in colors: #FOR문을 돌려서
#     r = color.rgb.r #RGB 각 값들을 뽑아
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b) #튜플로 담는다.
#     color_palette.append(new_color) #append한다.
#
# print(color_palette)
screen = t.Screen()  # 스크린 객체 만들어 놓는다. 창이 꺼질 때까지 닫히지 않는다.

# 컬러그램에서 담은 rgb 값들을 콘솔창에서 복사해 와서 가져온다.
colors = [(250, 247, 244), (248, 245, 246), (213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31),
          (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244),
          (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143),
          (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18),
          (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]

# 20 원 간격은 50


tim = t.Turtle()  # 팀이라는 터틀 객체를 만든다.
tim.penup()  # 팀의 그림자를 가지 않게 한다.
t.colormode(255)  # 컬러모드 255색을 넣어준다.
tim.setheading(225)  # 터틀 머리 방향을 255각도로 해서 좌하 방향으로 내려가도록 한다.
tim.forward(250)  # 250만큼 움직이게 한다.
tim.setheading(0)  # 다시 터틀 방향을 0도로 만든다.

number_of_dots = 100 # 100개의 점을 찍는다

for dot_count in range(1, number_of_dots + 1): # 100번 반복한다
    tim.dot(20, random.choice(colors)) #터틀 객체의 색을 반복할 때마다 바꿔 준다.
    tim.forward(50) #점을 찍고 50씩 나아간다.

    if dot_count % 10 == 0: # 만약 10을 찍은 상태라면
        tim.setheading(90) #90도 각도를 틀고
        tim.forward(50) # 50만큼 전진
        tim.setheading(180) # 다시 180도 돌고
        tim.forward(500) # 온 만큼 돌아가서
        tim.setheading(0) # 초기값으로 각도 0으로 만들어준다.
tim.hideturtle() #for문이 끝난 후에는 터틀 객체를 숨겨주고
screen.exitonclick() #화면이 꺼질 때까지 화면이 닫히지 않게 함
