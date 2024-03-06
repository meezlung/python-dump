from cs12232prac03d import DesmondMarketplace, MollyMarketplace

t = 1000000

m = MollyMarketplace(3, t)
d = DesmondMarketplace(5, t)

successful = d.rent(2000000, 10000000)
assert successful

successful = d.rent(20000000, 10000)
assert successful

successful = d.rent(999999, 100000000)
assert not successful

successful = m.rent(2000000, 400000)
assert successful

successful = m.rent(2000000, 300000)
assert successful

successful = m.rent(2000000, 200000)
assert successful

successful = m.rent(2000000, 100000)
print(successful)
assert not successful
print(m.m.m)

print(d.m.m)
assert m.lowest_income(0, 2) == 300000
assert m.lowest_income(1, 3) == 200000
assert d.lowest_income(2, 5) == 10000
assert d.lowest_income
