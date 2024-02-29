class Metropolis:
    def __init__(self, H: list[int]) -> None:
        self.m: list[int] = H
    
    def expand_left(self, h: int) -> None:
        self.m.insert(0, h)

    def __len__(self) -> int:
        return len(self.m)
    
    def cost(self, i: int, j: int) -> int | None:
        if 0 <= i <= j < len(self.m) and self.m:
            total_cost = 0
            for x in range(i, j+1):
                if self.m[x] != min(self.m[i:j+1]):
                    difference = abs(self.m[x] - min(self.m[i:j+1]))
                    total_cost += difference
            return total_cost * 7
        return None