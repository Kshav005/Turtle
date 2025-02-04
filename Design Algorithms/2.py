import turtle as t, random
from time import sleep

# Flower

colors = ["green", "pink", "red", "black", "orange", "purple", "blue"]
t.width(2)
t.speed(speed=0)
diff = 0
for i in range(20) :
    t.pencolor(random.choice(colors))
    t.circle(15+diff, 360)
    t.penup()
    t.right(45)
    t.forward((15+diff)//2)
    t.pendown()
    diff += 1

t.penup()
t.left(90)
t.forward((15+diff))
t.pendown()
t.forward(200)
t.pencolor("green")
sleep(5)