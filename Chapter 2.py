# In this chapter, let's learn about the pen modifications. We can change the thickness and the color!
from turtle import *
import time 

speed(1)

# To change the thickness, use 'pensize(size)' and try all the sizes that are suiting you best.
pensize(10)

# To change the pen-color, use 'pencolor("color_name")'.
pencolor("red")

# If you want to test the codes above, don't forget to use those draw commands (forward, back, left, right) to check if anything changed. 

# Let's use the turtle to move up to another place without drawing anything.
penup()                       # First use 'penup' command and then it will allow us to move somewhere above.
goto(100, 200)          # Using the 'goto(x, y)' command to move to a certain point. 

# So, if you run the code, you will understand how all this works. It's based on simple mechanism called 'coordinate geometry'. In order to move your turtle efficiently and with ease, you need to have some knowledge regarding graphs, x-axis, y-axis etc.

# To move down, you just need to specify values in negative.
goto(-100, 60)
forward(50)             # You can also move the pen like this, but it will be really complicated.

# Now, if you want to draw again, use 'pendown()' and then use commands to start drawing. You can use the 'goto(x,y)' feature too, if you want! It works both ways.
time.sleep(2)
