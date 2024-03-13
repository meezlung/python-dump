from cs12232prac03a import MinReadyArray

class MaxReadyArray:
    def __init__(self):
        self.m: MinReadyArray = MinReadyArray()

    def append_right(self, value: int) -> None:
        self.m.append_right(value)

    def append_left(self, value: int) -> None:
        self.m.append_left(value)

    def pop_left(self) -> int | None:
        return self.m.pop_left()

    def pop_right(self) -> int | None:
        return self.m.pop_right()

    def __len__(self) -> int:
        return len(self.m)
    
    def __getitem__(self, i: int) -> int | None:
        return self.m[i]
    
    def max(self, i: int, j: int) -> int | None:
        if max(i, 0) < min(j, len(self.m)):
            self.negate(max(i, 0), min(j, len(self.m)))

            minimum: int | None = self.m.min(i, j)

            self.negate(max(i, 0), min(j, len(self.m)))

            return minimum * -1 if minimum is not None else None
        
        else:
            return None

    def negate(self, i: int, j: int):
        x: int = 0
        while x < len(self.m):
            number: int | None = self.m[0]
            if number is not None:
                self.m.append_right(number * -1)
                self.m.pop_left()
                x += 1
