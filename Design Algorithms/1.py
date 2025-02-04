import turtle as t, random

colors = ["green", "pink", "red", "black", "orange", "purple", "blue"]
t.width(2)
t.bgcolor("black")
diff = 0
for i in range(10000) :
    t.pendown()
    t.pencolor(random.choice(colors))
    t.forward(2+diff)
    t.right(60)
    t.forward(2+diff)
    t.right(60)
    t.penup()
    diff += 3
    t.forward(2+diff)
    