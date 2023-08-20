import math
def prod(L):
    # initializes the value / the placeholder
    one = 1 # where we append the final product and each individual elements on the list are multiplied
    
    # so for every number in L, it will be multiplied to 1 and then transfer to variable one
    # one = 1 * 1 ; the variable one would update its value to 1
    # one = 1 * 2 ; the variable one would update its value to 2
    # one = 2 * 3 ; the variable one would update its value to 6
    # until there's nothing to iterate anymore or until all individual values are iterated over, the program would stop
    # leaving the variable one with the desired product

    for number in L:
        one = one * number

    product = math.prod(L)
    return one

    
    

print(prod([1, 2, 3]))