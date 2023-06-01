from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.width(4)

def move_forwards():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_right():
    tim.right(5)
def turn_left():
    tim.left(5)
def clear_screen():
    tim.clear()

screen.listen()
screen.onkey(key='w', fun=move_forwards) #()를 사용하지 않는다.
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='c', fun=clear_screen)


#함수를 입력으로 전달할 때, 괄호를 붙이지 않고 사용한다.
#다른 함수를 입력으로 받아들이는 함수가 고차함수라고 불린다.

screen.exitonclick()