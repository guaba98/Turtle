import turtle
import turtle as t
import random

tim = t.Turtle() #터틀 객체 생성

t.colormode(255)

def random_color():
    """r, g, b 색 반환 함수"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


screen = t.Screen() #화면 생성
tim.speed('fastest') #터틀 속도: 가장 빠르게

def draw_the_circle(size_of_gap):
    """터틀이 원 그리는 함수"""
    for i in range(int(360 / size_of_gap)): #360도를 함수에 넣은 숫자로 나눈 만큼 반복
        tim.color(random_color()) #랜덤한 숫자 받아옴
        tim.circle(100) #반지름은 100
        tim.setheading(tim.heading() + size_of_gap) #for문이 돌아갈 때마다 터틀의 각도 변경해줌

# 함수 호출
draw_the_circle(5)

screen.exitonclick() #클릭하기 전까지 켜져 있게 함