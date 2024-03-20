from cs12232prac04e import SnoopingStack

s = SnoopingStack[int]()

s.push(20)

# assert len(s) == 1

res = s.pop()

assert res == 20

assert s.history() == [20, None], f'{s.history()}'