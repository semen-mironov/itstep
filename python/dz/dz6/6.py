import turtle

window = turtle.Screen()
turtle.reset()

turtle.shape("turtle")
turtle.bgcolor("black")
turtle.color("white")
turtle.speed(0)
turtle.pensize(2)

for i in range(10):
    for j in range(10):
        turtle.forward(j*10)
        turtle.left(10*j*2)
    turtle.circle(10*j*2)
    turtle.left(15+j*10)

window.exitonclick()