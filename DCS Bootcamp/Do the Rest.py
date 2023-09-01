from typing import Self

class Complex:
    def __init__(self, real: float, imaginary: float):
        self.a = real
        self.b = imaginary
    
    def __str__(self):
        return(f'{self.a} + {self.b}i' 
               if self.b >= 0
               else f'{self.a} - {-self.b}i')

    def __add__(self, other: Self):
        a = self.a + other.a
        b = self.b + other.b

        return Complex(a, b)
    
    def __sub__(self, other: Self):
        a = self.a - other.a
        b = self.b - other.b

        return Complex(a, b)
    
    def __mul__(self, other: Self):
        a = self.a + other.a
        b = self.b + other.b

        a = (self.a * other.a)
        b = (self.a * other.b)
        c = (self.b * other.a)
        d = (self.b * other.b)

        return Complex(a - d, c + d)
    
    def __div__(self, other: Self):
        a = self.a / other.a
        b = self.b / other.b

        return Complex(a, b)

z1 = Complex(1, 2)
z2 = Complex(3, 4)
print("Add", z1 + z2)
print("Subtract", z1 - z2)
print("Multiply", z1 * z2)