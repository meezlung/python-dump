from cs12232prac03a import MinReadyArray

class MollyMarketplace:
    def __init__(self, n: int, t: int) -> None:
        self.n: int = n # number of stalls
        self.t: int = t # threshold
        self.m: MinReadyArray = MinReadyArray()

    def rent(self, payment: int, income: int) -> bool:
        if payment >= self.t and len(self.m) != self.n:
            self.m.append_right(income)
            return True
        return False
    
    def lowest_income(self, i: int, j: int) -> int:
        min_income = self.m.min(i, j)
        return min_income if min_income is not None else 0

class DesmondMarketplace:
    def __init__(self, s: int, t: int) -> None:
        self.s: int = s # number of stalls
        self.t: int = t # threshold
        self.m: MinReadyArray = MinReadyArray()

    def rent(self, payment: int, income: int) -> bool:
        if payment >= self.t and len(self.m) != self.s:
            self.m.append_right(income)
            return True
        return False
    
    def lowest_income(self, i: int, j: int) -> int:
        min_income: int | None = self.m.min(self.s - j, self.s - i)
        return min_income if min_income is not None else 0