def factorial(number):
    result = 1
    for i in range(number):
        result *= i + 1
    return result

"""
Pros of recursion:
1. Elegant, readable
2. Great for naturally recursive solutions
3. "Contained" variables lead to relatively safer methods

Cons of recursion:
1. Harder to think of a solution if you're not well-practiced
2. Always consumes more memory kasi stinostore ung kada recursive step
   Unlike sa for loops, nauupdate lang sa isang variable ung final value after ng lahat ng recursive step
"""


def recursion_factorial(number): 
    if number == 1: return 1
    else: return number * recursion_factorial(number - 1)

# Replacing this main function with the functions below without for loop
"""
def main():
    test_cases = int(input())  # Read the number of test cases
    for _ in range(test_cases):
        number = int(input())   # Read each number for which you want to calculate the factorial
        print(recursion_factorial(number))

if __name__ == "__main__":
    main()
"""

def solve(test_cases):
    if test_cases == 0: return
    number = int(input())
    print(recursion_factorial(number))
    print(test_cases - 1)
    solve(test_cases - 1)

def main():
    test_cases = int(input())
    print(test_cases)
    solve(test_cases)

if __name__ == "__main__":
    main()