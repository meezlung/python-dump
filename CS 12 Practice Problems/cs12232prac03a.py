class MinReadyArray:
    def __init__(self):
        self.m = list()

    def append_right(self, value: int) -> None:
        self.m.append(value)

    def append_left(self, value: int) -> None:
        self.m.insert(0, value)

    def pop_left(self) -> int | None:
        return self.m.pop(0) if self.m else None 

    def pop_right(self) -> int | None:
        return self.m.pop() if self.m else None

    def __len__(self) -> int:
        return len(self.m)
    
    def __getitem__(self, i: int) -> int | None:
        return self.m[i] if (0 <= i < len(self.m) and self.m != None) else( None)
    
    def min(self, i: int, j: int) -> int | None:
        return min(self.m[i:j]) if i >= 0 and j <= len(self.m) and i < len(self.m) and j >= i else None