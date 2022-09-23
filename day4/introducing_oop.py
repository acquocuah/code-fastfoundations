import math
import sys
import os
import turtle


class Circle:
    units = 'cm'  # all circles will have the same units

    def __init__(self, radius, position=(0, 0), fill='red', stroke='green'):
        self.radius = radius  # each circle will have a particular radius
        self.position = position
        self.fill = fill
        self.stroke = stroke

    def __str__(self):  # Python special methods
        return f"I am a circle of size {self.radius}{self.units} located at {self.position}."

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def arc_length(self, angle, degrees=False):
        """Function to compute the arc length l for the angle provided"""
        if degrees:  # angle is in degrees
            return self.radius * math.radians(angle)
        return self.radius * angle  # assume angle is in radians

    def bounding_box(self):
        """Function to compute the four values of the bounding box for a circle"""
        # xmin, xmax, ymin, ymax
        return (
            self.position[0] - self.radius,
            self.position[0] + self.radius,
            self.position[1] - self.radius,
            self.position[1] + self.radius,
        )

    def draw(self, pen):
        if pen.isdown():
            pen.up()
        pen.goto(15, 28)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self.stroke)
        pen.fillcolor(self.fill)
        pen.circle(self.radius)
        pen.end_fill()
        pen.up()


class Rectangle:
    def __init__(self, width, height, position=(0, 0), fill='white', stroke='black'):
        self.width = width
        self.height = height
        self.position = position
        self.fill = fill
        self.stroke = stroke

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def bounding_box(self):
        # xmin, xmax, ymin, ymax
        return self.position[0] - self.width / 2
        return self.position[0] + self.width / 2
        return self.position[0] - self.height / 2
        return self.position[0] + self.height / 2

    #   def __str__(self):  # Python special methods
    #      return f"I am a rectangle of area {self.area}, perimeter {self.perimeter} and diagonal {self.diagonal}."

    def __str__(self):
        return f"Rectangle: ({self.width}x{self.height}) loc: {self.position}"


class Text:
    def __init__(self, text, position=(0, 0), colour='black'):
        self.text = text
        self.position = position
        self.colour = colour

    def write(self, pen):
        text.write(self.pen)


class Square(Rectangle):
    def __init__(self, width, height=None):
        super().__init__(width, width)

    def area(self):
        return self.width ** 2

    def perimeter(self):
        return 2 * (self.width * 2)

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.width ** 2)

    def bounding_box(self):
        # xmin, xmax, ymin, ymax
        return (
            self.position[0] - self.width / 2,
            self.position[0] + self.width / 2,
            self.position[0] - self.width / 2,
            self.position[0] + self.width / 2
        )

    def __str__(self):
        return f"Square sides: ({self.width}x{self.width}) location: {self.position}"

    def draw(self, pen):
        if pen.isdown():
            pen.up()
        pen.goto(*self.position)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self.stroke)
        pen.fillcolor(self.fill)
        pen.forward(self.width)
        pen.right(90)
        pen.forward(self.height)
        pen.right(90)
        pen.forward(self.width)
        pen.right(90)
        pen.forward(self.height)
        pen.right(90)
        pen.end_fill()
        pen.up()

class Square(Rectangle):
    def __init__(self, width, *args, **kwargs):
        super().__init__(width, width, *args, **kwargs)

class Canvas(turtle.TurtleScreen):
    def __init__(self, width, height, bg):
        canvas = turtle.getcanvas()
        super().__init__(canvas)
        self.width = width
        self.height = height
        self.bg = bg
        self.screensize(self.width, self.height, bg)
        self.pen = turtle.RawTurtle(canvas)

    def draw(self, shape):
        shape.draw(self.pen)


    def write(self, text):
        text.write(self.pen)



def main():
    # instantiate a rectangle
    # rectangle = Rectangle(16, 9)
    canvas = Canvas(1200, 750, "blue")
    # print the rectangle
    # print(rectangle)
    print(canvas)

    # instantiate a square
    # square = Square(16)
    # print the square
    # print(square)
    # print(f"Area of Square is: {square.area()}")
    # print(f"Perimeter of Square is: {square.perimeter()}")
    # print(f"Diagonal of Square is: {square.diagonal()}")
    # print(f"Bounding Box of Square is: {square.bounding_box()}")
    # canvas.Draw_axis()
    circle20 = Circle(20, position = (15,20), fill="orange")
    canvas.draw(circle20)

    circle70 = Circle(70, position=(5, 0), fill="green")
    canvas.draw(circle70)

    rectangle = Rectangle(37, 40, position=(-15, -15))
    canvas.draw(rectangle)


    #text = Text("This is a space for turtle")
    #canvas.write(text)

    turtle.done()

    return 0


if __name__ == '__main__':
    sys.exit(main())
