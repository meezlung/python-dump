from cs12232prac04a import stack_like_pancakes

assert stack_like_pancakes((
        [3, 1],
        [4],
        [1, 5, 9],
    )) == [1, 3, 4, 9, 5, 1]

assert stack_like_pancakes((
        ['maple', 'strawberry'],
        ['waffle', 'chocolate', 'burnt']
    )) == ['maple', 'strawberry', 'burnt', 'chocolate', 'waffle']