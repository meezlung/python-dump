# type: ignore

def combinations(iterable):
    # Base case: if the list is empty, return a list containing the empty list
    if len(iterable) == 0:
        return [[]]

    combos = []

    for combo in combinations(iterable[1:]):
        combos += [combo, combo + [iterable[0]]]

    return combos

# Example usage:
numbers = [1, 2, 3, 4, 7]
sublists = combinations(numbers)

for sublist in sublists:
    print(sublist)