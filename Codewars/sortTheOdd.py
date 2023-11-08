def sort_array(source_array):
    odd = {}

    for number in source_array:
        if number % 2 != 0:
            odd[number] = source_array.index(number)

    sorted_odd = dict(sorted(odd.items()))    

    return source_array, sorted_odd
            

print(sort_array([7, 1])) # [7, 1]  =>  [1, 7]
print(sort_array([5, 8, 6, 3, 4])) # [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]