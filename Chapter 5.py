# In this chapter, we are going to learn about drawing a circle using turtle in python
# It may sound complicated but it is not as turtle has something easy for you!
# Let's start the tutorial.

from turtle import * 
import time 

speed(1)
color("red")

# A circle can be drawn using the 'circle' function of turtle.
circle(100)


penup()
right(90)
forward(50)
pendown()

# In order to make a semicircle, specify the extend argument of the function. Extend is the angle, till which you want to create the circle. As we know, the semi-circle is of 180 degrees only so I am going to mention the extend as '180'
color("green")
circle(30, 180)

# There is one more argument of 'circle' and it's the steps. Steps is used to create a polygon. Suppose I want a 7 sided close polygon, so I will be mentioning the 'steps' as '7'.
penup()
right(90)
forward(70)
pendown()
color("pink")

circle(50, 360, 7)

time.sleep(2)