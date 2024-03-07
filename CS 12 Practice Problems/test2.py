from cs12232prac03a import MinReadyArray

class Moles:
    def __init__(self, moles: list[tuple[int, int]]) -> None:
        self._moles = moles
        self.m: MinReadyArray = MinReadyArray()

    def burrow(self, x: int, y: int) -> None:
        self._moles.append((x, y))
        self._moles.pop(0)
    
    def __getitem__(self, i: int) -> tuple[int, int] | None:
        return self._moles[i] if 0 <= i < len(self._moles) and self._moles else None
    
    def spread(self, i: int, j: int) -> int:
        x_list = [self._moles[x][0] for x in range(i, j)]
        y_list = [self._moles[y][1] for y in range(i, j)]

        x = (max(x_list) + 1) - (min(x_list) - 1)
        y = (max(y_list) + 1) - (min(y_list) - 1)
        return x*y
