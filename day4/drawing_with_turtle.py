import sys
import turtle


def draw_rectangle():
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)


def draw_circle():
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(15, 28)
    pen.down()
    pen.begin_fill()
    pen.pencolor("red")
    pen.fillcolor("purple")
    pen.circle(60)
    pen.end_fill()
    pen.up()


def draw_triangle():
    pen = turtle.Turtle()
    pen.begin_fill()
    pen.pencolor("Blue")
    pen.fillcolor("Green")
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(135)
    pen.forward(150)
    pen.end_fill()

def draw_pentagon():
    pen = turtle.Turtle()
    turtle.title("My turtle window")
    pen.begin_fill()
    pen.pencolor("Blue")
    pen.fillcolor("Green")
    for i in range(5):
        pen.forward(100)
        pen.left(72)
    pen.end_fill()












def main():
    #draw_rectangle()
    #draw_circle()
    #draw_triangle()
    draw_pentagon()
    turtle.done()

    return 0


if __name__ == "__main__":
    sys.exit(main())

#sudo apt get install python3_tk