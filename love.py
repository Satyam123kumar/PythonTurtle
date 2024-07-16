
import turtle
import time 

t = turtle.Turtle()
t.screen.bgcolor("black")
t.color("white", "red")
t.pensize(5)
t.speed(7)
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# I
move(-550, -180)
t.left(90)
t.forward(400)

#<3
move( -100, -150)
t.begin_fill()
t.left(50) 
t.forward(230)
t.circle(-120, 200)
t.left(120)
t.circle(-120, 200)
t.forward(238)
t.end_fill()

#U
t.setheading(270)
move(300, 200 )
t.forward(250)
t.circle(120, 180)
t.forward(250)

time.sleep(3)