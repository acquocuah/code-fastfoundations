import math
import os
import sys


class Circle:
    units = 'cm'  # all circles will have the same units

    def __init__(self, radius, position=(0, 0)):
        self.radius = radius  # each circle will have a particular radius
        self.position = position
        self.diameter = radius*2
        # self.area = math.pi * radius**2

    def __str__(self):  # Python special methods
        return f"I am a circle of size {self.radius}{self.units} and {self.diameter}{self.units} located at {self.position} for circle of area {self.area}."

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return math.pi * 2 * self.radius

    def arc_length(self, angle, degrees=False):
        return (math.pi * self.radius * 2) * (angle / 360)

    def bounding_box(self):
        """Function to compute the four values of the bounding box for a circle"""
        # xmin, xmax, ymin, ymax
        return self.position[0] - self.radius
        return self.position[0] + self.radius
        return self.position[0] - self.radius
        return self.position[0] + self.radius

# def area(circle):
#     return math.pi * circle.radius ** 2
#
# def perimeter(circle):
#     return math.pi * 2 * circle.radius
#
# def arc_length(circle, angle, degrees=False):
#     return (math.pi * circle.radius * 2) * (angle / 360)
#

# def bounding_box(circle):
#     """Function to compute the four values of the bounding box for a circle"""
#     xmin, xmax, ymin, ymax
    # return circle.position[0]-circle.radius
    # return circle.position[0]+circle.radius
    # return circle.position[0]-circle.radius
    # return circle.position[0]+circle.radius

def main():
    small_circle = Circle(10)
    big_circle = Circle(50)

    print(small_circle)
    print(big_circle)

    # now we change units for all instances on the class
    Circle.units = 'pm'

    print(small_circle)
    print(big_circle)

    # but
    big_circle.units = 'hm'  # only change for the big_circle instance

    print(small_circle)
    print(big_circle)

    print(small_circle.area())

  #  canvas = Canvas(1200, 780)
   # canvas.mystery_method()
    #turtle.done()

    return os.EX_OK


if __name__ == '__main__':
    sys.exit(main())
