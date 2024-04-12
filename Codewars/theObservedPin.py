# TODO
# 1. Iterate through each digit
# 2. For each digit, check all their adjacents in a hashmap
# 3. Use itertools for each lists in the hashmaps
# Time Complexity: O(n^k)
# Space Complexity: O(n)

from itertools import product

def get_pins(observed):
    adjacent_digits = {'1': ['1', '2', '4'], 
                       '2': ['1', '2', '3', '5'], 
                       '3': ['2', '3', '6'], 
                       '4': ['1', '4', '5', '7'], 
                       '5': ['2', '4', '5', '6', '8'], 
                       '6': ['3', '5', '6', '9'], 
                       '7': ['4', '7', '8'], 
                       '8': ['5', '7', '8', '9', '0'], 
                       '9': ['6', '8', '9'], 
                       '0': ['0', '8']}
    

    return [''.join(each_combination) for each_combination in list(product(*[adjacent_digits[digit] for digit in observed]))]


print(get_pins('8'))
print(get_pins('11'))
print(get_pins('369'))