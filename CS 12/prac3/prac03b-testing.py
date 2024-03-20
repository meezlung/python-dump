from cs12232prac03b import Metropolis

m = Metropolis([3, 1, 4, 1, 5])

assert m.cost(0, 0) == 0
assert m.cost(0, 1) == 14
assert m.cost(0, 2) == 35
assert len(m) == 5
m.expand_left(2)
assert len(m) == 6
assert m.cost(1, 3) == 35