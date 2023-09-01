# Classes to the rescue!

# PascalCase (has class) > snake_case (because snake_case is just a local variable)

class Team:
    
# Classes vs Objects

team1 = Team()
team2 = Team()

assert team1 is not team2 # comparing the memory allocated between the two variables of team1 and team2

print(team1) 
print(team2)



# Variables and Functions inside Classes

class Team:
    def message():
        return 'Teamwork'

Team.message() # Returns 'Teamwork'



# Object Constructors
# __ double index (double dunder? yung tawag nila) --> checking the results, printing the output

class Team:
    def __init__(self, name: str): # self is the new person or object that we put attributes to
        self.name = name

up = Team('krazy')
print(up.name) # outputs krazy



# Object Instance Methods
# Functions that change the behavior of an object's internal object
# Analogy is just a simple remote. Only focus on pressing buttons, 

class Team:
    def __init__(self, name: str):
        self.name = name
    
    def shout(self):
        print("Go{}".format(self.name))

up = Team('lrazy')
Team.shout(up)
up.shout()



#

class Complex:
    def __init__(self, real: float, imaginary: float):
        self.a = real
        self.b = imaginary
    
    def __str__(self):
        return(f'{self.a} + {self.b}i' 
               if self.b >= 0
               else f'{self.a} - {-self.b}i')
    




# C++

int main() {
    std::cout << "hello world"
    return 0
}



#

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

z1 = Complex(1, 2)
z2 = Complex(2, 3)
print(z1 + z2)


# Class Inheritance
# Allows children class to extend the capabilities of parents
# Removes duplication

# Summary: Abstraction, Encapsulation, Inheritance, Polymorphism