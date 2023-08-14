from turtle import *
from random import randint
from time import *

def razmetka(): #функция рисует разметку гоночного поля
    t = Turtle()
    t.speed(0)
    for i in range (1,21):
        t.penup()
        t.goto(-200+i*20,50)
        t.pendown()
        t.goto(-200+i*20,-100)
    t.hideturtle()

def catch1(x,y):    #это обработчик события нажатия на объект
    t1.write('Ouch!', font=('Arial', 14, 'normal')) #пишем на экране Ауч!
    t1.fd(randint(1,5))     #черепашка делает случайный шаг от 1 до 5
   
def catch2(x,y):
    t2.write('Ouch!', font=('Arial', 14, 'normal'))
    t2.fd(randint(1,5))
    
x_finish = 200

t1 = Turtle() #тут рождается новая черепашка класса Черепах
t1.shape("turtle")
t1.color("red")
t1.penup()
t1.goto(-200,20)
t1.pendown()
t1.speed(2)
t1.onclick(catch1)

t2 = Turtle()
t2.shape("turtle")
t2.color("blue")
t2.penup()
t2.goto(-200,-20)
t2.pendown()
t2.speed(2)
t2.onclick(catch2)

razmetka()

while t1.xcor() < x_finish and t2.xcor() < x_finish:
    t1.fd(randint(3,6))
    t2.fd(randint(3,6))
    sleep(0.05)

if t1.xcor() >= x_finish:
    t1.write('I am Winner!!!', font=('Arial', 14, 'normal'))
else:
    t2.write('I am Winner!!!', font=('Arial', 14, 'normal'))
exitonclick()

