# In this exercise, you need to draw 'H' and 'T', side by side and with two different colors, using the turtle.
# No need to worry if you fail. The tutorial is uploaded to help you only, so just feel free to take help. But if you want your learning to be good enough, then first try yourself few times and then look at the solution below.







from turtle import * 
import time 

speed(1)
pensize(5)
pencolor("green")

# For letter 'H'
left(90)
forward(100)
back(50)
right(90)
forward(50)
left(90)
forward(50)
back(100)

# Creating a gap
penup()
right(90)
forward(60)

# Creating the letter (T)
pendown()
pencolor("blue")
left(90)
forward(100)
left(90)
forward(30)
back(60)
time.sleep(2)


# Hence, the exercise is complete. If you made this all by yourself then you are growing like a fine wine. Congratulations for that! But those who couldn't solve, don't be sad because small contributions make big outcomes. Just don't give up and keep learning happily!