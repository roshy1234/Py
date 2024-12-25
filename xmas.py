import turtle
import random

# Setup screen
turtle.setup(600, 500)
turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(10)
t.hideturtle()

# Function to generate random colors
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Draw star function
def draw_star(size):
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

# Main drawing loop
turtle.colormode(255)
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(10, 300, 30):
    t.color(random_color())
    draw_star(i)
    t.right(36)

# Write Happy Xmas
t.penup()
t.goto(-150, -200)
t.color("white")
t.write("Happy Xmas", font=("Arial", 30, "bold"))

# End program
turtle.done()