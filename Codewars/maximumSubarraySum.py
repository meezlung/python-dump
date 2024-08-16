# type: ignore

def max_sequence_inefficient_bruteforce(arr):
    n = len(arr)
    negative_counter = 0
    max_sum = 0
    
    for i in range(n):
        if arr[i] < 0:
            negative_counter += 1

        for j in range(n):
            curr_sum = sum(arr[i:j + 1])
            if max_sum < curr_sum:
                max_sum = curr_sum                

    if n == negative_counter:
        return 0
    
    return max_sum

def max_sequence_long(arr):
    n = len(arr)
    max_ending_here = 0
    max_so_far = float('-inf')
    negative_counter = 0 

    for i in range(0, n):
        if arr[i] < 0:
            negative_counter += 1

        max_ending_here = max_ending_here + arr[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    if n == negative_counter:
        return 0

    return max_so_far

def max_sequence(arr):
    n = len(arr)
    max_ending_here = 0
    max_so_far = float('-inf')
    negative_counter = 0 

    for i in range(n):
        if arr[i] < 0: negative_counter += 1
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far if n != negative_counter else 0
    
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)
print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155)