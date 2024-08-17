# type: ignore

# def find_combination(n, max_num):
#     if n == 0:
#         return []
    
#     for i in range(max_num, 0, -1):
#         if n >= i**2:
#             remainder = n - i**2
#             result = find_combination(remainder, i - 1)
#             if result is not None:
#                 return result + [i]
    
#     return None

# def decompose(n):
#     result = find_combination(n**2, n - 1)
#     return result if result else None


# Most readable 

def decompose(n):
    goal = 0
    result = [n] # 50

    while result:
        current = result.pop() 
        goal += current ** 2 

        for i in range(current - 1, 0, -1):
            if goal - (i ** 2) >= 0: 
                goal -= i ** 2 
                result.append(i) 
                if goal == 0:
                    result.sort()
                    return result
                
    return None


# Fastest though a bit confusing

# from math import sqrt

# def decompose(n):
#     return decompose_alt(n**2, n-1)

# def decompose_alt(n, m):
#     if sqrt(n) == int(sqrt(n)) and int(sqrt(n)) <= m: # Basically checks agad if perfect square yung inimput
#         return [int(sqrt(n))]
    
#     for i in range(min(int(sqrt(n)), m), 0, -1):
#         result = decompose_alt(n - i**2, i - 1)
#         if result: 
#             return result + [i]
#     return None


print(decompose(1))
print(decompose(2))
print(decompose(3))
print(decompose(4))
print(decompose(5))
print(decompose(11))
print(decompose(50))
print(decompose(49))


