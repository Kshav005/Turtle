import turtle as t, random
from time import sleep

# Flower

colors = ["green", "pink", "red", "black", "orange", "purple", "blue"]
t.width(2)
t.speed(speed=0)
diff = 0
for i in range(2000) :
    t.pencolor(random.choice(colors))
    t.circle(15+diff, 360, 6)
    t.penup()
    t.right(45)
    t.forward((15+diff)//2)
    t.pendown()
    diff += 0.2