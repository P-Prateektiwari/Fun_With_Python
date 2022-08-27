import turtle as t
from random import randint

t.speed(0)


t.color("cyan")
t.begin_fill()
t.left(90)
t.forward(200)
t.right(90)
t,t.forward(21)
t.right(90)
t.forward(200)
for i in range(200):
        t.right(1)
        t.forward(1)
t.right(80)
t.forward(20)
t.right(88)
for i in range(110):
        t.left(1.5)
        t.forward(1)
t.left(1.25)
t.forward(3)


t.end_fill()

t.penup()
t.goto(182,-15)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(220)
t.end_fill()

t.penup()
t.goto(160,-10)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(190)
t.end_fill()

t.home()
t.color("cyan")
t.begin_fill()
t.left(90)
t.forward(200)
t.right(90)
t,t.forward(21)
t.right(90)
t.forward(200)
for i in range(200):
        t.right(1)
        t.forward(1)
t.right(80)
t.forward(20)
t.right(88)
for i in range(110):
        t.left(1.5)
        t.forward(1)
t.left(1.25)
t.forward(3)
t.end_fill()


for i in range(60):
        t.penup()
        t.setx(randint(-160,160))
        t.sety(randint(-150,200))
        t.pendown()
        t.color("cyan")
        t.begin_fill()
        for c in range(5):
        
                t.forward(5)
                t.left(144)
        t.end_fill()
t.hideturtle()
t.done()