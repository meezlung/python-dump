class MinReadyArray:
    def __init__(self):
        self.m: list[int] = list()

    def append_right(self, value: int) -> None:
        self.m.append(value)

    def append_left(self, value: int) -> None:
        self.m.insert(0, value)

    def pop_left(self) -> int:
        if self.m: 
            return self.m.pop(0) 
        else:
            raise IndexError
        
    def pop_right(self) -> int | None:
        if self.m:
            return self.m.pop()
        else:
            raise IndexError

    def __len__(self) -> int:
        return len(self.m)
    
    def __getitem__(self, i: int) -> int | None:
        if 0 <= i < len(self.m) and self.m:
            return self.m[i]
        else:
            raise IndexError
    
    def min(self, i: int, j: int) -> int | None:
        if max(i, 0) < min(j, len(self.m)):
            return min(self.m[max(i, 0): min(j, len(self.m))])  
        else: 
            raise IndexError