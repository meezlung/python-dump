import math
def hypotenuse(a, b):
    cSquared = a**2 + b**2
    sqrtC = math.sqrt(cSquared)
    return int(sqrtC)

print(hypotenuse(11, 12))