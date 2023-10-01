# Todady we are going to learn about another amazing module in python which is majorly used in drawing stuff and creating games!
# The module name is 'turtle'. 
# A turtle is just a pencil (you must be knowing it if you have learnt it in young age). We control the turtle using coding language and all the movement is done by us, by passing certain arguments
# You needn't download the module as it's inbuilt. So let's begin using that!

# Importing all the functions in our python file
from turtle import *
import time

# Use 'speed()' to set the speed of the turtle movement. Type 1 if you want slow movement then increase it by 'n' number of times, depending upon how you like the speed.
speed(1)

# Use 'forward(distance)' to move your turtle to a forward distance.
# The distance is known as steps. The turtle is at 0 (centre) defaultly.
forward(50)        # run the code after typing till here.

# If your turtle window is closing on it's own then don't worry. It's the way that it works. To wait for few time, use the 'sleep' from the time module at the end.


# To move back, use 'back(distance)' and the turtle will move backwards. 
back(100)

# Now let's learn about the left/right movement of the turtle. 
# We use 'left(angle)' and 'right(angle)' in order to do so. 
# We have to define an angle which will tell the turtle to turn left/right till that degree.
# By this this method, let's try making a square!
left(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
time.sleep(3)

# If you know about the directions precisely, then you can create shapes easily.