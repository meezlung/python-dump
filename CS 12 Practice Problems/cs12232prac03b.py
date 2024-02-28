from cs12232prac03a import MinReadyArray

class Metropolis:
    def __init__(self, H: list[int]) -> None:
        self.m = H
        self.total_cost = 0
    
    def expand_left(self, h: int) -> None:
        MinReadyArray.append_left(h)

    def __len__(self) -> int:
        return len(self.m)
    
    def cost(self, i: int, j: int) -> int | None:
        if 0 <= i <= j <= len(self.m):
            min_value = MinReadyArray.min(self, i, j)

            for x in range(len(self.m)):
                difference = abs(self.m[x] - min_value)
                self.total_cost += difference
            
            return self.total_cost * 7
        return None