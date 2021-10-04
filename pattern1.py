import turtle


t = turtle.Turtle()

t.getscreen().bgcolor("black")

t.speed(20)


for i in range(5):
    for colours in ["red","cyan","lime","lightblue","magenta","orange"]:
        t.color(colours)
        t.pensize(4)
        t.lt(12)
        for i in range(4):
            t.fd(200)
            t.lt(90)
turtle.done()

#A KHUSH MUNSHI PRODUCTION
