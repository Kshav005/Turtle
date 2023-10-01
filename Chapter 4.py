# Let's learn about some more about the turtle module.

from turtle import * 
import time

pensize(5)
pencolor("pink")
speed(1)

# If you like to use a background image then make sure the format of the image file in '.gif' and then use it by 'bgpic("location")'
bgpic("im1.gif")

# Did you know that you can change the shape of the turtle icon in the window? Let me show you how!
# There are 6 shapes provided by the turtle. These are - turtle, arrow, circle, square, triangle and classic. 'Classic' shape is used as the default.
shape("turtle")

# If you want turtle and line color to be different then use 'color("line_color", "turtle_color")'
color("green", "purple")
forward(90)

# We can change the color in form of rgb terms too!
# But you will need to change the color mode to 255.
colormode(255)
color(56, 223, 153)
left(90)
forward(100)

# You can change the title of the window using turtle by 'title("title_name")'
title("Chapter 4")




time.sleep(2)