# type: ignore

import math
def hypotenuse(a, b):
    cSquared = a**2 + b**2
    sqrtC = math.sqrt(cSquared)
    return int(sqrtC)

'''
def rightTrianglePerimeter(a, b):
    c = hypotenuse(a, b)
    sum = a + b + c
    return sum
'''

def distance2D(x1, y1, x2, y2):
    a = abs(x2-x1)
    b = abs(y2-y1)
    c = hypotenuse(a, b)
    return c

def trianglePerimeter(xA, yA, xB, yB, xC, yC):
    AB = distance2D(xA, yA, xB, yB)
    BC = distance2D(xB, yB, xC, yC)
    CA = distance2D(xC, yC, xA, yA)
    perimeter = AB + BC + CA
    return perimeter

print(trianglePerimeter(1, 2, 1, 0, -1, 0))