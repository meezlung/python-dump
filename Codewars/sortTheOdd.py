def sort_array_draft(source_array):
    odd = []
    odd_index = []
    index_tracker = 0
    for number in source_array:
        if number % 2 != 0:
            odd.append(number)
            odd_index.append(index_tracker)
            index_tracker += 1
        else:
            index_tracker += 1
    odd.sort()

    for index in odd_index:
        source_array[index] = odd[odd_index.index(index)]

    return source_array

def sort_array(source_array):
    result = sorted([l for l in source_array if l % 2 == 1])
    print(result)
    for index, item in enumerate(source_array):
        print(index, item)
        if item % 2 == 0:
            result.insert(index, item)
    return result
            
print(sort_array([1, -22, -24, 5, 19, -3, 46, -22, 1])) 
print(sort_array([5, 8, 6, 3, 4])) # [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]