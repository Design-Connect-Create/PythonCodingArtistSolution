
import turtle

t = turtle.Turtle()

"""
Drawing a Self Portrait  
"""
# face circle
t.color("tan")
t.circle(50)

t.penup()

# right eye
t.setposition(-25,60)
t.pendown()
t.color("brown")
t.circle(5)

t.penup()

# left eye
t.setposition(25,60)
t.pendown()
t.color("brown")
t.circle(5)

t.penup()

#smile
t.setposition(-25,40)
t.color("red")
t.pendown()
t.right(55)
t.forward(25)
t.left(55)
t.forward(35)
t.left(55)
t.forward(25)

# hide turtle
t.hideturtle()

