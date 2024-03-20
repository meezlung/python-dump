from cs12232prac04c import sort_parcels

res1: dict[int, list[str]] = sort_parcels((
        (1000, 'shirt'),
        (3000, 'light bulb'),
        (1000, 'kfc'),
        (1000, 'jollibee'),
        (2000, 'kfc'),
        (1000, 'shirt'),
        (3000, 'pen'),
    ))
assert res1 == {
    1000: ['shirt', 'kfc', 'jollibee', 'shirt'],
    2000: ['kfc'],
    3000: ['light bulb', 'pen'],
}


res2: dict[str, list[str]] = sort_parcels((
        ('jerome@down.edu.ph', 'shirt'),
        ('felipe@down.edu.ph', 'light bulb'),
        ('jerome@down.edu.ph', 'kfc'),
        ('jerome@down.edu.ph', 'jollibee'),
        ('thanos@down.edu.ph', 'kfc'),
        ('jerome@down.edu.ph', 'shirt'),
        ('felipe@down.edu.ph', 'pen'),
    ))
assert res2 == {
    'thanos@down.edu.ph': ['kfc'],
    'jerome@down.edu.ph': ['shirt', 'kfc', 'jollibee', 'shirt'],
    'felipe@down.edu.ph': ['light bulb', 'pen'],
}
