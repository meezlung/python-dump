def filter_list(l):
    filtered = []
    for i in l:
        if type(i) == int:
            filtered.append(i)
    return filtered

print(filter_list([1, 2, "a", "b", 3]))