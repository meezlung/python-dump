from cs12232prac04b import swap_pairs

assert swap_pairs((3, 1, 4, 1, 5, 9)) == [1, 3, 1, 4, 9, 5], f'{swap_pairs((3, 1, 4, 1, 5, 9))}'
assert swap_pairs(('Kelly', 'Alec', 'Xochitl', 'Valentin')) == ['Alec', 'Kelly', 'Valentin', 'Xochitl']

# test ValueError when odd
try:
    swap_pairs([1, 2, 3])
except ValueError:
    pass
else:
    assert False, "should have raised ValueError!"