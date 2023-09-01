# Using disjoint (edgepoint ng mga rectangle ang basehan (hitbox))

from typing import Self

class Interval:
    # this just initializes the values of the upper and lower values
    # the assert function below checks if upper is greater than lower
    # just means that upper, supposedly, is literally greater than lower
    def __init__(self, lower: float, upper: float):
        assert upper > lower
        self.lower = lower
        self.upper = upper
    
    # this function checks if the value is within the edgepoints
    # of the coordinates of the other rectangle
    def __contains__(self, value: float): 
        return self.lower <= value <= self.upper
    
    # this function checks whether a rectangle is behind or to the left
    # or behind another rectangle's edgepoint (specifically self.lower)
    def is_behind(self, value: float):
        return self.upper < value
    
    # this function checks whether a rectangle is ahead or to the right
    # or behind another rectangle's edgepoint (specifically self.lower)
    def is_ahead(self, value: float):
        return value < self.lower
    
    # this function just combines is_behind and is_ahead
    def is_disjoint_from(self, other: Self):
        return self.is_behind(other.lower) or self.is_ahead(other.upper)
    
class Point:
    x: float = 0
    y: float = 0

class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.width = Interval(top_left.x, bottom_right.x)
        self.height = Interval(bottom_right.y, top_left.y)

    def __contains__(self, point: Point):
        return point.x in self.width and point.y in self.height
    
    # this function whether this rectangle is disjoint from another
    def is_disjoint_from(self, other: Self):
        return self.height.is_disjoint_from(other.height) or self.width.is_disjoint_from(other.width)

# rectangle 1
top_left1 = Point()
top_left1.x = 0
top_left1.y = 4

bottom_right1 = Point()
bottom_right1.x = 4
bottom_right1.y = 0

# rectangle 2
top_left2 = Point()
top_left2.x = 1
top_left2.y = 2

bottom_right2 = Point()
bottom_right2.x = 6
bottom_right2.y = -2

rectangle1 = Rectangle(top_left1, bottom_right1)
rectangle2 = Rectangle(top_left2, bottom_right2)

collision = not(rectangle1.is_disjoint_from(rectangle2))

if collision:
    print("The rectangles have collided.")

else:
    print("The rectangles have not collided.")