# This chapter is a little short. We are going to learn about the coloring in turtle shapes.
# Let's do this!

from turtle import * 
import time 

Screen()
pensize(6)
pencolor("green")
speed(1)

# To fill the shape with color, we will be using 'fillcolor()' along with some attributess
# To test the command, let's create a square or a rectangle, anything you like! Here, I will be creating a rectangle.
# Use 'fillcolor("colorname")' to select the color for filling in the shape.
fillcolor("yellow")

# Use the 'begin_fill()' to mark the starting.
begin_fill()
forward(300)
left(90)
forward(100)
left(90)
forward(300)
left(90)
forward(100)

# After creating the rectangle, let's stop the coloring by using 'end_fill()'
end_fill()

# You can also choose a background color using 'bgcolor("color_name")'
bgcolor("black")

# To hide the turtle after creating the shape, use 'hideturtle()'
hideturtle()


# That's all to learn in this chapter. But if you feel like gaining a little more knowledge then I am going to tell you about how to create shapes of equal sides easily using python loops!
# Moving the turtle to another location and resetting it.
penup()
goto(-100, 0)
right(90)
pendown()
# Equilateral triangle 
for i in range(3) : 
    left(120)
    forward(80)
    
    
    
time.sleep(2.5)
