# from cs12232prac03d import DesmondMarketplace, MollyMarketplace

# t = 1000000

# m = MollyMarketplace(5, t)
# d = DesmondMarketplace(7, t)

# successful = d.rent(2000000, 10000000)
# assert successful
# print("Case 1")
# print(m.m.m)
# print(d.m.m)
# assert m.lowest_income(0, 2) == 0
# assert m.lowest_income(1, 3) == 0
# assert d.lowest_income(2, 5) == 0
# assert d.lowest_income(5, 2) == 0
# print()

# successful = d.rent(20000000, 1)
# assert successful
# print("Case 2")
# print(m.m.m)
# print(d.m.m)
# assert m.lowest_income(0, 2) == 0
# assert m.lowest_income(1, 3) == 0
# assert d.lowest_income(2, 5) == 0
# assert d.lowest_income(5, 2) == 0
# print()

# successful = d.rent(20000000, 10000)
# assert successful
# print("Case 3")
# print(m.m.m)
# print(d.m.m)
# assert m.lowest_income(0, 2) == 0
# assert m.lowest_income(1, 3) == 0
# assert d.lowest_income(2, 5) == 0, f'{d.lowest_income(2, 5)}'
# assert d.lowest_income(5, 2) == 0
# print()

# successful = d.rent(20000000, 10001)
# assert successful
# print("Case 4")
# print(m.m.m)
# print(d.m.m)
# assert m.lowest_income(0, 2) == 0
# assert m.lowest_income(1, 3) == 0
# assert d.lowest_income(2, 5) == 10001
# assert d.lowest_income(5, 2) == 0
# print()

# successful = d.rent(20000000, 3)
# assert successful
# print("Case 5")
# print(m.m.m)
# print(d.m.m)
# assert m.lowest_income(0, 2) == 0
# assert m.lowest_income(1, 3) == 0
# assert d.lowest_income(4, 5) == 10001, f'{d.lowest_income(4, 5)}'
# assert d.lowest_income(3, 5) == 3, f'{d.lowest_income(3, 5)}'
# assert d.lowest_income(5, 2) == 0
# print()

# successful = d.rent(20000000, 2)
# assert successful
# print("Case 6")
# print(m.m.m)
# print(d.m.m)
# assert m.lowest_income(0, 2) == 0
# assert m.lowest_income(1, 3) == 0
# assert d.lowest_income(4, 5) == 10001, f'{d.lowest_income(4, 5)}'
# assert d.lowest_income(3, 5) == 3, f'{d.lowest_income(3, 5)}'
# assert d.lowest_income(2, 6) == 2, f'{d.lowest_income(2, 6)}'
# assert d.lowest_income(2, 7) == 1, f'{d.lowest_income(2, 7)}'
# assert d.lowest_income(5, 2) == 0
# print()

# successful = d.rent(1000000, 0)
# assert successful
# print("Case 7")
# print(m.m.m)
# print(d.m.m)
# assert m.lowest_income(0, 2) == 0
# assert m.lowest_income(1, 3) == 0
# assert d.lowest_income(4, 5) == 10001, f'{d.lowest_income(4, 5)}'
# assert d.lowest_income(3, 5) == 3, f'{d.lowest_income(3, 5)}'
# assert d.lowest_income(2, 5) == 2, f'{d.lowest_income(2, 5)}'
# assert d.lowest_income(1, 5) == 1, f'{d.lowest_income(1, 5)}'
# assert d.lowest_income(0, 7) == 0, f'{d.lowest_income(0, 7)}'
# assert d.lowest_income(8, 1000) == 0
# print()

# successful = d.rent(1000000, 100000000)
# assert not successful

# successful = m.rent(2000000, 400000)
# assert successful

# successful = m.rent(2000000, 300000)
# assert successful

# successful = m.rent(2000000, 200000)
# assert successful

# successful = m.rent(2000000, 100000)
# assert successful

# successful = m.rent(2000000, 100000)
# assert successful



# # print(m.m.m)
# # print(d.m.m)

# # assert m.lowest_income(0, 2) == 300000
# # assert m.lowest_income(1, 3) == 200000
# # assert d.lowest_income(2, 5) == 10000

# # print(d.lowest_income(-1294871290847190274, 52839728475))

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
assert not successful

assert m.lowest_income(0, 2) == 300000
assert m.lowest_income(1, 3) == 200000
assert d.lowest_income(2, 5) == 10000


