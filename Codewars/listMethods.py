def replace(list, X, Y):
    count = 0
    length = len(list)
    while count <= length:
        for element in list:
            if element == X:
                position = list.index(element) # this marks the index of the element the same as X
                list.remove(element)
                list.insert(position, Y)
                count += 1
        return list

L = [3, 1, 4, 1, 5, 9]
print(replace(L, 1, 7))
