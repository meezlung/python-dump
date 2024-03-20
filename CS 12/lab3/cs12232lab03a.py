from prac3.cs12232prac03a import MinReadyArray

class MaxReadyArray:
    def __init__(self):
        self.m: MinReadyArray = MinReadyArray()
        self.m_copy: MinReadyArray = MinReadyArray()

    def append_right(self, value: int) -> None:
        self.m.append_right(value * -1)

    def append_left(self, value: int) -> None:
        self.m.append_left(value * -1)

    def pop_left(self) -> int | None:
        number: int | None = self.m.pop_left() 
        if number is not None:
            return number * -1
        return None

    def pop_right(self) -> int | None:
        number: int | None = self.m.pop_right() 
        if number is not None:
            return number * -1
        return None

    def __len__(self) -> int:
        return len(self.m)
    
    def __getitem__(self, i: int) -> int | None:
        number: int | None = self.m[i]
        if number is not None:
            return number * -1
        return None
    
    def max(self, i: int, j: int) -> int | None:
        minimum: int | None = self.m.min(i, j)
        if minimum is not None:
            return minimum * -1
        return None